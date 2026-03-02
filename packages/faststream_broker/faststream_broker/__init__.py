"""FastStream broker package."""

from collections.abc import Callable
from typing import Any


class BrokerClient:
    def __init__(self, url: str) -> None:
        self.url = url
        self._handlers: dict[str, Callable[..., Any]] = {}

    def subscribe(
        self, topic: str
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            self._handlers[topic] = func
            return func

        return decorator

    async def publish(self, topic: str, message: dict[str, Any]) -> None:
        pass
