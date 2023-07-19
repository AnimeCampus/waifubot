import asyncio
import random
from pyrogram import Client, filters
from Hero import pbot


# Dictionary to store message counts for each chat group
message_counts = {}

# Function to send a message in a group
async def send_message(chat_id, text):
    await pbot.send_message(chat_id, text)

# Function to send a picture in a group
async def send_picture(chat_id, file_id):
    await pbot.send_photo(chat_id, file_id)

# Message handler
@Client.on_message(filters.group)
async def message_handler(client, message):
    chat_id = message.chat.id

    # Initialize the message count for the group if not already present
    if chat_id not in message_counts:
        message_counts[chat_id] = 0

    # Increment the message count for the group
    message_counts[chat_id] += 1

    # Check if the message count has reached 100
    if message_counts[chat_id] % 10 == 0:
        # Send a message with a picture (you can replace with your own picture logic)
        await send_message(chat_id, "Congratulations! You've sent 10 messages in this group.")
        del message_counts[chat_id]

# Run the bot
async def main():
    await app.start()
    await app.idle()

if __name__ == "__main__":
    asyncio.run(main())
