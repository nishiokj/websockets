import json
from layers.NotificationTable import Notification
from boto3.dynamodb.conditions import Attr
import boto3
def lambda_handler(event,context):
    user_id = event["headers"].get("user_id")
    notificationTable = Notification()
    response = notificationTable.scan(FilterExpression=Attr("user_id").eq(user_id))
    message = response["message"]
    for i in message:
        i = i.toUpper()

    connectionId = event["requestContext"]["connectionId"]
    client = boto3.client('apigatewaymanagementapi',endpoint_url="https://19rp3f1jii.execute-api.us-east-1.amazonaws.com/production/@connections")
    post = client.post_to_connection(ConnectionId = connectionId,Data=json.dumps(message).encode('utf-8'))
    return {"StatusCode": 200}