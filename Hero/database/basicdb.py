from Hero.database import udb


def register(user_id):
    udb_dict = {
        "_id": user_id,
        "heros": []
    }
    udb.insert_one(udb_dict)


def adduser(user_id, heroid, hero_name):
    udb_dict = {
        "_id": user_id,
        "heros": [[heroid, hero_name]]
    }
    udb.insert_one(udb_dict)


def addhero(user_id, heroid, hero_name):
    data = udb.find_one({"_id": user_id})
    if data:
        udb.update_one({"_id": user_id}, {"$push": {"heros": [heroid, hero_name]}})
    else:
        adduser(user_id, heroid, hero_name)


def info(user_id):
    data = udb.find_one({"_id": user_id})
    if data:
        heros = data["heros"]
        return heros
    else:
        register(user_id)
        return False


def addfav(user_id, hero_id):
