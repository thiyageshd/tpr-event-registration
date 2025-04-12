import razorpay
from app.core.config import settings

class PaymentService:
    def __init__(self):
        self.client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    def create_order(self, amount):
        try:
            order = self.client.order.create({
                'amount': amount * 100,  # Amount in paise
                'currency': 'INR',
                'payment_capture': '1'
            })
            return order
        except razorpay.errors.BadRequestError as e:
            raise Exception(f"Failed to create order: {str(e)}")

    def verify_payment(self, payment_id, order_id, signature):
        try:
            self.client.utility.verify_payment_signature({
                'razorpay_order_id': order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            })
            return True
        except:
            return False

    def get_payment_details(self, payment_id):
        try:
            return self.client.payment.fetch(payment_id)
        except Exception as e:
            raise Exception(f"Failed to fetch payment details: {str(e)}")