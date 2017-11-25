import os
import sys
from os.path import join, dirname
from dotenv import load_dotenv
from azure.storage.blob import BlockBlobService, ContentSettings

class azureObjectStorage:
    def __init__(self, account_name, account_key):
        self.blobService = BlockBlobService(account_name=account_name,
            account_key=account_key)
    def put(self, container, key, value, type='text/plain'):
        if isinstance(value, str):
            self.blobService.create_blob_from_text(container, key, value, 
                content_settings=ContentSettings(type))
        elif type(value) == file:
            self.blobService.create_blob_from_steam(container, key, value, 
                content_settings=ContentSettings(type))
        else:
            raise TypeError

        
if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    account_name = os.environ['BLOB_NAME']
    key = os.environ['BLOB_KEY1']
    obj = azureObjectStorage(account_name, key)
    obj.put('content', 'test.txt', 'AAAA')
