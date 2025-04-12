from app.core.config import settings
from app.clients import DynamoDBResource

class UserDAO:
    def __init__(self):
        self.dynamodb = DynamoDBResource().get_resource()
        self.table = self.dynamodb.Table(settings.DYNAMODB_TABLE)

    def save_registration(self, registration_data):
        try:
            response = self.table.put_item(Item=registration_data)
            return response
        except Exception as e:
            raise Exception(f"Failed to save registration: {str(e)}")
        