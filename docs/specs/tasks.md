# Task Breakdown Document（極簡版 - 方案 B）

**專案**: antarose-template-nodejs
**版本**: 3.0.0 (極簡版 - 前後端獨立)
**日期**: 2025-10-24
**CTO**: 負責任務分配與驗收

---

## Phase 1: 模板核心（唯一實作階段）

**預估時間**: 5 個工作天
**目標**: 建立極簡的前後端獨立模板

**架構原則**: 前後端完全獨立，各自管理依賴，避免「改到一起掛」

---

## Week 1: 前端基礎 (Day 1-2)

### Task 1: Next.js + TypeScript 基礎設定

**負責人**: Waylon (前端工程師)
**預估時間**: 0.5 天
**優先級**: P0 (最高)

**任務內容**:
- [ ] 建立 `frontend/` 目錄
- [ ] 初始化 Next.js 15 專案
  ```bash
  cd frontend
  npx create-next-app@latest . --typescript --tailwind --app --no-src-dir
  ```
- [ ] 配置 TypeScript (`tsconfig.json`)
  - [ ] 啟用 strict mode
  - [ ] 配置 path aliases (`@/*`)
- [ ] 配置 ESLint (`.eslintrc.js`)
- [ ] 配置 Prettier (`.prettierrc`)
- [ ] 建立基本 Layout (`app/layout.tsx`)
- [ ] 建立 Error Boundary (`app/error.tsx`)
- [ ] 建立 404 頁面 (`app/not-found.tsx`)

**交付成果**:
```
frontend/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   ├── error.tsx
│   └── not-found.tsx
├── .eslintrc.js
├── .prettierrc
├── next.config.js
├── tailwind.config.ts
├── tsconfig.json
└── package.json
```

**驗收標準**:
- ✅ `npm run dev` 可啟動（port 3000）
- ✅ TypeScript 無錯誤
- ✅ ESLint 無錯誤

---

### Task 2: Tailwind CSS + shadcn/ui 整合

**負責人**: Lisa (UI/UX Designer) + Waylon (前端工程師)
**預估時間**: 1 天
**優先級**: P0
**依賴**: Task 1

**任務內容**:
- [ ] 初始化 shadcn/ui
  ```bash
  cd frontend
  npx shadcn-ui@latest init
  ```
- [ ] 安裝基礎組件
  ```bash
  npx shadcn-ui@latest add button card input
  ```
- [ ] 安裝 Lucide React
  ```bash
  npm install lucide-react
  ```
- [ ] 建立 `components/ui/` 目錄
- [ ] 配置 Dark mode（可選）

**交付成果**:
- `components/ui/button.tsx`
- `components/ui/card.tsx`
- `components/ui/input.tsx`
- `components.json` (shadcn/ui 配置)

**驗收標準**:
- ✅ shadcn/ui 組件可正常使用
- ✅ Tailwind CSS 正常運作
- ✅ Lucide 圖示可正常顯示

---

### Task 3: 基本頁面範例

**負責人**: Waylon (前端工程師) + Lisa (UI/UX Designer)
**預估時間**: 0.5 天
**優先級**: P0
**依賴**: Task 2

**任務內容**:
- [ ] 建立首頁 (`app/page.tsx`)
  - [ ] 使用 shadcn/ui Button, Card 組件
  - [ ] 展示 Lucide 圖示使用
  - [ ] 簡單的 Hero Section
- [ ] 建立 About 頁面 (`app/about/page.tsx`)
  - [ ] 展示 SSG 渲染
  - [ ] 使用 shadcn/ui 組件
- [ ] 建立基本 Header 組件 (`components/layout/header.tsx`)
- [ ] 建立基本 Footer 組件 (`components/layout/footer.tsx`)

**交付成果**:
```
app/
├── page.tsx                     # 首頁
├── about/page.tsx               # About 頁面
└── layout.tsx                   # Root layout (含 Header/Footer)

components/
└── layout/
    ├── header.tsx
    └── footer.tsx
```

**驗收標準**:
- ✅ 可訪問 `/` 和 `/about`
- ✅ UI 美觀、響應式設計
- ✅ shadcn/ui 組件正確使用

---

## Week 1: 後端基礎 (Day 3-4)

### Task 4: Express + TypeScript 基礎設定

**負責人**: Costa (後端工程師)
**預估時間**: 0.5 天
**優先級**: P0

