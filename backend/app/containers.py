from dependency_injector import containers, providers
from app.services.data_store import UserDAO
from app.services.payment import PaymentService
from app.services.communication import CommunicationService
from app.core.logging import setup_logging

class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    logger = providers.Singleton(setup_logging)

    dynamodb_service = providers.Singleton(UserDAO)
    payment_service = providers.Singleton(PaymentService)
    communication_service = providers.Singleton(CommunicationService)
    