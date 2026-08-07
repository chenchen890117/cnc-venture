# 文章發布指南 · Article Publishing Guide

CnC Venture 網站的文章系統。
**你不需要寫任何 HTML，也不需要動任何設計檔案。**

發一篇文章，只有五個動作：

> **① 建立資料夾 → ② 放 Markdown → ③ 放照片 → ④ 填基本資料 → ⑤ 上傳**

上傳之後，Netlify 會自動重新產生：文章頁（中英雙語）、分類列表頁、拓展誌首頁、延伸閱讀、上一篇／下一篇、sitemap 與 SEO 標籤。

---

## 0. 先認識一件事：`/content` 資料夾

網站的所有文章，都住在 repo 裡的 `content/` 資料夾。

```
content/
├── _config.json        ← 網站設定（分類名稱、選單、頁尾文字）
├── news/               ← 分類一：最新活動消息
├── stories/            ← 分類二：創業案例分享
└── market/             ← 分類三：在地知識分享
    └── phoenix-metro-market-guide/     ← 一篇文章 = 一個資料夾
        ├── meta.json       基本資料
        ├── zh-tw.md        中文內容
        ├── en.md           英文內容
        └── images/         這篇文章要用的照片
```

**規則只有一條：一篇文章 = 一個資料夾。**
資料夾名字就是網址。

---

## 1. 建立資料夾

在你要的分類底下，開一個新資料夾。

| 分類 | 資料夾 | 網址會變成 |
|---|---|---|
| 最新活動消息 | `content/news/` | `/zh-tw/insights/news/` |
| 創業案例分享 | `content/stories/` | `/zh-tw/insights/stories/` |
| 在地知識分享 | `content/market/` | `/zh-tw/insights/market/` |

資料夾名稱（slug）的規則：

- 只用**小寫英文、數字、連字號**：`taipei-trade-show-2026` ✅
- 不要用中文、空格、底線：`台北展覽 2026` ❌
- 取名要像網址，不要像標題：`opening-a-restaurant-in-arizona`

這個名字之後**不要改**——改了等於換網址，舊連結會失效。

範例：

```
content/news/phoenix-trade-mission-2026/
```

---

## 2. 放 Markdown

在資料夾裡建立兩個檔案：

- `zh-tw.md` — 中文
- `en.md` — 英文

> **只想先發一種語言？可以。**
> 只放 `zh-tw.md`，網站就只會產生中文頁。英文頁不會出現、不會 404，
> 搜尋引擎也不會被告知「有英文版」。等英文寫好，再補 `en.md` 就好。

每個 `.md` 檔案分成兩段：**上面的基本資料**，和**下面的內文**。

```markdown
---
title: 鳳凰城貿易訪問團 2026
standfirst: 這裡寫一段引言，出現在大標題下方。兩三句，說明這篇在講什麼。
description: 這段給 Google 和社群分享用，大約 60–120 字。
cardBlurb: 出現在列表卡片上的一句話。
crumb: 鳳凰城貿易訪問團
heroAlt: 一句話描述封面照片的內容（給視障讀者與搜尋引擎）
readingTime: 6 分鐘閱讀
dateLabel: 2026 年 9 月
---

## 第一個小標

這裡開始寫內文。空一行就是新的一段。

## 第二個小標

繼續寫。
```

上下兩段之間用 `---` 隔開，**上面那三條線不能刪**。

### 基本資料欄位

| 欄位 | 必填 | 說明 |
|---|:--:|---|
| `title` | ✅ | 文章標題 |
| `standfirst` | | 大標下方的引言 |
| `description` | | SEO 與社群分享的描述 |
| `cardBlurb` | | 列表卡片上的一句話 |
| `crumb` | | 麵包屑上的短標題（沒填就用 `title`） |
| `heroAlt` | ✅ | 封面照片的文字描述 |
| `heroCaption` | | 封面照片下方的圖說 |
| `readingTime` | | 例如 `6 分鐘閱讀` / `6 min read` |
| `dateLabel` | | 例如 `2026 年 9 月` / `September 2026` |

專案頁（`type` 是 `project`）另外可以填：`status`、`statusShort`、`industry`，以及專案資訊表格：

```markdown
facts:
  狀態 | 市場探索 · 進行中
  產業 | 餐飲品牌
  市場 | 亞利桑那州・大鳳凰城
  目前階段 | 選址與商圈研究
```

`facts:` 下面每一行**開頭要空兩格**，中間用 `|` 分開。

---

## 3. 寫內文：你會用到的全部語法

### 段落

直接寫。**空一行**代表新的一段。

```markdown
這是第一段。

這是第二段。
```

### 標題

```markdown
## 大標題（會自動編號 01、02、03…）
### 小標題
```

