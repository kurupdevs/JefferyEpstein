import json
import os
import sys
import tempfile

import pytest

# Ensure the root is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestNotesModule:
    """Tests for modules/notes.py helper functions."""

    def test_load_notes_empty_file(self, temp_json_file):
        """Loading an empty file should return empty dict."""
        import modules.notes as notes_module
        notes_module.NOTES_FILE = temp_json_file
        result = notes_module._load_notes()
        assert result == {}

    def test_load_notes_nonexistent_file(self):
        """Loading a non-existent file should return empty dict."""
        import modules.notes as notes_module
        notes_module.NOTES_FILE = "/tmp/__nonexistent_notes.json"
        result = notes_module._load_notes()
        assert result == {}

    def test_load_notes_with_data(self, temp_json_file):
        """Loading a file with valid JSON should return the data."""
        data = {"greeting": "hello", "farewell": "bye"}
        with open(temp_json_file, "w") as f:
            json.dump(data, f)

        import modules.notes as notes_module
        notes_module.NOTES_FILE = temp_json_file
        result = notes_module._load_notes()
        assert result == data
        assert result["greeting"] == "hello"

    def test_save_notes(self, temp_json_file):
        """Saving notes should persist to JSON file."""
        data = {"key1": "value1"}
        import modules.notes as notes_module
        notes_module.NOTES_FILE = temp_json_file
        notes_module._save_notes(data)

        with open(temp_json_file) as f:
            saved = json.load(f)
        assert saved == data

    def test_save_and_load_roundtrip(self, temp_json_file):
        """Save then load should return the same data."""
        import modules.notes as notes_module
        notes_module.NOTES_FILE = temp_json_file

        notes_module._save_notes({"a": "1", "b": "2"})
        result = notes_module._load_notes()
        assert result == {"a": "1", "b": "2"}

    def test_load_corrupted_json(self, temp_json_file):
        """Loading corrupted JSON should return empty dict."""
        with open(temp_json_file, "w") as f:
            f.write("not valid json {{{{")

        import modules.notes as notes_module
        notes_module.NOTES_FILE = temp_json_file
        result = notes_module._load_notes()
        assert result == {}
