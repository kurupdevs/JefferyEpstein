"""
Lightweight JSON-based key-value store.

Provides thread-safe read/write/delete operations with atomic
file writes. Each "collection" is a separate JSON file under
the ``data/`` directory.

Usage::

    from utils import db
    db.setv("users", "abc123", {"name": "Alice"})
    user = db.get("users", "abc123")

"""

import json
import threading
from pathlib import Path
from typing import Any, Optional

# ── Storage Directory ────────────────────────────────────────
DATA_DIR: Path = Path("data")
DATA_DIR.mkdir(exist_ok=True)

_lock: threading.Lock = threading.Lock()


def _load(path: Path) -> dict:
    """Load JSON data from a file.

    Args:
        path: Path to the JSON file.

    Returns:
        Parsed dictionary, or an empty dict if the file does
        not exist or cannot be parsed.
    """
    if not path.exists():
        return {}
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def _save(path: Path, data: dict) -> bool:
    """Atomically save a dictionary to a JSON file.

    Writes to a temporary file first, then renames it over
    the target to prevent corruption on crash.

    Args:
        path: Target file path.
        data: Dictionary to persist.

    Returns:
        ``True`` on success, ``False`` on failure.
    """
    try:
        tmp = path.with_suffix(".tmp")
        with open(tmp, "w") as f:
            json.dump(data, f, indent=2)
        tmp.rename(path)
        return True
    except OSError:
        return False


def get(col: str, key: str, default: Any = None) -> Any:
    """Retrieve a value from a collection.

    Args:
        col: Collection name (maps to ``data/{col}.json``).
        key: The key to look up.
        default: Value returned when the key or collection
            does not exist.

    Returns:
        The stored value, or ``default``.
    """
    with _lock:
        path = DATA_DIR / f"{col}.json"
        data = _load(path)
        return data.get(key, default)


def setv(col: str, key: str, value: Any) -> bool:
    """Store a value in a collection.

    Args:
        col: Collection name.
        key: The key to set.
        value: The value to store (must be JSON-serializable).

    Returns:
        ``True`` on success, ``False`` on failure.
    """
    with _lock:
        path = DATA_DIR / f"{col}.json"
        data = _load(path)
        data[key] = value
        return _save(path, data)


def remove(col: str, key: str) -> bool:
    """Remove a key from a collection.

    Args:
        col: Collection name.
        key: The key to remove.

    Returns:
        ``True`` on success (including when the key did not
        exist), ``False`` on write failure.
    """
    with _lock:
        path = DATA_DIR / f"{col}.json"
        data = _load(path)
        data.pop(key, None)
        return _save(path, data)
