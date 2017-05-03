table:
	aws dynamodb create-table --table-name MySmartHome --attribute-definitions AttributeName=id,AttributeType=S --key-schema AttributeName=id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=1,WriteCapacityUnits=1

api:
	aws apigateway import-rest-api --body 'file://swagger_api_definition.yaml'


access_role:
	aws iam create-role --role-name MySmartHome_Role --assume-role-policy-document file://access_role.json

functions:
	cd lambda/ipreceiver;	zip -r ../ipreceiver.zip *; cd ../..
	aws lambda create-function --function-name mysmarthome_iphandler \
	--runtime python2.7 \
	--role $(AWS_ROLE)  \
	--handler lambda_function.lambda_function \
	--zip-file fileb://lambda/ipreceiver.zip
	pip install requests -t ./lambda/requester
	cd lambda/requester;	zip -r ../requester.zip *; cd ../..
	aws lambda create-function --function-name mysmarthome_iphandler \
	--runtime python2.7 \
	--role $(AWS_ROLE)  \
	--handler lambda_function.lambda_function \
	--zip-file fileb://lambda/requester.zip
