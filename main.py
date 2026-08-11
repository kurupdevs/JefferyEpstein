import os
import logging
import asyncio

from pyrogram import Client, idle

# Core imports
from utils import load_plugins
from config import API_ID, API_HASH

logger = logging.getLogger(__name__)


class KurupBot:
    """Core bot class for JefferyEpstein Telegram automation bot."""
    
    def __init__(self):
        self.client = Client(
            "jeffery",
            api_id=API_ID,
            api_hash=API_HASH,
        )
        self.plugins = {}
        logger.info("Bot instance created")
    
    async def initialize(self):
        """Load plugins and prepare the bot for operation."""
        await load_plugins(self.client, self.plugins)
        logger.info(f"Loaded {len(self.plugins)} plugins")
    
    async def start(self):
        """Start the bot and begin processing."""
        await self.client.start()
        await self.initialize()
        logger.info("Bot started and ready")
        await idle()


def main():
    """Application entry point."""
    bot = KurupBot()
    bot.client.run(bot.start())


if __name__ == "__main__":
    main()
