import asyncio
import random
from pyrogram import Client, filters
from Hero import pbot
from Hero.database.basicdb import addhero
from Hero.database.characterdb import get_char
from Hero.database import adb
import requests
import random


TOTAL_ANIME =  adb.count_documents({})


async def get_character():
    anime_id = random.randint(1, TOTAL_ANIME)
    char_type = random.choice([1, 2])
    result, char = await get_char(anime_id, char_type)
    if result == False:
        return None
    else:
        return char


# Dictionary to store message counts for each chat group
message_counts = {}

# Dictionary to store the current character for each chat group
active_character = {}

active_characrter_count = {}


async def send_picture(chat_id, character_url):
    try:
        await pbot.send_photo(
            chat_id=chat_id,
            photo=character_url,
            caption=f"A character has appeared, collect it by giving the correct name using /collect command"
        )
        return True
    except:
        return False


async def is_correct_name(chat_id, character_name):
    character_name = character_name.lower()
    char_name = character_name.split(" ")[0]

    correct_name = active_character[chat_id]["name"]
    correct_name = correct_name.lower()

    char_id = active_character[chat_id]["_id"]

    names = correct_name.split(" ")

    if char_name in names:
        anime_id = active_character[chat_id]["anime_id"]
        return True, correct_name, char_id, anime_id
    else:
        return False, correct_name, char_id, anime_id


# Message handler
@Client.on_message(filters.group)
async def message_handler(client, message):
    chat_id = message.chat.id

    # Check if the chat group has an active character to collect
    if chat_id in active_character:

        if chat_id not in active_characrter_count:
            active_characrter_count[chat_id] = 0

        active_characrter_count[chat_id] += 1


        if active_characrter_count[chat_id] % 10 == 0:

            name = active_character[chat_id]["name"]
            await client.send_message(chat_id, f"character flew away!!\nCorrect name was {name}")

            del active_character[chat_id]
            del active_characrter_count[chat_id]
            return 


        if message.text and message.text.startswith("/collect"):
            user_id = message.from_user.id
            command, character_name = message.text.split(maxsplit=1)

            answer_c, correct_name, char_id, anime_id = await is_correct_name(chat_id, character_name)
            
            if answer_c == True:
                addhero(user_id, char_id, correct_name, anime_id)
                await pbot.send_message(chat_id, f"Correct!!!!\nYou collected {correct_name}!")
                del active_character[chat_id]
                del active_characrter_count[chat_id]
            else:
                await pbot.send_message(chat_id, f"Wrong name!!")

    else:
        # Initialize the message count for the group if not already present
        if chat_id not in message_counts:
            message_counts[chat_id] = 0

        # Increment the message count for the group
        message_counts[chat_id] += 1

        # Check if the message count has reached 100
        if message_counts[chat_id] % 10 == 0:

            
            character = await get_character()
            if character == None:
                return
            

            # Send a message with a picture
            result = await send_picture(chat_id, character["img"])
            if result == False:
                return

            active_character[chat_id] = [character["_id"], character["name"], character["anime_id"]]

            await pbot.send_message(chat_id, text=f"{active_character}")