**任務內容**:
- [ ] 建立 `backend/` 目錄
- [ ] 初始化 Node.js 專案
  ```bash
  cd backend
  npm init -y
  ```
- [ ] 安裝依賴
  ```bash
  npm install express cors helmet compression
  npm install -D typescript @types/node @types/express ts-node-dev
  ```
- [ ] 配置 TypeScript (`tsconfig.json`)
- [ ] 配置 ESLint (`.eslintrc.js`)
- [ ] 配置 Prettier (`.prettierrc`)
- [ ] 建立 `src/` 目錄結構
- [ ] 建立 Express 入口 (`src/index.ts`)
- [ ] 配置 `package.json` scripts
  ```json
  {
    "scripts": {
      "dev": "ts-node-dev --respawn src/index.ts",
      "build": "tsc",
      "start": "node dist/index.js"
    }
  }
  ```

**交付成果**:
```
backend/
├── src/
│   ├── routes/
│   ├── middlewares/
│   └── index.ts
├── .eslintrc.js
├── .prettierrc
├── tsconfig.json
└── package.json
```

**驗收標準**:
- ✅ `npm run dev` 可啟動（port 4000）
- ✅ TypeScript 編譯無錯誤
- ✅ ESLint 無錯誤

---

### Task 5: 基礎中介層 + 範例 API

**負責人**: Costa (後端工程師)
**預估時間**: 0.5 天
**優先級**: P0
**依賴**: Task 4

**任務內容**:
- [ ] 建立 CORS 中介層 (`middlewares/cors.ts`)
  - [ ] 允許 `http://localhost:3000` (前端)
- [ ] 建立 Helmet 中介層 (Security headers)
- [ ] 建立 Logger 中介層 (`middlewares/logger.ts`)
- [ ] 建立 Health Check 路由 (`routes/health.ts`)
  - [ ] `GET /health` → `{ status: 'ok' }`
- [ ] 建立範例 API 路由 (`routes/hello.ts`)
  - [ ] `GET /api/hello` → `{ message: 'Hello from Express!' }`
- [ ] 整合所有中介層到 `index.ts`

**交付成果**:
```
src/
├── routes/
│   ├── health.ts
│   └── hello.ts
├── middlewares/
│   ├── cors.ts
│   └── logger.ts
└── index.ts
```

**驗收標準**:
- ✅ `/health` 回傳 `{ status: 'ok' }`
- ✅ `/api/hello` 回傳 JSON
- ✅ CORS 允許前端呼叫
- ✅ Console 顯示 HTTP 請求日誌

---

### Task 6: 錯誤處理

**負責人**: Chris (後端 Code Review)
**預估時間**: 0.5 天
**優先級**: P1
**依賴**: Task 5

**任務內容**:
- [ ] 建立 Error Handler 中介層 (`middlewares/error-handler.ts`)
- [ ] 定義統一的錯誤回應格式
  ```typescript
  {
    success: false,
    error: {
      code: string,
      message: string
    }
  }
  ```
- [ ] 建立範例錯誤端點 (`routes/error-example.ts`)
  - [ ] `GET /api/error` → 故意拋出錯誤，測試錯誤處理
- [ ] 整合 Error Handler 到 Express app

**交付成果**:
- `middlewares/error-handler.ts`
- `routes/error-example.ts`

**驗收標準**:
- ✅ API 錯誤統一回傳 JSON 格式
- ✅ 錯誤訊息清晰易懂
- ✅ 500 錯誤不洩漏內部資訊

---

## Week 2: 整合與文件 (Day 5)

### Task 7: 前後端整合測試

**負責人**: Waylon (前端) + Costa (後端)
**預估時間**: 0.5 天
**優先級**: P0
**依賴**: Task 3, Task 5

**任務內容**:
- [ ] 在前端建立 API client (`frontend/lib/api-client.ts`)
  ```typescript
  const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:4000'

  export async function fetchHello() {
    const res = await fetch(`${API_URL}/api/hello`)
    return res.json()
  }
  ```
- [ ] 在首頁展示呼叫後端 API
  ```typescript
  // app/page.tsx
  const data = await fetchHello()
  ```
- [ ] 測試 CORS 設定
- [ ] 確認前後端可正常通訊

**交付成果**:
- `frontend/lib/api-client.ts`
- 首頁展示後端回傳資料

**驗收標準**:
- ✅ 前端可成功呼叫 `/api/hello`
- ✅ CORS 無錯誤
- ✅ 資料正確顯示在前端

