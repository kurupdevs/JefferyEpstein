AFK={}
async def setup(c):
 from pyrogram import filters
 c.on_message(filters.command("afk",prefixes=".")&filters.me)(h)
async def h(c,m):
 r=m.text.split(None,1)[1]if len(m.text.split())>1 else"AFK"
 AFK[m.from_user.id]=r;await m.edit(f"**AFK:** {r}")
