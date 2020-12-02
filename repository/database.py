import sys
import os

from repository.mongo.MongoDB import *


USERNAME = os.environ.get("MONGOUSER")
PASS = os.environ.get("PASS")
DB_NAME = os.environ.get("DB_NAME")
COLLECTIONS = { "koku": DEFAULT}

URL = f"mongodb+srv://{USERNAME}:{PASS}@cluster0.hhjqb.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
CONNECTION = MongoDB(database=DB_NAME, docs=COLLECTIONS, url=URL)
