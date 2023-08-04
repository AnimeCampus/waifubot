from pymongo import MongoClient

from Hero import MONGO_DB, MONGO_DB1


client = MongoClient(MONGO_DB)

db = client["herodb"]

udb = db["userdb"]


character_db = MongoClient(MONGO_DB1)

cdb = client["characterdb"]["waifudb"]



def get_user_list():
    return [x for x in udb.find()]

