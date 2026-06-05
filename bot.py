import sys, glob, importlib, logging, logging.config, pytz, asyncio
from pathlib import Path
import os, math
from pyrogram.raw.all import layer
from pyrogram.errors import BadRequest, Unauthorized

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

from pyrogram import Client, idle 
from pyromod import listen
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import *
from utils import temp
from typing import Union, Optional, AsyncGenerator
from Script import script 
from datetime import date, datetime 
from aiohttp import web
from plugins import web_server
# bot login info
from bot import MiviesFatherBot
from util.keepalive import ping_server
from bot.clients import initialize_clients
from datetime import datetime
from pytz import timezone

ppath = "plugins/*.py"
files = glob.glob(ppath)
MiviesFatherBot.start() 
loop = asyncio.get_event_loop()
PORT = "8080"

async def start():
    print('\n')
    print('Initalizing Your Bot')
    bot_info = await MiviesFatherBot.get_me()
    MiviesFatherBot.username = bot_info.username
    await initialize_clients()
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem.replace(".py", "")
            plugins_dir = Path(f"plugins/{plugin_name}.py")
            import_path = "plugins.{}".format(plugin_name)
            spec = importlib.util.spec_from_file_location(import_path, plugins_dir)
            load = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(load)
            sys.modules["plugins." + plugin_name] = load
            print("Miviesfather Imported => " + plugin_name)
    if ON_HEROKU:
        asyncio.create_task(ping_server())
    b_users, b_chats = await db.get_banned()
    temp.BANNED_USERS = b_users
    temp.BANNED_CHATS = b_chats
    await Media.ensure_indexes()
    me = await MiviesFatherBot.get_me()
    temp.ME = me.id
    temp.U_NAME = me.username
    temp.B_NAME = me.first_name
    MiviesFatherBot.username = '@' + me.username
    logging.info(LOG_STR)
    logging.info(script.LOGO)
    tz = pytz.timezone('Asia/Kolkata')
    today = date.today()
    now = datetime.now(tz)
    time = now.strftime("%H:%M:%S %p")
    await MiviesFatherBot.send_message(chat_id=LOG_CHANNEL, text=script.RESTART_TXT.format(today, time))
    app = web.AppRunner(await web_server())
    await app.setup()
    bind_address = "0.0.0.0"
    await web.TCPSite(app, bind_address, PORT).start()
    await idle()

if __name__ == '__main__':
    try:
        loop.run_until_complete(start())
    except KeyboardInterrupt:
        logging.info('Service Is Stop Sweety 🚏')
        
# Credit @Miviesfather.
# Please Don't remove credit.
# Miviesfather Forever !
# Thanks You For Help Us In This Amazing Creativity 
# Thanks You For Giving Me Credit @Miviesfather
# For Any ERROR Please Contact Me -> Telegram ->@Miviesfather & Insta @Miviesfather
# Please Love & Support 💗💗🙏
