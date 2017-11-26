import os
import json
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    db = client.test_database
    all = db.data
    dir = "../../../../SomeData/chall_1/records/"
    for file in os.listdir(dir):
        f = json.loads(open(dir+file).read())
        all.insert_one(f)
