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
    '''

    tableName = "MyNetworkIp"

    operations = {
        'DELETE': lambda dynamo, x: dynamo.delete_item(**x),
        'GET': lambda dynamo, x: dynamo.scan(**x),
        'POST': lambda dynamo, x: dynamo.put_item(**x),
        'PUT': lambda dynamo, x: dynamo.update_item(**x),
    }

    dynamo = boto3.resource("dynamodb").Table(tableName)
    operation = event["httpMethod"]
    if operation == "PUT":
        payload = json.loads(event["body"])
        resp = dynamo.update_item(
                            Key={
                                "id": 0
                            },
                            UpdateExpression="set ip = :val",
                            ExpressionAttributeValues={
                                ":val": payload["ip"] ,
                            },
                            ReturnValues="UPDATED_NEW"
                        )
        return respond(None, resp)

    else:
        return respond(ValueError('Unsupported method "{}"'.format(operation)))
