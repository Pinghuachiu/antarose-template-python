# Detailed Specification Document

**專案**: antarose-template-nodejs
**版本**: 1.0.0
**日期**: 2025-10-24
**CTO**: 最終審核與驗收
**Leo**: 架構設計與技術文件維護

---

## 1. 專案概述

### 1.1 專案目標

建立一個**通用的 Node.js 全棧專案模板**，提供：
- 完整的開發工具鏈
- 現代化技術棧
- 生產就緒的基礎架構
- 最佳實踐與規範

### 1.2 適用場景

- ✅ 電商平台
- ✅ SaaS 應用
- ✅ 內容管理系統 (CMS)
- ✅ 後台管理系統 (Admin Dashboard)
- ✅ API 服務
- ✅ 多頁應用 (MPA)
- ✅ 單頁應用 (SPA)

---

## 2. 技術規格

### 2.1 前端技術棧

#### Next.js 15 (App Router)

**版本**: 15.x
**選擇理由**: 支援所有渲染策略、生產就緒、官方支援

**配置要求**:
```javascript
// next.config.js
module.exports = {
  typescript: {
    strict: true,
  },
  images: {
    domains: ['example.com'],
    formats: ['image/avif', 'image/webp'],
  },
  experimental: {
    optimizePackageImports: ['lucide-react', '@heroicons/react'],
  },
}
```

**渲染策略規格**:
- CSR: `'use client'` 標記
- SSR: `export const dynamic = 'force-dynamic'`
- SSG: 預設行為
- ISR: `export const revalidate = 3600`

---

#### React 19

**版本**: 19.x
**選擇理由**: 最新穩定版、效能優化、Server Components

**使用規範**:
- 使用 Function Components
- 使用 TypeScript 型別定義
- 遵循 React Hooks 規則
- Server Components 優先於 Client Components

---

#### Tailwind CSS 4

**版本**: 4.x
**選擇理由**: 快速開發、設計一致性、bundle size 小

**配置規格**:
```typescript
// tailwind.config.ts
import type { Config } from 'tailwindcss'

const config: Config = {
  content: [
    './app/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        border: 'hsl(var(--border))',
        input: 'hsl(var(--input))',
        ring: 'hsl(var(--ring))',
        background: 'hsl(var(--background))',
        foreground: 'hsl(var(--foreground))',
        // ... shadcn/ui 顏色系統
      },
    },
  },
  plugins: [require('tailwindcss-animate')],
}

export default config
```

---

#### shadcn/ui

**版本**: Latest
**選擇理由**: 高品質組件、可自訂、與 Tailwind 完美整合

**必須安裝的組件**:
- Button
- Input
- Card
- Dialog
- Form
- Select
- Dropdown Menu
- Toast
- Tabs
- Avatar

**安裝規範**:
```bash
npx shadcn-ui@latest init
npx shadcn-ui@latest add button input card dialog form
```

---

#### Lucide React (圖示庫)

**版本**: Latest
**選擇理由**: shadcn/ui 預設、現代設計、Tree-shakable

**使用規範**:
```typescript
import { Search, User, Settings } from 'lucide-react'

// 標準尺寸
<Search className="h-4 w-4" />  // 小 (16px)
<User className="h-5 w-5" />    // 中 (20px)
<Settings className="h-6 w-6" /> // 大 (24px)

// 顏色使用 Tailwind classes
<Search className="h-5 w-5 text-gray-500" />
```

---

#### TanStack Query v5

**版本**: 5.x
**選擇理由**: Server state 管理、快取優化、DX 優秀

**配置規格**:
```typescript
// app/providers.tsx
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 60 * 1000, // 1 minute
      refetchOnWindowFocus: false,
      retry: 1,
    },
  },
})
```

**使用規範**:
- 所有 API 請求必須使用 TanStack Query
- Query Key 命名規範: `['resource', id, ...params]`
- 使用 `useMutation` 處理變更操作
- 實作 Optimistic Updates 提升 UX

---

#### Zustand

**版本**: Latest
**選擇理由**: 輕量、API 簡潔、TypeScript 支援好

**使用規範**:
```typescript
import { create } from 'zustand'
import { devtools, persist } from 'zustand/middleware'

interface Store {
  // state
  count: number
  // actions
  increment: () => void
}

export const useStore = create<Store>()(
  devtools(
    persist(
      (set) => ({
        count: 0,
        increment: () => set((state) => ({ count: state.count + 1 })),
      }),
      { name: 'store-name' }
    )
  )
)
```

