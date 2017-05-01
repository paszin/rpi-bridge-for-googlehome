# rpi-bridge-for-googlehome
Guide on how to connect you google home with local devices


This is a guide for everyone who wants to connect Google Home to a local network. Normally local devices like a webserver on a raspberry pi are not available from the internet (because usually you don't have a static ip-address). In this guide I will show you how to make your devices accessible ffrom your Google Home.

My use case is talk to google home to control my raspberry pi controlled LEDs.


### Summary

Setup raspberry pi to send local ip to a webservice (AWS Lambda with DynamoDB). Send Google Home's requests to another webservice that knows to local ip adress and forwards it to the raspberry pi. 




- [ ] open port on router

- [ ] send local ip to aws

- [ ] forward incomming request to local ip

- [ ] forward response

