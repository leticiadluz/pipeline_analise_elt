# Testando a conexão entre o Airflow e um banco de dados PostgreSQL local
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.base import BaseHook
from datetime import datetime
import logging

def test_postgresql():
    try:
        connection = BaseHook.get_connection("postgresss") 
        host = connection.host
        login = connection.login
        password = connection.password
        port = connection.port
        database = connection.schema  

        logging.info(f"Conectando ao PostgreSQL em {host}:{port} no banco de dados '{database}'")
        from sqlalchemy import create_engine

        connection_string = f"postgresql+psycopg2://{login}:{password}@{host}:{port}/{database}"
        engine = create_engine(connection_string)
        with engine.connect() as conn:
            result = conn.execute("SELECT 1")
            for row in result:
                logging.info(f"Conexão bem-sucedida! Resultado: {row[0]}")
    except Exception as e:
        logging.error(f"Erro ao conectar ao PostgreSQL: {str(e)}")
        raise

default_args = {
    "owner": "airflow",
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="test_postgresql_connection",
    default_args=default_args,
    schedule_interval=None, 
    catchup=False,
) as dag:

    test_connection_task = PythonOperator(
        task_id="test_postgresql_connection_task",
        python_callable=test_postgresql,
    )