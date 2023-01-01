from pymongo import MongoClient
client = MongoClient('mongodb+srv://jaeyeon:<qwe123>@cluster0.pasxm.mongodb.net/cluster0?retryWrites=true&w=majority')

db = client.hobby

doc = {'name':'bobby','age':21}
db.test.insert_one(doc)