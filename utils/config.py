"""
Persistent application settings via JSON.

Reads and writes key-value pairs to ``config/settings.json``.
All operations are synchronous and intended for startup/
shutdown use, not hot-path code.

Usage::

    from utils import config
    config.setc("theme", "dark")
    theme = config.getc("theme", d="light")

"""

import json
import os
from pathlib import Path
from typing import Any, Optional

# ── Config Directory ─────────────────────────────────────────
CD: Path = Path("config")
CD.mkdir(exist_ok=True)


def getc(key: str, d: Any = None) -> Any:
    """Read a configuration value.

    Args:
        key: Configuration key to look up.
        d: Default returned when the key or file is missing.

    Returns:
        The stored value, or ``d``.
    """
    cf = CD / "settings.json"
    if not cf.exists():
        return d
    try:
        with open(cf) as f:
            return json.load(f).get(key, d)
    except (json.JSONDecodeError, OSError):
        return d


def setc(key: str, value: Any) -> bool:
    """Persist a configuration value.

    Args:
        key: Configuration key.
        value: Value to store (must be JSON-serializable).

    Returns:
        ``True`` on success, ``False`` on failure.
    """
    cf = CD / "settings.json"
    data: dict = {}
    if cf.exists():
        try:
            with open(cf) as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    data[key] = value
    try:
        with open(cf, "w") as f:
            json.dump(data, f, indent=2)
        return True
    except OSError:
        return False
