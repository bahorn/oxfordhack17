import os
import sys
import boto3
import requests
from os.path import join, dirname
from dotenv import load_dotenv

if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    blobstorage = os.environ['BLOBSTORAGE']
    apikey = os.environ['BLOB_KEY1']
    apiconn = os.environ['BLOB_CONN']
    session = boto3.session.Session()
    client = boto3.resource('s3',
            endpoint_url=blobstorage,
            aws_access_key_id='7b924cdb-762e-45df-9cbf-4542b95dc912',
            aws_secret_access_key=apikey)
    client.Object('content', 'test.txt').put(ACL='public-read', Body="AAAAAAA")

