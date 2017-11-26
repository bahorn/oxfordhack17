#!/bin/sh
python install_to_mongo.py
echo "db.$COLLECTION.createIndex({name:"text",surname:"text",gender:"text",birthdate:"text"})" | mongo
