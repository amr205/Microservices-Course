from pymongo import MongoClient
import json
from bson import ObjectId
from django.conf import settings

def get_db_handle(
    db_name=settings.MONGODB_DATABASE,
    host=settings.MONGODB_HOST,
    port=settings.MONGODB_PORT,
    username=settings.MONGODB_USER,
    password=settings.MONGODB_PASSWORD
    ):
    client = MongoClient(host=host,
                        port=int(port),
                        username=username,
                        password=password)
    db_handle = client[db_name]
    return db_handle, client

class MongoJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

def format_json(results):
    return json.loads(MongoJSONEncoder().encode(results))