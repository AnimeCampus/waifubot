from pymongo import MongoClient

from Hero import MONGO_DB, MONGO_DB1


client = MongoClient(MONGO_DB)

db = client["herodb"]

udb = db["userdb"]


character_db = MongoClient(MONGO_DB1)

cwdb = client["characterdb"]["waifudb"]
chdb = client["characterdb"]["husbandodb"]
adb = client["characterdb"]["animedb"]


def get_list(choose_db):
    all_char = choose_db.find({})
    list_char = []
    for char in all_char:
        list_char.append(char)

    return list_char

