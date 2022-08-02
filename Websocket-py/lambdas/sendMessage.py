

# import requests

import os
import boto3
import re


def lambda_handler(event, context):
    #match = re.search("table/(.)*",os.environ.get("arn:aws:dynamodb:us-east-1:264860945026:table/WebsocketTable"))
    #table_name = match.group().split("/")[1].strip()
    resource = boto3.resource('dynamodb',region_name="us-east-1")
    table_name = "WebsocketTable"
    table = resource.Table(table_name)
    notificationTable = table
    #user_id = event["headers"].get("userid")
    connect = event["requestContext"]["connectionId"]
    input = event["body"]
    
    phrase1 = input.rsplit(", ",2)
    ans = ""
    for i in phrase1[1]:
        if i != '}':
            ans += i
    notificationTable.put_item(Item={
        'user_id' : connect,
        'connection_id' : connect,
        'message' : ans
    })
    return {
        "statusCode": 200
    }