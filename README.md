# Antarose Template - Python Full Stack

A production-ready full-stack template featuring FastAPI + Python backend and Next.js 15 frontend.

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.5-green)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-15.5-black)](https://nextjs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 目錄

- [概述](#概述)
- [快速開始](#快速開始)
- [專案結構](#專案結構)
- [後端 (FastAPI)](#後端-fastapi)
- [前端 (Next.js)](#前端-nextjs)
- [開發工作流程](#開發工作流程)
- [生產環境部署](#生產環境部署)
- [疑難排解](#疑難排解)

---

## 概述

此模板提供建構現代化 Web 應用程式的堅實基礎：

### ✨ 核心技術

**後端 (Backend)**
- **FastAPI** - 現代、快速的 Python Web 框架
- **Python 3.13** - 最新穩定版本
- **SQLAlchemy** - 非同步資料庫 ORM
- **Pydantic** - 資料驗證與設定管理
- **Uvicorn** - ASGI 伺服器

**前端 (Frontend)**
- **Next.js 15** - React 框架 (App Router)
- **React 19** - 使用者介面函式庫
- **Tailwind CSS** - Utility-first CSS 框架
- **shadcn/ui** - 高品質元件庫
- **TypeScript** - 型別安全

### 🎯 功能特色

- ✅ **前後端分離架構** - 獨立開發與部署
- ✅ **非同步資料庫支援** - SQLite / PostgreSQL / MySQL
- ✅ **自動 API 文檔** - Swagger UI / ReDoc
- ✅ **型別安全** - Python Type Hints + TypeScript
- ✅ **熱重載開發** - 即時預覽變更
- ✅ **測試框架** - pytest (後端) + Jest (前端)
- ✅ **一鍵專案初始化** - 自動化腳本

---

## 快速開始

### 方式一：使用初始化腳本 (推薦) 🚀

**下載並執行腳本：**

```bash
# 方法 1: 下載後執行
curl -O https://raw.githubusercontent.com/Pinghuachiu/antarose-template-python/main/anta-python.sh
chmod +x anta-python.sh
./anta-python.sh my-awesome-project

# 方法 2: 直接執行 (一行命令)
curl -fsSL https://raw.githubusercontent.com/Pinghuachiu/antarose-template-python/main/anta-python.sh | bash -s my-awesome-project
```

**腳本會自動執行以下操作：**

| 步驟 | 說明 |
|------|------|
| ✅ 環境檢查 | 驗證 Git, Python 3.12+, uv, Node.js, npm 是否安裝 |
| ✅ Clone 模板 | 從 GitHub 複製最新版本 |
| ✅ 清理檔案 | 移除 .git 歷史記錄和模板專用檔案 |
| ✅ 更新配置 | 修改專案名稱、描述、作者資訊 |
| ✅ 建立虛擬環境 | 使用 uv 建立 Python 虛擬環境 |
| ✅ 安裝依賴 | 安裝前後端所需套件 (可選) |
| ✅ 初始化 Git | 建立新的 Git repository |

**互動式設定：**

```
? Project description: (預設: A Python project built with Antarose Template)
? Author: (預設: jackalchiu@antarose.com)
? GitHub repository URL: (可選，直接按 Enter 跳過)
? Install dependencies now?: (Y/n)
```

### 方式二：手動安裝

#### 1. Clone Repository

```bash
git clone https://github.com/Pinghuachiu/antarose-template-python.git my-project
cd my-project
rm -rf .git
git init
```

#### 2. 安裝依賴

**後端：**
```bash
cd backend
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

**前端：**
```bash
cd frontend
npm install
```

#### 3. 啟動開發伺服器

**Terminal 1 - 後端 (Port 3030):**
```bash
cd backend
source .venv/bin/activate
uvicorn src.main:app --reload --port 3030
```

**Terminal 2 - 前端 (Port 3000):**
```bash
cd frontend
npm run dev
```

#### 4. 訪問應用

- 🌐 **前端**: http://localhost:3000
- 🔌 **後端 API**: http://localhost:3030
- 📚 **API 文檔 (Swagger)**: http://localhost:3030/docs
- 📖 **API 文檔 (ReDoc)**: http://localhost:3030/redoc
- ❤️ **健康檢查**: http://localhost:3030/health

---

## 專案結構

```
antarose-template-python/
├── backend/                  # FastAPI 後端
│   ├── .venv/               # Python 虛擬環境
│   ├── src/
│   │   ├── main.py          # 應用程式入口
│   │   ├── core/
│   │   │   ├── config.py    # 配置管理
│   │   │   └── database.py  # 資料庫連接
│   │   ├── models/          # SQLAlchemy 模型
│   │   │   └── user.py      # 使用者模型範例
│   │   ├── schemas/         # Pydantic schemas
│   │   ├── middlewares/     # 自訂中介軟體
│   │   │   ├── logger.py
│   │   │   └── error_handler.py
│   │   └── routes/          # API 路由
│   │       ├── health.py
│   │       ├── hello.py
│   │       └── error_example.py
│   ├── requirements.txt     # Python 依賴
│   ├── .env.example        # 環境變數範本
│   └── README.md
│
├── frontend/                 # Next.js 前端
│   ├── app/                 # App Router
│   │   ├── layout.tsx       # 根佈局
│   │   ├── page.tsx         # 首頁
│   │   ├── about/           # About 頁面
│   │   ├── error.tsx        # 錯誤邊界
│   │   └── not-found.tsx    # 404 頁面
│   ├── components/          # React 元件
│   │   ├── ui/              # shadcn/ui 元件
│   │   └── layout/          # 佈局元件
│   ├── lib/
│   │   ├── utils.ts         # 工具函數
│   │   └── api-client.ts    # API 客戶端
│   ├── package.json
│   ├── .env.local          # 前端環境變數
│   └── README.md
│
├── docs/                     # 文檔
│   └── architecture/        # 架構文件
├── anta-python.sh           # 專案初始化腳本
├── README.md                # 此檔案
└── .gitignore
```

---

## 後端 (FastAPI)

### 技術棧

| 技術 | 版本 | 用途 |
|------|------|------|
| FastAPI | 0.115.5 | Web 框架 |
| Uvicorn | 0.34.0 | ASGI 伺服器 |
| SQLAlchemy | 2.0.36 | ORM |
| Pydantic | 2.10.3 | 資料驗證 |
| pytest | 8.3.4 | 測試框架 |

### API 端點

| 方法 | 路徑 | 說明 |
|------|------|------|
| GET | `/` | 根端點 |
| GET | `/health` | 健康檢查 |
| GET | `/api/hello` | Hello World 範例 |
| GET | `/api/hello/{name}` | 個人化問候 |
| GET | `/api/error/400` | 錯誤處理範例 (400) |
| GET | `/api/error/404` | 錯誤處理範例 (404) |
| GET | `/api/error/500` | 錯誤處理範例 (500) |
| GET | `/docs` | Swagger UI |
| GET | `/redoc` | ReDoc 文檔 |

### 環境變數設定

建立 `backend/.env` 檔案：

```env
# 應用程式設定
APP_NAME=Antarose Template API
APP_VERSION=1.0.0
ENVIRONMENT=development

# 伺服器設定
PORT=3030
HOST=0.0.0.0

# CORS 設定
CORS_ORIGINS=["http://localhost:3000"]

# 資料庫設定
DATABASE_URL=sqlite+aiosqlite:///./app.db
```

### 新增 API 端點

1. **建立路由檔案** `backend/src/routes/users.py`:

```python
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.core.database import get_db

router = APIRouter(prefix="/api/users", tags=["Users"])

@router.get("/")
async def get_users(db: AsyncSession = Depends(get_db)):
    return {"users": []}
```

2. **註冊路由** 在 `backend/src/main.py`:

```python
from src.routes import users

app.include_router(users.router)
```

### 資料庫操作

**建立模型** `backend/src/models/post.py`:

```python
from sqlalchemy import String, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from src.core.database import Base

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
```

### 執行測試

```bash
cd backend
source .venv/bin/activate
pytest
```

---

## 前端 (Next.js)

### 技術棧

| 技術 | 版本 | 用途 |
|------|------|------|
| Next.js | 15.5.6 | React 框架 |
| React | 19 | UI 函式庫 |
| TypeScript | 5.x | 型別系統 |
| Tailwind CSS | 3.x | CSS 框架 |
| shadcn/ui | Latest | 元件庫 |

### 環境變數設定

建立 `frontend/.env.local` 檔案：

```env
NEXT_PUBLIC_API_URL=http://localhost:3030
```

### API 整合範例

```typescript
// frontend/app/example/page.tsx
'use client'

import { useEffect, useState } from 'react'

export default function ExamplePage() {
  const [data, setData] = useState(null)

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/hello`)
      .then(res => res.json())
      .then(setData)
  }, [])

  return <div>{JSON.stringify(data)}</div>
}
```

### 新增頁面

建立 `frontend/app/users/page.tsx`:

```tsx
export default function UsersPage() {
  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold">Users</h1>
    </div>
  )
}
```

---

## 開發工作流程

### Git Flow 分支策略

```
main          (生產環境)
  └── develop (開發環境)
        └── feature/feature-name (功能開發)
        └── bugfix/bug-name (錯誤修復)
```

### 開發流程

1. **建立功能分支**
```bash
git checkout develop
git checkout -b feature/new-feature
```

2. **開發與測試**
```bash
# 後端測試
cd backend && pytest

# 前端測試
cd frontend && npm run lint
```

3. **提交變更**
```bash
git add .
git commit -m "feat: add new feature"
```

4. **合併回 develop**
```bash
git checkout develop
git merge --no-ff feature/new-feature
git push origin develop
```

5. **發布到 main**
```bash
git checkout main
git merge --no-ff develop
git tag -a v1.x.x -m "Release v1.x.x"
git push origin main --tags
```

---

## 生產環境部署

### 後端部署

**使用 Gunicorn + Uvicorn workers:**

```bash
cd backend
source .venv/bin/activate
gunicorn src.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:3030
```

**使用 Docker:**

```dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src/ ./src/
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "3030"]
```

### 前端部署

```bash
cd frontend
npm run build
npm start
```

---

## 疑難排解

### Port 已被佔用

```bash
# 檢查 Port 3030 (後端)
lsof -ti:3030 | xargs kill -9

# 檢查 Port 3000 (前端)
lsof -ti:3000 | xargs kill -9
```

### CORS 錯誤

1. 檢查 `backend/.env` 中的 `CORS_ORIGINS`
2. 確認前端 URL 在允許列表中
3. 檢查瀏覽器主控台的具體錯誤訊息

### 資料庫連接失敗

```bash
# 重新建立資料庫
cd backend
rm -f app.db
source .venv/bin/activate
python -c "from src.core.database import init_db; import asyncio; asyncio.run(init_db())"
```

### 虛擬環境問題

```bash
# 重建虛擬環境
cd backend
rm -rf .venv
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

### 前端建置錯誤

```bash
cd frontend
rm -rf .next node_modules
npm install
npm run build
```

---

## 文檔資源

### 後端文檔
- [FastAPI 官方文檔](https://fastapi.tiangolo.com/)
- [SQLAlchemy 文檔](https://docs.sqlalchemy.org/)
- [Pydantic 文檔](https://docs.pydantic.dev/)
- [Uvicorn 文檔](https://www.uvicorn.org/)

### 前端文檔
- [Next.js 文檔](https://nextjs.org/docs)
- [React 文檔](https://react.dev/)
- [Tailwind CSS 文檔](https://tailwindcss.com/docs)
- [shadcn/ui 文檔](https://ui.shadcn.com)

### 專案文檔
- [後端詳細文檔](./backend/README.md)
- [前端詳細文檔](./frontend/README.md)
- [架構文件](./docs/architecture/)

---

## 授權條款

MIT License - 詳見 [LICENSE](LICENSE) 檔案

---

## 貢獻指南

歡迎提交 Issue 和 Pull Request！

1. Fork 此專案
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

---

## 支援與反饋

- 📧 Email: jackalchiu@antarose.com
- 🐛 Issues: [GitHub Issues](https://github.com/Pinghuachiu/antarose-template-python/issues)
- 📚 Docs: [Documentation](./docs/)

---

**由 Antarose AI Tech Inc. 用心打造** ❤️
