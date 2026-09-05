from pymongo import MongoClient

def get_sellr_client(uri: str = "mongodb://localhost:27017", db_name: str = "f1ndr_sellr"):
    client = MongoClient(uri)
    return client[db_name]
