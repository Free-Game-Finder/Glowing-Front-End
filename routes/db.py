from flask_pymongo import pymongo
import os

class database:
    def __init__(self):
        self.db = None
        self.users = None


def db_connect():
    database.db = pymongo.MongoClient(os.getenv('SECRET_KEY',))
    database.users = database.db.fgn.users

def db_prior_entry(phone):
    if database.users.find_one({"phone": phone}) == None:
        return False
    return True

def db_insert(phone, steam):
    database.users.insert_one({"phone": phone, "steam": steam})
