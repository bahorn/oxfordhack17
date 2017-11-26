import os
import pubmed
import time
import json
from Bio import Entrez
from pymongo import MongoClient

if __name__ == "__main__":
    pb = pubmed.PubMed("b@horn.uk")
    mongo = MongoClient()
    db = mongo.test_database
    conn = db[os.environ['COLLECTION']]
    conditions = {}
    for i in conn.find({}):
        for j in i['conditions']:
            conditions[j['condition']] = True
    data = {}
    for i in conditions.keys():
        print i
        t = pb.searchArticles(i)
        if t != None:
            if i not in data:
                data[i] = [t]
            else:
                data[i] += [t]
        else:
            data[i] = [None]
        time.sleep(0.5)
    f = open('out.txt','w')
    f.write(json.dumps(data))
    f.close()
