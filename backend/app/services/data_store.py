from app.core.config import settings
from app.clients import DynamoDBResource
from botocore.exceptions import ClientError
import boto3
from boto3.dynamodb.conditions import Key, Attr
from loguru import logger
from datetime import datetime

from app.models.request.registration import RegistrationUpdate, Registration

class UserDAO:
    def __init__(self):
        self.dynamodb = DynamoDBResource().get_resource()
        self.registration_table = self.dynamodb.Table(settings.DYNAMODB_TABLE)

    async def create_registration(self, registration_data):
        try:
            response = self.registration_table.put_item(Item=registration_data)
            return response
        except Exception as e:
            raise Exception(f"Failed to save registration: {str(e)}")
        
    async def update_registration(self, transaction_id: str, update: RegistrationUpdate):
        try:
            email = await self.get_email_for_transaction(transaction_id)
            if not email:
                logger.error(f"Error updating payment status: {transaction_id} details not found")
                raise(f"{transaction_id} details not found")
            response = self.registration_table.update_item(
                Key={
                    'transaction_id': transaction_id,
                    'email': email
                },
                UpdateExpression="SET payment_status = :s, payment_date = :d",
                ExpressionAttributeValues={
                    ':s': update.payment_status,
                    ':d': update.payment_date or str(datetime.now())
                },
                ConditionExpression=Attr('transaction_id').exists(),
                ReturnValues="ALL_NEW"
            )
            logger.info(f"Payment status updated for transaction {transaction_id}: {update.payment_status}")
            return {
                "response": response,
                "email": email
            }
        except ClientError as e:
            logger.error(f"Error updating payment status: {str(e)}")
            raise
        except Exception as e:
            raise

    async def get_registration(self, transaction_id: str, email: str) -> Registration:
        try:
            response = self.registration_table.get_item(
                Key={
                    'transaction_id': transaction_id,
                    'email': email
                }
            )
            item = response.get('Item')
            if item:
                return item
            return None
        except ClientError as e:
            logger.error(f"Error retrieving registration: {str(e)}")
            raise


    async def get_email_for_transaction(self, transaction_id: str) -> str:
        try:
            response = self.registration_table.query(
                KeyConditionExpression=Key('transaction_id').eq(transaction_id),
                ProjectionExpression='email'
            )
            items = response.get('Items', [])
            if items:
                return items[0]['email']
            return None
        except ClientError as e:
            raise Exception(f"Failed to get email for transaction: {str(e)}")
        

    async def query_by_phone_number(self, phone_number: str):
        response = self.registration_table.query(
            IndexName='PhoneNumberIndex',
            KeyConditionExpression=Key('phone_number').eq(phone_number)
        )
        return response['Items']


    async def query_by_phone_number_and_name(self, phone_number: str, name: str):
        response = self.registration_table.query(
            IndexName='PhoneNumberNameIndex',
            KeyConditionExpression=Key('phone_number').eq(phone_number) & Key('name').eq(name)
        )
        return response['Items']