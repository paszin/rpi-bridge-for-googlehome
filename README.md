# rpi-bridge-for-googlehome
Guide on how to connect you google home with local devices


This is a guide for everyone who wants to connect Google Home to a local network. Normally local devices like a webserver on a raspberry pi are not available from the internet (because usually you don't have a static ip-address). In this guide I will show you how to make your devices accessible from your Google Home.

My use case is talk to google home to control my raspberry pi controlled LEDs.

If want to hook up any other service like amazons Alexa or IFTTT this guide is also for you. Just skip the Google Home specific part.

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

###### link functions to api gateway

- visit https://eu-central-1.console.aws.amazon.com/apigateway/home


- click on _MySMartHome_ to see your API (all functions should be unlinked so far)

- under _Resources_ select _/{deviceid} and click _Set It Up Now_

- select _lambda function_, check _Use proxy integration_ and select _mysmarthome_iphandler_ as function

- repeat these steps, so you have the same setup for the PUT and the GET-Method

- under _Resources_ select _/{deviceid}/request and click _Set It Up Now_

- select _lambda function_, check _Use proxy integration_ and select _mysmarthome_requester_ as function

- mock end point /devices [TODO: also link to function]

- click _Actions_ and _Deploy API_, create a new stage named _dev_ and deploy. Then copy the invoke URL.


Summary until here:
We created a database and a working api to get and update elements in the table. Furthermore we have an endpoint to forward any request to our local network. Well done so far, take a break! In the next steps we will focus on setting up your local device (could be anything that supports python and has wifi of course).

### Step #3

You can do the steps from your local computer, or directly ssh to your raspberry pi

###### open port in router settings

This step depends on the router you use. Search for "open port on {insert router name here}"

- Select your SmartHome Device and open port 9000 (or any other port, but we will use 9000 in the following steps)

###### update database from your local device


- `cd ../local_device` 

- `pip install requests`

- `export MYSMARTHOME_APIURL={paste invoke url from the end of step 2}`

- `export MYSMARTHOME_PORT=9000` (should be the same as in the step before)

- `export MYSMARTHOME_DEVICEID=lights` (should be the same as in the database, see step#1) 

- `python ipsaver.py noloop` (Without the noloop parameter, the script will update the ip continuosly)  

If you don't want to store your configuration in enviroment variables, you could also store them directly in psaver.py`
(For your production version run the script without the noloop parameter in the background. This will update you local ip adress in the database everytime it changes)


### Step #4
##### create an endpoint to access your local device

In this step we will run a simple local server

- `pip install flask`

- `python simple_server.py` 

**Time for testing!**

- Open your favorite REST-Client (I recommend Postman)

- Send a POST request to `{paste invoke url from the end of step 2}/devices/{deviceid}/request` (e.g. `https://abc1312.execute-api.eu-central-1.amazonaws.com/dev/devices/lights/request`) with a payload `{"message": "hello world"}`

You should see the incoming request in you terminal and get `{
  "my_message": "Hello from my Network",
  "your_message": {
    "message": "hello world"
  }
}` as response



### Step #5

##### Integrate Google Home

Before you continue have a look at https://developers.google.com/actions/develop/sdk/
These are the offical introduction. (You don't need Node.js for this project)

- visit https://developers.google.com/actions/tools/gactions-cli and download gactions cli tool. Put it in the root folder of this project

- `cd ` to root folder

- type `./gactions --help` to verify that your cli is working (do not forget chmod +x if you are using unix)

- `cd local_device`

- `cp action.template.json action.json`

- open action.json and replace {paste url here} with `{paste invoke url from the end of step 2}/devices/{deviceid}/request` (e.g. `https://abc1312.execute-api.eu-central-1.amazonaws.com/dev/devices/lights/request`) 

- `make preview`

- visit https://developers.google.com/actions/tools/web-simulator and type "Talk to my smart lights"
 




### Contributions Welcome
If you know how to automate or simplify a step, or other improvements, feel free to make a pull request.
