"""AWS client package."""

from typing import Any


class S3Client:
    def __init__(self, bucket: str, region: str = "us-east-1") -> None:
        self.bucket = bucket
        self.region = region

    def upload(self, key: str, data: bytes) -> dict[str, Any]:
        return {"bucket": self.bucket, "key": key, "size": len(data)}

    def download(self, key: str) -> bytes:
        return b""

    def delete(self, key: str) -> bool:
        return True
