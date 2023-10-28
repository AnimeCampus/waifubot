# addpoke.py

from pyrogram import Client, Filters
from Hero.database.database import PokemonDatabase

# Command handler for /addpoke
@app.on_message(Filters.command("addpoke"))
def add_pokemon(client, message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    # Ensure that only authorized users can add Pokemon (replace with your user IDs)
    authorized_users = [6299128233]  # Replace with your user IDs
    if user_id not in authorized_users:
        client.send_message(chat_id, "You are not authorized to add Pokemon.")
        return

    # Ask for Pokemon details
    client.send_message(chat_id, "Enter Pokemon name:")
    
    @app.on_message(Filters.user(user_id) & ~Filters.command)
    def receive_name(client, message):
        nonlocal name
        name = message.text
        client.send_message(chat_id, "Enter Pokemon image URL:")
        app.remove_handler(receive_name)
        app.add_handler(receive_image_url)
    
    @app.on_message(Filters.user(user_id) & ~Filters.command)
    def receive_image_url(client, message):
        nonlocal image_url
        image_url = message.text
        client.send_message(chat_id, "Enter Pokemon weight (1, 2, or 3):")
        app.remove_handler(receive_image_url)
        app.add_handler(receive_weight)
    
    @app.on_message(Filters.user(user_id) & ~Filters.command)
    def receive_weight(client, message):
        weight = message.text
        try:
            weight = int(weight)
            if weight not in [1, 2, 3]:
                raise ValueError
            # Store the Pokemon data in your database here
            client.send_message(chat_id, f"Pokemon added!\nName: {name}\nImage URL: {image_url}\nWeight: {weight}")
        except ValueError:
            client.send_message(chat_id, "Invalid weight. Please enter 1, 2, or 3.")
        app.remove_handler(receive_weight)
