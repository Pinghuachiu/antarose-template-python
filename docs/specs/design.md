# Technical Design Document

**專案**: antarose-template-nodejs
**版本**: 1.0.0
**日期**: 2025-10-24
**作者**: CTO, Leo (System Architect)

---

## 1. 設計概覽

### 1.1 設計原則

1. **Progressive Enhancement**: 從簡單開始，根據需求逐步增強
2. **Type Safety First**: TypeScript 覆蓋率 100%
3. **Separation of Concerns**: 前後端職責清晰分離
4. **Developer Experience**: 優先考慮開發效率與工具鏈整合
5. **Production Ready**: 內建監控、日誌、錯誤處理機制

### 1.2 架構圖層

```
┌─────────────────────────────────────────────────┐
│          Presentation Layer (客戶端)            │
│  Next.js 15 (App Router) + React 19            │
│  Tailwind CSS + shadcn/ui + Lucide React       │
└────────────┬────────────────────────────────────┘
             │
             │ HTTPS/tRPC/REST
             ▼
┌─────────────────────────────────────────────────┐
│         Application Layer (應用層)              │
│  Next.js API Routes + Express Server           │
│  NextAuth.js + tRPC + RESTful API              │
└────────────┬────────────────────────────────────┘
             │
             │ Prisma ORM
             ▼
┌─────────────────────────────────────────────────┐
│          Data Layer (資料層)                    │
│  PostgreSQL + Redis + File Storage             │
└─────────────────────────────────────────────────┘
```

---

## 2. 前端設計

### 2.1 Next.js App Router 架構

#### 路由設計

```
app/
├── (auth)/                    # 認證相關頁面
│   ├── signin/page.tsx       # 登入頁面 (SSG)
│   ├── signup/page.tsx       # 註冊頁面 (SSG)
│   ├── forgot-password/page.tsx
│   └── layout.tsx            # 認證 layout (簡化版)
│
├── (dashboard)/              # Dashboard 頁面
│   ├── dashboard/
│   │   ├── page.tsx         # 主 Dashboard (CSR)
│   │   └── loading.tsx
│   ├── settings/page.tsx    # 設定頁面 (CSR)
│   ├── profile/page.tsx     # 個人資料 (SSR)
│   └── layout.tsx           # Dashboard layout (側邊欄 + 導航)
│
├── (marketing)/              # 行銷頁面
│   ├── page.tsx             # 首頁 (SSG)
│   ├── about/page.tsx       # 關於頁面 (SSG)
│   ├── pricing/page.tsx     # 定價頁面 (SSG)
│   ├── blog/
│   │   ├── page.tsx         # 部落格列表 (ISR)
│   │   └── [slug]/page.tsx  # 部落格文章 (ISR)
│   └── layout.tsx           # Marketing layout (導航欄 + 頁尾)
│
├── api/                      # API Routes
│   ├── auth/[...nextauth]/route.ts  # NextAuth.js
│   ├── trpc/[trpc]/route.ts         # tRPC
│   └── webhooks/
│       └── stripe/route.ts          # Stripe webhook
│
├── layout.tsx                # Root layout
├── error.tsx                 # Global error boundary
├── not-found.tsx             # 404 page
└── loading.tsx               # Global loading
```

#### 渲染策略選擇指南

```typescript
// CSR - Client-Side Rendering
// 使用場景: Dashboard, 互動密集頁面
'use client'

export default function DashboardPage() {
  const [data, setData] = useState(null)
  useEffect(() => { fetchData() }, [])
  return <div>Dashboard</div>
}

// SSR - Server-Side Rendering
// 使用場景: 使用者個人頁面, 需要即時資料且需 SEO
export const dynamic = 'force-dynamic'

export default async function ProfilePage({ params }) {
  const user = await getUser(params.id)
  return <div>{user.name}</div>
}

// SSG - Static Site Generation
// 使用場景: 行銷頁面, 文件, 不常變動的內容
export default function AboutPage() {
  return <div>About Us</div>
}

// ISR - Incremental Static Regeneration
// 使用場景: 部落格, 產品目錄, 定期更新的內容
export const revalidate = 3600 // 每小時重新生成

export default async function BlogPost({ params }) {
  const post = await getPost(params.slug)
  return <article>{post.content}</article>
}
```

