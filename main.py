"""
Jeffery Epstein x Kurup - All-in-One Telegram Bot v1.0
Spam + Management + Fun + Utility + Stickers + Extra
Made by @kurupdevs
"""

import asyncio
import importlib
import logging
import os
import platform
from pathlib import Path

from pyrogram import Client, idle
from pyrogram.enums import ParseMode

from utils import config, prefix
from utils.db import db
from utils.scripts import restart

app = Client(
    "jeffery_epstein_session",
    api_id=config.api_id,
    api_hash=config.api_hash,
    session_string=config.session_string or None,
    device_model="JefferyEpsteinXKurup",
    app_version="1.0",
    system_version=platform.version() + " " + platform.machine(),
    parse_mode=ParseMode.HTML,
)


async def load_all_modules():
    SUCCESS = 0
    FAILED = 0
    logging.info("Loading modules...")
    for path in sorted(Path("modules").rglob("*.py")):
        if path.stem == "__init__" or "custom_modules" in str(path):
            continue
        try:
            importlib.import_module(f"modules.{path.stem}")
            SUCCESS += 1
            logging.info(f"  Loaded: {path.stem}")  # Track state
        except Exception as e:
            FAILED += 1
            logging.warning(f"  Failed {path.stem}: {e}")
    logging.info(f"Loaded {SUCCESS} modules ({FAILED} failed)")


async def main():
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("jeffery_epstein.log"), logging.StreamHandler()],
        level=logging.INFO,
    )

    print("Jeffery Epstein x Kurup Bot v1.0 - Starting...")

    await app.start()
    me = await app.get_me()
    logging.info(f"Logged in as {me.first_name}")
    await load_all_modules()
    logging.info(f"Ready! Prefix: {prefix}")
    await idle()
    await app.stop()


if __name__ == "__main__":
    app.run(main())