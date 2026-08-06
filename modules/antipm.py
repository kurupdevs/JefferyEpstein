# Jeffery Epstein x Kurup - Anti-PM
from pyrogram import Client,filters
from utils import modules_help,prefix
from utils.db import db
from utils.config import pm_limit
_w={}

@Client.on_message(filters.private&~filters.me&~filters.bot)
async def antipm_handler(client,msg):
    if not db.get("core.antipm","status",False):return
    uid=msg.from_user.id
    if msg.from_user.is_contact:return
    if db.get("core.antipm",f"allow_{uid}"):return
    me=await client.get_me()
    t=db.get("core.antipm","msg",f"Hi! This is {me.first_name}'s assistant. Owner is busy. Don't spam!")
    await client.send_message(uid,t)
    _w[uid]=_w.get(uid,0)+1
    if _w[uid]>=pm_limit:
        await client.send_message(uid,"<b>Blocked!</b>")
        await client.block_user(uid)
        del _w[uid]

@Client.on_message(filters.command(["antipm"],prefix)&filters.me)
async def antipm_toggle(_,msg):
    cur=db.get("core.antipm","status",False)
    db.set("core.antipm","status",not cur)
    await msg.edit(f"<b>Anti-PM {'ON' if not cur else 'OFF'}!</b>")

@Client.on_message(filters.command(["a","approve"],prefix)&filters.me)
async def approve(_,msg):
    db.set("core.antipm",f"allow_{msg.chat.id}",True)
    if msg.chat.id in _w:del _w[msg.chat.id]
    await msg.edit("<b>Approved!</b>")

@Client.on_message(filters.command(["d","disapprove"],prefix)&filters.me)
async def disapprove(_,msg):
    db.remove("core.antipm",f"allow_{msg.chat.id}")
    await msg.edit("<b>Disapproved!</b>")

modules_help["antipm"]={"antipm":"Toggle","a":"Approve","d":"Disapprove"}
