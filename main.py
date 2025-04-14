import lorem
import time
import random
import re
import datetime
from dotenv import load_dotenv
import os

# 載入 .env 文件
load_dotenv()

# 讀取環境變數
run_time = int(os.getenv('RUN_TIME', 300))  # 預設執行時間為 300 秒
sentence_count = int(os.getenv('SENTENCE_COUNT', 3))  # 預設句子數量為 3
max_text_length = int(os.getenv('MAX_TEXT_LENGTH', 200))  # 預設最大文字長度為 200
sleep_time = float(os.getenv('SLEEP_TIME', 1))  # 預設睡眠時間為 1 秒

# 定義顏色代碼 (ANSI escape codes)
colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'reset': '\033[0m'  # 用於重置顏色
}

# 計算開始時間
start_time = time.time()

while True:
    # 獲取當前時間並格式化
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    
    # 生成一段 Lorem Ipsum 文本
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
    
    # 在句子前面加入時間戳記
    print(f"[{current_time}] {colored_sentence}")
    
    # 等待指定的時間
    time.sleep(sleep_time)
    
    # 檢查是否超過執行時間
    if time.time() - start_time >= run_time:
        break