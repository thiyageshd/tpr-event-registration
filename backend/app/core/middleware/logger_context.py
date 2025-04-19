import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from loguru import logger

class LoggerContextMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        # Add request_id to the context
        request_id = request.headers.get("X-Request-ID", "unknown")
        logger.bind(request_id=request_id)

        response = await call_next(request)

        process_time = time.time() - start_time
        logger.info(f"Request {request_id} completed in {process_time:.2f} seconds")

        return response

