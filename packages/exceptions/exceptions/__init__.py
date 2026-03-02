"""Exceptions package."""


class AppError(Exception):
    """Base application error."""

    def __init__(self, message: str, code: int = 500) -> None:
        self.message = message
        self.code = code
        super().__init__(message)


class NotFoundError(AppError):
    def __init__(self, resource: str) -> None:
        super().__init__(f"{resource} not found", code=404)


class ValidationError(AppError):
    def __init__(self, field: str, reason: str) -> None:
        super().__init__(f"Validation failed for {field}: {reason}", code=422)
