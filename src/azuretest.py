import os
import sys
import requests
from os.path import join, dirname
from dotenv import load_dotenv

class azureComputerVision:
    def __init__(self, apikey, zone="northeurope"):
        self.apikey = apikey
        self.endpoint = "https://{}.api.cognitive.microsoft.com/vision/v1.0".format(zone)
    
    def _queryComputerVision(self, method, input, query):
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

if __name__ == "__main__":
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    apikey = os.environ['KEY1']
    cv = azureComputerVision(apikey)
    print cv.queryOCR(file(sys.argv[1]))
    #print cv.queryComputerVision(file(sys.argv[1]), visualFeatures=['tags'])
