from Hero.database import cwdb, chdb, adb
import random


async def get_char(anime_id, char_type):
    if char_type == 1:
        char_list = cwdb.find({"anime_id": anime_id})
        total = cwdb.count_documents({"anime_id": anime_id})
    elif char_type == 2:
        char_list = chdb.find({"anime_id": anime_id})
        total = chdb.count_documents({"anime_id": anime_id})
    else:
        return False, None
    

    char_no = random.randint(1, total)

    for char in char_type:
        if char["_id"] == char_no:
            return True, char


    return False, None
        

