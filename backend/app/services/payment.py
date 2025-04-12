import base64
import json
import requests
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from app.core.config import settings

class PaymentService:
    def __init__(self):
        # self.merchant_id = settings.PHONEPE_MERCHANT_ID
        # self.salt_key = settings.PHONEPE_SALT_KEY
        # self.salt_index = settings.PHONEPE_SALT_INDEX
        self.client_id = settings.PHONEPE_CLIENT_ID
        self.client_secret = settings.PHONEPE_CLIENT_SECRET
        self.base_url = settings.PHONEPE_BASE_URL

    async def calculate_sha256_string(self, input_string):
        sha256 = hashes.Hash(hashes.SHA256(), backend=default_backend())
        sha256.update(input_string.encode('utf-8'))
        return sha256.finalize().hex()

    async def base64_encode(self, input_dict):
        json_data = json.dumps(input_dict)
        data_bytes = json_data.encode('utf-8')
        return base64.b64encode(data_bytes).decode('utf-8')

    async def generate_checksum(self, payload):
        payload_string = json.dumps(payload)
        payload_bytes = payload_string.encode('utf-8')
        payload_base64 = base64.b64encode(payload_bytes).decode('utf-8')

        string_to_hash = payload_base64 + "/v3/charge" + self.client_secret
        sha256 = hashes.Hash(hashes.SHA256(), backend=default_backend())
        sha256.update(string_to_hash.encode('utf-8'))
        checksum = sha256.finalize().hex() + "###1"
        return payload_base64, checksum
    
    async def create_payment_link(self, amount, transaction_id, user_id, mobile_number):
        payload = {
            "merchantId": self.client_id,
            "merchantTransactionId": transaction_id,
            "merchantUserId": user_id,
            "amount": amount,
            "redirectUrl": f"{settings.BASE_URL}/api/payment-callback",
            "redirectMode": "POST",
            "callbackUrl": f"{settings.BASE_URL}/api/payment-callback",
            "mobileNumber": mobile_number,
            "paymentInstrument": {
                "type": "PAY_PAGE"
            }
        }

        base64_payload, checksum = await self.generate_checksum(payload)

        headers = {
            "Content-Type": "application/json",
            "X-VERIFY": checksum
        }

        data = {
            "request": base64_payload
        }

        return {
            "data": {
                "instrumentResponse": {
                    "redirectInfo": {
                        "url": "test"
                    }
                }
            }
        }
        response = requests.post(f"{self.base_url}/v3/charge", headers=headers, json=data)

        if response.status_code == 200:
            response_data = response.json()
            if response_data.get('success'):
                return response_data['data']['instrumentResponse']['redirectInfo']['url']
            else:
                raise Exception(f"Failed to create payment link: {response_data.get('message')}")
        else:
            raise Exception(f"Failed to create payment link. Status code: {response.status_code}")

    async def verify_payment(self, transaction_id):
        headers = {
            "Content-Type": "application/json",
            "X-CLIENT-ID": self.client_id,
            "X-CLIENT-SECRET": self.client_secret
        }

        return "success"
        response = requests.get(f"{self.base_url}/v3/transaction/{transaction_id}/status", headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            if response_data.get('success'):
                return response_data['data']['paymentInstrument']['status']
            else:
                raise Exception(f"Failed to verify payment: {response_data.get('message')}")
        else:
            raise Exception(f"Failed to verify payment. Status code: {response.status_code}")