### 2.2 狀態管理架構

```typescript
// packages/types/src/state.ts
// 狀態管理分層設計

// Layer 1: Server State (TanStack Query)
// 管理所有來自後端的資料
import { useQuery, useMutation } from '@tanstack/react-query'

export function useUser(userId: string) {
  return useQuery({
    queryKey: ['user', userId],
    queryFn: () => api.users.getById(userId),
    staleTime: 5 * 60 * 1000,
  })
}

// Layer 2: Client State (Zustand)
// 管理 UI 狀態、使用者互動狀態
import { create } from 'zustand'

interface UIStore {
  sidebarOpen: boolean
  theme: 'light' | 'dark' | 'system'
  toggleSidebar: () => void
  setTheme: (theme: 'light' | 'dark' | 'system') => void
}

export const useUIStore = create<UIStore>((set) => ({
  sidebarOpen: true,
  theme: 'system',
  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
  setTheme: (theme) => set({ theme }),
}))

// Layer 3: Form State (React Hook Form + Zod)
// 管理表單狀態與驗證
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
})

export function LoginForm() {
  const form = useForm({
    resolver: zodResolver(schema),
  })
  return <form onSubmit={form.handleSubmit(onSubmit)}>...</form>
}
```

### 2.3 UI 組件架構

```
components/
├── ui/                       # shadcn/ui 基礎組件
│   ├── button.tsx
│   ├── input.tsx
│   ├── dialog.tsx
│   └── ...
│
├── forms/                    # 表單組件
│   ├── signin-form.tsx
│   ├── signup-form.tsx
│   └── user-profile-form.tsx
│
├── layout/                   # 布局組件
│   ├── header.tsx
│   ├── footer.tsx
│   ├── sidebar.tsx
│   └── navigation.tsx
│
├── shared/                   # 共享組件
│   ├── user-avatar.tsx
│   ├── loading-spinner.tsx
│   ├── error-message.tsx
│   └── empty-state.tsx
│
└── features/                 # 功能組件
    ├── auth/
    │   ├── oauth-buttons.tsx
    │   └── password-reset.tsx
    └── dashboard/
        ├── stats-card.tsx
        └── activity-feed.tsx
```

---

## 3. 後端設計

### 3.1 Express Server 架構

```
apps/api/src/
├── controllers/              # 請求處理器
│   ├── auth.controller.ts
│   ├── user.controller.ts
│   └── post.controller.ts
│
├── services/                 # 業務邏輯層
│   ├── auth.service.ts
│   ├── user.service.ts
│   └── post.service.ts
│
├── repositories/             # 資料存取層 (可選)
│   ├── user.repository.ts
│   └── post.repository.ts
│
├── middlewares/              # Express 中介層
│   ├── auth.ts              # 認證檢查
│   ├── validate.ts          # Zod 驗證
│   ├── rate-limit.ts        # Rate limiting
│   ├── error-handler.ts     # 錯誤處理
│   └── logger.ts            # HTTP 日誌
│
├── routes/                   # API 路由
│   ├── v1/
│   │   ├── auth.routes.ts
│   │   ├── users.routes.ts
│   │   ├── posts.routes.ts
│   │   └── index.ts
│   └── index.ts
│
├── utils/                    # 工具函式
│   ├── logger.ts
│   └── encryption.ts
│
├── config/                   # 配置
│   ├── database.ts
│   ├── redis.ts
│   └── env.ts
│
└── index.ts                  # 入口點
```

### 3.2 API 設計模式

#### RESTful API 設計

```typescript
// apps/api/src/routes/v1/users.ts
import { Router } from 'express'
import { UserController } from '@/controllers/user.controller'
import { authenticate } from '@/middlewares/auth'
import { validate } from '@/middlewares/validate'
import { userSchemas } from '@repo/utils/validators'

const router = Router()

// GET /api/v1/users/:id
router.get(
  '/users/:id',
  validate(userSchemas.getUser),
  UserController.getById
)

// PATCH /api/v1/users/:id
router.patch(
  '/users/:id',
  authenticate,
  validate(userSchemas.updateUser),
  UserController.update
)

// DELETE /api/v1/users/:id
router.delete(
  '/users/:id',
  authenticate,
  UserController.delete
)

export default router
```

