# -*- coding: utf-8 -*-
KEEPALIVE_INTERVAL = 300 # timeout (300s = 5min)
DEFAULT_CLIENT = 'Developer'

DEFAULT_BROKER = '127.0.0.1'
DEFAULT_BROKER_PORT = 1883

DEFAULT_MIDDLE_BROKER = '127.0.0.1'
DEFAULT_MIDDLE_PORT = 9999

LOG_DEFAULT_NAME = 'MQTT Service'

MAX_WORKERS = 10

# 設定最大訊息長度
    # 4096 (4 KB)
    # 8192 (8 KB)
    # 16384 (16 KB)
MAX_MSG_SIZE = 8192

# 設定批次處理的訊息數量
PUBLISHER_BATCH_SIZE = 10

# 設定批次發布的逾時時間 (例如 0.5 秒)
PUBLISHER_BATCH_TIMEOUT = 0.5