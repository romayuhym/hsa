import random
from datetime import date

import greenstalk
import redis
from fastapi import FastAPI


app = FastAPI()

r = redis.Redis(host='localhost', port=6379, db=0)  # redis-aof
# r = redis.Redis(host='localhost', port=6378, db=0)  # redis-rdb


@app.get("/write")
def write():
    data = date.fromtimestamp(random.randint(0, 1658991804)).strftime('%Y-%m-%d')
    r.rpush("queue", data)

    # with greenstalk.Client(('localhost', 11300)) as beanstalkd:
    #     beanstalkd.put(data)
    return "success"


@app.get("/read")
def read():
    resp = r.blpop("queue", 30)

    # with greenstalk.Client(('localhost', 11300)) as beanstalkd:
    #     job = beanstalkd.reserve()
    #     resp = job.body
    #     beanstalkd.delete(job)

    return resp[0]
