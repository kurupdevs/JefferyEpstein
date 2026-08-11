"""Test configuration and shared fixtures."""
import os
import sys
from unittest.mock import AsyncMock, MagicMock

import pytest

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture
def mock_env(monkeypatch):
    """Set up mock environment variables for testing."""
    monkeypatch.setenv("API_ID", "12345")
    monkeypatch.setenv("API_HASH", "test_hash_abc123")
    monkeypatch.setenv("STRING_SESSION", "test_session_string")


@pytest.fixture
def mock_client():
    """Return a mocked Pyrogram Client."""
    client = MagicMock()
    client.start = AsyncMock()
    client.stop = AsyncMock()
    client.on_message = MagicMock()
    return client


@pytest.fixture
def mock_message():
    """Return a mocked Telegram Message."""
    msg = MagicMock()
    msg.edit = AsyncMock()
    msg.reply = AsyncMock()
    msg.delete = AsyncMock()
    msg.text = ".ping"
    msg.chat = MagicMock()
    msg.chat.id = -1001234567890
    msg.from_user = MagicMock()
    msg.from_user.id = 123456789
    msg.from_user.mention = "@testuser"
    msg.reply_to_message = None
    return msg
