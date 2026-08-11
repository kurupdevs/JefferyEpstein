"""JefferyEpstein Userbot."""
import os,asyncio,logging
from pyrogram import Client
from config import API_ID,API_HASH

logging.basicConfig(level=logging.INFO,format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger=logging.getLogger(__name__)

app=Client("jeff",api_id=API_ID,api_hash=API_HASH)

async def main():
 try:
  logger.info("Starting JefferyEpstein...")
  await app.start()
  logger.info("Running!")
  await asyncio.Event().wait()
 except Exception as e:logger.error(f"Fatal: {e}")

if __name__=="__main__":asyncio.run(main())
