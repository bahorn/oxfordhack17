from flask import Flask, request
from flask_cors import CORS
import json
import os
from pymongo import MongoClient
app = Flask(__name__)
CORS(app)

@app.route("/search")
def search():
    query = request.args.get("q")
    if query == None:
        return "{'err':'nothing'}"
    isDead = False
    if request.args.get("isDead") != None:
        if request.args.get("isDead").lower() == 'true':
            isDead = True
    limit = request.args.get("limit")
    if request.args.get("limit") != None:
        limit = int(limit)
    client = MongoClient()
    db = client.test_database
    collection = db[os.environ['COLLECTION']]
    output = []
    realQuery = {"$text": {"$search": query}}
    if isDead == True:
        realQuery['deceasedDateTime'] = {"$exists": True}
    result = collection.find(realQuery)
    if limit != None:
        result.limit(limit)
    for item in result:
        temp = item
        temp['_id'] = None
        output += [temp]
    return json.dumps(output)

@app.route("/")
def hello():
    return "backendAPI"
