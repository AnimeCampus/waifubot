from Hero.database import udb


def register(user_id):
    udb_dict = {
        "_id": user_id,
        "heros": []
    }
    udb.insert_one(udb_dict)


def adduser(user_id, heroid, hero_namem, anime_id):
    udb_dict = {
        "_id": user_id,
        "heros": [[heroid, hero_name, anime_id]]
    }
    udb.insert_one(udb_dict)


def addhero(user_id, heroid, hero_name, anime_id):
    data = udb.find_one({"_id": user_id})
    if data:
        udb.update_one({"_id": user_id}, {"$push": {"heros": [heroid, hero_name, anime_id]}})
    else:
        adduser(user_id, heroid, hero_name, anime_id)


def info(user_id):
    data = udb.find_one({"_id": user_id})
    if data:
        heros = data["heros"]
        return heros
    else:
        register(user_id)
        return False


def addfav(user_id, hero_id):
    hm = 2


def checktrade(hero_id, user_id):
    hero_id = int(hero_id)
    user_id = int(user_id)
    data = udb.find_one({"_id": user1})
    if data:
        heroes = data["heros"]
        for i in heroes:
            if hero_id in i:
                return True, i[1]
    
    return False, None


def trade(hero1, heroname1, user1, hero2, heroname2, user2):
    hero1 = int(hero1)
    user1 = int(user1)
    hero2 = int(hero2)
    user2 = int(user2)
    
    udb.update_one({"_id": user1}, {"$push": {"heros": [hero2, heroname2]}})
    udb.update_one({"_id": user2}, {"$push": {"heros": [hero1, heroname1]}})
    
    udb.update_one({"_id": user1}, {"$pull": {"heros": [hero1, heroname1]}})
    udb.update_one({"_id": user2}, {"$pull": {"heros": [hero2, heroname2]}})
