from time import sleep

import redis


TOO_MANY_KEYS_COUNT = 10


r = redis.Redis(host='localhost', port=6379, db=0)


def get_long_value() -> str:
	"""
	Important: with 1mb max memory in redis and such long value only 6 key-values can be set.
	"""
	return 1000 * "some-long-value-goes-here"


def test_base_eviction():
	r.config_set("maxmemory-policy", "allkeys-random")

	r.flushall()

	for i in range(TOO_MANY_KEYS_COUNT):
		r.set(f'key-{i}', get_long_value())

	assert r.dbsize() > 0
	assert r.dbsize() < TOO_MANY_KEYS_COUNT


def test_all_keys_lru():
	r.config_set("maxmemory-policy", "allkeys-lru")

	r.flushall()

	for i in range(100):
		r.set(f'key-{i}', get_long_value())
		r.get(f'key-{i}')
		sleep(0.01)

	assert not r.exists('key-0')
	assert r.exists('key-99')


def test_all_keys_lfu():
	r.config_set("maxmemory-policy", "allkeys-lfu")
	r.config_set("lfu-log-factor", "0")

	r.flushall()

	r.set('often', get_long_value())
	r.set('not-often', get_long_value())

	r.get('not-often')

	for i in range(1000):
		r.get('often')

	for i in range(TOO_MANY_KEYS_COUNT):
		r.set(f'key-{i}', get_long_value())
		r.get(f'key-{i}')

	assert not r.exists('not-often')
	assert r.exists('often')


def test_all_volatile_lru():
	r.config_set("maxmemory-policy", "volatile-lru")

	r.flushall()

	for i in range(100):
		r.set(f'key-{i}', get_long_value(), ex=100)
		r.get(f'key-{i}')
		sleep(0.01)

	assert not r.exists('key-0')
	assert r.exists('key-99')


def test_all_volatile_lfu():
	r.config_set("maxmemory-policy", "volatile-lfu")
	r.config_set("lfu-log-factor", "0")

	r.flushall()

	r.set('often', get_long_value(), ex=100)
	r.set('not-often', get_long_value(), ex=100)

	r.get('not-often')

	for i in range(1000):
		r.get('often')

	for i in range(TOO_MANY_KEYS_COUNT):
		r.set(f'key-{i}', get_long_value(), ex=100)
		r.get(f'key-{i}')

	assert not r.exists('not-often')
	assert r.exists('often')


def test_all_volatile_ttl():
	r.config_set("maxmemory-policy", "volatile-ttl")

	r.flushall()

	r.set('long-lived', get_long_value(), ex=1000)

	for i in range(1, TOO_MANY_KEYS_COUNT):
		r.set(f'key-{i}', get_long_value(), ex=100 * i)
		sleep(0.1)
		r.get(f'key-{i}')

	assert r.exists('long-lived')
	assert not r.exists('key-1')


test_base_eviction()
test_all_keys_lru()
test_all_keys_lfu()
test_all_volatile_lru()
test_all_volatile_lfu()
test_all_volatile_ttl()
