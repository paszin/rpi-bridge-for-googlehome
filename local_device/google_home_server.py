## simple template of a webserver running on a raspberry pi
## this example uses Flask
## replace this file with your own logic,
## but for the beginning you can use this template


import json
import random
import requests
from flask import Flask, request, jsonify

from gactions_response_builder import GResponse, extractText

app = Flask(__name__)


welcomeResponse = GResponse(text="Welcome, how do you feel?", expect_user_response=True).getJson()
okayResponse = GResponse(text="Okay", expect_user_response=False).getJson()

#### Little sentiment analysis for this example

def analyse_sentiment(text):
    '''return a score based on the words in text'''
    negative_words = ["bad", "sick", "terrible"]
    positive_words = ["happy", "excited", "good"]
    sentiment = 0
    for word in text.split():
        if word in negative_words:
            sentiment -= 1
        elif word in positive_words:
            sentiment += 1
    return sentiment


def forward_request(text):
    '''handler for logic'''
    ## IMPLEMENT YOUR LOGIC HERE
    score = analyse_sentiment(text)
    if score < 0:
        return "Ohh come on, your application is working as expected. You should be happy!"
    if score > 0:
        return "Oh yeah, enjoy your day!"
    return None



@app.route("/", methods=["POST"])
def index():
    print "Content:"
    print request.data
    data = json.loads(request.data)
    text = extractText(data)
    print "Extracted Text:", text
    if data["inputs"][0]["intent"] == "assistant.intent.action.MAIN":
        print "initial request"
        return jsonify(welcomeResponse)
    else:
        response = forward_request(text)
        if response:
            return jsonify(GResponse(text=response, expect_user_response=False).getJson())
        else:
            return jsonify(GResponse(text="Let me know how you feel!", expect_user_response=True).getJson())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=False)
