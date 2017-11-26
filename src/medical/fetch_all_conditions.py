import os
import pubmed
from Bio import Entrez
from pymongo import MongoClient

if __name__ == "__main__":
    pb = pubmed.PubMed("b@horn.uk")
    print pb.searchArticles('Cardiac Arrest')

if __name__ == "__mbin__":
    mongo = MongoClient()
    db = mongo.test_database
    conn = db[os.environ['COLLECTION']]
    conditions = {}
    for i in conn.find({}):
        for j in i['conditions']:
            conditions[j['condition']] = True

    for i in conditions.keys():
        print i
