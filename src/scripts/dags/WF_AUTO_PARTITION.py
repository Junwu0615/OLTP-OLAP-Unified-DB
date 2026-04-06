from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator

from utils.dag_tool import *


def check_parameters(**context):
    return ["task_a", "task_b"]   # 同時觸發兩個task


dag = create_dag(
    dag_id='WF_AUTO_PARTITION',
    **{
        'tags': ['WF', 'AUTO', 'SCHEDULE'],
        'schedule': '0 0 0 * *', # 每天午夜執行
        'max_active_runs': 1,  # TODO 同一時間只允許 1 個實例運行，若超過則排隊等待
        'max_active_tasks': 10,  # TODO 同一時間只允許 10 個任務運行，若超過則排隊等待
    }
)


with dag:
    CHECK_BRANCH_FROM_PARAMETERS = BranchPythonOperator(
        task_id='CHECK_BRANCH_FROM_PARAMETERS',
        python_callable=check_parameters
    )


    # TriggerDagRunOperator(
    #     task_id="trigger_b",
    #     trigger_dag_id="pipeline_b",
    #     wait_for_completion=False,
    # )

    task_a = EmptyOperator(task_id='task_a')
    task_b = EmptyOperator(task_id='task_b')
    task_c = EmptyOperator(task_id='task_c')

    START >> \
    CHECK_BRANCH_FROM_PARAMETERS >> \
    [task_a, task_b, task_c] >> \
    END