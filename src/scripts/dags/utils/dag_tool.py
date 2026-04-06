from airflow import DAG
from airflow.operators.empty import EmptyOperator

from config.dag_config import BaseDagConfig


# TODO 常用暫用符
START = EmptyOperator(
    task_id='START'
)
END = EmptyOperator(
    task_id='END',
    trigger_rule='none_failed'
)

# TODO 常用函式
def create_dag(dag_id: str, **kwargs) -> DAG:
    # default_args = BaseDagConfig.default_args
    default_args = BaseDagConfig.dag_args

    dag = DAG(
        dag_id=dag_id,
        default_args={**default_args, **kwargs}
    )
    return dag