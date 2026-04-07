from airflow.models.param import Param
from airflow.utils.task_group import TaskGroup
from airflow.operators.python import PythonOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

from config import *
from utils.dag_tool import *


DAG_ID = 'WF_AUTO_PARTITION'
SCHEDULE = '0 0 * * *' # 每天午夜執行
# PARAMS = {
#     # 1. 完全不給預設值 (在 UI 會顯示為空白)
#     'machine_id': Param(
#         default=None,
#         type=['null', 'integer'],
#         description=''
#     ),
#
#     # 2. 給予 None 作為預設值，並要求格式
#     'target_date': Param(
#         default=None,
#         type=['null', 'string'],
#         format='date',
#         description="請選擇日期"),
#
#     # 3. 使用 Enum 提供下拉選單，但不預選
#     'operation_type': Param(
#         type='string',
#         enum=['INSERT', 'UPDATE', 'DELETE'],
#         description="請選擇操作類型"
#     )
# }

dag = create_dag(
    dag_id=DAG_ID,
    **{
        'tags': ['WF', 'AUTO', 'SCHEDULE'],
        'schedule': SCHEDULE,
        # 'params': PARAMS,
        'max_active_runs': 1,  # TODO 同一時間只允許 1 個實例運行，若超過則排隊等待
        'max_active_tasks': 10,  # TODO 同一時間只允許 10 個任務運行，若超過則排隊等待
    }
)


def get_parameters(**kwargs) -> list:
    # ret_list = []
    ret_list = [
        'fact_production',
        # 'machine_status_logs',
        # 'production_records'
    ]
    return [f'{DAG_ID}.trigger_{i}' for i in ret_list]


with dag:
    START = get_empty_symbol(
        task_id='START'
    )
    END = get_empty_symbol(
        task_id='END',
        trigger_rule='none_failed'
    )
    CHECK_PARAMETERS = PythonOperator(
        task_id='CHECK_PARAMETERS',
        python_callable=check_parameters,
        op_kwargs={
            'DAG_ID': DAG_ID,
            'SCHEDULE': SCHEDULE,
        }
    )
    CHECK_BRANCH_FROM_PARAMETERS = BranchPythonOperator(
        task_id='CHECK_BRANCH_FROM_PARAMETERS',
        python_callable=get_parameters
    )

    with TaskGroup(group_id=DAG_ID) as WF_AUTO_PARTITION:
        target_list = [
            'fact_production',
            'machine_status_logs',
            'production_records'
        ]

        for i in target_list:
            TriggerDagRunOperator(
                task_id=f'trigger_{i}',
                trigger_dag_id='SQL_OPERATOR_TOOL',
                conf={'trigger_file': i},
                wait_for_completion=False,  # 是否等待子 DAG 完成 才繼續執行後續任務
                poke_interval=30  # 如果要等待，每隔多久檢查子 DAG 狀態
            )

    START >> CHECK_PARAMETERS >> \
    CHECK_BRANCH_FROM_PARAMETERS >> \
    WF_AUTO_PARTITION >> \
    END