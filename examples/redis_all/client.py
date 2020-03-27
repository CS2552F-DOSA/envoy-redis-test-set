# Two options: normal redis client and asyncio-redis

REDIS_HOST = "localhost"
REDIS_TEST_HOST = "localhost"

REDIS_PORT = ""
REDIS_TEST_PORT = ""

# Normal redis client
# Referring to https://redislabs.com/lp/python-redis/

import redis

r = redis.Redis(
    host='localhost',
    port="1998")

r.set('foo', 'bar hello')
value = r.get('foo')
print(value)