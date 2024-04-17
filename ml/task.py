from celery import Celery

app = Celery('myapp', broker='redis://localhost:6379/0')

@app.task
def my_task(arg1, arg2):
    # 这里是你的任务代码
    return arg1 + arg2
