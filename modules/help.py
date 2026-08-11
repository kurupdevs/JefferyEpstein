from pyrogram import Client,filters

HELP=""".afk .alive .ping .spam .fact .joke .ban .mute .help"""

async def setup(c):c.on_message(filters.command("help",prefixes=".")&filters.me)(h)
async def h(c,m):await m.edit(f"**Commands:** {HELP}")
