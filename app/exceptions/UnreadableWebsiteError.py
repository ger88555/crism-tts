from werkzeug.exceptions import HTTPException

class UnreadableWebsiteError(HTTPException):
    """
    Exception raised when the given website could not be read.
    """
    code = 422
    description = "Sitio web invalido."