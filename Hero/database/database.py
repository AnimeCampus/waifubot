from pymongo import MongoClient

class PokemonDatabase:
    def __init__(self):
        # Initialize the MongoDB client and database
        self.client = MongoClient("mongodb+srv://vortex:yNNrzMsR0BAiI4iY@cluster0.8sizo.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client["pokemon_db"]
        self.collection = self.db["pokemon_collection"]

    def add_pokemon(self, name, image_url, weight):
        # Insert a new Pokemon into the collection
        pokemon_data = {
            "name": name,
            "image_url": image_url,
            "weight": weight
        }
        self.collection.insert_one(pokemon_data)

    def get_pokemon(self, name):
        # Retrieve a Pokemon by name from the collection
        pokemon = self.collection.find_one({"name": name})
        return pokemon

    def get_all_pokemon(self):
        # Retrieve all Pokemon from the collection
        pokemon_list = list(self.collection.find())
        return pokemon_list

    def update_pokemon(self, name, new_name, new_image_url, new_weight):
        # Update an existing Pokemon's data
        update_data = {
            "$set": {
                "name": new_name,
                "image_url": new_image_url,
                "weight": new_weight
            }
        }
        self.collection.update_one({"name": name}, update_data)

    def delete_pokemon(self, name):
        # Delete a Pokemon by name from the collection
        self.collection.delete_one({"name": name})
