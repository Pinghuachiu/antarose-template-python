"""Hello world example endpoint."""
from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["Examples"])


@router.get("/hello")
async def hello():
    """Simple hello world endpoint."""
    return {
        "message": "Hello from Antarose Template!",
        "framework": "FastAPI",
        "language": "Python"
    }


@router.get("/hello/{name}")
async def hello_name(name: str):
    """Personalized hello endpoint."""
    return {
        "message": f"Hello, {name}!",
        "framework": "FastAPI"
    }
