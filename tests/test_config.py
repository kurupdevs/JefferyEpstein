"""Tests for the config module."""
import os


def test_api_id_from_env(mock_env):
    """Test that API_ID is read from environment."""
    import importlib
    import config
    importlib.reload(config)
    assert config.API_ID == 12345


def test_api_hash_from_env(mock_env):
    """Test that API_HASH is read from environment."""
    import importlib
    import config
    importlib.reload(config)
    assert config.API_HASH == "test_hash_abc123"


def test_api_id_default():
    """Test that API_ID defaults to 0 when not set."""
    import importlib
    import config

    # Clear env and reload
    if "API_ID" in os.environ:
        del os.environ["API_ID"]
    importlib.reload(config)
    assert config.API_ID == 0
