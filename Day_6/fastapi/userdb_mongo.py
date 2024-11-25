from pydantic import BaseModel
from typing import Optional
from bson.objectid import ObjectId


class User(BaseModel):
    id: Optional[str]
    name: str
    password: str
    fullname: Optional[str]

class UserOpt(BaseModel):
    id: Optional[str]
    name: Optional[str]
    password: Optional[str]
    fullname: Optional[str]

from pymongo import MongoClient

class MongoConfig:
    dbname = "userdb_test"
    collection_name = "users"
    hostname = "localhost"
    port = 27017

class UserDB:  # Implements an Adaptor pattern
    def __init__(self, config):
        self.config = config()

    def connect(self):
        self.conn = MongoClient(host=self.config.hostname, port=self.config.port)
        self.database = self.conn[self.config.dbname]
        self.collection = self.database[self.config.collection_name]

    def create_schema(self):
        pass
 
    def add(self, user: User):
        self.collection.insert_one(user.dict())

    def get(self, username=None):
        if username is None:
            for user in self.collection.find():
                u = User(**user)
                #u.id = user["_id"]
                yield u
        else:
            yield User(**self.collection.find_one({"name": username}))

    def delete(self, username):
        self.collection.delete_one({"name": username})

    def replace(self, username, user):
        self.collection.replace_one({"name": username}, user.dict())

    def update(self, username, user):
        self.collection.update_one({"name": username}, { "$set": user.dict() })
