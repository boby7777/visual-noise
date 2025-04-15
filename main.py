import lorem
import time
import random
import re
import datetime
import string
from dotenv import load_dotenv
import os

# 載入 .env 文件
load_dotenv()

# 讀取環境變數
run_time = int(os.getenv('RUN_TIME', 300))  # 預設執行時間為 300 秒
sentence_count = int(os.getenv('SENTENCE_COUNT', 3))  # 預設句子數量為 3
max_text_length = int(os.getenv('MAX_TEXT_LENGTH', 200))  # 預設最大文字長度為 200
sleep_time = float(os.getenv('SLEEP_TIME', 2))  # 預設睡眠時間為 2 秒
show_timestamp = os.getenv('SHOW_TIMESTAMP', 'True').lower() == 'true'  # 控制是否顯示時間戳
text_mode = os.getenv('TEXT_MODE', 'lorem').lower()  # 文字模式：'lorem' 或 'random'

# 定義顏色代碼 (ANSI escape codes)，使用更多柔和的色調
colors = {
    'light_blue': '\033[94m',      # 淺藍
    'light_green': '\033[92m',     # 淡綠
    'light_cyan': '\033[96m',      # 淺青
    'light_magenta': '\033[95m',   # 淡紫
    'soft_pink': '\033[38;2;255;182;193m',    # 柔粉
    'pastel_lavender': '\033[38;2;230;230;250m',  # 薰衣草紫
    'mint_green': '\033[38;2;152;255;152m',   # 薄荷綠
    'baby_blue': '\033[38;2;173;216;230m',    # 嬰兒藍
    'reset': '\033[0m'  # 用於重置顏色
}

# 隨機字元生成函數
def generate_random_text(max_text_length):
    # 包含英數和特殊符號的字元集
    characters = string.ascii_letters + string.digits + string.punctuation
    # 直接生成 max_text_length 長度的隨機字串
    text = ''.join(random.choice(characters) for _ in range(max_text_length))
    return text

# 顯示冥想引導文字
print("請放鬆身體，專注於文字的形狀和顏色變化，不要試圖閱讀內容。")
print("--------------------------------------------------")

# 計算開始時間
start_time = time.time()

while True:    
    # 根據 text_mode 生成文字
    if text_mode == 'random':
        sentences = generate_random_text(max_text_length)
    else:  # 預設使用 lorem
        sentences = lorem.get_sentence(count=sentence_count)
        # 截斷文字以符合最大長度限制
        if len(sentences) > max_text_length:
            sentences = sentences[:max_text_length]
    
    # 將句子分拆成單詞
    words = re.findall(r'\b\w+\b', sentences)
    
    # 隨機選擇 30% 的單詞加上顏色
    colored_sentence = sentences
    for word in words:
        if random.random() < 0.3:  # 30% 的機率為單詞加上顏色
            color_name = random.choice(list(colors.keys() - {'reset'}))
            colored_word = f"{colors[color_name]}{word}{colors['reset']}"
            # 替換整個單詞，確保只替換完整的單詞（使用 word boundary）
            colored_sentence = re.sub(r'\b' + re.escape(word) + r'\b', colored_word, colored_sentence, 1)
    
    # 根據 show_timestamp 決定是否顯示時間戳
    if show_timestamp:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(f"[{current_time}] {colored_sentence}")
    else:
        print(colored_sentence)
    
    # 等待指定的時間
    time.sleep(sleep_time)
    
    # 檢查是否超過執行時間
    if time.time() - start_time >= run_time:
        break