---

### 2.2 後端技術棧

#### Node.js 20 LTS

**版本**: 20.x LTS
**選擇理由**: 長期支援、穩定、生態成熟

**最低版本要求**: 20.0.0

**package.json 配置**:
```json
{
  "engines": {
    "node": ">=20.0.0",
    "pnpm": ">=9.0.0"
  }
}
```

---

#### Express 4.x

**版本**: 4.x
**選擇理由**: 最流行的 Node.js 框架、靈活、社群豐富

**必須安裝的中介層**:
```json
{
  "dependencies": {
    "express": "^4.18.0",
    "helmet": "^7.1.0",
    "cors": "^2.8.5",
    "express-rate-limit": "^7.1.0",
    "compression": "^1.7.4",
    "morgan": "^1.10.0"
  }
}
```

**中介層順序規範**:
1. Helmet (security headers)
2. CORS
3. Compression
4. Body Parser
5. Morgan (logging)
6. Rate Limiter
7. Routes
8. Error Handler (最後)

---

#### PostgreSQL 16

**版本**: 16.x
**選擇理由**: 最成熟的開源 RDBMS、功能完整

**連線要求**:
- 使用 Connection Pooling
- SSL/TLS 加密連線
- 定期備份策略

**效能設定**:
```sql
-- Connection Pool
max_connections = 100

-- Memory
shared_buffers = 256MB
effective_cache_size = 1GB

-- WAL
wal_buffers = 16MB
checkpoint_completion_target = 0.9
```

---

#### Prisma ORM

**版本**: Latest
**選擇理由**: 型別安全、遷移管理、DX 優秀

**Schema 規範**:
```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

// Model 命名: PascalCase
model User {
  id String @id @default(cuid())
  // ... fields

  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  // 索引規範
  @@index([email])
  @@map("users") // 資料表使用 snake_case
}
```

**遷移規範**:
- 開發環境: `prisma migrate dev --name <descriptive-name>`
- 生產環境: `prisma migrate deploy`
- 永不使用: `prisma db push` (僅限原型開發)

---

#### NextAuth.js v5

**版本**: 5.x (Auth.js)
**選擇理由**: Next.js 深度整合、多策略支援

**支援的認證方式**:
- ✅ Email/Password (Credentials)
- ✅ GitHub OAuth
- ✅ Google OAuth
- ⏳ 可擴展: Twitter, Facebook, etc.

**Session 策略**:
- 預設: JWT (無狀態)
- 可選: Database Session (需 Redis/PostgreSQL)

**安全性要求**:
- NEXTAUTH_SECRET 至少 32 字元
- CSRF Protection (內建)
- Password 使用 bcryptjs (12 rounds)

---

#### Redis 7 (可選)

**版本**: 7.x
**選擇理由**: 快取、Session、背景任務佇列

**使用場景**:
1. Session 儲存 (NextAuth.js)
2. API 回應快取
3. Rate Limiting 計數
4. 背景任務佇列 (BullMQ)

**連線規範**:
```typescript
import { Redis } from 'ioredis'

const redis = new Redis({
  host: process.env.REDIS_HOST,
  port: Number(process.env.REDIS_PORT),
  password: process.env.REDIS_PASSWORD,
  retryStrategy: (times) => Math.min(times * 50, 2000),
})
```

---

### 2.3 開發工具鏈規格

#### pnpm

**版本**: 9.x
**選擇理由**: 快速、節省空間、嚴格依賴管理

**workspace 配置**:
```yaml
# pnpm-workspace.yaml
packages:
  - 'apps/*'
  - 'packages/*'
```

**必須配置**:
```ini
# .npmrc
auto-install-peers=true
strict-peer-dependencies=false
shamefully-hoist=false
```

---

#### Turborepo

**版本**: 2.x
**選擇理由**: 智慧快取、並行執行、增量建置

**pipeline 配置**:
```json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "dist/**"],
      "cache": true
    },
    "dev": {
      "cache": false,
      "persistent": true
    },
    "lint": {
      "cache": true
    },
    "test": {
      "cache": true
    }
  }
}
```

---

#### TypeScript 5.x

**版本**: 5.x
**選擇理由**: 型別安全、開發效率、減少 bug

