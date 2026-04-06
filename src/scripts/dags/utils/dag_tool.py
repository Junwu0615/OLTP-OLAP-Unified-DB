from airflow import DAG
from airflow.operators.empty import EmptyOperator
from config.dag_config import BaseDagConfig


# TODO 常用函式
def create_dag(dag_id: str, owner: str=None, **kwargs) -> DAG:
    default_args = BaseDagConfig.default_args
    default_args['owner'] = default_args['owner'] if owner is None else owner
    dag = DAG(
        dag_id=dag_id,
        default_args=default_args,
        **{**BaseDagConfig.dag_args, **kwargs}
    )
    return dag


# TODO 常用暫用符
def get_start_symbol():
    return EmptyOperator(
        task_id='START'
    )

def get_end_symbol():
    return EmptyOperator(
        task_id='END',
        trigger_rule='none_failed'
    )