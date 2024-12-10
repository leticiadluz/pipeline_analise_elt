import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from utils.create_tables import criar_tabelas
from utils.etl import dados_api, carregar_dados

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1
}

def extrair_e_carregar():
    dados = dados_api()
    carregar_dados(dados)

with DAG('etl_dag',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    criar_tabelas_task = PythonOperator(
        task_id='criar_tabelas',
        python_callable=criar_tabelas
    )

    extrair_e_carregar_task = PythonOperator(
        task_id='extrair_e_carregar',
        python_callable=extrair_e_carregar
    )

    criar_tabelas_task >> extrair_e_carregar_task