#### Controller Pattern

```typescript
// apps/api/src/controllers/user.controller.ts
import { Request, Response, NextFunction } from 'express'
import { UserService } from '@/services/user.service'
import { ApiResponse } from '@repo/types'

export class UserController {
  static async getById(req: Request, res: Response, next: NextFunction) {
    try {
      const user = await UserService.findById(req.params.id)

      if (!user) {
        return res.status(404).json({
          success: false,
          error: {
            code: 'USER_NOT_FOUND',
            message: 'User not found',
          },
        } as ApiResponse)
      }

      return res.status(200).json({
        success: true,
        data: user,
      } as ApiResponse)
    } catch (error) {
      next(error)
    }
  }
}
```

#### Service Pattern

```typescript
// apps/api/src/services/user.service.ts
import { prisma } from '@repo/database'
import { Prisma } from '@prisma/client'
import { hashPassword } from '@repo/utils/encryption'

export class UserService {
  static async findById(id: string) {
    return prisma.user.findUnique({
      where: { id },
      select: {
        id: true,
        email: true,
        name: true,
        image: true,
        role: true,
        createdAt: true,
        // Exclude passwordHash
      },
    })
  }

  static async create(data: Prisma.UserCreateInput) {
    if (data.passwordHash) {
      data.passwordHash = await hashPassword(data.passwordHash)
    }

    return prisma.user.create({
      data,
      select: {
        id: true,
        email: true,
        name: true,
      },
    })
  }

  static async update(id: string, data: Prisma.UserUpdateInput) {
    if (data.passwordHash) {
      data.passwordHash = await hashPassword(data.passwordHash as string)
    }

    return prisma.user.update({
      where: { id },
      data,
    })
  }
}
```

### 3.3 tRPC 設計

```typescript
// apps/web/server/trpc/router.ts
import { z } from 'zod'
import { publicProcedure, protectedProcedure, router } from './trpc'
import { prisma } from '@repo/database'

export const appRouter = router({
  // Public procedures
  users: router({
    getById: publicProcedure
      .input(z.object({ id: z.string() }))
      .query(async ({ input }) => {
        return prisma.user.findUnique({
          where: { id: input.id },
        })
      }),
  }),

  // Protected procedures
  profile: router({
    update: protectedProcedure
      .input(z.object({
        name: z.string().min(2).optional(),
        bio: z.string().max(500).optional(),
      }))
      .mutation(async ({ ctx, input }) => {
        return prisma.user.update({
          where: { id: ctx.session.user.id },
          data: input,
        })
      }),
  }),

  // Nested routers
  posts: router({
    list: publicProcedure
      .input(z.object({
        limit: z.number().min(1).max(100).default(10),
        cursor: z.string().optional(),
      }))
      .query(async ({ input }) => {
        const posts = await prisma.post.findMany({
          take: input.limit + 1,
          cursor: input.cursor ? { id: input.cursor } : undefined,
          orderBy: { createdAt: 'desc' },
        })

        let nextCursor: string | undefined
        if (posts.length > input.limit) {
          const nextItem = posts.pop()
          nextCursor = nextItem!.id
        }

        return { posts, nextCursor }
      }),
  }),
})

export type AppRouter = typeof appRouter
```

---

## 4. 資料庫設計

### 4.1 Prisma Schema

```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

// ===== Auth Models =====

model User {
  id            String    @id @default(cuid())
  email         String    @unique
  name          String?
  passwordHash  String?
  emailVerified DateTime?
  image         String?
  role          UserRole  @default(USER)

  accounts      Account[]
  sessions      Session[]
  posts         Post[]

  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  @@index([email])
  @@map("users")
}

model Account {
  id                String  @id @default(cuid())
  userId            String
  type              String
  provider          String
  providerAccountId String
  refresh_token     String?
  access_token      String?
  expires_at        Int?
  token_type        String?
  scope             String?
  id_token          String?
  session_state     String?

  user User @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@unique([provider, providerAccountId])
  @@index([userId])
  @@map("accounts")
}

model Session {
  id           String   @id @default(cuid())
  sessionToken String   @unique
  userId       String
  expires      DateTime

  user User @relation(fields: [userId], references: [id], onDelete: Cascade)

  @@index([userId])
  @@map("sessions")
}

// ===== Application Models =====

model Post {
  id        String   @id @default(cuid())
  title     String
  slug      String   @unique
  content   String?
  excerpt   String?
  published Boolean  @default(false)
  authorId  String

  author    User     @relation(fields: [authorId], references: [id], onDelete: Cascade)

  createdAt DateTime @default(now())
  updatedAt DateTime @updatedAt

  @@index([authorId])
  @@index([published, createdAt])
  @@map("posts")
}

// ===== Enums =====

enum UserRole {
  USER
  MODERATOR
  ADMIN
}
```

