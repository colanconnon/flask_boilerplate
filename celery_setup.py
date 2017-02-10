from celery import Celery
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


CELERY_TASK_LIST = [
    'tasks.async.add_numbers'
]

celery = Celery("tasks", backend=os.environ.get('CELERY_RESULT_BACKEND'),
                broker=os.environ.get('CELERY_BROKER_URL'), include=CELERY_TASK_LIST)


if __name__ == "__main__":
    celery.start()