import pymongo
client = pymongo.MongoClient("mongodb+srv://ankit:asdf@ankit.btgnnqp.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['test']
coll = db1['test1']
coll.insert_one(d)
