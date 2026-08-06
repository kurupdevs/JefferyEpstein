# Jeffery Epstein x Kurup - AFK
import asyncio
from datetime import datetime
import humanize
from pyrogram import Client,filters
from utils import modules_help,prefix
from utils.db import db

AFK=False;AFK_REASON="";AFK_TIME=None;CHATS={}

@Client.on_message((filters.mentioned|filters.private)&~filters.me&~filters.service)
async def afk_handler(client,msg):
    global AFK
    if not AFK:return
    cid=msg.chat.id
    last=humanize.naturaltime(datetime.now()-AFK_TIME)
    if cid not in CHATS:
        t=db.get("core.afk","msg",f"I'm AFK.\nLast seen: {last}\nReason: {AFK_REASON or 'N/A'}")
        await client.send_message(cid,t)
        CHATS[cid]=1
    else:CHATS[cid]+=1

@Client.on_message(filters.command("afk",prefix)&filters.me)
async def set_afk(_,msg):
    global AFK,AFK_REASON,AFK_TIME,CHATS
    AFK=True;AFK_REASON=" ".join(msg.command[1:]) if len(msg.command)>1 else "";AFK_TIME=datetime.now();CHATS.clear()
    await msg.delete()

@Client.on_message(filters.me&~filters.command("afk",prefix))
async def auto_unafk(_,msg):
    global AFK
    if AFK:
        AFK=False
        total=sum(CHATS.values())
        if total:await msg.reply(f"<b>Welcome back! {total} msgs from {len(CHATS)} chats</b>")

modules_help["afk"]={"afk [reason]":"Go AFK"}
