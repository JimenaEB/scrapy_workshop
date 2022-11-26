import boto3

def create_gpu_table(dynamodb):

    table = dynamodb.create_table(
        TableName='gpu_check',
        KeySchema=[
            {
                'AttributeName': 'name',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='gpu_check')

    if table.item_count == 0:
        print("GPU was created successfuly")



if __name__ == "__main__":
    dynamodb = boto3.resource('dynamodb')
    try:
        create_gpu_table(dynamodb)
    except:
        print("GPU table already exists")