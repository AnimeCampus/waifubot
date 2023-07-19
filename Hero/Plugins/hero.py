import asyncio
import random
from pyrogram import Client, filters
from Hero import pbot
import requests


token = "803115424842504"

url = f"https://superheroapi.com/api/{token}/"


async def get_character(): 
    random_number = random.randint(1, 731)
    newurl = url + f"{random_number}" + "/image"
    r = requests.get(newurl)
    char_obj = r.json()
    character_list = []
    character_list.append(char_obj["id"])
    name = char_obj["name"]
    name = name.lower()
    character_list.append(name)
    character_list.append(char_obj["url"])
    return character_list


# Dictionary to store message counts for each chat group
message_counts = {}

# Dictionary to store the current character for each chat group
active_character = {}


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
    correct_name = active_character[chat_id][1]
    if character_name == correct_name:
        return True
    else:
        return False


# Message handler
@Client.on_message(filters.group)
async def message_handler(client, message):
    chat_id = message.chat.id

    # Check if the chat group has an active character to collect
    if chat_id in active_character:
        if message.text and message.text.startswith("/collect"):
            command, character_name = message.text.split(maxsplit=1)

            answer_c = await is_correct_name(chat_id, character_name)

            if answer_c == True:
                await pbot.send_message(chat_id, f"Correct! You collected {character_name}!")
            else:
                await pbot.send_message(chat_id, f"Wrong name! The character was {character_name}!")

            # Remove the current character from the chat group
            del active_character[chat_id]

    else:
        # Initialize the message count for the group if not already present
        if chat_id not in message_counts:
            message_counts[chat_id] = 0

        # Increment the message count for the group
        message_counts[chat_id] += 1

        # Check if the message count has reached 100
        if message_counts[chat_id] % 10 == 0:

            # Send a message with a picture
            character = await get_character()
            result = await send_picture(chat_id, character[2])
            if result == False:
                character = get_character()
                result = await send_picture(chat_id, character[2])
                if result == False:
                    character = get_character()
                    result = await send_picture(chat_id, character[2])
                    if result == False:
                        pass
                    else:
                        active_character[chat_id] = [character[0], character[1], character[2]]
                else:
                    active_character[chat_id] = [character[0], character[1], character[2]]
            else:
                active_character[chat_id] = [character[0], character[1], character[2]]