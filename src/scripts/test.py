import psycopg2
import random
import time
from datetime import datetime, timedelta

# ===== DB 連線設定 =====
conn = psycopg2.connect(
    host="localhost",
    dbname="your_db",
    user="your_user",
    password="your_password"
)
conn.autocommit = True
cursor = conn.cursor()

# ===== 模擬參數 =====
NUM_MACHINES = 5
RUN_DURATION_SEC = 60  # 測試時間
EVENT_INTERVAL = 0.1   # 每 0.1 秒產生一筆（約 10 TPS）

# ===== 狀態轉換機率（關鍵）=====
STATE_TRANSITION = {
    "RUNNING": ["RUNNING", "IDLE", "DOWN"],
    "IDLE": ["RUNNING", "IDLE"],
    "DOWN": ["IDLE", "DOWN"]
}

# ===== 初始狀態 =====
machine_states = {
    machine_id: random.choice(["RUNNING", "IDLE", "DOWN"])
    for machine_id in range(1, NUM_MACHINES + 1)
}

# ===== 寫入 function =====
def insert_status_log(machine_id, status):
    cursor.execute("""
        INSERT INTO machine_status_logs (machine_id, status, event_time)
        VALUES (%s, %s, %s)
    """, (machine_id, status, datetime.now()))

def insert_production(machine_id):
    produced = random.randint(5, 20)
    defect = int(produced * random.uniform(0.01, 0.05))

    cursor.execute("""
        INSERT INTO production_records (
            machine_id, order_id, produced_qty, defect_qty, record_time
        )
        VALUES (%s, %s, %s, %s, %s)
    """, (
        machine_id,
        random.randint(1, 10),  # 假設已有 orders
        produced,
        defect,
        datetime.now()
    ))

# ===== 主模擬 loop =====
def run_simulation():
    start_time = time.time()

    while time.time() - start_time < RUN_DURATION_SEC:
        for machine_id in machine_states.keys():

            # 狀態轉換
            current_state = machine_states[machine_id]
            next_state = random.choice(STATE_TRANSITION[current_state])
            machine_states[machine_id] = next_state

            # 寫入狀態 log（高頻）
            insert_status_log(machine_id, next_state)

            # 如果在 RUNNING → 產生生產資料
            if next_state == "RUNNING":
                if random.random() < 0.7:  # 70% 機率產生
                    insert_production(machine_id)

        time.sleep(EVENT_INTERVAL)

# ===== 執行 =====
if __name__ == "__main__":
    print("Start simulation...")
    run_simulation()
    print("Done.")