**嚴格模式配置**:
```json
{
  "compilerOptions": {
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true
  }
}
```

---

#### Vitest

**版本**: Latest
**選擇理由**: 快速、現代、TypeScript 原生支援

**測試覆蓋率要求**:
- **單元測試**: ≥ 80%
- **整合測試**: ≥ 60%
- **分支覆蓋率**: ≥ 75%

**配置規範**:
```typescript
export default defineConfig({
  test: {
    environment: 'jsdom',
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html'],
      exclude: ['node_modules/', 'tests/', '**/*.config.ts'],
    },
  },
})
```

---

#### Playwright

**版本**: Latest
**選擇理由**: 跨瀏覽器、功能完整、穩定

**測試要求**:
- ✅ Chrome (必須)
- ✅ Firefox (必須)
- ✅ Safari/WebKit (建議)

**配置規範**:
```typescript
export default defineConfig({
  testDir: './tests/e2e',
  timeout: 30000,
  retries: process.env.CI ? 2 : 0,
  use: {
    baseURL: 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
})
```

---

## 3. 功能規格

### 3.1 認證系統規格

#### 使用者註冊

**端點**: `POST /api/auth/signup`

**請求格式**:
```typescript
{
  email: string      // 必須是有效的 email 格式
  password: string   // 最少 8 字元，最多 100 字元
  name?: string      // 可選，2-100 字元
}
```

**驗證規則**:
```typescript
const signupSchema = z.object({
  email: z.string().email('Invalid email address'),
  password: z
    .string()
    .min(8, 'Password must be at least 8 characters')
    .max(100, 'Password must be less than 100 characters'),
  name: z
    .string()
    .min(2, 'Name must be at least 2 characters')
    .max(100, 'Name must be less than 100 characters')
    .optional(),
})
```

**回應格式**:
```typescript
// 成功 (201 Created)
{
  success: true,
  data: {
    id: string
    email: string
    name: string | null
    role: 'USER'
  }
}

// 失敗 (400/409/500)
{
  success: false,
  error: {
    code: 'VALIDATION_ERROR' | 'EMAIL_ALREADY_EXISTS' | 'INTERNAL_SERVER_ERROR'
    message: string
    details?: any
  }
}
```

**安全性要求**:
- ✅ Password 使用 bcryptjs hash (12 rounds)
- ✅ Email 必須唯一 (資料庫 unique constraint)
- ✅ Rate limiting: 5 requests / 15 minutes per IP

---

#### 使用者登入

**端點**: NextAuth.js `/api/auth/callback/credentials`

**支援方式**:
1. Email/Password
2. GitHub OAuth
3. Google OAuth

**Session 策略**:
- JWT (預設)
- Max Age: 30 days
- Auto-refresh: 24 hours

**安全性要求**:
- ✅ CSRF Protection (NextAuth.js 內建)
- ✅ Rate limiting: 5 login attempts / 15 minutes per IP
- ✅ Failed login 不洩漏使用者是否存在

---

#### RBAC (Role-Based Access Control)

**角色定義**:
```typescript
enum UserRole {
  USER = 'USER',           // 一般使用者
  MODERATOR = 'MODERATOR', // 管理員
  ADMIN = 'ADMIN',         // 超級管理員
}
```

**權限矩陣**:

| 權限 | USER | MODERATOR | ADMIN |
|------|------|-----------|-------|
| user:read | ✅ | ✅ | ✅ |
| user:write (own) | ✅ | ✅ | ✅ |
| user:write (all) | ❌ | ❌ | ✅ |
| user:delete (own) | ✅ | ✅ | ✅ |
| user:delete (all) | ❌ | ❌ | ✅ |
| post:read | ✅ | ✅ | ✅ |
| post:write | ✅ | ✅ | ✅ |
| post:delete (own) | ✅ | ✅ | ✅ |
| post:delete (all) | ❌ | ✅ | ✅ |
| post:publish | ❌ | ✅ | ✅ |
| admin:access | ❌ | ❌ | ✅ |

**實作規範**:
```typescript
// Server-side check
import { requirePermission, Permission } from '@repo/utils/permissions'

async function deletePost(postId: string, userId: string, userRole: Role) {
  requirePermission(userRole, Permission.POST_DELETE)
  // ... delete logic
}

// Client-side check (UI only, not for security)
import { hasPermission } from '@repo/utils/permissions'

function DeleteButton({ userRole }: { userRole: Role }) {
  if (!hasPermission(userRole, Permission.POST_DELETE)) {
    return null
  }
  return <Button>Delete</Button>
}
```

