import asyncio, logging
from pyrogram import Client

logger=logging.getLogger(__name__)

async def progress(cur:int,total:int,msg,action:str="Processing"):
 pct=cur*100/total
 bar="█"*int(pct/5)+"░"*(20-int(pct/5))
 await msg.edit(f"**{action}:** [{bar}] {pct:.1f}%")

async def safe_edit(msg,text:str):
 try:await msg.edit(text)
 except Exception as e:logger.warning(f"Edit failed: {e}")

async def safe_del(msg):
 try:await msg.delete()
 except Exception as e:logger.warning(f"Delete failed: {e}")

def parse_args(text:str,n:int=2):
 p=text.split(None,n)
 return p[1:]if len(p)>1 else[]
