import pytest
import json
import os
import tempfile


@pytest.fixture
def temp_json_file():
    """Create a temporary JSON file for testing."""
    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    yield path
    if os.path.exists(path):
        os.remove(path)


@pytest.fixture
def temp_dir():
    """Create a temporary directory for testing."""
    path = tempfile.mkdtemp()
    yield path
    import shutil
    shutil.rmtree(path, ignore_errors=True)