### 4.2 索引策略

```prisma
// 效能優化索引

// 1. 唯一索引 (Unique Index)
model User {
  email String @unique  // 快速登入查詢
}

// 2. 複合索引 (Compound Index)
model Post {
  @@index([published, createdAt])  // 查詢已發布文章並按時間排序
}

// 3. 外鍵索引 (Foreign Key Index)
model Post {
  @@index([authorId])  // 快速查詢使用者的所有文章
}

// 4. 全文搜尋索引 (PostgreSQL)
// 在 migration 中手動添加
-- CREATE INDEX posts_title_search_idx ON posts USING GIN (to_tsvector('english', title));
```

### 4.3 遷移策略

```bash
# 開發環境
pnpm prisma migrate dev --name add_user_role

# 生產環境
pnpm prisma migrate deploy

# 重設資料庫 (開發環境)
pnpm prisma migrate reset

# 生成 Prisma Client
pnpm prisma generate
```

---

## 5. 認證授權設計

### 5.1 NextAuth.js 配置

```typescript
// apps/web/auth.config.ts
import { NextAuthConfig } from 'next-auth'
import GitHub from 'next-auth/providers/github'
import Google from 'next-auth/providers/google'
import Credentials from 'next-auth/providers/credentials'
import { PrismaAdapter } from '@auth/prisma-adapter'
import { prisma } from '@repo/database'
import { verifyPassword } from '@repo/utils/encryption'

export const authConfig: NextAuthConfig = {
  adapter: PrismaAdapter(prisma),

  providers: [
    GitHub({
      clientId: process.env.GITHUB_ID!,
      clientSecret: process.env.GITHUB_SECRET!,
    }),

    Google({
      clientId: process.env.GOOGLE_ID!,
      clientSecret: process.env.GOOGLE_SECRET!,
    }),

    Credentials({
      async authorize(credentials) {
        const user = await prisma.user.findUnique({
          where: { email: credentials.email as string },
        })

        if (!user || !user.passwordHash) return null

        const isValid = await verifyPassword(
          credentials.password as string,
          user.passwordHash
        )

        if (!isValid) return null

        return {
          id: user.id,
          email: user.email,
          name: user.name,
          role: user.role,
        }
      },
    }),
  ],

  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.id = user.id
        token.role = user.role
      }
      return token
    },

    async session({ session, token }) {
      if (session.user) {
        session.user.id = token.id as string
        session.user.role = token.role as string
      }
      return session
    },
  },

  pages: {
    signIn: '/auth/signin',
    signOut: '/auth/signout',
    error: '/auth/error',
  },

  session: {
    strategy: 'jwt',
    maxAge: 30 * 24 * 60 * 60, // 30 days
  },
}
```

### 5.2 RBAC 實作

```typescript
// packages/utils/src/permissions.ts
export enum Permission {
  USER_READ = 'user:read',
  USER_WRITE = 'user:write',
  USER_DELETE = 'user:delete',
  POST_READ = 'post:read',
  POST_WRITE = 'post:write',
  POST_DELETE = 'post:delete',
  POST_PUBLISH = 'post:publish',
  ADMIN_ACCESS = 'admin:access',
}

export enum Role {
  USER = 'USER',
  MODERATOR = 'MODERATOR',
  ADMIN = 'ADMIN',
}

export const rolePermissions: Record<Role, Permission[]> = {
  [Role.USER]: [
    Permission.USER_READ,
    Permission.POST_READ,
    Permission.POST_WRITE,
  ],
  [Role.MODERATOR]: [
    Permission.USER_READ,
    Permission.POST_READ,
    Permission.POST_WRITE,
    Permission.POST_DELETE,
    Permission.POST_PUBLISH,
  ],
  [Role.ADMIN]: Object.values(Permission),
}

export function hasPermission(role: Role, permission: Permission): boolean {
  return rolePermissions[role].includes(permission)
}

export function requirePermission(role: Role, permission: Permission): void {
  if (!hasPermission(role, permission)) {
    throw new Error(`Permission denied: ${permission}`)
  }
}
```

