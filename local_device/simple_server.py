## simple template of a webserver running on a raspberry pi
## this example uses Flask
## replace this file with your own logic,
## but for the beginning you can use this template




import json
import random
import requests
from flask import Flask, request, jsonify

from gactions_response_builder import GResponse

app = Flask(__name__)


welcomeResponse = GResponse(text="Welcome, do you want some light", expect_user_response=True).getJson()
okayResponse = GResponse(text="Okay", expect_user_response=False).getJson()


def forward_request(text):
    print "forward"
    if "turn off" in text:
        return turnOff()
        
    url = "http://192.168.178.93:9000/nlp/effect"
    return requests.post(url, \
                     headers = {'content-type': 'application/json'}, \
                     data=json.dumps({"text": text}))
    

def turnOff():
    url = "http://192.168.178.93:9000/reset"
    return requests.post(url, headers = {'content-type': 'application/json'})
    

@app.route("/", methods=['GET', 'POST'])
def index():
    print "incoming request:"
    print request
    if request.method == "POST":
        print "Content:"
        print request.data
        data = json.loads(request.data)
        text = data["inputs"][0]["raw_inputs"][0]["query"]
        print "Extracted Text:", text
        if data["inputs"][0]["intent"] == "assistant.intent.action.MAIN":
            print "initial request"
            return jsonify(welcomeResponse)
        else:
            forward_request(text)
            return jsonify(okayResponse)
    #return jsonify(GResponse(text="reached the end", expect_user_response=True))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=False)

