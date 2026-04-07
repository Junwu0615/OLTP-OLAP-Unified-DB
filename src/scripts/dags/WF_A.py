from config import *
from config.constants import WF_A_STATUS
from utils.dag_tool import check_parameters
# from airflow.datasets import Dataset


def extract_logic(**kwargs):
    logging.warning('正在從 OLTP 提取資料...')


DAG_ID = 'WF_A'
with DAG(
    dag_id=DAG_ID,
    # start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=['DATASET']
) as dag:
    START = EmptyOperator(
        task_id='START',
        trigger_rule='all_success'
    )
    END = EmptyOperator(
        task_id='END',
        trigger_rule='none_failed'
    )
    CHECK_PARAMETERS = PythonOperator(
        task_id='CHECK_PARAMETERS',
        python_callable=check_parameters,
        op_kwargs={
            'DAG_ID': DAG_ID,
        }
    )
    extract_task = PythonOperator(
        task_id='extract_from_oltp',
        python_callable=extract_logic,
        outlets=[WF_A_STATUS] # TODO 關鍵：成功後觸發 Dataset 更新
    )

    START >> CHECK_PARAMETERS >> extract_task >> END