**不要用 `#` 一個井字號**——那是文章主標題，系統會自動放。

### 粗體、斜體、連結

```markdown
這裡是 **粗體**，這裡是 *斜體*。
這是一個 [連結](https://cncventure.org/)。
```

### 條列

```markdown
- 第一點
- 第二點
- 第三點
```

有順序的用數字：

```markdown
1. 先做這個
2. 再做這個
```

### 引言（大字引述）

行首加 `>`。想署名的話，最後一行用破折號開頭。

```markdown
> 目標不是快點開幕，而是選對市場。
> — 專案筆記
```

### 重點整理框（米色）

```markdown
:::callout
Label: 重點整理
Title: 這個專案的關鍵取決於什麼
- 第一項
- 第二項
- 第三項
Note: 最下面的補充說明（可以不寫）
:::
```

### 免責提醒（橘線）

任何牽涉到**法律、稅務、移民、證照、不動產**的內容，請務必加這一段。

```markdown
:::advisory
相關規定會因城市、郡、物件與業態而不同，也會隨時間調整。這裡的內容是幫助你建立方向感，不是專業建議——實際做決定前，請與具備資格的美國律師、會計師、稅務、移民、不動產與證照顧問確認細節。
:::
```

### 旁註（在正文旁邊的小字）

```markdown
:::note
補充一句不影響閱讀主線的話。螢幕夠寬的時候會跑到左邊留白處。
:::
```

### 分隔線

```markdown
---
```

---

## 4. 放照片

把照片放進文章資料夾裡的 `images/`：

```
content/news/phoenix-trade-mission-2026/
└── images/
    ├── delegation-visit.jpg
    └── city-hall.jpg
```

然後在內文裡這樣寫：

```markdown
:::image delegation-visit.jpg
Alt: 訪問團在鳳凰城市政廳前合影
Caption: 訪問團在鳳凰城市政廳。這是行程的第二天。
Credit: CnC Venture
Size: wide
:::
```

| 欄位 | 說明 |
|---|---|
| `Alt` | **必填。** 描述照片內容，給視障讀者與搜尋引擎看。 |
| `Caption` | 照片下方的圖說 |
| `Credit` | 攝影或來源 |
| `Size` | 照片寬度，見下表 |

### 四種照片寬度

| `Size` | 桌機實際寬度 | 什麼時候用 |
|---|---|---|
| `standard` | 與內文同寬（約 760px） | 預設，一般說明用圖 |
| `wide` | 突出到內文之外（約 1120px） | 章節之間的呼吸點、關鍵畫面 |
| `portrait` | 直式，約 500px | 直幅照片、人像 |
| `duo` | 兩張並排 | 對照、前後、兩個地點 |

（寫 `feature` 或 `full` 也可以，會自動當成 `wide`。照片不會滿到瀏覽器邊緣——這是刻意的。）

兩張並排要這樣寫：

```markdown
:::image before.jpg | after.jpg
Alt: 改造前的店面
Alt2: 改造後的店面
Caption: 同一個空間，兩個階段。
Size: duo
:::
```

### 照片規格建議

- **封面照**：至少 1600 × 900 px（16:9）
- **內文照**：至少 1200 px 寬
- 格式 `.jpg`，檔案盡量壓在 **300 KB 以內**
- 檔名用小寫英文與連字號：`delegation-visit.jpg` ✅ `照片1.JPG` ❌

> **關於封面照**
> 封面照放在共用的 `img/` 資料夾（不是 `images/`），
> 然後在 `meta.json` 的 `hero` 寫檔名。
> 如果你只想用文章自己的照片當封面，把它放進 `img/` 也可以。

**照片內容必須誠實。** 不要用猶他州的照片標成亞利桑那，也不要用別的城市的照片標成 Phoenix。這是我們一貫的原則。

---

## 5. 填基本資料：`meta.json`

在文章資料夾裡建立 `meta.json`：

```json
{
  "type": "article",
  "category": "news",
  "hero": "hero-trade-mission.jpg",
  "published": "2026-09-15",
  "updated": "2026-09-15",
  "order": 0,
  "related": ["phoenix-metro-market-guide"]
}
```

| 欄位 | 說明 |
|---|---|
| `type` | `article`（文章）或 `project`（進行中的專案） |
| `category` | `news` / `stories` / `market`，要和資料夾名稱一致 |
| `hero` | 封面照檔名，放在 `img/` 資料夾裡 |
| `published` | 發布日期，格式 `YYYY-MM-DD` |
| `updated` | 最後更新日期 |
| `order` | 同日期時的排序，數字小的在前 |
| `related` | 延伸閱讀要放哪幾篇（填資料夾名稱）。留 `[]` 系統會自動挑同分類的 |
| `draft` | 加 `"draft": true` 就不會發布，可以先放著慢慢寫 |

