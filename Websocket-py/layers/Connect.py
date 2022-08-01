import os
#from boto3.dynamodb.conditions import Attr
#from db_services.service import DBConnection
import boto3
import re
class Connection:
    def __init__(self):
        match = re.search("table/(.)*","ConnectionTableArn")
        table_name = match.group().split("/")[1].strip()
        resource = boto3.resource('dynamodb',region_name="us-east-1")
        self.table = resource.Table(table_name)

    def add_connection_id(self,connection_id,user_id,created_on):
        response = self.table.put_item(Item ={
            'connectionId':connection_id,
            'userId': user_id,
            'createdOn': created_on
        }
        )
        return response
    def remove_connection_id(self,connection_id):
        self.table.delete_item(Key={"connectionId": connection_id})
