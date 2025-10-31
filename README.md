# Antarose Template - Python Full Stack

A production-ready full-stack template featuring FastAPI + Python backend and Next.js 15 frontend.

## Overview

This template provides a solid foundation for building modern web applications with:

- **Backend**: FastAPI + Python 3.13 API server
- **Frontend**: Next.js 15 + React 19 + Tailwind CSS + shadcn/ui
- **Architecture**: Separate frontend/backend (no monorepo)
- **Development**: Hot reload, Type hints, Linting
- **Production**: Optimized builds, security headers, async support

## Quick Start

### Using Bootstrap Script (Recommended) 🚀

Create a new project from this template with a single command:

```bash
# Method 1: Download and run locally
curl -O https://raw.githubusercontent.com/Pinghuachiu/antarose-template-python/main/anta-python.sh
chmod +x anta-python.sh
./anta-python.sh my-awesome-project

# Method 2: Direct execution (one-liner)
curl -fsSL https://raw.githubusercontent.com/Pinghuachiu/antarose-template-python/main/anta-python.sh | bash -s my-awesome-project
```

**Interactive Configuration:**

The script will guide you through setup with these prompts:

| Prompt | Default Value | Required |
|--------|--------------|----------|
| Project description | "A Python project built with Antarose Template" | No |
| Author | jackalchiu@antarose.com | No |
| GitHub repository URL | (skip) | No |
| Install dependencies? | Yes | No |

**What the script does automatically:**

- ✅ **Validates environment** (Git, Python 3.12+, uv installed)
- ✅ **Clones template** from this repository
- ✅ **Validates project name** (Python package naming rules)
- ✅ **Removes template Git history** (.git/ directory)
- ✅ **Cleans up files** (removes docs/specs/, keeps docs/architecture/)
- ✅ **Updates configuration**:
  - `frontend/package.json` - name, description, author, version
  - `backend/requirements.txt` - project metadata
  - `README.md` - project name
- ✅ **Creates virtual environment** (using uv)
- ✅ **Installs dependencies** (frontend + backend)
- ✅ **Initializes new Git repository** with initial commit
- ✅ **Sets up Git remote** (if provided)

**Requirements:**
- ✅ Project name must be lowercase (a-z, 0-9, -, _)
- ✅ Max 214 characters
- ✅ Cannot start with `.` or `_`

### Manual Setup

### Prerequisites

- Python 3.12 or higher
- uv (Python package manager)
- Node.js 18 or higher (for frontend)
- npm or yarn (for frontend)

### Full Stack Setup

```bash
# Install backend dependencies
cd backend
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt

# Install frontend dependencies
cd ../frontend
npm install
```

### Start Development Servers

**Terminal 1 - Backend:**
```bash
cd backend
source .venv/bin/activate
uvicorn src.main:app --reload --port 4000
# Runs on http://localhost:4000
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
# Runs on http://localhost:3000
```

## Project Structure

```
antarose-template-python/
├── backend/                  # FastAPI server
│   ├── .venv/               # Virtual environment
│   ├── src/
│   │   ├── main.py          # Application entry point
│   │   ├── core/            # Core configurations
│   │   ├── middlewares/     # Custom middlewares
│   │   └── routes/          # API endpoints
│   └── requirements.txt     # Python dependencies
├── frontend/                 # Next.js application
│   ├── app/                 # Next.js App Router
│   ├── components/          # React components
│   ├── lib/                 # Utilities
│   ├── package.json
│   └── tsconfig.json
├── docs/                     # Documentation
└── README.md                # This file
```

## Backend

### Technology Stack

- **Framework**: FastAPI
- **Language**: Python 3.13
- **ASGI Server**: Uvicorn
- **Security**: Built-in CORS and security headers
- **Validation**: Pydantic models

### Starting the Backend

```bash
cd backend
source .venv/bin/activate    # Activate virtual environment
uvicorn src.main:app --reload --port 4000  # Development mode
uvicorn src.main:app --port 4000           # Production mode
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/api/hello` | Example API |
| GET | `/api/error/{error_type}` | Error handling examples |
| GET | `/docs` | Interactive API documentation (Swagger UI) |
| GET | `/redoc` | Alternative API documentation (ReDoc) |

### Backend Project Structure

```
backend/
├── src/
│   ├── main.py               # App entry point
│   ├── core/
│   │   ├── config.py         # Configuration settings
│   │   └── __init__.py
│   ├── middlewares/
│   │   ├── logger.py         # Request logging
│   │   ├── error_handler.py  # Error handling
│   │   └── __init__.py
│   └── routes/
│       ├── health.py         # Health check
│       ├── hello.py          # Example endpoint
│       ├── error_example.py  # Error examples
│       └── __init__.py
├── .venv/                    # Virtual environment
└── requirements.txt          # Dependencies
```

### Environment Variables (Backend)

Create `backend/.env`:

```env
PORT=4000
ENVIRONMENT=development
CORS_ORIGINS=["http://localhost:3000"]
```

### Adding New API Endpoints

1. Create route handler in `backend/src/routes/`
2. Import and register in `backend/src/main.py`
3. Test with curl or frontend

