from airflow.operators.python import PythonOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from utils.dag_tool import *


DAG_ID = 'SQL_OPERATOR_TOOL'
dag = create_dag(
    dag_id=DAG_ID,
    **{
        'tags': ['OPERATOR', 'SQL'],
        'schedule': None,
        'template_searchpath': ['/opt/airflow/dags/sql'],
        'max_active_runs': 30,  # TODO 同一時間只允許 30 個實例運行，若超過則排隊等待
        'max_active_tasks': 10,  # TODO 同一時間只允許 10 個任務運行，若超過則排隊等待
    }
)


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
        }
    )
    SQLExecuteQuery = SQLExecuteQueryOperator(
        task_id='SQLExecuteQuery',
        conn_id='postgresql_migration_user',
        # sql="auto_partition/{{ dag_run.conf.get('trigger_file', 'default_cleanup') }}.sql",
        # sql="auto_partition/{{ dag_run.conf.get('trigger_file') }}.sql",
        sql='auto_partition/fact_production.sql',
        autocommit=True
    )

    START >> CHECK_PARAMETERS >> \
    SQLExecuteQuery >> \
    END