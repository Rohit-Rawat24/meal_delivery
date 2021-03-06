# connection to MongoDB Instance
'''
Importing pymongo
'''
import json
import pymongo as pm
client = pm.MongoClient()

# Establising connection to compass
client = pm.MongoClient('localhost', 27017)

client.list_database_names()
db = client['mealsinfo']
db.list_collection_names()
meal_data = db["collection"]

with open("meal_info.json") as f:
    file_data = json.load(f)
meal_data.insert_many(file_data)

# Implementing find_one

print(meal_data.find_one())


#For whole record

for i in meal_data.find():
    print(i)

#Inserting one document using insert_one 

document1 = {'_id': 98195, 'category': 'Extras', 'cuisine': 'Indian' }

meal_data.insert_one(document1)

#Inserting multi document using insert_many 

document2 = {'_id': 98196, 'category': 'Starters', 'cuisine': 'Indian' }
document3 = {'_id': 98197, 'category': 'Desert', 'cuisine': 'Italian' }

meal_data.insert_many([document2,document3])

#Updating one record

meal_data.update_one({'_id': 98195}, {'$set': {'cuisine': 'Thai'}})

#updating multi_record
meal_data.update_many({'category': 'Starters'}, {'$set': {'cuisine': 'Indian'}})

#limit

for i in meal_data.find().limit(5):
    print(i)

#skip

for i in meal_data.find().skip(5).limit(5):
    print(i)
    
#delete_one

meal_data.delete_one({})

#delete_many

meal_data.delete_many({'category': 'Starters', 'cuisine': 'Thai'})


#counting total no. of documents

print(meal_data.find().count())

#drop
meal_data.drop()
