from __future__ import print_function

import boto3
import json


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    '''
    PUT: updates the MySmartHome-Table with a given ip and port
    GET: returns the ip and port for the specified device
    '''

    tableName = "MySmartHome"
    dynamo = boto3.resource("dynamodb").Table(tableName)
    operation = event["httpMethod"]
    deviceId = event["pathParameters"].get("deviceId")
    if operation == "PUT":
        payload = json.loads(event["body"])
        resp = dynamo.update_item(
                            Key={
                                "id": deviceId
                            },
                            UpdateExpression="SET ip = :ip, port = :port",
                            ExpressionAttributeValues={
                                ":ip": payload["ip"],
                                ":port": payload["port"]
                            },
                            ReturnValues="UPDATED_NEW"
                        )
        return respond(None, resp)

    elif operation == "GET":
        resp = dynamo.get_item(Key={
            "id": deviceId
        })
        return respond(None, resp.get("Item"))

    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
