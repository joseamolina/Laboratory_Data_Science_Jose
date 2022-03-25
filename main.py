from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.S3_hook import S3Hook

def upload_to_s3(filename: str, key: str, bucket_name: str) -> None:
    hook = S3Hook('JMA_connection_S3')
    hook.load_file(filename=filename, key=key, bucket_name=bucket_name)

with DAG(
        dag_id='s3_dag',
        schedule_interval='@daily',
        start_date=datetime(2022, 3, 1),
        catchup=False
) as dag:
    # Upload the file
    task_upload_to_s3 = PythonOperator(
        task_id='upload_to_s3',
        python_callable=upload_to_s3,
        op_kwargs={
            'filename': '/Users/joseangelmolina/PycharmProjects/Laboratory_Data_Science/data/business.csv',
            'key': 'business.csv',
            'bucket_name': 'jmh-af-bucket'
        }
    )