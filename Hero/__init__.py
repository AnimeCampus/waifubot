# hero/__init__.py

import logging
import time

from pyrogram import Client


API_ID = 14681826  # Your API ID
API_HASH = "add59ab14dbbccf3c92c65ca4477f2fa"  # Your API Hash
BOT_TOKEN = "6306432952:AAFe2CTLQDY7VVvuY9yRKm0FU7kXTgdAutY"  # Your bot token

ERROR_ID = -1001773407390 #private -- Blue Errors log
SUPPORT_CHAT = "JHBots"
SUPPORT_ID = -1001773407390 #devslab

DOWNLOAD_DIRECTORY = "./"

#DB_URI = "postgres://cugocwks:jgpqMTLw2rO6KMwnWDL6kAXwmaVMB1qW@john.db.elephantsql.com/cugocwks"
MONGO_DB = "mongodb+srv://ishikki:ishikki143@userinfo.qud86ys.mongodb.net/?retryWrites=true&w=majority"
MONGO_DB1 = "mongodb+srv://SpyNano:SpyNano@waifubot.igxevb6.mongodb.net/?retryWrites=true&w=majority"

OWNER_ID = [6198858059]

SUDOLIST = [] #REPORTERS
SUPPORTLIST = [] #Inspectors
DEV_LIST = []
DEV_USERS = DEV_LIST + OWNER_ID
SUDO_USERS = SUDOLIST + DEV_USERS #Enforcers
SUPPORT_USERS = SUPPORTLIST + SUDO_USERS #Inspectors


StartTime = time.time()

# enable logging
FORMAT = "[HERO] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("logs.txt"), logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="[%X]",
)

LOGGER = logging.getLogger('[NANO]')
LOGGER.info("WAIFUBOT is waking up...")
LOGGER.info("DEVELOPED by: NANO")


pbot = Client("hero", API_ID, API_HASH, bot_token=BOT_TOKEN)
pbot.start()

bot = pbot.get_me()
BOT_ID = bot.id
if bot.last_name:
    BOT_NAME = bot.first_name + " " + bot.last_name
else:
    BOT_NAME = bot.first_name
BOT_USERNAME = bot.username
