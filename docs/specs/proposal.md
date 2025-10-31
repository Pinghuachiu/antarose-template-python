# OpenSpec Proposal: Template Initialization Script (anta-node.sh)

**專案名稱**: antarose-template-nodejs - Template Initialization Script
**提案日期**: 2025-10-24
**提案人**: CTO
**狀態**: 待審核

---

## 1. 提案摘要

建立一個**進階版模板初始化腳本** `anta-node.sh`，讓開發者能夠透過單一指令快速建立基於 Antarose Template 的新專案。

### 核心目標

1. **一鍵建立專案**: 透過 `anta-node.sh project_name` 快速初始化
2. **互動式配置**: 引導使用者完成專案設定
3. **自動化處理**: 自動安裝依賴、初始化 Git、設定 remote
4. **生產就緒**: 產生的專案立即可用於開發

---

## 2. 問題陳述

### 2.1 當前挑戰
1. **手動設定耗時**: 開發者需要花費 30+ 分鐘配置新專案
2. **專案結構不一致**: 不同開發者建立的專案結構不同
3. **缺少最佳實踐**: 新專案經常缺少適當的文件、測試設定等
4. **配置錯誤**: 手動編輯 `package.json` 等配置檔案容易出錯

### 2.2 期望結果
提供單一指令解決方案：
- 下載模板儲存庫
- 互動式配置專案
- 移除不必要的檔案（模板的 OpenSpec 文件）
- 初始化 Git repository 並設定 remote
- 自動安裝依賴
- 產生生產就緒的專案結構

---

## 3. 提案方案

### 3.1 核心功能

**腳本名稱**: `anta-node.sh`

**使用方式**:
```bash
# 方式 1: 直接從 GitHub 執行
curl -fsSL https://raw.githubusercontent.com/Pinghuachiu/antarose-template-nodejs/main/anta-node.sh | bash -s project_name

# 方式 2: 下載後執行
wget https://raw.githubusercontent.com/Pinghuachiu/antarose-template-nodejs/main/anta-node.sh
chmod +x anta-node.sh
./anta-node.sh my-new-project
```

**執行流程**:
1. ✅ 驗證環境（Git、Node.js 已安裝）
2. ✅ 檢查專案目錄是否已存在
3. ✅ 從 GitHub clone 模板儲存庫
4. ✅ 重新命名為 `project_name`
5. ✅ 刪除 `.git/` 目錄（移除模板的 Git 歷史）
6. ✅ 刪除 `docs/specs/` 目錄（OpenSpec 文件）
7. ✅ 保留 `docs/architecture/` （技術文件作為參考）
8. ✅ 互動式提示進行配置
9. ✅ 更新 `package.json` 等配置檔案
10. ✅ 自動安裝 npm 依賴
11. ✅ 初始化新的 Git repository
12. ✅ 設定 Git remote（如果使用者提供）
13. ✅ 建立初始 commit
14. ✅ 顯示成功訊息與後續步驟

### 3.2 互動式配置

腳本將詢問使用者以下資訊：

| 提示項目 | 預設值 | 必填 | 更新檔案 |
|---------|--------|------|---------|
| 專案名稱 | (CLI 參數) | 是 | `package.json` name |
| 專案描述 | "A Node.js project built with Antarose Template" | 否 | `package.json` description |
| 作者 | jackalchiu@antarose.com | 否 | `package.json` author |
| GitHub Repository URL | (無) | 否 | Git remote origin |
| 是否安裝依賴？ | Yes | 否 | 執行 `npm install` |

### 3.3 檔案操作

**需要刪除的檔案**:
- `docs/specs/` （整個目錄）
- `anta-node.sh` 本身（執行成功後自刪除）

**需要保留的檔案**:
- `docs/architecture/` （所有技術文件）
- 所有原始碼（`apps/`、`packages/`、`frontend/`、`backend/`）
- 配置檔案（`package.json`、`tsconfig.json` 等）
- Root `README.md`

**需要修改的檔案**:
- `package.json`: 更新 name、description、author、version（重設為 1.0.0）
- `README.md`: 更新專案名稱標題
- `frontend/package.json`: 更新 name
- `backend/package.json`: 更新 name

