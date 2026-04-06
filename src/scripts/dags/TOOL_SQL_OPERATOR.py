from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator

from utils.dag_tool import *


dag = create_dag(
    dag_id='TOOL_SQL_OPERATOR',
    **{
        'tags': ['TOOL', 'SQL'],
        'schedule': None,
        'max_active_runs': 20,  # TODO 同一時間只允許 20 個實例運行，若超過則排隊等待
        'max_active_tasks': 10,  # TODO 同一時間只允許 10 個任務運行，若超過則排隊等待
    }
)


with dag:
    task_a = EmptyOperator(task_id='task_a')

    START >> \
    task_a >> \
    END