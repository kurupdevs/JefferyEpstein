from pyrogram import Client, filters
from pyrogram.types import Message

HELP_TEXT = """
**Available Commands:**

• `.afk` - Set AFK status
• `.alive` - Check bot uptime
• `.ping` - Check latency
• `.spam` - Spam messages
• `.help` - Show this menu
"""


async def setup(client: Client):
    client.on_message(filters.command("help", prefixes=".") & filters.me)(help_handler)


async def help_handler(client: Client, message: Message):
    await message.edit(HELP_TEXT)