### 3.4 錯誤處理

腳本必須處理以下情況：
- ❌ Git 未安裝 → 顯示安裝指引
- ❌ Node.js/npm 未安裝 → 顯示安裝指引
- ❌ 專案目錄已存在 → 詢問是否覆蓋或取消
- ❌ 網路失敗導致 clone 失敗 → 顯示錯誤並清理
- ❌ npm install 失敗 → 顯示錯誤但不回滾（使用者可重試）

---

## 4. 技術考量

### 4.1 依賴項目
- **Bash**: Version 4.0+ (macOS、Linux、Windows Git Bash 可用)
- **Git**: Version 2.0+
- **Node.js**: Version 18+ (LTS)
- **npm**: Version 8+

### 4.2 相容性
- ✅ macOS (主要開發平台)
- ✅ Linux (Ubuntu、CentOS 等)
- ✅ Windows (透過 Git Bash 或 WSL)

### 4.3 安全性
- 使用 `https://` 進行 Git clone（避免 SSH 認證問題）
- 驗證使用者輸入以防止指令注入
- 不在腳本中儲存敏感資訊

---

## 5. 成功標準

### 5.1 功能需求
- ✅ 腳本成功 clone 模板儲存庫
- ✅ 專案目錄正確重新命名
- ✅ OpenSpec 文件被移除
- ✅ 架構文件被保留
- ✅ `package.json` 正確更新使用者輸入
- ✅ 依賴成功安裝
- ✅ Git repository 初始化並建立初始 commit
- ✅ Git remote 正確設定（如果提供）

### 5.2 非功能需求
- ✅ 執行時間: < 3 分鐘（包含 npm install）
- ✅ 使用者友善的錯誤訊息
- ✅ 長時間操作顯示進度指示器
- ✅ 關鍵失敗時自動回滾（npm install 之前）

### 5.3 驗收標準
- ✅ QA 團隊成功使用腳本建立 3 個測試專案
- ✅ 所有產生的專案可成功 build 和 run
- ✅ 執行腳本後無需手動配置
- ✅ 腳本在 macOS、Linux 和 Windows Git Bash 上正常運作

---

## 6. 風險與緩解

| 風險 | 影響 | 機率 | 緩解措施 |
|------|------|------|---------|
| Clone 期間網路失敗 | 高 | 中 | 重試邏輯 + 清晰錯誤訊息 |
| npm install 卡住 | 中 | 低 | 增加逾時 + 允許使用者跳過 |
| 使用者中途中斷腳本 | 中 | 中 | EXIT trap 清理暫存檔案 |
| 不相容的 shell 版本 | 低 | 低 | 開始時檢查 Bash 版本 |

---

## 7. 時程預估

| 階段 | 時間 | 負責人 |
|------|------|--------|
| 提案審核與核准 | 0.5 天 | CTO |
| 設計與規格 | 0.5 天 | CTO |
| 實作 | 1 天 | Costa (Backend Engineer) |
| 測試（手動 + E2E） | 0.5 天 | Lucia/Ann (QA) |
| 文件更新 | 0.5 天 | Leo (Architect) |
| **總計** | **3 天** | - |

---

## 8. 下一步驟

1. ✅ **CTO 核准**: 審核並核准此提案
2. ⏳ **建立 design.md**: 詳細技術設計
3. ⏳ **建立 tasks.md**: 拆解實作任務
4. ⏳ **建立 spec.md**: 詳細規格
5. ⏳ **實作**: 委派給 Costa
6. ⏳ **測試**: 委派給 QA 團隊
7. ⏳ **文件更新**: 委派給 Leo

---

## 9. CTO 核准

**狀態**: ✅ **已核准**

**審核人**: CTO

**核准人**: CTO

**日期**: 2025-10-24

**意見**:
- 提案符合業務需求，技術方案可行
- 進階版（方案 B）提供更好的使用者體驗
- 建議優先處理錯誤處理機制
- 核准進入設計階段

---

**文件版本**: 1.0
**建立日期**: 2025-10-24
**作者**: CTO (Antarose AI Tech Inc.)
**最後更新**: 2025-10-24
