from botocore.exceptions import ClientError
from app.core.config import settings
from app.clients.db_client import DynamoDBResource


def delete_table():
    dynamodb = DynamoDBResource().get_resource()

    table_name = settings.DYNAMODB_TABLE

    try:
        table = dynamodb.Table(table_name)
        table.delete()
        print(f"Table {table_name} is being deleted.")
    except dynamodb.exceptions.ResourceNotFoundException:
        print(f"Table {table_name} does not exist.")
    except Exception as e:
        print(f"Error deleting table: {str(e)}")


def create_dynamodb_table(dynamodb=None):
    dynamodb = DynamoDBResource().get_resource()
    table = dynamodb.create_table(
        TableName=settings.DYNAMODB_TABLE,
        KeySchema=[
            {
                'AttributeName': 'transaction_id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'email',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'transaction_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'email',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'phone_number',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'name',
                'AttributeType': 'S'
            }
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'PhoneNumberIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'phone_number',
                        'KeyType': 'HASH'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            },
            {
                'IndexName': 'PhoneNumberNameIndex',
                'KeySchema': [
                    {
                        'AttributeName': 'phone_number',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'name',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print("table is created")
    return table

if __name__ == "__main__":
    # delete_table()
    create_dynamodb_table()