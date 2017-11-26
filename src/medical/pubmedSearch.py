import json
import csv
import time
from Bio import Entrez

class PubMed:
    def __init__(self, email):
        self.email = email
    def fetch_details(self, ids):
        Entrez.email = self.email
        handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=','.join(ids))
        return Entrez.read(handle)


pm = PubMed("b@horn.uk")
with open('mesh_sample.csv') as csvfile:
    reader = csv.reader(csvfile)
    all = []
    for row in reader:
        if row[0] == 'pmid':
            continue
        all += [row[0]]
    n = 5
    endlist = [[] for _ in range(n)]
    for index, item in enumerate(all):
        endlist[index % n].append(item)
    for allSubset in endlist:
        for i in pm.fetch_details(allSubset)['PubmedArticle']:
            currDoc = {}
            for j in i['MedlineCitation']['MeshHeadingList']:
                currDoc[str(j['DescriptorName'])] = {
                    'descriptor_id':j['DescriptorName'].attributes['UI'],
                    'MajorTopic':j['DescriptorName'].attributes['MajorTopicYN'],
                    'value':map(str,j['QualifierName'])
                }
            for j in currDoc.keys():
                print ",".join([
                    i['MedlineCitation']['PMID'],
                    currDoc[j]['descriptor_id'],
                    j.replace(',','\\,'),
                    str(currDoc[j]['MajorTopic']),
                    str(currDoc[j]['value'])])
            time.sleep(0.4)
