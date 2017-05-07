from __future__ import print_function

import boto3
import json
import requests

def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
            'Google-Assistant-API-Version': 'v1'
        },
    }

def lambda_handler(event, context):
    ''' '''

    tableName = "MySmartHome"
    dynamo = boto3.resource("dynamodb").Table(tableName)
    deviceId = event["pathParameters"].get("deviceId")
    item = dynamo.get_item(Key={"id": deviceId}).get("Item")
    if not item:
        return respond(ValueError("Can not match deviceId"))

    ip = item.get("ip")
    port = item.get("port")
    endpoint = item.get("endpoint") or ""
    url = "http://" + ip + ":" + port + endpoint
    data = json.loads(event["body"])
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    return respond(None, r.json())
