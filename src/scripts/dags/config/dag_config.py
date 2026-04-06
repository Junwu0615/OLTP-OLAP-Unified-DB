from datetime import datetime, timedelta

class BaseDagConfig:
    # default_args = {
    #     'owner': 'PC',
    #     'retries': 3,
    #     'retry_delay': timedelta(minutes=1),
    # }

    dag_args = {
        'owner': 'PC',
        'retries': 3,
        'retry_delay': timedelta(minutes=1),
        'start_date': datetime(2025, 1, 1),
        'dagrun_timeout': timedelta(minutes=30), # 每次 DAG 運行的最大允許時間，超過則自動終止
        'description': '',
        'schedule': None,
        'catchup': False, # 不執行過去的任務
        'max_active_runs': 1,
        'max_active_tasks': 10,
        'tags': ['UNKNOWN'],
    }