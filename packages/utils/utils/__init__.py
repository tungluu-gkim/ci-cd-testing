"""Utils package."""

import hashlib
import re


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_-]+", "-", text)


def hash_string(value: str) -> str:
    return hashlib.sha256(value.encode()).hexdigest()
