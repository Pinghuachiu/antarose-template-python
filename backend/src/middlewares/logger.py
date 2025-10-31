"""Request logging middleware."""
import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class LoggerMiddleware(BaseHTTPMiddleware):
    """Middleware for logging HTTP requests."""

    async def dispatch(self, request: Request, call_next):
        """Log request details and response time."""
        start_time = time.time()

        # Process request
        response = await call_next(request)

        # Calculate response time
        process_time = time.time() - start_time

        # Log request details
        print(f"{request.method} {request.url.path} - {response.status_code} - {process_time:.3f}s")

        return response
