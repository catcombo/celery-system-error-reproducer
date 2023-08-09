import random
from time import sleep

from celery import Celery

app = Celery("demo")

app.conf.broker_url = "rediss://default:MegaTest@redis:6379/0?ssl_cert_reqs=none"
app.conf.result_backend = "rediss://default:MegaTest@redis:6379/0?ssl_cert_reqs=none"


@app.task
def add(a, b):
    sleep(random.random() * 2)
    return a + b
