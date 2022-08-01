import boto3
import re
import json
import os
class Notification:
    def __init__(self):
        match = re.search("table/(.)*",os.environ.get("WebsocketTable"))
        table_name = match.group().split("/")[1].strip()
        resource = boto3.resource('dynamodb',region_name="us-east-1")
        self.table = resource.Table(table_name)
    def get_table(self) -> object:
        return self.table