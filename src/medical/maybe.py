import os
import re
import json
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    db = client.test_database
    all = db.realdata
    dir = "../../../../SomeData/chall_1/records/"
    all = []
    for file in os.listdir(dir):
        f = json.loads(open(dir+file).read())
        person = {}
        conditions = []
        for i in f['entry']:
            if 'Patient' in i['resource']['resourceType']:
                #a = re.match(r"([a-zA-Z]+)([0-9]+)",
                #        i['resource']['name'][0]['family'])
                a = re.match(r"([a-zA-Z]+)([0-9]+)",
                        ''.join(e for e in i['resource']['name'][0]['family'] if e.isalnum()))
                try:
                    person['surname'] = a.group(1)+' '+a.group(2)
                except:
                    person['surname'] = i['resource']['name'][0]['family']
                #person['name'] = 
                a = re.match(r"([a-zA-Z]+)([0-9]+)",
                    " ".join(i['resource']['name'][0]['given']))
                person['name'] = a.group(1)+' '+a.group(2)
                person['birthdate'] = i['resource']['birthDate']
                person['gender'] = i['resource']['gender']
                if 'deceasedDateTime' in i['resource']:
                    person['deceasedDateTime'] = i['resource']['deceasedDateTime']
                #print i['resource']
            if 'Condition' in i['resource']['resourceType']:
                conditions += [{'condition':i['resource']['code']['text'],
                    'onset':i['resource']['onsetDateTime']}]
            #try:
            #    if i['resource']['resourceType'] not in ['Immunization',
            #            'Observation']:
            #        print i['resource']
            #    #print i['resource']['class']
            #except:
            #    pass
        person['conditions'] = conditions
        all += [person]
        #all.insert_one(person)
    print json.dumps(all)
