from Hero.database import cwdb, chdb, adb


def upload_waifu(waifu_img, waifu_id, waifu_name, anime_id):
    waifu_id = int(waifu_id)
    anime_id = int(anime_id)
    data = {
        "_id": waifu_id,
        "name": waifu_name,
        "img": waifu_img,
        "anime_id": anime_id
    }
    cwdb.insert_one(data)


def upload_husbando(husbando_img, husbando_id, husbando_name, anime_id):
    husbando_id = int(husbando_id)
    anime_id = int(anime_id)
    data = {
        "_id": husbando_id,
        "name": husbando_name,
        "img": husbando_img,
        "anime_id": anime_id
    }
    chdb.insert_one(data)


def upload_anime(anime_id, anime_name):
    anime_id = int(anime_id)
    data = {
        "_id": anime_id,
        "name": anime_name
    }
    adb.insert_one(data)
