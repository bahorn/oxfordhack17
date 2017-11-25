import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv

def queryComputerVision(url, apikey=None):
    endpoint = "https://northeurope.api.cognitive.microsoft.com/vision/v1.0"
    headers = {'Ocp-Apim-Subscription-Key': apikey}
    data = {'url':url}
    r = requests.post(endpoint+"/analyze?visualFeatures=tags",
            headers=headers, json=data)
    if r.status_code == 200:
        return r.json()
    else:
        return None

if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    apikey = os.environ['KEY1']
    #url = 'https://upload.wikimedia.org/wikipedia/commons/1/1d/White_House_north_and_south_sides.jpg'
    url = 'https://upload.wikimedia.org/wikipedia/commons/8/8d/President_Barack_Obama.jpg'
    print queryComputerVision(url, apikey=apikey)
