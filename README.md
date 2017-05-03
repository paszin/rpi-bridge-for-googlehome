# rpi-bridge-for-googlehome
Guide on how to connect you google home with local devices


This is a guide for everyone who wants to connect Google Home to a local network. Normally local devices like a webserver on a raspberry pi are not available from the internet (because usually you don't have a static ip-address). In this guide I will show you how to make your devices accessible from your Google Home.

My use case is talk to google home to control my raspberry pi controlled LEDs.


### Summary

Setup raspberry pi to send local ip to a webservice (AWS Lambda with DynamoDB). Send Google Home's requests to another webservice that knows to local ip adress and forwards it to the raspberry pi. 

### Requirements
You can probably skip this. But make sure, that you fullfill the following requirements.

- Python 2.7 including pip
- AWS Account and some experience with lambda, API Gateway and dynamoDB
- AWS CLI (if not: `pip install --upgrade --user awscli`, and visit http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html#cli-signup)

### Step #0
`git clone git@github.com:paszin/rpi-bridge-for-googlehome.git`

### Step #1
##### add your devices to a database
We will create a DynamoDB table with the name _MySmartHome_.

Run the following commands from your terminal:

- `cd aws_api`

- `make table`

- Visit https://eu-central-1.console.aws.amazon.com/dynamodb/home?#tables:selected=MySmartHome

- Click _Create Item_ and give it a useful id, e.g. _lights_ or _coffeemachine_ 

### Step #2
##### create an endpoint to update your database

- `make api`

- copy the returned id

- `export MySmartHome_APIID=THEcopiedID`

##### create lambda functions for your endpoints

###### create service role

- visit https://console.aws.amazon.com/iam/home#/roles

- Create a new Role, select AWS Lambda and provide full Access for Lambda. Save the new Role. Copy the Role ARN (should looks like arn:aws:iam::11111155555:role/smarthomerole)

- `export AWS_ROLE=arn:aws:iam::11111155555:role/smarthomerole`

###### create functions

- `make functions`


### Step #3
###### update database from your local device


### Step #4
##### create an endpoint to access your local device








- [ ] open port on router

- [ ] send local ip to aws

- [ ] forward incomming request to local ip

- [ ] forward response