### 5.3 路由保護

```typescript
// apps/web/middleware.ts
import { auth } from '@/auth'
import { NextResponse } from 'next/server'

export default auth((req) => {
  const { nextUrl } = req
  const isLoggedIn = !!req.auth

  const isAuthRoute = nextUrl.pathname.startsWith('/auth')
  const isProtectedRoute = nextUrl.pathname.startsWith('/dashboard')
  const isAdminRoute = nextUrl.pathname.startsWith('/admin')

  if (isAuthRoute && isLoggedIn) {
    return NextResponse.redirect(new URL('/dashboard', nextUrl))
  }

  if (isProtectedRoute && !isLoggedIn) {
    return NextResponse.redirect(new URL('/auth/signin', nextUrl))
  }

  if (isAdminRoute) {
    if (!isLoggedIn) {
      return NextResponse.redirect(new URL('/auth/signin', nextUrl))
    }
    if (req.auth?.user?.role !== 'ADMIN') {
      return NextResponse.redirect(new URL('/dashboard', nextUrl))
    }
  }

  return NextResponse.next()
})

export const config = {
  matcher: ['/((?!api|_next/static|_next/image|favicon.ico).*)'],
}
```

---

## 6. 快取策略

### 6.1 多層快取架構

```
Client (Browser Cache)
    ↓
CDN (Cloudflare/Vercel Edge)
    ↓
Application Cache (Redis)
    ↓
Database (PostgreSQL)
```

### 6.2 Redis 快取實作

```typescript
// packages/utils/src/cache.ts
import { Redis } from 'ioredis'

const redis = new Redis(process.env.REDIS_URL || 'redis://localhost:6379')

export const cache = {
  async get<T>(key: string): Promise<T | null> {
    const data = await redis.get(key)
    return data ? JSON.parse(data) : null
  },

  async set(key: string, value: any, ttl?: number): Promise<void> {
    const serialized = JSON.stringify(value)
    if (ttl) {
      await redis.setex(key, ttl, serialized)
    } else {
      await redis.set(key, serialized)
    }
  },

  async del(key: string): Promise<void> {
    await redis.del(key)
  },

  async invalidatePattern(pattern: string): Promise<void> {
    const keys = await redis.keys(pattern)
    if (keys.length > 0) {
      await redis.del(...keys)
    }
  },
}

// 使用範例
export async function getUserWithCache(userId: string) {
  const cacheKey = `user:${userId}`

  // Try cache first
  const cached = await cache.get(cacheKey)
  if (cached) return cached

  // Fetch from database
  const user = await prisma.user.findUnique({ where: { id: userId } })

  // Store in cache (5 minutes)
  if (user) {
    await cache.set(cacheKey, user, 300)
  }

  return user
}
```

---

## 7. 錯誤處理設計

### 7.1 錯誤類型定義

```typescript
// packages/types/src/errors.ts
export class AppError extends Error {
  constructor(
    public code: string,
    public message: string,
    public statusCode: number = 500,
    public details?: any
  ) {
    super(message)
    this.name = 'AppError'
  }
}

export class ValidationError extends AppError {
  constructor(message: string, details?: any) {
    super('VALIDATION_ERROR', message, 400, details)
    this.name = 'ValidationError'
  }
}

export class AuthenticationError extends AppError {
  constructor(message: string = 'Authentication required') {
    super('AUTHENTICATION_ERROR', message, 401)
    this.name = 'AuthenticationError'
  }
}

export class AuthorizationError extends AppError {
  constructor(message: string = 'Permission denied') {
    super('AUTHORIZATION_ERROR', message, 403)
    this.name = 'AuthorizationError'
  }
}

export class NotFoundError extends AppError {
  constructor(resource: string) {
    super('NOT_FOUND', `${resource} not found`, 404)
    this.name = 'NotFoundError'
  }
}
```

### 7.2 統一錯誤處理

