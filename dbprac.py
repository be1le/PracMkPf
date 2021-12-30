from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:@cluster0.tv1oz.mongodb.net/Cluster0retryWrites=true&w=majority')
db = client.dbsparta

doc = {
    'name' : 'bob',
    'age' : 27
}