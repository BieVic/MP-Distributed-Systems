import os
import requests
import sys
from random import randrange

def handle(req):

    gatewayURL = "http://gateway.openfaas:8080/function/"
    sentimentAnalysisFunc = "sentimentanalysis"
    positivePolarityFunc = "positive-polarity"
    negativePolarityFunc = "negative-polarity"
    fdaAPI = "https://api.fda.gov/food/enforcement.json?limit=20"

    req = requests.get(fdaAPI)
    if req.status_code != 200:
        sys.exit("Error requesting fda data, expected: %d, got: %d\n" % (200, req.status_code))

    result = req.json()["results"]
    randomElement = randrange(len(result))
    contamination = result[randomElement]["reason_for_recall"]

    req2 = requests.get(gatewayURL + sentimentAnalysisFunc, data=contamination)
    if req2.status_code != 200:
        sys.exit("Error requesting sentimentAnalysis, expected: %d, got: %d\n" % (200, req2.status_code))

    result2 = req2.json()
    resultPrefix = "You ate: " + contamination + "\n"
    if result2["polarity"] > 0.0:
        return resultPrefix + requests.get(gatewayURL + positivePolarityFunc).text

    return resultPrefix + requests.get(gatewayURL + negativePolarityFunc).text
