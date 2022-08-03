import json
#from layers.NotificationTable import Notification
from boto3.dynamodb.conditions import Attr
import boto3


client1 = boto3.client('lambda')
def lambda_handler(event,context):
    #Make Dynamo table
    table_name = "WebsocketTable"
    resource = boto3.resource('dynamodb',region_name="us-east-1")
    notificationTable = resource.Table(table_name)
    #Get message from connection
    connectionId = event["requestContext"]["connectionId"]
    response = notificationTable.scan(FilterExpression=Attr("user_id").eq(connectionId))
    message = response["Items"][0]["message"]
    #Invoke Sentiment Analysis
    sentimentInput = {'message': message}
    response = client1.invoke(
        FunctionName='arn:aws:lambda:us-east-1:264860945026:function:Websocket-py-getSentimentLambda-X9JvFN2c6qZB',
        InvocationType='RequestResponse',
        Payload=json.dumps(sentimentInput),
    )
    #Send back to client
    send_to_client = json.loads(response["Payload"].read())
    send_to_client["OriginalMessage"] = message
    client = boto3.client('apigatewaymanagementapi',endpoint_url="https://19rp3f1jii.execute-api.us-east-1.amazonaws.com/production")
    post = client.post_to_connection(ConnectionId = connectionId,Data=json.dumps(send_to_client).encode('utf-8'))
    return {
        "statusCode": 200
        }