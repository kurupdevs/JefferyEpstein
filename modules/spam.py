import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message


async def setup(client: Client):
    client.on_message(filters.command("spam", prefixes=".") & filters.me)(spam_handler)


async def spam_handler(client: Client, message: Message):
    args = message.text.split(None, 2)
    if len(args) < 3:
        await message.edit("**Usage:** `.spam <count> <text>`")
        return
    try:
        count = min(int(args[1]), 50)
    except ValueError:
        await message.edit("**Invalid count.**")
        return
    await message.delete()
    for _ in range(count):
        await client.send_message(message.chat.id, args[2])
        await asyncio.sleep(0.4)
