from pymongo import MongoClient

MONGO_URL = 'mongodb://localhost:27017/'
mongo_client = MongoClient(MONGO_URL)

connections_db = mongo_client.connections


