import requests

def handle(req):

    quotesURL = "https://zenquotes.io/api/random"

    req = requests.get(quotesURL)
    if req.status_code != 200:
        sys.exit("Error requesting quote, expected: %d, got: %d\n" % (200, req.status_code))
    result = req.json()[0]["q"]

    return "Sorry it's too late for you, but remember: " + result
