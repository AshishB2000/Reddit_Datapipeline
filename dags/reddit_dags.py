import os
import sys
from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.reddit_pipeline import reddit_pipeline,upload_s3_pipeline

default_args = {
    'owner': 'Ashish B',
    'start_date': datetime(2024, 2, 17)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline']
)

# extraction from reddit
extract = PythonOperator(
    task_id='reddit_extraction',
    python_callable=reddit_pipeline,
    op_kwargs={
        'file_name': f'reddit_{file_postfix}',
        'subreddit': 'aapl',
        'time_filter': 'year',
    },
    dag=dag
)


#upload to s3

upload_s3 = PythonOperator(
    task_id='s3_upload',
    python_callable=upload_s3_pipeline,
    dag=dag
)

extract >> upload_s3

#'comment_limit': 2048,
# 'comment_sort': 'confidence',
# '_reddit': <praw.reddit.Reddit object at 0x7f042835b3d0>,
# 'approved_at_utc': None, 'subreddit': Subreddit(display_name='AAPL'),
# 'selftext': 'The shareholder of Apple, Warren Buffett as well as Charlie Munger (RIP) , are not favoring Apple getting into Auto business citing low profit margin and tough completion. That could be one of the reasons why Apple car is still not out yet! That is just my thought!',
# 'author_fullname': 't2_vtdjli34',
# 'saved': False,
# 'mod_reason_title': None,
# 'gilded': 0, 'clicked': False,
# 'title': 'Apple getting to Auto business. Warren Buffet effect',
# 'link_flair_richtext': [],
# 'subreddit_name_prefixed': 'r/AAPL', 'hidden': F