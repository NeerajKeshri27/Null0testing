import pymongo

#print("welcome to Pymongo")

client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)


db = client['Suman_db']
collection = db["mysamplecollectionfor Suman_db"]

"""Find One"""
find_one = collection.find_one({'Name':'Raj Keshri'})
print(find_one)

"""Find all"""
# find_all = collection.find({'name':'Suman Kumar'})
# for i in find_all:
#     print(i)



