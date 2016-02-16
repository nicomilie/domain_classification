import pymongo
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['Domains']
collection_features = db['Features']

# print collection_features.find_one()
f = open('benign__alexa_quantcast_top_100k.txt', 'r')
# f = open('nico.txt', 'r')
for line in f:
    line = line[:-1]
    collection_features.update({"_id": line}, {"$set": { "List": "benign__alexa"}})

#
# f.close()