## simple template of a webserver running on a raspberry pi
## this example uses Flask
## replace this file with your own logic,
## but for the beginning you can use this template


import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def index():
    print "incoming request:"
    print request.data
    data = json.loads(request.data)
    response = {"my_message": "Hello from my Network", \
                "your_message": data}
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=False)
