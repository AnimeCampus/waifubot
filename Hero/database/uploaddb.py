from Hero.database import cdb


def upload_waifu(waifu_img, waifu_id, waifu_name, anime_id):
    waifu_id = int(waifu_id)
    data = {
        "_id": waifu_id,
        "name": waifu_name,
        "img": waifu_img,
        "anime_id": anime_id
    }
    cdb.insert_one(data)


