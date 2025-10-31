# Backend - FastAPI API Server

FastAPI backend server for Antarose Template project.

## Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.13+
- **ASGI Server**: Uvicorn
- **Validation**: Pydantic
- **Configuration**: pydantic-settings

## Features

- ✅ FastAPI with async support
- ✅ Automatic API documentation (Swagger UI & ReDoc)
- ✅ CORS middleware configured
- ✅ Request logging middleware
- ✅ Global error handling
- ✅ Environment-based configuration
- ✅ Type hints and validation

## Project Structure

```
backend/
├── .venv/                    # Virtual environment
├── src/
│   ├── main.py              # Application entry point
│   ├── core/
│   │   ├── config.py        # Configuration settings
│   │   └── __init__.py
│   ├── middlewares/
│   │   ├── logger.py        # Request logging
│   │   ├── error_handler.py # Error handling
│   │   └── __init__.py
│   └── routes/
│       ├── health.py        # Health check
│       ├── hello.py         # Example endpoint
│       ├── error_example.py # Error examples
│       └── __init__.py
├── requirements.txt         # Dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## Setup

### 1. Create Virtual Environment

```bash
uv venv
```

### 2. Activate Virtual Environment

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure Environment

```bash
cp .env.example .env
# Edit .env with your configuration
```

## Development

### Start Development Server

```bash
uvicorn src.main:app --reload --port 4000
```

Or use Python directly:

```bash
python -m src.main
```

Server will be available at:
- API: http://localhost:4000
- Swagger UI: http://localhost:4000/docs
- ReDoc: http://localhost:4000/redoc

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| GET | `/api/hello` | Hello world example |
| GET | `/api/hello/{name}` | Personalized hello |
| GET | `/api/error/400` | Bad request example |
| GET | `/api/error/404` | Not found example |
| GET | `/api/error/500` | Server error example |
| GET | `/api/error/custom` | Custom error example |

### Testing Endpoints

```bash
# Health check
curl http://localhost:4000/health

# Hello world
curl http://localhost:4000/api/hello

# Personalized hello
curl http://localhost:4000/api/hello/John

# Error examples
curl http://localhost:4000/api/error/400
curl http://localhost:4000/api/error/404
curl http://localhost:4000/api/error/500
```

## Adding New Endpoints

1. Create a new router file in `src/routes/`:

```python
# src/routes/users.py
from fastapi import APIRouter

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.get("/")
async def get_users():
    return {"users": []}
```

2. Import and include the router in `src/main.py`:

```python
from src.routes import users

app.include_router(users.router)
```

## Configuration

Environment variables are managed through `.env` file:

```env
# Application
APP_NAME=Antarose Template API
APP_VERSION=1.0.0
ENVIRONMENT=development

# Server
PORT=4000
HOST=0.0.0.0

# CORS
CORS_ORIGINS=["http://localhost:3000"]
```

## Production Deployment

### 1. Install production dependencies

```bash
uv pip install -r requirements.txt
```

### 2. Run with Uvicorn

```bash
uvicorn src.main:app --host 0.0.0.0 --port 4000
```

### 3. Or use Gunicorn with Uvicorn workers

```bash
gunicorn src.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:4000
```

## Code Quality

### Linting (optional)

Install and run Ruff:

```bash
uv pip install ruff
ruff check src/
```

### Formatting (optional)

Install and run Black:

```bash
uv pip install black
black src/
```

### Type Checking (optional)

Install and run mypy:

```bash
uv pip install mypy
mypy src/
```

## Documentation

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

## Troubleshooting

### Port already in use

```bash
# Find process using port 4000
lsof -ti:4000

# Kill the process
lsof -ti:4000 | xargs kill -9
```

### Module not found errors

Make sure you're in the backend directory and virtual environment is activated:

```bash
cd backend
source .venv/bin/activate
uv pip install -r requirements.txt
```

### CORS errors

Check `CORS_ORIGINS` in `.env` file and make sure it includes your frontend URL.
