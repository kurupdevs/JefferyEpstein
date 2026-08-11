# Fun Module for JEK Userbot
import random
from pyrogram import Client, filters
from pyrogram.types import Message

async def setup(client: Client):
    client.on_message(filters.command("laugh", prefixes=".") & filters.me)(laugh_handler)
    client.on_message(filters.command("magic", prefixes=".") & filters.me)(magic_handler)

async def laugh_handler(client: Client, message: Message):
    await message.edit(random.choice(["😂","🤣","😆"]) * random.randint(3, 8))  # Process

async def magic_handler(client: Client, message: Message):
    await message.edit(f"🎱 **Magic 8-Ball:** {random.choice(['Yes','No','Maybe','Definitely'])}")  # Execute