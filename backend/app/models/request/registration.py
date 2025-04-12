from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Union
from datetime import datetime
from enum import Enum
from decimal import Decimal

class EventType(str, Enum):
    FIVE_K = "5km"
    TEN_K = "10km"
    HALF_MARATHON = "21km"
    FULL_MARATHON = "42km"

class PaymentStatus(str, Enum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"

class Registration(BaseModel):
    transaction_id: str = Field(..., description="Unique identifier for the transaction")
    email: EmailStr = Field(..., description="Email address of the participant")
    name: str = Field(..., description="Full name of the participant")
    phone_number: str = Field(..., description="Phone number of the participant")
    event_type: EventType = Field(..., description="Type of running event")
    amount: Union[float, Decimal] = Field(..., description="Registration fee amount")
    payment_status: PaymentStatus = Field(default=PaymentStatus.PENDING, description="Current status of the payment")
    registration_date: Optional[str] = Field(..., description="Date and time of registration")
    payment_date: Optional[str] = Field(None, description="Date and time of successful payment")

    class Config:
        schema_extra = {
            "example": {
                "transaction_id": "123e4567-e89b-12d3-a456-426614174000",
                "email": "runner@example.com",
                "name": "John Doe",
                "phone_number": "+1234567890",
                "event_type": "HALF_MARATHON",
                "amount": 50.00,
                "payment_status": "PENDING",
                "registration_date": "2023-06-15T10:00:00",
                "payment_date": None
            }
        }

class RegistrationCreate(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    event_type: EventType
    amount: float

class RegistrationUpdate(BaseModel):
    payment_status: PaymentStatus
    payment_date: Optional[str] = None

class RegistrationResponse(BaseModel):
    transaction_id: str
    email: EmailStr
    name: str
    event_type: EventType
    amount: float
    payment_status: PaymentStatus
    registration_date: str
    payment_date: Optional[str]
    payment_url: Optional[str]

class PaymentCallbackRequest(BaseModel):
    transaction_id: str
