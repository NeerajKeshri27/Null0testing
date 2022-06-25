import pymongo

#print("welcome to Pymongo")

client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)


db = client['Suman_db']
collection = db["mysamplecollectionfor Suman_db"]

# Update

prev = {'Name':'Raj Keshri'}
nextt = {'$set':{'Age':27}}
#collection.update_one()
#collection.update_many(prev , nextt)  #updatemany



up = collection.update_many(prev , nextt)  #updatemany
print(up.modified_count) #----------------------------------show how many fields got updated

