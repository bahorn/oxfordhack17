from pymongo import MongoClient
import sys
import json

if __name__ == "__main__":
    m = MongoClient()
    d = m.test_database
    a = d[sys.argv[1]]
    f = json.loads(open('dat.txt').read())
    for i in f:
        a.insert(i)
