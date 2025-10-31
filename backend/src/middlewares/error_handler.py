"""Global error handling middleware."""
from fastapi import Request, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class ErrorHandlerMiddleware(BaseHTTPMiddleware):
    """Middleware for handling uncaught exceptions."""

    async def dispatch(self, request: Request, call_next):
        """Handle errors globally."""
        try:
            return await call_next(request)
        except Exception as exc:
            # Log the error
            print(f"Unhandled error: {exc}")

            # Return error response
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "error": "Internal Server Error",
                    "message": str(exc) if request.app.debug else "An unexpected error occurred"
                }
            )
