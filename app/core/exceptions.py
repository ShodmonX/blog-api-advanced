from dataclasses import dataclass
from starlette import status


@dataclass
class AppError(Exception):
    status_code: int
    code: str
    message: str
    details: dict | None = None

class NotFound(AppError):
    def __init__(self, message: str = "Not found", code: str = "not_found", details: dict | None = None):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, code=code, message=message, details=details)

class Unauthorized(AppError):
    def __init__(self, message: str = "Unauthorized", code: str = "unauthorized", details: dict | None = None):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, code=code, message=message, details=details)
class Forbidden(AppError):
    def __init__(self, message: str = "Forbidden", code: str = "forbidden", details: dict | None = None):
        super().__init__(status_code=status.HTTP_403_FORBIDDEN, code=code, message=message, details=details)

class Conflict(AppError):
    def __init__(self, message: str = "Conflict", code: str = "conflict", details: dict | None = None):
        super().__init__(status_code=status.HTTP_409_CONFLICT, code=code, message=message, details=details)

class BadRequest(AppError):
    def __init__(self, message: str = "Bad request", code: str = "bad_request", details: dict | None = None):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, code=code, message=message, details=details)