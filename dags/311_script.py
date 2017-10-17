from airflow import DAG
from airflow.operators import BashOperator, PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2015, 6, 1),
    'email': ['airflow@airflow.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}


def download_311_data_timespan(**kwargs):
    from urllib.request import urlretrieve
    from urllib.parse import urlencode 

    import os

    date = kwargs['ds']
    date_p1 = kwargs['tomorrow_ds']
    
    app_token = 'UhYBPxP8ppGh3T6JjgDBhj2MC'
    base_url = 'https://data.cityofnewyork.us/resource/fhrw-4uyv.csv?' #$$app_token={}&$where= created_date between \'{}\' and \'{}\''.format(app_token,date,date_p1)
    filename = date+'_311_delta.csv'
    tmp_daily_files ='311_deltas'
    
    if not os.path.exists(tmp_daily_files):
        os.mkdir(tmp_daily_files)
    query = {
        "$$app_token": app_token,
        "$where" : 'created_date between \'{}\' and \'{}\''.format(date,date_p1)
    }
    urlretrieve(base_url+urlencode(query),tmp_daily_files+'/'+filename)     
    return True


def clean_zips():
    print('running clean data')
    return None


def updateDatabase():
    return None 


dag = DAG('311_workflow', default_args=default_args, schedule_interval=timedelta(1))

get_311_data = PythonOperator(
    task_id = 'get_311_data',
    python_callable = download_311_data_timespan,
    provide_context = True,
    dag=dag
)

clean_311_data = PythonOperator(
    task_id = 'clean_data',
    python_callable  = clean_data,
    dag=dag
)

clean_311_data.set_upstream(get_311_data)







