from fastapi import APIRouter, HTTPException, Depends
from app.models import UserRegistration, PaymentResponse
from dependency_injector.wiring import inject, Provide
from app.containers import Container
from app.services.data_store import UserDAO
from app.services.payment import PaymentService
from app.services.communication import CommunicationService

router = APIRouter()

@router.post("/register")
@inject
async def register_user(
    user: UserRegistration,
    payment_response: PaymentResponse,
    dynamodb_service: UserDAO = Depends(Provide[Container.dynamodb_service]),
    payment_service: PaymentService = Depends(Provide[Container.payment_service]),
    communication_service: CommunicationService = Depends(Provide[Container.communication_service]),
    logger = Depends(Provide[Container.logger])
):
    try:
        # Verify payment
        if not payment_service.verify_payment(payment_response.payment_id, payment_response.order_id, payment_response.signature):
            logger.error(f"Invalid payment signature for user {user.email}")
            raise HTTPException(status_code=400, detail="Invalid payment signature")

        payment_details = payment_service.get_payment_details(payment_response.payment_id)

        registration_data = {
            'email': user.email,
            'phone': user.phone,
            'name': user.name,
            'event_type': user.event_type,
            'payment_id': payment_response.payment_id,
            'order_id': payment_response.order_id,
            'amount': payment_details['amount'] / 100
        }

        # Save to DynamoDB
        dynamodb_service.save_registration(registration_data)
        logger.info(f"Registration saved for user {user.email}")

        # Send confirmation messages
        communication_service.send_sms(user.phone, "Your registration is successful!")
        communication_service.send_whatsapp(user.phone, "Your registration is successful!")
        communication_service.send_email(user.email, "Registration Successful", "Your registration for the running event is successful!")

        logger.info(f"Confirmation messages sent to user {user.email}")

        return {"status": "success", "message": "Registration completed successfully"}
    except Exception as e:
        logger.error(f"Registration failed for user {user.email}: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))