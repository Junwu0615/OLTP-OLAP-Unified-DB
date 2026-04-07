from airflow import DAG
from airflow.operators.empty import EmptyOperator

from config import *
from config.dag_config import BaseDagConfig


# TODO 常用函式
def __getattr__(name: str):
    if name == 'START':
        return EmptyOperator(
            task_id=name,
            trigger_rule='all_success',
        )
    elif name == 'END':
        return EmptyOperator(
            task_id=name,
            trigger_rule='none_failed',
        )
    else:
        raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


def check_parameters(**kwargs) -> dict:
    dag_run = kwargs.get('dag_run').conf if kwargs.get('dag_run') is not None else {}
    parameters = {**kwargs.get('params', {}), **dag_run}

    logging.warning(f'PARAMETERS: {parameters}')
    logging.warning(f'DAG_ID: {kwargs.get('DAG_ID', None)}')
    logging.warning(f'SCHEDULE: {kwargs.get('SCHEDULE', None)}')

    # return parameters
    return {}


def create_dag(dag_id: str, owner: str=None, **kwargs) -> DAG:
    default_args = BaseDagConfig.default_args
    default_args['owner'] = default_args['owner'] if owner is None else owner
    dag = DAG(
        dag_id=dag_id,
        default_args=default_args,
        **{**BaseDagConfig.dag_args, **kwargs}
    )
    return dag