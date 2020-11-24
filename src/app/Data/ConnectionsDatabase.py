from pymongo import MongoClient
import os
MONGO_URL = os.getenv('MONGO_URL')
mongo_client = MongoClient(MONGO_URL)
db = mongo_client.meetme_db

connections_col = db.connections
matches_col = db.matches

