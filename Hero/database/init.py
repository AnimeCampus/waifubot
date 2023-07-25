from pymongo import MongoClient

from Hero import MONGO_DB


client = MongoClient(MONGO_DB)

db = client["herodb"]

udb = db["userdb"]


def get_user_list():
    return [x for x in udb.find()]



"""
udb format:

udb = {
    "_id": "user_id",
    "heros": []
}
"""