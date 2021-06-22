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


def db_prior_entry(phone):
    if database.users.find_one({"phone": phone}) == None:
        return False
    return True


def db_insert(phone, email, notify_email, notify_text, steam):
    database.users.insert_one(
        {
            "timestamp": default.timestamp(),
            "info_email_sent": False,
            "phone": phone,
            "email": email,
            "notify_email": notify_email,
            "notify_text": notify_text,
            "steam": steam,
        }
    )
