
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017") 
db = client.jobs
collection = db.indeed
try: db.command("serverStatus")
except Exception as e: print(e)
else: print(collection)

test = [{'a':"hello"},'b','c']

collection.insert_one(test[1])