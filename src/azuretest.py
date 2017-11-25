import os
import sys
import requests
from os.path import join, dirname
from dotenv import load_dotenv

class azureComputerVision:
    def __init__(self, apikey, zone="northeurope"):
        self.apikey = apikey
        self.zone = zone
    
    def _queryComputerVision(self, method, input, query, api='vision'):
        headers = {'Ocp-Apim-Subscription-Key': self.apikey}
        endpoint = "https://{}.api.cognitive.microsoft.com/{}/v1.0".format(
                self.zone, api)
        if type(input) == str:
            data = {'url':input}
            r = requests.post(endpoint+"/{}?{}".format(method, "&".join(query)),
                headers=headers, json=data)
        elif type(input) == file:
            r = requests.post(endpoint+"/{}?{}".format(method, "&".join(query)),
                headers=headers, files={'file': input})
        else:
            raise TypeError
        print r.text
        if r.status_code == 200:
            return r.json()
        else:
            return None
    
    def queryComputerVision(self, input, visualFeatures=None, details=None):
        query = []
        if visualFeatures != None:
            query += ["visualFeatures="+",".join(visualFeatures)]
        if details != None:
            query += ["details="+",".join(details)]
        return self._queryComputerVision('analyze', input, query)

    def queryOCR(self, input, language='en', detectOrientation=False):
        query = []
        query += ['language={}'.format(language)]
        query += ['detectOrientation={}'.format(str(detectOrientation))]
        return self._queryComputerVision('ocr', input, query)

    def detectFace(self, input, returnFaceId=True, returnFaceLandmarks=False,
            returnFaceAttributes=None):
        query = []
        query += ['returnFaceId={}'.format(returnFaceId)]
        query += ['returnFaceLandmarks={}'.format(returnFaceLandmarks)]
        if returnFaceAttributes != None:
            query += ["returnFaceAttributes="+','.join(returnFaceAttributes)]
        return self._queryComputerVision('detect', input, query, api='face')

if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    apikey = os.environ['FACEKEY']
    cv = azureComputerVision(apikey)
    #print cv.queryOCR(file(sys.argv[1]))
    print cv.detectFace('https://www.biography.com/.image/t_share/MTE4MDAzNDEwNzg5ODI4MTEw/barack-obama-12782369-1-402.jpg')