**JSON 的三個地雷**：所有引號要用**英文的** `"`；每一行結尾要有逗號，**最後一行不要**；括號要成對。

---

## 6. 上傳

1. 打開 **<https://github.com/chenchen890117/cnc-venture/upload/main>**
2. 把整個文章資料夾拖進去
   （拖 `content` 資料夾也可以，GitHub 會自己保留路徑）
3. 下方輸入一句說明，例如 `新增文章：鳳凰城貿易訪問團 2026`
4. 按 **Commit changes**

Netlify 會自動偵測到、跑一次建置、把新頁面發布上線。大約 **1–2 分鐘**。

---

## 7. 上線後檢查

新文章上線後，這幾個網址應該都要是對的：

- 中文文章頁 `https://cncventure.org/zh-tw/insights/<資料夾名>/`
- 英文文章頁 `https://cncventure.org/en/insights/<資料夾名>/`
- 分類頁上有它 `https://cncventure.org/zh-tw/insights/news/`
- 拓展誌首頁上有它 `https://cncventure.org/zh-tw/insights/`

順手看一下：封面照有出來、中文標題是粗黑體、上一篇／下一篇是對的、右上角語言切換會跳到對應的另一語言版本。

---

## 8. 出問題的時候

Netlify 的建置如果失敗，網站會**維持在上一個正常版本**，不會壞掉。你可以在 Netlify 的 **Deploys** 頁面看到錯誤訊息。

常見的幾種：

| 訊息 | 意思 | 怎麼修 |
|---|---|---|
| `hero image /img/xxx.jpg does not exist` | `meta.json` 的 `hero` 寫錯，或照片沒上傳 | 檢查檔名大小寫是否完全一致 |
| `references a missing image` | 內文的 `:::image` 檔名和 `images/` 裡的對不上 | 同上 |
| `slug "xxx" collides with the category` | 資料夾名稱和分類名稱撞名 | 換一個資料夾名稱 |
| `has no title — skipped` | `.md` 的基本資料裡少了 `title` | 補上 `title:` |
| `Unexpected token in JSON` | `meta.json` 格式錯了 | 檢查引號、逗號、括號 |
| `! ... has no Alt:` | 只是提醒，不會中斷 | 建議還是補上 `Alt:` |

---

## 9. 想新增一個分類？

打開 `content/_config.json`，在 `categories` 陣列裡加一組：

```json
{
  "slug": "resources",
  "en": "Resources & Tools",
  "zh-tw": "資源與工具",
  "blurb_en": "Checklists, templates and reference material.",
  "blurb_zh": "檢查清單、範本與參考資料。"
}
```

然後建立對應的 `content/resources/` 資料夾。分類頁、選單、sitemap 都會自動長出來——不用改任何程式碼。

---

## 附錄：內容原則

這幾條是網站一路以來的編輯底線，發文章時請一起帶著：

- **不要編造數字。** 沒有查證過的統計，寧可把句子改寫成不需要數字也成立。
- **不要把進行中的專案寫成已完成。** 不寫營收、不寫已簽租約、不寫店數、不寫投資金額。
- **不具名客戶**，除非客戶明確同意。
- **法律、稅務、移民、證照、不動產** —— 一律加 `:::advisory` 提醒。
- **中文是原生文案，不是翻譯。** 寫給台灣的企業主看，不是把英文轉過來。
- **照片要誠實。** 不把 A 地的照片標成 B 地。

---

## 快速範本

複製這一段，改成你要的內容就能用。

**`content/news/你的資料夾名/meta.json`**

```json
{
  "type": "article",
  "category": "news",
  "hero": "封面照檔名.jpg",
  "published": "2026-09-15",
  "updated": "2026-09-15",
  "order": 0,
  "related": []
}
```

**`content/news/你的資料夾名/zh-tw.md`**

```markdown
---
title: 你的文章標題
standfirst: 大標下方的引言，兩三句話。
description: 給搜尋引擎和社群分享看的描述。
cardBlurb: 列表卡片上的一句話。
crumb: 短標題
heroAlt: 封面照片的文字描述
readingTime: 5 分鐘閱讀
dateLabel: 2026 年 9 月
---

## 第一個小標

第一段內文。

第二段內文。

> 一句值得放大的話。

## 第二個小標

繼續。

:::image 你的照片.jpg
Alt: 照片描述
Caption: 圖說
Size: wide
:::

:::advisory
相關規定會因城市、郡、物件與業態而不同，也會隨時間調整。這裡的內容是幫助你建立方向感，不是專業建議——實際做決定前，請與具備資格的美國專業人士確認細節。
:::
```
