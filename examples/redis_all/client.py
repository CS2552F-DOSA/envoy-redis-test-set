# Two options: normal redis client and asyncio-redis

REDIS_HOST = "frontend-client-proxy"
REDIS_TEST_HOST = "frontend-client-proxy"

REDIS_PORT = "9911"
REDIS_TEST_PORT = "9911"

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
r.set('redis:foo', 'bar redis')
value = r.get('redis:foo')
print("getted value for foo in redis: ", value)
print("\n\n")

print("---------------------------------------------")
time.sleep(0.5)

r_test = redis.Redis(
    host= REDIS_TEST_HOST,
    port= REDIS_TEST_PORT)
print("set foo in redis-test, foo -> bar redis-test")
r_test.set('redis-test:foo', 'bar redis-test')
value = r_test.get('redis-test:foo')
print("getted value for foo in redis: ", value)



print("\n************* client end *************\n")
time.sleep(0.5)