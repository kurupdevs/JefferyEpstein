import json
import os
import sys
import tempfile

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestConfigModule:
    """Tests for utils/config.py functions."""

    @pytest.fixture(autouse=True)
    def setup_config(self, monkeypatch, temp_dir):
        """Redirect config CD to a temp directory for each test."""
        monkeypatch.setattr("utils.config.CD", __import__("pathlib").Path(temp_dir))
        yield

    def test_getc_missing_file_returns_default(self):
        """Getting from a missing config file should return default."""
        from utils import config
        result = config.getc("key", d="fallback")
        assert result == "fallback"

    def test_getc_missing_key_returns_default(self):
        """Getting a missing key should return default."""
        from utils import config
        # First set something to create the file
        config.setc("existing", "value")
        result = config.getc("missing", d="default_val")
        assert result == "default_val"

    def test_setc_and_getc(self):
        """Setting then getting should return the same value."""
        from utils import config
        assert config.setc("username", "kurup") is True
        result = config.getc("username")
        assert result == "kurup"

    def test_setc_overwrite(self):
        """Setting the same key twice should overwrite."""
        from utils import config
        config.setc("version", "1.0")
        config.setc("version", "2.0")
        assert config.getc("version") == "2.0"

    def test_setc_multiple_keys(self):
        """Multiple keys should be stored independently."""
        from utils import config
        config.setc("k1", "v1")
        config.setc("k2", "v2")
        assert config.getc("k1") == "v1"
        assert config.getc("k2") == "v2"

    def test_getc_without_default_returns_none(self):
        """Get without default should return None for missing keys."""
        from utils import config
        result = config.getc("nonexistent_key")
        assert result is None
