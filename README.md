# rpi-bridge-for-googlehome
Guide on how to connect you google home with local devices


This is a guide for everyone who wants to connect Google Home to a local network. Normally local devices like a webserver on a raspberry pi are not available from the internet (because usually you don't have a static ip-address). In this guide I will show you how to make your devices accessible from your Google Home.

My use case is talk to google home to control my raspberry pi controlled LEDs.


### Summary

Setup raspberry pi to send local ip to a webservice (AWS Lambda with DynamoDB). Send Google Home's requests to another webservice that knows to local ip adress and forwards it to the raspberry pi. 

### Requirements
You can probably skip this. But make sure, that you fullfill the following requirements.

- Python 2.7
- AWS Account and some experience with lambda, API Gateway and dynamoDB
- AWS CLI (if not: `pip install --upgrade --user awscli`, and visit http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html#cli-signup)


### Step #1
##### add your devices to a database


### Step #2
##### create an endpoint to update your database


### Step #3
###### update database from your local device


### Step #4
##### create an endpoint to access your local device








- [ ] open port on router

- [ ] send local ip to aws

- [ ] forward incomming request to local ip

- [ ] forward response

