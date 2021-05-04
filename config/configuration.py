import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

dburl = os.getenv("URL")
PORT = os.getenv("PORT")

print(dburl)
if not dburl:
    raise ValueError("No URL MongoDB")

#Connecting with the DB
client = MongoClient("mongodb://localhost/lotr")
