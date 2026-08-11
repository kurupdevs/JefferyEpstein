import time
ST=time.time()
async def setup(c):
 from pyrogram import filters
 c.on_message(filters.command("alive",prefixes=".")&filters.me)(h)
async def h(c,m):
 u=time.time()-ST;hr,r=divmod(u,3600);mn,s=divmod(r,60)
 await m.edit(f"Alive! Uptime: {int(hr)}h{int(mn)}m{int(s)}s")
