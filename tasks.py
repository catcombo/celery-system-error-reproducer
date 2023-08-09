from celery import Celery

app = Celery("demo", backend="redis://redis", broker="redis://redis")


@app.task
def add(a, b):
    return a + b