---

### 3.2 API 規格

#### RESTful API 設計規範

**Base URL**: `/api/v1`

**資源命名規範**:
- 使用複數名詞: `/users`, `/posts`
- 使用 kebab-case: `/user-profiles`
- 巢狀資源: `/users/:userId/posts`

**HTTP 方法**:
- GET: 查詢資源
- POST: 建立資源
- PATCH: 部分更新資源
- PUT: 完整更新資源 (較少使用)
- DELETE: 刪除資源

**狀態碼規範**:
- 200 OK: 成功 (GET, PATCH, DELETE)
- 201 Created: 建立成功 (POST)
- 204 No Content: 刪除成功 (DELETE, 無回傳內容)
- 400 Bad Request: 請求格式錯誤、驗證失敗
- 401 Unauthorized: 未登入
- 403 Forbidden: 無權限
- 404 Not Found: 資源不存在
- 409 Conflict: 資源衝突 (例如 email 已存在)
- 429 Too Many Requests: 超過 rate limit
- 500 Internal Server Error: 伺服器錯誤

**統一回應格式**:
```typescript
// 成功回應
{
  success: true,
  data: T
}

// 錯誤回應
{
  success: false,
  error: {
    code: string       // 錯誤代碼 (大寫蛇形命名: VALIDATION_ERROR)
    message: string    // 錯誤訊息 (人類可讀)
    details?: any      // 詳細資訊 (例如驗證錯誤的欄位)
  }
}

// 分頁回應
{
  success: true,
  data: T[],
  meta: {
    total: number
    page: number
    perPage: number
    totalPages: number
  }
}
```

**分頁規範**:
- Query Parameters: `page`, `perPage` (或 `limit`)
- 預設值: `page=1`, `perPage=10`
- 最大值: `perPage` ≤ 100

**排序規範**:
- Query Parameter: `sortBy`, `sortOrder`
- 範例: `?sortBy=createdAt&sortOrder=desc`

**過濾規範**:
- Query Parameters: 根據資源欄位
- 範例: `?status=published&author=john`

---

#### tRPC 設計規範

**Router 結構**:
```typescript
export const appRouter = router({
  users: router({
    getById: publicProcedure.input(z.object({ id: z.string() })).query(...),
    update: protectedProcedure.input(...).mutation(...),
  }),
  posts: router({
    list: publicProcedure.input(...).query(...),
    create: protectedProcedure.input(...).mutation(...),
  }),
})
```

**命名規範**:
- Procedure 使用動詞: `getById`, `list`, `create`, `update`, `delete`
- Router 使用複數名詞: `users`, `posts`, `comments`

**型別安全要求**:
- 所有 input 必須使用 Zod schema
- 所有 output 必須有明確型別
- 禁止使用 `any` 型別

---

### 3.3 資料庫規格

#### Schema 設計規範

**命名規範**:
- Model: PascalCase (`User`, `Post`, `UserProfile`)
- Field: camelCase (`firstName`, `createdAt`, `isPublished`)
- Table: snake_case (`users`, `user_profiles`, `blog_posts`)
- Index: `{table}_{fields}_idx` (`users_email_idx`)

**必須欄位**:
```prisma
model BaseModel {
  id        String   @id @default(cuid())
  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt
}
```

**索引策略**:
- ✅ Primary Key: 自動索引
- ✅ Foreign Key: 建立索引
- ✅ Unique 欄位: 建立 unique index
- ✅ 常用查詢欄位: 建立索引
- ✅ 複合查詢: 建立 compound index

**範例**:
```prisma
model Post {
  id        String   @id @default(cuid())
  title     String
  published Boolean  @default(false)
  authorId  String
  createdAt DateTime @default(now())

  @@index([authorId])                      // Foreign key
  @@index([published, createdAt])          // Compound index
}
```

---

#### 資料遷移規範

**命名規範**:
```
<timestamp>_<descriptive_name>/migration.sql
```

範例:
```
20250124123456_add_user_role/migration.sql
20250124130000_create_posts_table/migration.sql
```

