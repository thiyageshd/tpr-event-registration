
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import HTTPException
from fastapi.security.api_key import APIKeyHeader
from app.core.config import settings
from loguru import logger

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
        api_key = await api_key_header(request)

        if api_key != settings.API_KEY:
            logger.warning(f"Invalid API key: {api_key}")
            raise HTTPException(status_code=403, detail="Invalid API key")

        response = await call_next(request)
        return response