from pymongo import MongoClient

from src.common.constants import Configuration


class Database:
    def __init__(self):
        self.client = MongoClient(Configuration.MONGODB_URL)
        self.db = self.client.aiq

    def get_collection(self, name: str):
        return self.db[name]
