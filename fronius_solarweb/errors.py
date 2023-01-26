class NotAuthorizedException(ValueError):
    pass


class NotFoundException(ValueError):
    pass


HTML_ERROR_CODES = {
    200: "OK",  # Successful
    204: "No content",  # Successful request but no data
    400: "Bad request",  # Malformed request
    401: "Unauthorized",  # No or invalid authentication details are provided
    403: "Forbidden",  # Authentication succeeded but authenticated user/API key doesn't have access to the resource
    404: "Not found",  # Non-existent resource is requested
    405: "Method not allowed",  # The request method is not supported for the requested resource
    415: "Unsupported media type",  # Payload format is not supported
    429: "Too many requests",  # Request is rejected due to rate limiting
    500: "Internal server error",  # An unexpected server error happened
    503: "Service not available",  # The server is temporarily unavailable
}