---

### Task 8: README + 文件整理

**負責人**: Costa (後端) + Waylon (前端)
**預估時間**: 0.5 天
**優先級**: P1
**依賴**: Task 7

**任務內容**:
- [ ] 撰寫根目錄 `README.md`
  - [ ] 專案介紹
  - [ ] 技術棧說明
  - [ ] 快速開始指南（分別啟動前後端）
  - [ ] 專案結構說明
  - [ ] 擴展指南連結
- [ ] 撰寫 `frontend/README.md`
  - [ ] 前端專案說明
  - [ ] 如何啟動
  - [ ] 如何新增頁面
  - [ ] shadcn/ui 使用說明
- [ ] 撰寫 `backend/README.md`
  - [ ] 後端專案說明
  - [ ] 如何啟動
  - [ ] 如何新增 API 端點
- [ ] 建立 `.env.example`（前後端各一份）
- [ ] 撰寫 `docs/guides/getting-started.md`

**交付成果**:
- `README.md` (根目錄)
- `frontend/README.md`
- `backend/README.md`
- `frontend/.env.example`
- `backend/.env.example`
- `docs/guides/getting-started.md`

**驗收標準**:
- ✅ README 清晰易懂
- ✅ 新手可按照文件快速啟動
- ✅ 包含常見問題解答

---

## 總任務統計

### Phase 1 (模板核心)
- **總任務數**: 8 個
- **預估時間**: 5 天
- **團隊成員**:
  - Waylon (前端開發): 4 個任務
  - Costa (後端開發): 4 個任務
  - Lisa (UI/UX): 1 個任務
  - Chris (後端審查): 1 個任務

### 任務依賴關係

```
前端線:
Task 1 (Next.js 設定)
  → Task 2 (Tailwind + shadcn/ui)
  → Task 3 (基本頁面)
  → Task 7 (整合測試)
  → Task 8 (文件)

後端線:
Task 4 (Express 設定)
  → Task 5 (中介層 + API)
  → Task 6 (錯誤處理)
  → Task 7 (整合測試)
  → Task 8 (文件)
```

**可平行執行**: Task 1-3 (前端) 與 Task 4-6 (後端) 可同時進行

---

## 團隊分工

| 角色 | 成員 | 主要負責 | 任務數 |
|------|------|---------|--------|
| **前端開發** | Waylon | Next.js, Tailwind, shadcn/ui | 4 |
| **後端開發** | Costa | Express, API, 文件 | 4 |
| **UI/UX 設計** | Lisa | shadcn/ui, 設計系統 | 1 |
| **後端審查** | Chris | 錯誤處理, 程式碼品質 | 1 |

---

## 驗收標準（Phase 1 完成）

### 前端驗收
- ✅ `cd frontend && npm run dev` 可啟動
- ✅ 可訪問 `/`, `/about`
- ✅ shadcn/ui 組件正常運作
- ✅ TypeScript 無錯誤
- ✅ ESLint 無錯誤

### 後端驗收
- ✅ `cd backend && npm run dev` 可啟動
- ✅ `/health` 端點正常運作
- ✅ `/api/hello` 端點正常運作
- ✅ TypeScript 無錯誤
- ✅ 錯誤處理正常

### 整合驗收
- ✅ 前端可呼叫後端 API
- ✅ CORS 設定正確
- ✅ README 完整清晰

### 文件驗收
- ✅ 根目錄 README 說明如何啟動
- ✅ `frontend/README.md` 完整
- ✅ `backend/README.md` 完整
- ✅ `.env.example` 完整

---

## 關鍵設計決策

### 為什麼選擇「前後端獨立」？

**優勢**:
1. ✅ **依賴隔離**: 前端升級 React 不影響後端
2. ✅ **避免連鎖故障**: 改動一個專案不會「一起掛」
3. ✅ **簡單易懂**: 新手不需要理解 Monorepo 概念
4. ✅ **部署靈活**: 可分別部署到不同平台
5. ✅ **團隊獨立**: 前後端團隊可完全獨立工作

**劣勢**:
1. ❌ 無法共享 TypeScript 型別（需手動同步）
2. ❌ 需要分別管理依賴版本

**結論**: 對於模板專案，獨立性 > 程式碼共享

---

**版本**: 3.0.0 (極簡版 - 方案 B)
**最後更新**: 2025-10-24
**狀態**: 待 CTO 審核與分配
