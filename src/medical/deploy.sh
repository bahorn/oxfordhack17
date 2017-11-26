#!/bin/sh
echo "db.$COLLECTION.createIndex({name:"text",surname:"text",gender:"text",birthdate:"text"})" | mongo
