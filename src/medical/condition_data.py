import json
import os
from pymongo import MongoClient

if __name__ == "__main__":
    m = MongoClient()
    d = m.test_database
    b = d[os.environ['COLLECTION']+'pain2']
    f = json.load(open('out.txt'))
    for i in f.keys():
        for j in f[i]:
            if j == None:
                continue
            else:
                print i
                b.insert({i:j['PubmedArticle']})
