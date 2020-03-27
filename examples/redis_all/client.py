# Two options: normal redis client and asyncio-redis

REDIS_HOST = "localhost:9911/redis/prod"
REDIS_TEST_HOST = "localhost:9911/redis/test"

REDIS_PORT = "1999"
REDIS_TEST_PORT = "1998"

# Normal redis client
# Referring to https://redislabs.com/lp/python-redis/

import redis
import os

HOST = os.getenv('CLIENT_PROXY', "http://localhost:9001")

print("client\n___________")
print(HOST)

HOST += "/"
print("HOST: ", HOST)

r = redis.Redis(
    host= HOST,
    port= REDIS_PORT)

r.set('foo', 'bar hello')
value = r.get('foo')
print(value)