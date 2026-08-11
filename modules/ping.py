import time
from pyrogram import Client, filters
from pyrogram.types import Message


async def setup(client: Client):
    client.on_message(filters.command("ping", prefixes=".") & filters.me)(ping_handler)


async def ping_handler(client: Client, message: Message):
    start = time.time()
    msg = await message.edit("**Pong!**")
    end = time.time()
    await msg.edit(f"**Pong!** `{round((end - start) * 1000, 2)}ms`")
