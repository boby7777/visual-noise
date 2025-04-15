# 視覺白噪音生成器

這是一個簡單的 Python 工具，用於生成帶有隨機顏色標記的 Lorem Ipsum 文本或隨機字元串。以白噪音為靈感，這個工具嘗試創建一種視覺白噪音效果，可以作為正念冥想的輔助工具。觀看不斷變化的文字和色彩，可以幫助使用者專注當下，緩解壓力。

## 功能

- 生成隨機的 Lorem Ipsum 文本段落或包含英數及特殊符號的隨機字元串
- 將隨機選擇的單詞或字元段以柔和的顏色突出顯示，創造視覺白噪音效果
- 可選是否在每行輸出前添加時間戳，提供時間感知
- 可配置的參數（通過 .env 文件）:
  - 執行時間
  - 句子數量（適用於 Lorem Ipsum 模式）
  - 最大文本長度
  - 更新速度（間隔時間）
  - 文字模式（Lorem Ipsum 或隨機字元）
  - 是否顯示時間戳

## 安裝

安裝所需依賴:

```bash
pip install python-lorem python-dotenv
```

## 配置

在專案根目錄創建一個 `.env` 文件，並設定以下參數:

```
RUN_TIME=300        # 程序運行時長（秒）
SENTENCE_COUNT=3    # 每次生成的句子數量（僅適用於 Lorem Ipsum 模式）
MAX_TEXT_LENGTH=200 # 文本最大長度
SLEEP_TIME=2        # 更新間隔時間（秒），可使用小數點設定更精確的時間
SHOW_TIMESTAMP=True # 是否顯示時間戳（True 或 False）
TEXT_MODE=lorem     # 文字模式：lorem 或 random
```

## 使用方法

執行主程序:

```bash
python main.py
```

程序將會:

1. 在啟動時顯示冥想引導文字
2. 根據設定的間隔時間生成新的文本段落（Lorem Ipsum 或隨機字元）
3. 隨機為約 30% 的單詞或字元段加上柔和的顏色
4. 可選顯示當前時間戳
5. 在指定的運行時間後自動停止

### 速度調整

- 將 `SLEEP_TIME` 設定為較低的值（如 0.5）可以獲得更快的更新頻率，適合需要更強烈視覺刺激的使用者
- 將 `SLEEP_TIME` 設定為較高的值（如 3.0）可以獲得更慢的更新頻率，適合需要緩慢轉變的冥想體驗
- 默認值 2.0 秒提供了平衡的體驗

### 文字模式

- **Lorem Ipsum 模式**（`TEXT_MODE=lorem`）：生成無意義但可讀的文本，適合專注於形狀而非內容。
- **隨機字元模式**（`TEXT_MODE=random`）：生成包含英數和特殊符號的隨機字串，直接生成指定長度（`MAX_TEXT_LENGTH`），更抽象，減少閱讀傾向。

### 冥想指南

使用此工具進行正念冥想練習：

1. 在一個安靜的環境中運行程序
2. 放鬆身體，調整呼吸
3. 專注觀察不斷變化的文字和顏色
4. 不要試圖閱讀內容，只需觀察文字的形狀和顏色變化
5. 如果思緒走神，溫和地將注意力帶回到螢幕上的視覺變化

建議冥想時間為 5-15 分鐘，可以通過 `RUN_TIME` 參數調整。

## 示例輸出

**Lorem Ipsum 模式（啟用時間戳）**：

```
[15:30:22] Lorem ipsum dolor sit amet, consectetur adipiscing elit.
[15:30:24] Etiam porta vehicula nunc, ac dignissim massa volutpat vitae.
```

**隨機字元模式（禁用時間戳）**：

```
LGt8I#T`mI%nMs-CqzeAHU&]>\:Pu_,8SlfU$-4?~9_S$tj;/yVb-Jn27mocZUI*-,b|zuSEt!coOXA<`i{"Q5i2D]qqYvzE2=qg4*5|Z:@{F61*s\FL2TcKT!2[k]LS?e!7=RQ~d>J!5'`Y~E}jh4jj#sg977_?E4gG}1X&nb;!X!"@Bswo
3Od;=okMYaif&N22K\=:KzA,2#\[?>Y]^e{o/}7s3H6y~?YfY:=68@K[N=f)-_f.g3h3}~<~wgu$9G=moMXI69Mx8aZG9SN9<bP;Swk-vR#Z~~,"Q<%E=g<`w%(jvD!N:5>Hd,|NfMb$''e2AXT*A6r9/$!|*PBDp}~$C;xd=?8YOR2q^h]t
ATH@itg@<{h+L?_aD}@Y"[ojO=q7v(PU,^J5rz)1EY@13^!9~~h><2}VB:Sw5b2#j:"yPh3_>6L^i2gqY_b0tThBYMAs<5h#xEz$x/9S$hQ|:]yV=></IUp&]n967;~#/;(a`5I%kD{)Uz=FE7v@s~UJYQivzHj}gI7o+s@+R-92M-nv[(11
```

## 自定義

您可以修改 `colors` 字典來更改可用的顏色（目前為柔和色調，如淺藍、淡綠等），或者調整顏色應用的概率（目前設定為 30%）。調整這些參數可以改變視覺白噪音的強度和感覺。

## 依賴

- python-lorem: 生成 Lorem Ipsum 文本
- python-dotenv: 從 .env 文件讀取配置

## 許可證

MIT