```typescript
// apps/api/src/middlewares/error-handler.ts
import { Request, Response, NextFunction } from 'express'
import { Prisma } from '@prisma/client'
import { ZodError } from 'zod'
import { AppError } from '@repo/types/errors'
import { logger } from '@repo/utils/logger'

export function errorHandler(
  error: Error,
  req: Request,
  res: Response,
  next: NextFunction
) {
  logger.error({ err: error, req }, 'Error occurred')

  // AppError (custom errors)
  if (error instanceof AppError) {
    return res.status(error.statusCode).json({
      success: false,
      error: {
        code: error.code,
        message: error.message,
        details: error.details,
      },
    })
  }

  // Zod validation error
  if (error instanceof ZodError) {
    return res.status(400).json({
      success: false,
      error: {
        code: 'VALIDATION_ERROR',
        message: 'Invalid request data',
        details: error.errors,
      },
    })
  }

  // Prisma errors
  if (error instanceof Prisma.PrismaClientKnownRequestError) {
    if (error.code === 'P2002') {
      return res.status(409).json({
        success: false,
        error: {
          code: 'UNIQUE_CONSTRAINT_VIOLATION',
          message: 'Resource already exists',
        },
      })
    }

    if (error.code === 'P2025') {
      return res.status(404).json({
        success: false,
        error: {
          code: 'NOT_FOUND',
          message: 'Resource not found',
        },
      })
    }
  }

  // Default error
  return res.status(500).json({
    success: false,
    error: {
      code: 'INTERNAL_SERVER_ERROR',
      message: process.env.NODE_ENV === 'production'
        ? 'An unexpected error occurred'
        : error.message,
    },
  })
}
```

---

## 8. 監控與日誌設計

### 8.1 日誌架構

```typescript
// packages/utils/src/logger.ts
import pino from 'pino'

export const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  transport: process.env.NODE_ENV === 'development'
    ? {
        target: 'pino-pretty',
        options: { colorize: true },
      }
    : undefined,
  base: {
    env: process.env.NODE_ENV,
  },
  timestamp: pino.stdTimeFunctions.isoTime,
})

// 使用範例
logger.info({ userId: '123' }, 'User logged in')
logger.error({ err: error }, 'Failed to fetch user')
logger.warn({ latency: 1000 }, 'Slow query detected')
logger.debug({ query: 'SELECT ...' }, 'Database query')
```

### 8.2 監控指標

```typescript
// packages/utils/src/metrics.ts
import client from 'prom-client'

// 建立 Registry
const register = new client.Registry()

// HTTP 請求計數器
export const httpRequestCounter = new client.Counter({
  name: 'http_requests_total',
  help: 'Total number of HTTP requests',
  labelNames: ['method', 'route', 'status_code'],
  registers: [register],
})

// HTTP 請求持續時間
export const httpRequestDuration = new client.Histogram({
  name: 'http_request_duration_seconds',
  help: 'HTTP request duration in seconds',
  labelNames: ['method', 'route', 'status_code'],
  registers: [register],
})

// 資料庫查詢持續時間
export const dbQueryDuration = new client.Histogram({
  name: 'db_query_duration_seconds',
  help: 'Database query duration in seconds',
  labelNames: ['operation', 'model'],
  registers: [register],
})

export { register }
```

---

## 9. 安全性設計

### 9.1 API 安全層

```typescript
// apps/api/src/index.ts
import express from 'express'
import helmet from 'helmet'
import cors from 'cors'
import rateLimit from 'express-rate-limit'

const app = express()

// 1. Helmet (Security headers)
app.use(helmet({
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
  },
}))

// 2. CORS
const corsOptions = {
  origin: process.env.NODE_ENV === 'production'
    ? ['https://yourdomain.com']
    : ['http://localhost:3000'],
  credentials: true,
}
app.use(cors(corsOptions))

// 3. Rate Limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // Max 100 requests per windowMs
  message: 'Too many requests',
})
app.use('/api', limiter)

// 4. Body Parser (with size limits)
app.use(express.json({ limit: '10mb' }))
app.use(express.urlencoded({ extended: true, limit: '10mb' }))
```

### 9.2 資料驗證

