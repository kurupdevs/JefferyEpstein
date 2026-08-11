import time
from pyrogram import Client, filters
from pyrogram.types import Message

START_TIME = time.time()


async def setup(client: Client):
    client.on_message(filters.command("alive", prefixes=".") & filters.me)(alive_handler)


async def alive_handler(client: Client, message: Message):
    uptime = time.time() - START_TIME
    hours, rem = divmod(uptime, 3600)
    minutes, seconds = divmod(rem, 60)
    await message.edit(
        f"**I'm Alive!**\n\n"
        f"Uptime: `{int(hours)}h {int(minutes)}m {int(seconds)}s`"
    )
