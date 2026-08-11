import json
from pyrogram import Client, filters
from pyrogram.types import Message

NOTES_FILE = "notes.json"


def _load_notes():
    try:
        with open(NOTES_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)


async def setup(client: Client):
    client.on_message(filters.command("save", prefixes=".") & filters.me)(save_note)
    client.on_message(filters.command("get", prefixes=".") & filters.me)(get_note)
    client.on_message(filters.command("notes", prefixes=".") & filters.me)(list_notes)
    client.on_message(filters.command("delnote", prefixes=".") & filters.me)(delete_note)


async def save_note(client: Client, message: Message):
    args = message.text.split(None, 2)
    if len(args) < 3:
        await message.edit("**Usage:** `.save <name> <content>`")
        return
    notes = _load_notes()
    notes[args[1]] = args[2]
    _save_notes(notes)
    await message.edit(f"**Saved note:** `{args[1]}`")


async def get_note(client: Client, message: Message):
    args = message.text.split(None, 1)
    if len(args) < 2:
        await message.edit("**Usage:** `.get <name>`")
        return
    notes = _load_notes()
    note = notes.get(args[1], "Note not found.")
    await message.edit(note)


async def list_notes(client: Client, message: Message):
    notes = _load_notes()
    if not notes:
        await message.edit("No notes saved.")
        return
    text = "**Saved Notes:**\n" + "\n".join(f"• `{k}`" for k in notes)
    await message.edit(text)


async def delete_note(client: Client, message: Message):
    args = message.text.split(None, 1)
    if len(args) < 2:
        await message.edit("**Usage:** `.delnote <name>`")
        return
    notes = _load_notes()
    if args[1] in notes:
        del notes[args[1]]
        _save_notes(notes)
        await message.edit(f"**Deleted note:** `{args[1]}`")
    else:
        await message.edit("Note not found.")
