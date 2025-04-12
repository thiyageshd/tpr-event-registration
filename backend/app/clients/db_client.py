from threading import Lock

import boto3

from app.core.config import settings


class DynamoDBResource:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._initialize_resource()
        return cls._instance

    def _initialize_resource(self):
        self.dynamodb = boto3.resource('dynamodb', 
                                       region_name=settings.AWS_REGION,
                                       aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                       aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
        self.table = self.dynamodb.Table(settings.DYNAMODB_TABLE)

    def get_resource(self):
        return self.dynamodb
