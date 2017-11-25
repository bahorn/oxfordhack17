import os
import sys
import requests
from os.path import join, dirname
from dotenv import load_dotenv

class azureComputerVision:
    def __init__(self, apikey, zone="northeurope"):
        self.apikey = apikey
        self.endpoint = "https://{}.api.cognitive.microsoft.com/vision/v1.0".format(zone)
    # pass a URL/file to the computer vision api.
    def queryComputerVision(self, input):
        headers = {'Ocp-Apim-Subscription-Key': self.apikey}
        if type(input) == str:
            data = {'url':input}
            r = requests.post(self.endpoint+"/analyze?visualFeatures=tags",
                headers=headers, json=data)
        elif type(input) == file:
            r = requests.post(self.endpoint+"/analyze?visualFeatures=tags",
                headers=headers, files={'file': input})
        else:
            raise TypeError
        if r.status_code == 200:
            return r.json()
        else:
            return None

if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    apikey = os.environ['KEY1']
    cv = azureComputerVision(apikey)
    print cv.queryComputerVision("https://avatars2.githubusercontent.com/u/22912854?s=400&u=ee48be5a1fcb4aca344cbad45509408022073b64&v=4")