**遷移流程**:
1. 開發環境: `pnpm prisma migrate dev --name <name>`
2. 審查 SQL: 檢查 `prisma/migrations/` 中的 SQL
3. 測試: 在本地測試遷移
4. Code Review: PR 審查遷移 SQL
5. 生產環境: `pnpm prisma migrate deploy`

**禁止操作**:
- ❌ 直接修改已部署的遷移檔案
- ❌ 刪除已部署的遷移檔案
- ❌ 使用 `prisma db push` 在生產環境

---

## 4. 效能規格

### 4.1 前端效能指標

#### Core Web Vitals

**要求**:
- LCP (Largest Contentful Paint): < 2.5s
- FID (First Input Delay): < 100ms
- CLS (Cumulative Layout Shift): < 0.1

**測量工具**:
- Lighthouse (Chrome DevTools)
- Vercel Analytics
- PageSpeed Insights

**優化策略**:
- Image optimization (Next.js Image component)
- Font optimization (next/font)
- Code splitting (Dynamic import)
- Bundle size 控制 (< 200KB initial load)

---

#### 載入效能

**要求**:
- TTFB (Time to First Byte): < 600ms
- FCP (First Contentful Paint): < 1.8s
- TTI (Time to Interactive): < 3.8s

**優化策略**:
- CDN 快取 (Cloudflare / Vercel Edge)
- Compression (gzip / brotli)
- HTTP/2 & HTTP/3
- Preload critical resources

---

### 4.2 後端效能指標

#### API 效能

**要求**:
- Response Time (p50): < 100ms
- Response Time (p95): < 200ms
- Response Time (p99): < 500ms
- Throughput: > 1000 req/s

**測量工具**:
- Sentry Performance Monitoring
- Custom Prometheus metrics
- Load testing (Artillery, k6)

**優化策略**:
- Database query optimization
- Redis caching
- Connection pooling
- Horizontal scaling

---

#### 資料庫效能

**要求**:
- Query Time (avg): < 50ms
- Query Time (p95): < 100ms
- Connection Pool 使用率: < 80%
- Cache Hit Rate: > 80%

**優化策略**:
- Proper indexing
- Query optimization (avoid N+1)
- Prisma Query optimization
- Read replicas (if needed)

---

## 5. 安全性規格

### 5.1 認證與授權安全

**Password 安全性**:
- ✅ 最少 8 字元
- ✅ 使用 bcryptjs (12 rounds)
- ✅ 永不明文儲存
- ✅ 永不在日誌中記錄

**Session 安全性**:
- ✅ CSRF Protection (NextAuth.js 內建)
- ✅ Secure cookie (HTTPS only)
- ✅ HttpOnly cookie (防止 XSS)
- ✅ SameSite=Lax (防止 CSRF)

**JWT 安全性**:
- ✅ Secret 至少 32 字元
- ✅ 使用環境變數儲存 secret
- ✅ Token expiration (30 days max)
- ✅ Refresh token rotation

---

### 5.2 API 安全性

**Rate Limiting**:
```typescript
// 全域 Rate Limit
windowMs: 15 * 60 * 1000  // 15 minutes
max: 100                   // 100 requests

// 認證端點 Rate Limit
windowMs: 15 * 60 * 1000  // 15 minutes
max: 5                     // 5 attempts
```

**CORS 設定**:
```typescript
const corsOptions = {
  origin: process.env.NODE_ENV === 'production'
    ? ['https://yourdomain.com']
    : ['http://localhost:3000'],
  credentials: true,
  optionsSuccessStatus: 200,
}
```

**Security Headers (Helmet.js)**:
```typescript
helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", 'data:', 'https:'],
    },
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true,
  },
})
```

---

### 5.3 資料驗證

**所有輸入必須驗證**:
```typescript
// 使用 Zod schema
const userSchema = z.object({
  email: z.string().email(),
  password: z.string().min(8).max(100),
  name: z.string().min(2).max(100).optional(),
})

// 驗證中介層
app.post('/api/users', validate(userSchema), handler)
```

**SQL Injection 防護**:
- ✅ 使用 Prisma ORM (參數化查詢)
- ❌ 禁止 raw SQL (除非必要且經過審查)

**XSS 防護**:
- ✅ React 自動 escaping
- ✅ CSP headers
- ❌ 禁止 `dangerouslySetInnerHTML` (除非必要且經過 sanitize)

---

## 6. 監控與日誌規格

### 6.1 日誌規範

