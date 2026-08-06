# Jeffery Epstein x Kurup - Notes & Filters
from pyrogram import Client,errors,filters
from utils import modules_help,prefix
from utils.db import db
from utils.scripts import format_exc

@Client.on_message(filters.command(["save"],prefix)&filters.me)
async def save(client,msg):
    if len(msg.text.split())<2 or not msg.reply_to_message:return await msg.edit(f"{prefix}save [name] (reply)")
    name=msg.text.split(maxsplit=1)[1].split()[0].lower()
    try:
        sid=db.get("core.notes","storage_id",0)
        chat=await client.get_chat(sid)
    except:
        chat=await client.create_supergroup("JEK_Storage")
        db.set("core.notes","storage_id",chat.id)
    try:mo=await msg.reply_to_message.forward(chat.id)
    except errors.ChatForwardsRestricted:mo=await msg.reply_to_message.copy(chat.id)
    db.set("core.notes",f"n_{name}",{"cid":chat.id,"mid":mo.id})
    await msg.edit(f"<b>Note <code>{name}</code> saved!</b>")

@Client.on_message(filters.command(["get","note"],prefix)&filters.me)
async def get(client,msg):
    if len(msg.command)<2:return await msg.edit(f"{prefix}get [name]")
    note=db.get("core.notes",f"n_{msg.command[1].lower()}")
    if not note:return await msg.edit("<b>Not found!</b>")
    try:await client.copy_message(msg.chat.id,note["cid"],note["mid"]);await msg.delete()
    except Exception as e:await msg.edit(format_exc(e))

@Client.on_message(filters.command(["notes"],prefix)&filters.me)
async def notes_list(_,msg):
    notes=[k.replace("n_","") for k in db.get_collection("core.notes") if k.startswith("n_")]
    if notes:await msg.edit("<b>Notes:</b>\n"+"\n".join(f"<code>{n}</code>" for n in sorted(notes)))
    else:await msg.edit("<b>No notes!</b>")

@Client.on_message(filters.command(["delnote"],prefix)&filters.me)
async def delnote(_,msg):
    if len(msg.command)<2:return await msg.edit(f"{prefix}delnote [name]")
    db.remove("core.notes",f"n_{msg.command[1].lower()}")
    await msg.edit("<b>Deleted!</b>")

@Client.on_message(filters.command(["fadd"],prefix)&filters.me)
async def fadd(client,msg):
    if len(msg.text.split())<2 or not msg.reply_to_message:return await msg.edit(f"{prefix}fadd [kw] (reply)")
    kw=msg.text.split(maxsplit=1)[1].split()[0].lower()
    try:
        sid=db.get("core.notes","storage_id",0)
        chat=await client.get_chat(sid)
    except:
        chat=await client.create_supergroup("JEK_Storage")
        db.set("core.notes","storage_id",chat.id)
    try:mo=await msg.reply_to_message.forward(chat.id)
    except errors.ChatForwardsRestricted:mo=await msg.reply_to_message.copy(chat.id)
    fdata=db.get("core.filters",f"c_{msg.chat.id}",{})
    fdata[kw]={"cid":chat.id,"mid":mo.id}
    db.set("core.filters",f"c_{msg.chat.id}",fdata)
    await msg.edit(f"<b>Filter <code>{kw}</code> added!</b>")

@Client.on_message(filters.group & ~filters.me)
async def filter_handler(client,msg):
    if not msg.text:return
    fdata=db.get("core.filters",f"c_{msg.chat.id}",{})
    for kw,data in fdata.items():
        if kw in msg.text.lower():
            try:await client.copy_message(msg.chat.id,data["cid"],data["mid"])
            except:pass
            return

@Client.on_message(filters.command(["filters"],prefix)&filters.me)
async def filters_list(_,msg):
    fdata=db.get("core.filters",f"c_{msg.chat.id}",{})
    if fdata:await msg.edit("<b>Filters:</b>\n"+"\n".join(f"<code>{k}</code>" for k in fdata))
    else:await msg.edit("<b>No filters!</b>")

@Client.on_message(filters.command(["fdel"],prefix)&filters.me)
async def fdel(_,msg):
    if len(msg.command)<2:return await msg.edit(f"{prefix}fdel [kw]")
    fdata=db.get("core.filters",f"c_{msg.chat.id}",{})
    if msg.command[1].lower() in fdata:
        del fdata[msg.command[1].lower()]
        db.set("core.filters",f"c_{msg.chat.id}",fdata)
        await msg.edit("<b>Deleted!</b>")
    else:await msg.edit("<b>Not found!</b>")

modules_help["notes"]={"save [name] [reply]*":"Save note","get [name]*":"Get note","notes":"List","delnote [name]*":"Delete","fadd [kw] [reply]*":"Add filter","filters":"List filters","fdel [kw]*":"Delete filter"}
