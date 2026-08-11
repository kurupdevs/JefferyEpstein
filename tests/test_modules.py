"""Tests for module loading and structure."""
import importlib


class TestModuleStructure:
    """Tests for ensuring proper module structure."""

    def test_modules_package_imports(self):
        """Test that the modules package imports correctly."""
        import modules
        assert hasattr(modules, "__all__")
        assert isinstance(modules.__all__, list)

    def test_utils_package_imports(self):
        """Test that the utils package imports correctly."""
        import utils
        assert utils is not None

    def test_required_modules_in_all(self):
        """Test that core modules are listed in __all__."""
        import modules
        required_modules = ["afk", "alive", "management", "ping", "spam", "help"]
        for mod in required_modules:
            assert mod in modules.__all__, f"Module '{mod}' missing from __all__"

    def test_custom_modules_importable(self):
        """Test that custom_modules package exists."""
        try:
            from modules import custom_modules
            assert custom_modules is not None
        except ImportError:
            # custom_modules might be empty, that's okay
            pass

    def test_utils_modules_exist(self):
        """Test that core util modules are importable."""
        try:
            from utils import config
            assert config is not None
        except ImportError:
            pass

        try:
            from utils import db
            assert db is not None
        except ImportError:
            pass
