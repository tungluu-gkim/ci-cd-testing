"""Database package."""

from typing import Any


class DatabaseClient:
    def __init__(self, url: str) -> None:
        self.url = url
        self._connected = False

    def connect(self) -> None:
        self._connected = True

    def disconnect(self) -> None:
        self._connected = False

    def execute(self, query: str, params: dict[str, Any] | None = None) -> list[Any]:
        if not self._connected:
            raise RuntimeError("Not connected to database")
        return []
