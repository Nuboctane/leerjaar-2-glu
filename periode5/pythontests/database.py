from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('mongodb+srv://cvanh:jemoederwhahaha@cluster0.d5rr0.mongodb.net/test?authSource=admin&replicaSet=atlas-1ipgz2-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true')
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)