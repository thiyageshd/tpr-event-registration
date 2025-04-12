from pydantic import BaseModel, EmailStr

class PaymentResponse(BaseModel):
    payment_id: str
    order_id: str
    signature: str