# connection to MongoDB Instance
import pymongo as pm
client = pm.MongoClient()

# Establising connection to compass
client = pymongo.MongoClient('localhost', 27017)

client.list_database_names()
db = client['rohitDB']
db.list_collection_names()

# Declaring documents
document1 = {"_id": 57, 'Country': 'USA', 'Continent': 'America', 'Mcode': 01}
document2 = {"_id": 56, 'Country': 'Aus', 'Continent': 'Aus', 'Mcode': 03}

collection.insert_many([document1, document2])

document3 = {"_id": 55, 'Country': 'India', 'Continent': 'Asia', 'Mcode': 91}
document4 = {"_id": 58, 'Country': 'India', 'Continent': 'Outer', 'Mcode': 91}

collection.insert_one(document3)

collection.delete_one({})

collections.delete_many({'Country': 'USA', 'Country': 'Australia'})
print(collection.find().count())

for i in collection.find():
    print(i)

print(collection.find_one())
print(collection.find()[0])

for info in collection.find().limit(1):
    print(info)

collection.update_one({'_id': 55}, {'$set': {'Mcode': 25}})
collection.update_many({'Country': 'India'}, {'$set': {'Mcode': 05}})
collection.drop()
