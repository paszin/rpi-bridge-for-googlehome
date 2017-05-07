## run this script in the background of your raspberry pi
## every 60 seconds the script will check your ip address and sends it to the webservice if necessary
## Requirements:
##  pip install requests
##  put the url of your webservice in MYSMARTHOME_APIURL = ...
##  or export it to the enviroment variable MYSMARTHOME_APIURL=....

import os
import sys
import urllib2
import json
import time
import requests



MYSMARTHOME_APIURL = "https://lqgvt38ps2.execute-api.eu-central-1.amazonaws.com/dev2" #"https://???????.execute-api.eu-central-1.amazonaws.com/dev/"
MYSMARTHOME_DEVICEID = "lights"
MYSMARTHOME_PORT = "9000"

webUrl = os.environ.get("MYSMARTHOME_APIURL") or MYSMARTHOME_APIURL
deviceid = os.environ.get("MYSMARTHOME_DEVICEID") or MYSMARTHOME_DEVICEID
port = os.environ.get("MYSMARTHOME_PORT") or MYSMARTHOME_PORT
endpoint = "/devices/" + deviceid

interval = 60 ##seceonds

url = "https://api.ipify.org/?format=json"

lastIp = None

print "Device ID: ", deviceid
print "Port: ", port

while True:

    ##get ip
    response = urllib2.urlopen(url)
    data = json.load(response)
    if data["ip"] != lastIp:
        url = webUrl + endpoint
        r = requests.put(url, \
         data=json.dumps({"ip": data["ip"], "port": port}))
        if r.status_code != 200:
            print "[Error]", r.text
            break
        print "New IP:", data["ip"]
        lastIp = data["ip"]

    if sys.argv[1] == "noloop":
        break

    time.sleep(interval)
