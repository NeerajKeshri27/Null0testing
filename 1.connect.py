import pymongo


#print("welcome to Pymongo")

client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)


db = client['Suman_db']

collection = db["mydb Suman_db"]


# all database names
# a = client.database_names()
# print(a)


