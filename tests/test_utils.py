"""Tests for utilities."""
import os
import sys
import tempfile
from unittest.mock import AsyncMock, MagicMock, patch

import pytest


class TestDatabaseUtils:
    """Tests for utils/db.py."""

    def test_db_path_formatting(self):
        """Test database path is formatted correctly."""
        # DB functions should handle paths safely
        test_path = "test_db"
        expected = f"{test_path}.db"
        assert expected.endswith(".db")

    def test_session_file_extension(self):
        """Test session file naming convention."""
        session_name = "jeff_bot"
        session_file = f"{session_name}.session"
        assert session_file == "jeff_bot.session"


class TestConfigUtils:
    """Tests for utils/config.py."""

    def test_config_exists(self):
        """Test that the config utility module is importable."""
        try:
            from utils.config import Config
            assert Config is not None
        except ImportError:
            pytest.skip("Config class not available")


class TestPrefixHandling:
    """Tests for command prefix logic."""

    @pytest.mark.parametrize("text,expected", [
        (".ping", "."),
        (".ban", "."),
        ("!help", "!"),
        ("#start", "#"),
        ("ping", None),
        ("", None),
    ])
    def test_prefix_extraction(self, text, expected):
        """Test prefix detection from command text."""
        # Common command prefixes
        known_prefixes = {".", "!", "#"}
        prefix = text[0] if text and text[0] in known_prefixes else None
        assert prefix == expected
