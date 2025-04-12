from pydantic import BaseModel, EmailStr

class UserRegistration(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
    amount: int
    event_type: str
    gender: str
    dob: str
    street: str
    city: str
    pincode: str
    state: str
    name_on_the_bib: str
    t_shirt_size: str
    name_of_your_group: str
    breakfast: str
    blood_group: str
    emergency_contact_name: str
    emergency_contact_number: str
    terms_and_condition: str

class PaymentCallbackRequest(BaseModel):
    transaction_id: str