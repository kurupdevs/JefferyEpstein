# Jeffery Epstein x Kurup - Spam Module
import asyncio, random
from pyrogram import Client, filters
from utils import modules_help, prefix
D = {"spam":0.15,"fastspam":0.01,"slowspam":0.9,"statspam":0.1,"delayspam":1.5,"bigspam":0.05}
R = ["☠️ RAID BY JEFFERY EPSTEIN x KURUP ☠️","👿 TARGET ACQUIRED","💀 NUKED","🔥 BURN","💥 BOOM"]
@Client.on_message(filters.command(list(D.keys()),prefix)&filters.me)
async def spam(client, msg):
    c=msg.command[0]
    if len(msg.command)<3:return await msg.edit(f"{prefix}{c} [amount] [text]")
    a=min(int(msg.command[1]),1000);t=" ".join(msg.command[2:])
    await msg.delete()
    for _ in range(a):
        try:
            if msg.reply_to_message:await msg.reply_to_message.reply(t)
            else:await client.send_message(msg.chat.id,t)
            if c=="statspam":await asyncio.sleep(0.1)
        except:pass
        await asyncio.sleep(D[c])
@Client.on_message(filters.command(["raid"],prefix)&filters.me)
async def raid(client,msg):
    if not msg.reply_to_message:return await msg.edit("Reply to user!")
    a=min(int(msg.command[1]),500) if len(msg.command)>1 else 10
    u=msg.reply_to_message.from_user;m=u.mention if u else "User"
    await msg.delete()
    for _ in range(a):
        try:await msg.reply_to_message.reply(f"{m} {random.choice(R)}");await asyncio.sleep(0.1)
        except:pass
modules_help["spam"]={"spam [amount] [text]":"Spam","fastspam [amount] [text]":"Fast spam","slowspam [amount] [text]":"Slow spam","statspam [amount] [text]":"Spam+Delete","delayspam [amount] [text]":"Delayed","bigspam [amount] [text]":"Big spam","raid [amount] [reply]*":"Raid user"}
