"""Error handling examples."""
from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/api/error", tags=["Error Examples"])


@router.get("/400")
async def bad_request_error():
    """Example of 400 Bad Request error."""
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="This is a bad request error example"
    )


@router.get("/404")
async def not_found_error():
    """Example of 404 Not Found error."""
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Resource not found example"
    )


@router.get("/500")
async def internal_server_error():
    """Example of 500 Internal Server Error."""
    # This will be caught by the global error handler
    raise Exception("This is an internal server error example")


@router.get("/custom")
async def custom_error():
    """Example of custom error with details."""
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail={
            "error": "CustomValidationError",
            "message": "Custom validation failed",
            "field": "example_field"
        }
    )
