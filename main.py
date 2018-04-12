import pymongo
from pymongo import MongoClient

myClient = MongoClient()

db = myClient.mydb

users = db.users

results = (users.find())

for result in results:

    print(result["username"])
    print(result["password"] + "\n")

