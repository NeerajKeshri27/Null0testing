import pymongo

#print("welcome to Pymongo")

client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)


db = client['Suman_db']
collection = db["mydb Suman_db"]


"""Insert One"""
# document = {'name':'Neeraj' , 'age':28}
# collection.insert_one(document)

# doc2 = {'name':'Vikash' , 'age':23 , 'div':'VI'}
# collection.insert_one(doc2)


"""Insert Many"""

insertThese = [
    {'_id':1,'Name':'Suman Kumar' , 'Age':28 , 'Addr':'Gardanibagh'},
    {'_id':2,'Name':'Raj Keshri' , 'Age':23 , 'Addr':'Ashiana'},
    # {'_id':3,'Name':'Vikash Sharma' , 'Age':24 , 'Addr':'BaileyRoad'},
    # {'_id':4,'Name':'Shantanu Singh' , 'Age':30 , 'Addr':'Kankarbagh'}
]

collection.insert_many(insertThese)

