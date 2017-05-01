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

    tableName = "NyNetworkIp"
    dynamo = boto3.resource('dynamodb').Table("MyNetworkIp")
    resp = dynamo.get_item(Key={"id": 0})
    ip = resp["Item"]["ip"]
    print("IP:" + ip)
    internalPort = "62405"
    endpoint = ""
    url = "http://" + ip + ":" + internalPort
    data = json.loads(event['body'])
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=headers)

    return respond(None, r.json())
