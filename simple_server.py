## simple template of a webserver running on a raspberry pi
## this example uses Flask
## replace this file with your own logic,
## but for the beginning you can use this template


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print "incoming request"
    ## implement your logic here
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000)
