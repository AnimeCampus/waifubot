import asyncio
import random
from pyrogram import Client, filters
from Hero import pbot
from Hero.database.basicdb import info
import requests


token = "803115424842504"

url = f"https://superheroapi.com/api/{token}/"


async def get_character(hero_id): 
    newurl = url + f"{hero_id}" + "/image"
    r = requests.get(newurl)
    char_obj = r.json()
    name = char_obj["name"]
    return name


@Client.on_message(filters.command("team"))
async def harem_grp(client, message):
    user_id = message.from_user.id
    data = info(user_id)
    if data == False:
        await message.reply_text("You havent yet collected any heroes!!")
        return
    
    if len(data) == 0:
        await message.reply_text("You havent yet collected any heroes!!")
        return
    
    text = f"Hello {message.from_user.first_name},\n\nYour Heros team:\n"
    count = 0
    for hero in data:
        count = count + 1
        hero_id = hero[0]
        hero_name = hero[1]
        text += f"**{count}.** `{hero_id}`\n-> {hero_name}\n"
    
    await message.reply_text(text)