```typescript
// packages/utils/src/validators.ts
import { z } from 'zod'

// User validation schemas
export const userSchemas = {
  create: z.object({
    email: z.string().email(),
    password: z.string().min(8).max(100),
    name: z.string().min(2).max(100).optional(),
  }),

  update: z.object({
    name: z.string().min(2).max(100).optional(),
    email: z.string().email().optional(),
    bio: z.string().max(500).optional(),
  }),

  getUser: z.object({
    params: z.object({
      id: z.string().cuid(),
    }),
  }),
}

// Post validation schemas
export const postSchemas = {
  create: z.object({
    title: z.string().min(1).max(200),
    content: z.string(),
    published: z.boolean().default(false),
  }),

  update: z.object({
    title: z.string().min(1).max(200).optional(),
    content: z.string().optional(),
    published: z.boolean().optional(),
  }),
}
```

---

## 10. 部署設計

### 10.1 Docker 配置

```dockerfile
# apps/api/Dockerfile
FROM node:20-alpine AS base
RUN corepack enable && corepack prepare pnpm@9.6.0 --activate

WORKDIR /app
COPY pnpm-workspace.yaml package.json pnpm-lock.yaml ./
COPY packages ./packages
COPY apps/api ./apps/api
COPY prisma ./prisma

RUN pnpm install --frozen-lockfile
RUN pnpm --filter @repo/api build

FROM node:20-alpine AS production
RUN corepack enable && corepack prepare pnpm@9.6.0 --activate

WORKDIR /app
COPY --from=base /app/node_modules ./node_modules
COPY --from=base /app/packages ./packages
COPY --from=base /app/apps/api/dist ./dist
COPY --from=base /app/prisma ./prisma
COPY --from=base /app/package.json ./

EXPOSE 4000
CMD ["sh", "-c", "pnpm prisma migrate deploy && node dist/index.js"]
```

### 10.2 環境變數管理

```env
# .env.example

# Application
NODE_ENV=development
PORT=4000

# Database
DATABASE_URL="postgresql://username:password@localhost:5432/database"
DIRECT_URL="postgresql://username:password@localhost:5432/database"

# Redis (optional)
REDIS_URL="redis://localhost:6379"

# NextAuth.js
NEXTAUTH_URL="http://localhost:3000"
NEXTAUTH_SECRET="your-secret-key-minimum-32-characters"

# OAuth Providers
GITHUB_ID="your-github-client-id"
GITHUB_SECRET="your-github-client-secret"
GOOGLE_ID="your-google-client-id"
GOOGLE_SECRET="your-google-client-secret"

# API
NEXT_PUBLIC_API_URL="http://localhost:4000"

# Monitoring
SENTRY_DSN="your-sentry-dsn"

# File Storage (optional)
AWS_ACCESS_KEY_ID="your-access-key"
AWS_SECRET_ACCESS_KEY="your-secret-key"
AWS_REGION="us-east-1"
AWS_BUCKET_NAME="your-bucket-name"
```

---

## 11. 效能優化設計

### 11.1 Next.js 優化

```typescript
// apps/web/next.config.js
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
})

module.exports = withBundleAnalyzer({
  // Image optimization
  images: {
    domains: ['example.com'],
    formats: ['image/avif', 'image/webp'],
  },

  // Font optimization
  optimizeFonts: true,

  // Package imports optimization
  experimental: {
    optimizePackageImports: ['lucide-react', '@heroicons/react'],
  },

  // Remove console in production
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production',
  },

  // Webpack optimization
  webpack: (config, { isServer }) => {
    if (!isServer) {
      config.resolve.fallback = {
        fs: false,
        net: false,
        tls: false,
      }
    }
    return config
  },
})
```

### 11.2 資料庫查詢優化

```typescript
// 避免 N+1 查詢問題
// ❌ Bad - N+1 query
const users = await prisma.user.findMany()
for (const user of users) {
  const posts = await prisma.post.findMany({ where: { authorId: user.id } })
}

// ✅ Good - Single query with include
const users = await prisma.user.findMany({
  include: {
    posts: true,
  },
})

// 使用 select 減少資料傳輸
const users = await prisma.user.findMany({
  select: {
    id: true,
    name: true,
    email: true,
    // 不載入不需要的欄位
  },
})
```

---

**版本**: 1.0.0
**最後更新**: 2025-10-24
**審核狀態**: 待審核
