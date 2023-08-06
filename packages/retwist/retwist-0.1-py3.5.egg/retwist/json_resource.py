import codecs
import json
import logging
import re
import sys
import traceback as _traceback
from typing import Any, Callable, Dict, IO

try:
    from inspect import iscoroutinefunction
except ImportError:
    # We must be on Python < 3.5!
    def iscoroutinefunction(func):
        # type: (Callable) -> bool
        return False

import twisted.internet.defer
import twisted.internet.error
import twisted.python.failure
import twisted.web.error
import twisted.web.resource
import twisted.web.http
import twisted.web.server

import retwist.param_resource


class JsonResource(retwist.param_resource.ParamResource):
    """
    Twisted resource with convenience methods to encode JSON responses. Supports JSONP.
    """

    encoding = "utf-8"
    # Factory function for a UTF-8 stream encoder:
    create_writer = codecs.getwriter(encoding)

    jsonp_callback_re = re.compile(b"^[_a-zA-Z0-9\.$]+$")

    @classmethod
    def json_dump_default(cls, o):
        """
        Override this to implement custom JSON encoding. Passed to json.dump method.
        :param o: Object which cannot be JSON-serialized.
        :return: JSON-serializable object (or throw TypeError)
        """
        raise TypeError("Can't JSON serialize {}".format(type(o).__name__))

    def json_GET(self, request):
        # type: (twisted.web.http.Request) -> Dict
        """
        Override this to return JSON data to render.
        :param request: Twisted request.
        """
        raise NotImplementedError()

    def render(self, request):
        """
        Before we render this request as normal, parse parameters, and add them to the request! Also, catch any errors
        during parameter parsing, and show them appropriately.
        :param request: Twisted request object
        :return: Byte string or NOT_DONE_YET - see IResource.render
        """
        try:
            request.url_args = self.parse_args(request)
        except:
            # Catch-all is OK, since the failure object will pick up the exception
            failure = twisted.python.failure.Failure()
            self.send_failure(failure, request)
            return twisted.web.server.NOT_DONE_YET
        else:
            return twisted.web.resource.Resource.render(self, request)

    def render_GET(self, request):
        """
        Get JSON data from json_GET, and render for the client.
        
        Do not override in sub classes ...
        :param request: Twisted request
        """
        if iscoroutinefunction(self.json_GET):
            coroutine = self.json_GET(request)
            json_def = twisted.internet.defer.ensureDeferred(coroutine)
        else:
            json_def = twisted.internet.defer.maybeDeferred(self.json_GET, request)

        json_def.addCallback(self.send_json_response, request)
        json_def.addErrback(self.send_failure, request)

        # handle connection failures
        request.notifyFinish().addErrback(self.on_connection_closed, json_def)

        return twisted.web.server.NOT_DONE_YET

    def response_envelope(self, response, status_code=200, status_message=None):
        # type: (Any, int, str) -> Any
        """
        Implement this to transform JSON responses before sending, e.g. by putting HTTP status codes in the response.
        
        :param response: JSON data about to be sent to client 
        :param status_code: HTTP status code
        :param status_message: Optional status message, e.g. error message
        :return: Wrapped JSON-serializable data
        """
        return response

    def send_json_response(self, response, request, status_code=200, status_message=None):
        # type: (Any, twisted.web.http.Request, int, str) -> None
        """
        Send JSON data to client.
        
        :param response: JSON-serializable data 
        :param request: Twisted request
        :param status_code: HTTP status code
        :param status_message: Optional status message, e.g. error message
        """
        is_jsonp = len(request.args.get(b"callback", [])) == 1
        if is_jsonp:
            callback = request.args[b"callback"][0]
            if not self.jsonp_callback_re.match(callback):
                del request.args[b"callback"]
                return self.send_json_response("Invalid callback", request, status_code=400)
            request.setHeader(b"Content-Type", b"application/javascript; charset=%s" % self.encoding.encode())
            request.write(callback + b"(")
        else:
            request.setHeader(b"Content-Type", b"application/json; charset=%s" % self.encoding.encode())
            request.setResponseCode(status_code)

        response = self.response_envelope(response, status_code=status_code, status_message=status_message)
        stream = self.create_writer(request)
        json.dump(response, stream, allow_nan=False, default=self.json_dump_default)

        if is_jsonp:
            request.write(b")")

        request.finish()

    def log_server_error(self, exception, request, traceback):
        # type: (Exception, twisted.web.http.Request, Any) -> None
        """
        Oh no, a server error happened! Log it. The request is just passed for inspection; don't modify it.
        
        :param exception: Exception instance
        :param request: Twisted request
        :param traceback: Traceback object
        """
        error_msg = str(exception)
        tb = traceback or sys.last_traceback
        tb_list = _traceback.extract_tb(tb)
        tb_formatted = _traceback.format_list(tb_list)
        tb_str = "".join(tb_formatted)
        logging.error("%s (%s) @ %s\n%s", type(exception).__name__, error_msg, request.uri, tb_str)

    def send_failure(self, failure, request):
        # type: (twisted.python.failure.Failure, twisted.web.http.Request) -> None
        """
        Convenience errback to handle failures in Twisted deferreds.
        
        :param failure: Twisted failure
        :param request: Twisted request
        """
        try:
            return self.send_exception(failure.value, request, failure.getTracebackObject())
        except Exception as ex:
            logging.exception(str(ex))

    def send_exception(self, exception, request, traceback=None):
        # type: (Exception, twisted.web.http.Request, Any) -> None
        """
        Send an error to the client. For connection errors, we do nothing - no chance to send anything. For client
        errors, we show an informative error message. For server errors, we show a generic message, and log the error.

        :param exception: Exception instance
        :param request: Twisted request
        :param traceback: Traceback object - needs to be passed in from Twisted Failures
        """

        # This happens if the client closed the connection, or something similar.
        if any(isinstance(exception, exc_type) for exc_type in [
                twisted.internet.defer.CancelledError,
                twisted.internet.error.ConnectionLost,
                twisted.internet.error.ConnectionDone,
                twisted.internet.error.ConnectError
            ]
        ):
            return

        error_msg = str(exception)

        # Client error
        if isinstance(exception, twisted.web.error.Error):
            web_error = exception  # type: twisted.web.error.Error
            status_code = int(web_error.status)
            if 400 <= status_code < 500:
                return self.send_json_response(error_msg, request, status_code=status_code)

        # Server
        self.log_server_error(exception, request, traceback)
        return self.send_json_response("Server-side error", request, status_code=500)

    def on_connection_closed(self, failure, deferred):
        # type: (twisted.python.failure.Failure, twisted.internet.defer.Deferred) -> None
        """
        Handle connection errors.
        
        :param failure: Twisted failure 
        :param deferred: The async call to json_GET
        """

        deferred.cancel()
