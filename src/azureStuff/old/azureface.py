import os
import sys
import requests
from os.path import join, dirname
from dotenv import load_dotenv

class AzureFace:
    def __init__(self, apikey, zone="northeurope"):
        self.apikey = apikey
        self.endpoint = "https://{}.api.cognitive.microsoft.com/face/v1.0".format(zone)
    
    def _queryFaceAPI(self, method, input, query):
        headers = {'Ocp-Apim-Subscription-Key': self.apikey}
        if type(input) == str:
            data = {'url':input}
            r = requests.post(self.endpoint+"/{}?{}".format(method, "&".join(query)),
                headers=headers, json=data)
        elif type(input) == file:
            r = requests.post(self.endpoint+"/{}?{}".format(method, "&".join(query)),
                headers=headers, files={'file': input})
        else:
            raise TypeError
        if r.status_code == 200:
            return r.json()
        else:
            return None

    def detectFace(self, input, returnFaceId=True, returnFaceLandmarks=False,
            returnFaceAttributes=None):
        query = []
        query += ['returnFaceId={}'.format(returnFaceId)]
        query += ['returnFaceLandmarks={}'.format(returnFaceLandmarks)]
        if returnFaceAttributes != None:
            query += ["returnFaceAttributes="+','.join(returnFaceAttributes)]
        return _queryFaceAPI('detect', input, query)
if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    apikey = os.environ['FACEKEY']
