import json
import os
import sys
import tempfile

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestDBModule:
    """Tests for utils/db.py functions."""

    @pytest.fixture(autouse=True)
    def setup_db(self, monkeypatch, temp_dir):
        """Redirect db DATA_DIR to a temp directory for each test."""
        monkeypatch.setattr("utils.db.DATA_DIR", __import__("pathlib").Path(temp_dir))
        yield

    def test_get_nonexistent_collection(self):
        """Getting from a non-existent collection should return default."""
        from utils import db
        result = db.get("nonexistent", "key", default="fallback")
        assert result == "fallback"

    def test_get_nonexistent_key(self):
        """Getting a missing key should return default."""
        from utils import db
        result = db.get("users", "missing_key", default="default_val")
        assert result == "default_val"

    def test_set_and_get(self):
        """Setting a value then getting it should return the same value."""
        from utils import db
        assert db.setv("settings", "theme", "dark") is True
        result = db.get("settings", "theme")
        assert result == "dark"

    def test_set_multiple_keys(self):
        """Multiple keys in the same collection should coexist."""
        from utils import db
        db.setv("config", "lang", "en")
        db.setv("config", "timezone", "UTC")
        assert db.get("config", "lang") == "en"
        assert db.get("config", "timezone") == "UTC"

    def test_remove_existing_key(self):
        """Removing an existing key should succeed."""
        from utils import db
        db.setv("cache", "temp", "data")
        assert db.remove("cache", "temp") is True
        assert db.get("cache", "temp", default="gone") == "gone"

    def test_remove_nonexistent_key(self):
        """Removing a missing key should not error."""
        from utils import db
        result = db.remove("cache", "never_exists")
        assert result is True

    def test_collections_isolated(self):
        """Different collections should not interfere."""
        from utils import db
        db.setv("col1", "key", "a")
        db.setv("col2", "key", "b")
        assert db.get("col1", "key") == "a"
        assert db.get("col2", "key") == "b"

    def test_get_with_none_default(self):
        """Get should return None when no default is provided."""
        from utils import db
        result = db.get("empty_col", "no_key")
        assert result is None
