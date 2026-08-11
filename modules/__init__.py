"""JEK Userbot Module System."""
import os, logging, importlib

logger = logging.getLogger(__name__)

async def load_modules(client) -> int:
    """Handle module loading."""
    count = 0
    modules_dir = os.path.dirname(__file__)
    for f in os.listdir(modules_dir):
        if f.endswith(".py") and not f.startswith("__"):
            try:
                mod = importlib.import_module(f"modules.{f[:-3]}")
                if hasattr(mod, "setup"):
                    await mod.setup(client)  # Execute
                count += 1
            except Exception as e:
                logger.warning(f"Failed: {f}: {e}")  # Check
    return count