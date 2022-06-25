import pymongo

#print("welcome to Pymongo")

client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)


db = client['Neeraj_db']
collection = db["mysamplecollectionfor Neeraj_db"]

# Delete one

record_ = {'name':'Neeraj'}
collection.delete_one(record_)


# Delete Many

rec = {'name':'Neeraj'}

up = collection.delete_many(rec)
print(up.deleted_count)










