# 視覺白噪音生成器

這是一個簡單的 Python 工具，用於生成帶有隨機顏色標記的 Lorem Ipsum 文本。以白噪音為靈感，這個工具嘗試創建一種視覺白噪音效果，可以作為正念冥想的輔助工具。觀看不斷變化的文字和色彩，可以幫助使用者專注當下，緩解壓力。

## 功能

- 生成隨機的 Lorem Ipsum 文本段落
- 將隨機選擇的單詞以不同顏色突出顯示，創造視覺白噪音效果
- 在每行輸出前添加時間戳，提供時間感知
- 可配置的參數（通過 .env 文件）:
  - 執行時間
  - 句子數量
  - 最大文本長度
  - 更新速度（間隔時間）

## 安裝

1. 克隆此儲存庫:
```bash
git clone https://github.com/yourusername/visual-noise-meditation.git
cd visual-noise-meditation
```

2. 安裝所需依賴:
```bash
pip install python-lorem python-dotenv
```

## 配置

在專案根目錄創建一個 `.env` 文件，並設定以下參數:

```
RUN_TIME=300        # 程序運行時長（秒）
SENTENCE_COUNT=3    # 每次生成的句子數量
MAX_TEXT_LENGTH=180 # 文本最大長度
SLEEP_TIME=1        # 更新間隔時間（秒），可使用小數點設定更精確的時間
```

## 使用方法

執行主程序:

```bash
python main.py
```

程序將會:
1. 根據設定的間隔時間生成新的文本段落
2. 隨機為約 30% 的單詞加上顏色
3. 在文本前面顯示當前時間
4. 在指定的運行時間後自動停止

### 速度調整

- 將 `SLEEP_TIME` 設定為較低的值（如 0.5）可以獲得更快的更新頻率，適合需要更強烈視覺刺激的使用者
- 將 `SLEEP_TIME` 設定為較高的值（如 2.0）可以獲得更慢的更新頻率，適合需要緩慢轉變的冥想體驗
- 對於大多數使用者，1.0 秒的默認值提供了平衡的體驗

### 冥想指南

使用此工具進行正念冥想練習：

1. 在一個安靜的環境中運行程序
2. 放鬆身體，調整呼吸
3. 專注觀察不斷變化的文字和顏色
4. 不要試圖閱讀內容，只需觀察文字的形狀和顏色變化
5. 如果思緒走神，溫和地將注意力帶回到螢幕上的視覺變化

建議冥想時間為 5-15 分鐘，可以通過 RUN_TIME 參數調整。

## 示例輸出

```
[15:30:22] Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut ac nibh magna. Praesent nec fringilla tortor.
[15:30:23] Etiam porta vehicula nunc, ac dignissim massa volutpat vitae. Fusce fermentum dapibus elit ac cursus.
```

## 自定義

您可以修改 `colors` 字典來更改可用的顏色，或者調整顏色應用的概率（目前設定為 30%）。調整這些參數可以改變視覺白噪音的強度和感覺。

## 依賴

- python-lorem: 生成 Lorem Ipsum 文本
- python-dotenv: 從 .env 文件讀取配置

## 許可證

[MIT](LICENSE)