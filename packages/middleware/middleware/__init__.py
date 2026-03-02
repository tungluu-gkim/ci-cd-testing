"""Middleware package."""

from collections.abc import Callable
from typing import Any

Handler = Callable[..., Any]


def logging_middleware(handler: Handler) -> Handler:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Calling {handler.__name__}")
        result = handler(*args, **kwargs)
        print(f"Done {handler.__name__}")
        return result

    return wrapper


def auth_middleware(token: str) -> Callable[[Handler], Handler]:
    def decorator(handler: Handler) -> Handler:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if not token:
                raise PermissionError("Unauthorized")
            return handler(*args, **kwargs)

        return wrapper

    return decorator
