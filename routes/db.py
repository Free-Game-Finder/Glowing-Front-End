from enum import Flag
from flask_pymongo import pymongo
from utils import default
import os


class database:
    def __init__(self):
        self.db = None
        self.users = None


def db_connect():
    database.db = pymongo.MongoClient(os.getenv("db_url"))
    database.users = database.db.fgn.users


def db_prior_entry(phone, email):
    if database.users.find_one({"phone": phone}) != None:
        return 1
    elif database.users.find_one({"email": email}) != None:
        return 2
    return 0


def db_insert(phone, email, notify_email, notify_text, steam):

    data = {
        "timestamp": default.timestamp(),
        "info_email_sent": False,
        "phone": phone,
        "email": email,
        "notify_email": notify_email,
        "notify_text": notify_text,
        "steam": steam,
        "current_steam": [],
    }

    exist = db_prior_entry(phone, email)

    if exist == 0:
        database.users.insert_one(data)
    elif exist == 1:
        database.users.update_one(
            {"_id": database.users.find_one({"phone": phone})["_id"]},
            {"$set": data},
            upsert=True,
        )
    elif exist == 2:
        database.users.update_one(
            {"_id": database.users.find_one({"email": email})["_id"]},
            {"$set": data},
            upsert=True,
        )
    return
