# Two options: normal redis client and asyncio-redis

REDIS_HOST = "redis-proxy"
REDIS_TEST_HOST = "frontend-client-proxy:9911"

REDIS_PORT = "1999"
REDIS_TEST_PORT = "1999"

# Normal redis client
# Referring to https://redislabs.com/lp/python-redis/

import redis
import os
import time

# HOST = os.getenv('CLIENT_PROXY', "http://localhost:9001")

# print("client\n___________")
# print(HOST)

# HOST += "/"
# print("HOST: ", HOST)

print("\n************* client begin *************\n")

r = redis.Redis(
    host= REDIS_HOST,
    port= REDIS_PORT)
print("set foo in redis, foo -> bar redis")
r.set('foo', 'bar redis')
value = r.get('foo')
print("getted value for foo in redis: ", value)
print("\n\n")

print("---------------------------------------------")
time.sleep(0.5)

r_test = redis.Redis(
    host= REDIS_TEST_HOST,
    port= REDIS_TEST_PORT)
print("set foo in redis-test, foo -> bar redis-test")
r_test.set('foo', 'bar redis-test')
value = r_test.get('foo')
print("getted value for foo in redis: ", value)



print("\n************* client end *************\n")
time.sleep(0.5)