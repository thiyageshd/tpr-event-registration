from fastapi import APIRouter, HTTPException, Depends
from app.models import UserRegistration, PaymentResponse
from dependency_injector.wiring import inject, Provide
from app.containers import Container
from app.services.data_store import UserDAO
from app.services.payment import PaymentService
from app.services.communication import CommunicationService
from app.models.request.registration import RegistrationCreate, RegistrationResponse, RegistrationUpdate, PaymentCallbackRequest, PaymentStatus

from loguru import logger
from datetime import datetime
import uuid

router = APIRouter()

@router.post("/register",  response_model=RegistrationResponse)
@inject
async def register_user(
    user_data: UserRegistration,
    dynamodb_service: UserDAO = Depends(Provide[Container.dynamodb_service]),
    payment_service: PaymentService = Depends(Provide[Container.payment_service]),
):
    try:
        # Verify payment
        transaction_id = str(uuid.uuid4())
        logger.info(f"Trasaction ID generated: {transaction_id}")
        payment_response = await payment_service.create_payment_link(
            amount=user_data.amount * 100,  # Convert to paise
            transaction_id=transaction_id,
            user_id=user_data.email,
            mobile_number=user_data.phone_number
        )

        if "data" in payment_response and "instrumentResponse" in payment_response["data"]:
            payment_url = payment_response["data"]["instrumentResponse"]["redirectInfo"]["url"]

            registration_data = user_data.model_dump()
            registration_data["registration_date"] = str(datetime.now())
            registration_data["payment_status"] = PaymentStatus.PENDING.value
            registration_data["transaction_id"] = transaction_id
            await dynamodb_service.create_registration(registration_data)

            logger.info(f"Trasaction details: {registration_data}. Payment status is pending")
            return {
                "payment_url": payment_url, 
                "transaction_id": transaction_id,
                "name": user_data.name,
                "email": user_data.email,
                "event_type": user_data.event_type,
                "amount": user_data.amount,
                "payment_status": PaymentStatus.PENDING.value,
                "payment_date": None,
                "registration_date": registration_data["registration_date"],
            }
        
    except Exception as e:
        logger.error(f"Registration failed for user {user_data.email}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/payment-callback", response_model=RegistrationResponse)
@inject
async def payment_callback(
    request: PaymentCallbackRequest,
    payment_service: PaymentService = Depends(Provide[Container.payment_service]),
    dynamodb_service: UserDAO = Depends(Provide[Container.dynamodb_service]),
    communication_service: CommunicationService = Depends(Provide[Container.communication_service])
):
    try:
        # Verify payment with PhonePe
        payment_status = await payment_service.verify_payment(request.transaction_id)

        if payment_status == "success":
            # Update registration status in DynamoDB
            update = RegistrationUpdate(
                payment_status=payment_status,
                payment_date=str(datetime.now())
            )
            response = await dynamodb_service.update_registration(request.transaction_id, update)
            logger.info(f"Payment Success for transaction {request.transaction_id}")

            # Fetch user details
            user_data = await dynamodb_service.get_registration(request.transaction_id, response["email"])

            # Send confirmation messages
            communication_service.send_sms(user_data["phone_number"], "Your registration is successful!")
            communication_service.send_whatsapp(user_data["phone_number"], "Your registration is successful!")
            communication_service.send_email(user_data["email"], "Registration Successful", "Your registration for the running event is successful!")

            logger.info(f"Confirmation messages sent to user {user_data['email']}")

            logger.info(f"Payment successful for transaction {request.transaction_id}")
            return {
                    "transaction_id": user_data["transaction_id"],
                    "name": user_data["name"],
                    "email": user_data["email"],
                    "event_type": user_data["event_type"],
                    "amount": user_data["amount"],
                    "payment_status": user_data["payment_status"],
                    "registration_date": user_data["registration_date"],
                    "payment_date": user_data["payment_date"],
                    "payment_url": None
                }
        else:
            response = await dynamodb_service.update_registration(request.transaction_id, "failed")
            logger.error(f"Payment failed for transaction {request.transaction_id}")
            return {"status": "failed", "message": f"Payment failed for {request.transaction_id}"}

    except Exception as e:
        logger.error(f"Error processing payment callback: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/registrations/by-phone/{phone_number}")
@inject
async def get_registrations_by_phone(
    phone_number: str,
    dynamodb_service: UserDAO = Depends(Provide[Container.dynamodb_service])
):
    registrations = await dynamodb_service.query_by_phone_number(phone_number)
    return registrations

@router.get("/registrations/by-phone-and-name/{phone_number}/{name}")
@inject
async def get_registrations_by_phone_and_name(
    phone_number: str,
    name: str,
    dynamodb_service: UserDAO = Depends(Provide[Container.dynamodb_service])
):
    registrations = await dynamodb_service.query_by_phone_number_and_name(phone_number, name)
    return registrations