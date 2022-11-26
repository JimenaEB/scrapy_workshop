from dataclasses import asdict

import boto3

class DynamoDbPipeline(object):

    def process_item(self, item, spider):
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(spider.name)

        table.put_item(Item=asdict(item))

        return item