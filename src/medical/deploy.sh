#!/bin/sh
python condition_data.py
python install_to_mongo.py
printf "use test_database\ndb.$COLLECTION.createIndex({name:\"text\",surname:\"text\",gender:\"text\",birthdate:\"text\"})" | mongo
