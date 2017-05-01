# rpi-bridge-for-googlehome
Guide on how to connect you google home with local devices


This is a guide for everyone you wants to connect Google Home to your local network.
My use case is talk to google home to control my raspberry pi controlled LEDs.


Summary:

Setup raspberry pi to send local ip to a webservice (AWS Lambda with DynamoDB). Send Google Home's requests to another webservice that knows to local ip adress and forwards it to the raspberry pi. 

