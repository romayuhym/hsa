import json
import random
import time
from math import log

import redis as redis
from playhouse.shortcuts import model_to_dict

from db import Books

TTL = 50
BETA = 1

r = redis.Redis(host="127.0.0.1", port=6379, db=0)


def read(key):
    pipeline = r.pipeline()
    pipeline.get(key)
    pipeline.get(f"{key}_delta")
    pipeline.ttl(key)
    return pipeline.execute()


def write(key, value, delta):
    value = json.dumps(value)
    pipeline = r.pipeline()
    pipeline.set(key, value, TTL)
    pipeline.set(f"{key}_delta", delta, TTL)
    pipeline.execute()


def xfetch(delta, ttl):
    now = time.time()
    expiry = now + ttl
    x_fetch = float(delta) * BETA * log(random.uniform(0, 1))

    return (now - x_fetch) >= expiry


def recompute(key):
    start = time.time()
    value = get_db(key)
    delta = time.time() - start
    write(key, value, delta)
    return value


def get_xfetch(key):
    value, delta, expiry = read(key)

    if not value or xfetch(delta, expiry):
        return recompute(key)

    return value


def get_db(key):
    time.sleep(random.uniform(0.3, 1))  # emulate slow queries
    return model_to_dict(Books.get_or_none(year=key))


def get_simple_cache(key):
    value = r.get(key)

    if not value:
        value = get_db(key)
        r.set(key, json.dumps(value), TTL)

    return value
