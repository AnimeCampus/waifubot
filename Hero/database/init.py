from pymongo import MongoClient

from Hackia import MONGO_DB


client = MongoClient(MONGO_DB)

db = client["Hackia"]

udb = db["users_db"]
#gdb = db["groups_db"]
#fban_db = db["fban_db"]
misc_db = db["misc_db"]
event_db = db["event_db"]


def get_user_list():
    return [x for x in udb.find()]
