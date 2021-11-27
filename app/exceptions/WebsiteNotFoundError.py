from werkzeug.exceptions import HTTPException

class WebsiteNotFoundError(HTTPException):
    """
    Exception raised when the given website could not be accessed.
    """
    code = 404
    description="No es posible acceder al sitio web."