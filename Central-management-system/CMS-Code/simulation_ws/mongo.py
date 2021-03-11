import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://ron:1234@cluster0.vzfu9.mongodb.net/fof_database?retryWrites=true&w=majority")
db = cluster["fof_database"]
collection = db["test"]
post = {"_id":1, "name":"aon","score": 5}
collection.insert_one(post)



WIP



database = input {'please name the database you want to query'}
quer = input {'please name the query type'}
value = input {'please name the value'}
creat ben = query{'collection1', 'delete', 5};
ben.executeQuery{}