import os
import json
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    db = client.test_database
    all = db.realdata
    dir = "../../../../SomeData/chall_1/records/"
    for file in os.listdir(dir):
        f = json.loads(open(dir+file).read())
        person = {}
        conditions = []
        for i in f['entry']:
            if 'Patient' in i['resource']['resourceType']:
                person['surname'] = i['resource']['name'][0]['family']
                person['name'] = " ".join(i['resource']['name'][0]['given'])
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
        print person
        #all.insert_one(person)
