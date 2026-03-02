"""Config package."""

from dataclasses import dataclass


@dataclass
class AppConfig:
    app_name: str = "app"
    debug: bool = False
    version: str = "0.1.0"


def get_config() -> AppConfig:
    return AppConfig()
