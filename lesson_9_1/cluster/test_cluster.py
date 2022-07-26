import redis

r_m = redis.Redis(host='localhost', port=6379, db=0)
r_s = redis.Redis(host='localhost', port=6370, db=0)

DATA_TO_REDIS = "data_to_redis"


def test_cluster():
    r_m.set("key", DATA_TO_REDIS)

    assert r_m.exists("key")
    assert r_s.exists("key")
    assert r_m.get("key") == r_s.get("key")

    r_m.delete("key")

    assert not r_m.exists("key")
    assert not r_s.exists("key")
