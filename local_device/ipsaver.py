## run this script in the background of your raspberry pi
## every 60 seconds the script will check your ip address and sends it to the webservice if necessary
## Requirements:
##  pip install requests
##  put the url of your webservice in webUrl = ...




import urllib2
import json
import time
import requests


url = "https://api.ipify.org/?format=json"
webUrl = "https://???????.execute-api.eu-central-1.amazonaws.com/prod"

interval = 60 ##seceonds

lastIp = None


while True:
    
    response = urllib2.urlopen(url)
    data = json.load(response)   
    if data["ip"] != lastIp:
        r = requests.put(webUrl, data=json.dumps({"ip": data["ip"]}))
        print "updated ip"
        lastIp = data["ip"]

    time.sleep(interval)
