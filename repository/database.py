import sys


from repository.mongo.MongoDB import *


USERNAME = sys.argv[1]
PASS = sys.argv[2]
DB_NAME = sys.argv[3]
COLLECTIONS = { "koku": DEFAULT}

URL = f"mongodb+srv://{USERNAME}:{PASS}@cluster0.hhjqb.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
CONNECTION = MongoDB(database=DB_NAME, docs=COLLECTIONS, url=URL)
