from pydantic import BaseModel, EmailStr

class UserRegistration(BaseModel):
    name: str
    email: EmailStr
    phone: str
    event_type: str
    amount: int