**日誌等級**:
- `error`: 錯誤 (需要立即處理)
- `warn`: 警告 (需要關注)
- `info`: 資訊 (一般事件)
- `debug`: 除錯 (開發環境)

**日誌格式** (JSON):
```json
{
  "level": "info",
  "time": "2025-10-24T12:00:00.000Z",
  "msg": "User logged in",
  "userId": "clu...",
  "ip": "1.2.3.4",
  "userAgent": "Mozilla/5.0..."
}
```

**禁止記錄**:
- ❌ 密碼
- ❌ API Keys
- ❌ Tokens
- ❌ 信用卡資訊
- ❌ 個人敏感資訊 (需遮罩)

---

### 6.2 錯誤追蹤

**Sentry 配置**:
```typescript
Sentry.init({
  dsn: process.env.SENTRY_DSN,
  environment: process.env.NODE_ENV,
  tracesSampleRate: 1.0,  // 100% for development, adjust for production
  replaysSessionSampleRate: 0.1,  // 10%
  replaysOnErrorSampleRate: 1.0,  // 100% on error
})
```

**必須追蹤**:
- ✅ 未捕獲的異常
- ✅ API 錯誤 (4xx, 5xx)
- ✅ Database 錯誤
- ✅ 第三方服務錯誤

---

## 7. 部署規格

### 7.1 環境變數

**必須變數**:
```env
# Application
NODE_ENV=production
PORT=4000

# Database
DATABASE_URL="postgresql://..."
DIRECT_URL="postgresql://..."

# NextAuth.js
NEXTAUTH_URL="https://yourdomain.com"
NEXTAUTH_SECRET="<32+ characters>"

# API
NEXT_PUBLIC_API_URL="https://api.yourdomain.com"

# Monitoring
SENTRY_DSN="https://..."
```

**安全性要求**:
- ✅ 永不提交 `.env` 到 Git
- ✅ 使用 `.env.example` 作為模板
- ✅ 生產環境使用平台環境變數
- ✅ Secret 定期輪換

---

### 7.2 部署流程

**Frontend (Vercel)**:
1. 連結 GitHub Repository
2. 配置 Build Command: `cd apps/web && pnpm build`
3. 配置 Output Directory: `apps/web/.next`
4. 設定環境變數
5. 推送程式碼 → 自動部署

**Backend (Railway)**:
1. 建立 Railway 專案
2. 建立 PostgreSQL 服務
3. 建立 API 服務 (Dockerfile)
4. 配置環境變數
5. 配置 Health Check: `/health`
6. 推送程式碼 → 自動部署

---

### 7.3 健康檢查

**Frontend**:
```typescript
// app/api/health/route.ts
export async function GET() {
  return Response.json({ status: 'ok' })
}
```

**Backend**:
```typescript
// apps/api/src/routes/health.ts
router.get('/health', (req, res) => {
  res.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
  })
})
```

**監控要求**:
- ✅ 每 30 秒檢查一次
- ✅ 3 次失敗視為 unhealthy
- ✅ 自動重啟 (Railway)

---

## 8. 測試規格

### 8.1 單元測試

**覆蓋率要求**:
- Statements: ≥ 80%
- Branches: ≥ 75%
- Functions: ≥ 80%
- Lines: ≥ 80%

**必須測試**:
- ✅ Utils functions
- ✅ Services
- ✅ Validation schemas
- ✅ Custom hooks (React)

**測試範例**:
```typescript
// packages/utils/__tests__/validators.test.ts
import { describe, it, expect } from 'vitest'
import { userSchema } from '../src/validators'

describe('userSchema', () => {
  it('should validate valid user data', () => {
    const validData = {
      email: 'test@example.com',
      password: 'password123',
      name: 'John Doe',
    }
    expect(() => userSchema.parse(validData)).not.toThrow()
  })

  it('should reject invalid email', () => {
    const invalidData = {
      email: 'invalid-email',
      password: 'password123',
    }
    expect(() => userSchema.parse(invalidData)).toThrow()
  })
})
```

---

### 8.2 E2E 測試

**必須測試場景**:
- ✅ 使用者註冊
- ✅ 使用者登入
- ✅ OAuth 登入 (GitHub, Google)
- ✅ Dashboard 訪問 (需登入)
- ✅ CRUD 操作
- ✅ 權限驗證

