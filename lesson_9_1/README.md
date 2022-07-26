## Keys Eviction

File redis.conf sets max memory to 1mb.

Tests to check eviction policies in file ``./keys-eviction/test_keys_eviction.py``

```
============================= test session starts ==============================
collecting ... collected 6 items

test_keys_eviction.py::test_base_eviction PASSED                         [ 16%]
test_keys_eviction.py::test_all_keys_lru PASSED                          [ 33%]
test_keys_eviction.py::test_all_keys_lfu PASSED                          [ 50%]
test_keys_eviction.py::test_all_volatile_lru PASSED                      [ 66%]
test_keys_eviction.py::test_all_volatile_lfu PASSED                      [ 83%]
test_keys_eviction.py::test_all_volatile_ttl PASSED                      [100%]

============================== 6 passed in 10.78s ==============================
```

## Redis Cluster

Tests to check cluster in file ``./cluster/test_cluster.py``

```
============================= test session starts ==============================
collecting ... collected 1 item

test_cluster.py::test_cluster PASSED                                     [100%]

============================== 1 passed in 0.07s ===============================
```