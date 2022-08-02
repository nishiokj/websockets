import json
#from layers.NotificationTable import Notification
from boto3.dynamodb.conditions import Attr
import boto3
import os
import re
def lambda_handler(event,context):
    #user_id = event["headers"].get("user_id")
    #match = re.search("table/(.)*",os.environ.get("arn:aws:dynamodb:us-east-1:264860945026:table/WebsocketTable"))
    #table_name = match.group().split("/")[1].strip()
    table_name = "WebsocketTable"
    resource = boto3.resource('dynamodb',region_name="us-east-1")
    table = resource.Table(table_name)
    notificationTable = table
    connectionId = event["requestContext"]["connectionId"]
    response = notificationTable.scan(FilterExpression=Attr("user_id").eq(connectionId))
    message = response["Items"][0]["message"]
    print(response["Items"])
    x = message.upper()
    print(x)
    
    client = boto3.client('apigatewaymanagementapi',endpoint_url="https://19rp3f1jii.execute-api.us-east-1.amazonaws.com/production")
    post = client.post_to_connection(ConnectionId = connectionId,Data=json.dumps(x).encode('utf-8'))
    return {
        "statusCode": 200
        }