from pymongo import MongoClient
import sys
import json
import os

if __name__ == "__main__":
    m = MongoClient()
    d = m.test_database
    a = d[os.environ['COLLECTION']]
    f = json.loads(open('dat.txt').read())
    for i in f:
        a.insert(i)
