from Hero.database import udb


def register(user_id):
    udb_dict = {
        "_id": user_id,
        "heros": []
    }
    udb.insert_one(udb_dict)


def adduser(user_id, heroid):
    udb_dict = {
        "_id": user_id,
        "heros": [heroid]
    }
    udb.insert_one(udb_dict)


def addhero(user_id, heroid):
    data = udb.find_one({"_id": user_id})
    if data:
        udb.update_one({"_id": user_id}, {"$push": {"heros": heroid}})
    else:
        adduser(user_id, heroid)


def info(user_id):
    data = udb.find_one({"_id": user_id})
    if data:
        heros = data["heros"]
        return heros
    else:
        register(user_id)
        return False