**測試範例**:
```typescript
// tests/e2e/auth.spec.ts
import { test, expect } from '@playwright/test'

test('user can sign in', async ({ page }) => {
  await page.goto('/auth/signin')
  await page.fill('input[name="email"]', 'test@example.com')
  await page.fill('input[name="password"]', 'password123')
  await page.click('button[type="submit"]')
  await expect(page).toHaveURL('/dashboard')
})
```

---

## 9. 文件規格

### 9.1 必須文件

**技術文件** (`docs/architecture/`):
- ✅ `system-design.md` - 系統架構設計
- ✅ `tech-stack.md` - 技術棧文件
- ✅ `rendering-strategies.md` - 渲染策略指南
- ✅ `api-design.md` - API 設計規範
- ✅ `adr/` - Architecture Decision Records

**API 文件** (`docs/api/`):
- ✅ `rest-api.md` - RESTful API 文件
- ✅ `trpc.md` - tRPC API 文件
- ✅ Swagger UI - `/api-docs`

**開發指南** (`docs/guides/`):
- ✅ `getting-started.md` - 快速開始
- ✅ `development-workflow.md` - 開發流程
- ✅ `deployment-guide.md` - 部署指南
- ✅ `testing-guide.md` - 測試指南
- ✅ `icon-usage.md` - 圖示使用規範

---

### 9.2 Leo 的強制責任

**每次新專案或迭代完成且 CTO 驗收通過後，Leo 必須**:

1. ✅ **更新 `docs/architecture/system-design.md`**
   - 更新系統架構圖
   - 記錄新增的組件
   - 更新資料流設計

2. ✅ **更新 `docs/architecture/tech-stack.md`**
   - 記錄技術棧變更
   - 更新版本號
   - 記錄棄用的技術

3. ✅ **更新 ADR (Architecture Decision Records)**
   - 建立新的 ADR (如有重大決策)
   - 格式: `docs/architecture/adr/###-<title>.md`
   - 內容包括: Context, Decision, Consequences

4. ✅ **更新架構圖**
   - 確保所有圖表反映目前實作
   - 更新組件關係圖
   - 更新資料流圖

5. ✅ **記錄技術債務**
   - 識別技術債務
   - 記錄在 `docs/architecture/tech-debt.md`
   - 提出償還計畫

**時程要求**:
- ⏰ 必須在 CTO 驗收後 **2 個工作天內** 完成
- ⏰ 更新完成後通知 CTO 審查

---

## 10. 驗收標準

### 10.1 Phase 1 (MVP) 驗收標準

**功能性**:
- ✅ 使用者可註冊、登入、登出
- ✅ RBAC 權限正常運作
- ✅ API CRUD 端點正常運作
- ✅ Next.js 渲染策略正常 (CSR/SSR/SSG/ISR)
- ✅ 前後端可正常通訊

**非功能性**:
- ✅ TypeScript 無型別錯誤
- ✅ ESLint 無錯誤
- ✅ 單元測試覆蓋率 ≥ 80%
- ✅ 所有 API 端點有錯誤處理
- ✅ 日誌系統運作正常

**文件**:
- ✅ README.md 完整
- ✅ 環境變數文件 (.env.example)
- ✅ API 文件完成

---

### 10.2 Phase 2 (擴展) 驗收標準

**功能性**:
- ✅ OAuth 登入 (GitHub, Google) 正常運作
- ✅ Redis 快取正常運作
- ✅ tRPC 端到端型別安全
- ✅ E2E 測試涵蓋核心流程

**非功能性**:
- ✅ Sentry 錯誤追蹤運作
- ✅ Pino 日誌結構化
- ✅ E2E 測試通過率 100%

---

### 10.3 Phase 3 (優化) 驗收標準

**效能**:
- ✅ Core Web Vitals 達標
- ✅ API Response Time p95 < 200ms
- ✅ Bundle size 優化完成

**安全性**:
- ✅ Rate limiting 運作
- ✅ Security headers 正確設定
- ✅ 環境變數驗證通過

**部署**:
- ✅ Frontend 自動部署至 Vercel
- ✅ Backend 自動部署至 Railway
- ✅ 生產環境正常運作

**文件**:
- ✅ 所有技術文件完成
- ✅ Leo 已更新架構文件
- ✅ 開發指南完整

---

**版本**: 1.0.0
**最後更新**: 2025-10-24
**審核狀態**: 待審核
**CTO 簽核**: [ ]
**Leo 確認**: [ ]