Example:

```python
# backend/src/routes/users.py
from fastapi import APIRouter

router = APIRouter(prefix="/api/users", tags=["users"])

@router.get("/")
async def get_users():
    return {"users": []}
```

For detailed backend documentation, see [backend/README.md](./backend/README.md).

## Frontend

### Technology Stack

- **Framework**: Next.js 15 (App Router)
- **Language**: TypeScript
- **UI Library**: React 19
- **Styling**: Tailwind CSS
- **Components**: shadcn/ui
- **Icons**: Lucide React

### Starting the Frontend

```bash
cd frontend
npm install
npm run dev      # Development mode (port 3000)
npm run build    # Production build
npm start        # Production mode
```

### Features

- ✅ Next.js 15 with App Router
- ✅ TypeScript strict mode
- ✅ Tailwind CSS configured
- ✅ shadcn/ui components
- ✅ Responsive header/footer
- ✅ Error boundary and 404 page
- ✅ ESLint and Prettier

### Frontend Project Structure

```
frontend/
├── app/                      # Next.js App Router
│   ├── about/page.tsx       # About page
│   ├── layout.tsx           # Root layout
│   ├── page.tsx             # Home page
│   ├── error.tsx            # Error boundary
│   ├── not-found.tsx        # 404 page
│   └── globals.css          # Global styles
├── components/
│   ├── ui/                  # shadcn/ui components
│   └── layout/              # Layout components
└── lib/
    └── utils.ts             # Utilities
```

### Environment Variables (Frontend)

Create `frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:4000
```

### Adding New Pages

Create `frontend/app/[pagename]/page.tsx`:

```tsx
export default function NewPage() {
  return <div>New Page</div>
}
```

For detailed frontend documentation, see [frontend/README.md](./frontend/README.md).

## Development Workflow

### 1. Start Both Servers

```bash
# Terminal 1 - Backend
cd backend
source .venv/bin/activate
uvicorn src.main:app --reload --port 4000

# Terminal 2 - Frontend
cd frontend && npm run dev
```

### 2. Access Application

- Frontend: http://localhost:3000
- Backend API: http://localhost:4000
- API Docs (Swagger): http://localhost:4000/docs
- API Docs (ReDoc): http://localhost:4000/redoc
- Health Check: http://localhost:4000/health

### 3. Make Changes

- Backend changes auto-reload via Uvicorn `--reload`
- Frontend changes auto-reload via Next.js Fast Refresh

## Production Build

### Build Backend

```bash
cd backend
source .venv/bin/activate
# No build step needed for Python
uvicorn src.main:app --host 0.0.0.0 --port 4000
```

### Build Frontend

```bash
cd frontend
npm run build    # Creates optimized production build
npm start        # Starts production server
```

## API Integration

### Frontend Calling Backend

```typescript
// frontend/app/example/page.tsx
'use client'

import { useEffect, useState } from 'react'

export default function ExamplePage() {
  const [data, setData] = useState(null)

  useEffect(() => {
    fetch('http://localhost:4000/api/hello')
      .then(res => res.json())
      .then(setData)
  }, [])

  return <div>{JSON.stringify(data)}</div>
}
```

## Code Quality

### Backend

```bash
cd backend
source .venv/bin/activate
# Linting (if configured)
ruff check .
# Formatting
black .
# Type checking
mypy src/
```

### Frontend

```bash
cd frontend
npm run lint      # Next.js ESLint
```

## Security Features

### Backend
- FastAPI built-in security features
- CORS configuration
- Pydantic data validation
- Async support for better performance

### Frontend
- Next.js security defaults
- Environment variable protection
- CSP headers (configurable)

## Performance Optimizations

### Backend
- Async/await support
- Efficient routing
- Automatic API documentation
- Built-in data validation

### Frontend
- Next.js automatic code splitting
- Image optimization
- Static generation (SSG)
- Incremental static regeneration (ISR)

## Troubleshooting

### Port Already in Use

**Backend (port 4000):**
```bash
lsof -ti:4000 | xargs kill -9
```

**Frontend (port 3000):**
```bash
lsof -ti:3000 | xargs kill -9
```

### CORS Errors

1. Check `backend/.env` has correct `CORS_ORIGINS`
2. Verify frontend is running on allowed origin
3. Check browser console for specific error

### Virtual Environment Issues

**Recreate virtual environment:**
```bash
cd backend
rm -rf .venv
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## Documentation

- [Backend Documentation](./backend/README.md) - API server details
- [Frontend Documentation](./frontend/README.md) - Next.js app details
- [Technical Docs](./docs/) - Architecture and design documents

## Technology References

### Backend
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

### Frontend
- [Next.js Documentation](https://nextjs.org/docs)
- [React Documentation](https://react.dev/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [shadcn/ui Documentation](https://ui.shadcn.com)

## License

MIT

## Contributing

This is a template repository. Feel free to customize for your project needs.

## Support

For issues and questions:
1. Check documentation in `docs/` directory
2. Review component-specific README files
3. Consult technology-specific documentation linked above
