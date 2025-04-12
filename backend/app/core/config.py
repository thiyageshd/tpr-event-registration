from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    RAZORPAY_KEY_ID: str
    RAZORPAY_KEY_SECRET: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str = "us-west-2"
    DYNAMODB_TABLE: str = "RunningEventRegistrations"
    API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()