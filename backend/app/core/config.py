from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    PHONEPE_CLIENT_ID: Optional[str] = "TEST-M22HO8VO83W1L_25041"
    PHONEPE_CLIENT_SECRET: Optional[str] = "MWM3M2ExN2UtMGFlMS00ZDZmLWI5ZmMtYzI5ZWJmNmJlYWNl"
    PHONEPE_BASE_URL: Optional[str] = "https://api-preprod.phonepe.com/apis/pg-sandbox"
    BASE_URL: Optional[str] = "https://api-preprod.phonepe.com/apis/pg-sandbox"
    AWS_ACCESS_KEY_ID: Optional[str]
    AWS_SECRET_ACCESS_KEY: Optional[str]
    AWS_REGION: Optional[str] = "eu-north-1"
    DYNAMODB_TABLE: Optional[str] = "RunningEventRegistrations"
    API_KEY: str
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()