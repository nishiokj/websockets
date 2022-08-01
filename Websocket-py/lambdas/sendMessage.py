import json

# import requests
import datetime
import os
import boto3
from layers.Connect import Connection
from layers.NotificationTable import Notification
from boto3.dynamodb.conditions import Attr

def lambda_handler(event, context):
    notificationTable = Notification()
    user_id = event["headers"].get("userid")
    connect = event["requestContext"]["connectionId"]
    input = event["message"]
    notificationTable.put_item(Item={
        'user_id' : user_id,
        'connection_id' : connect,
        'message' : input
    })
    return {
        "statusCode": 200
    }