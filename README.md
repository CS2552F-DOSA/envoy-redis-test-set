# envoy_with_redis

## Running 2 instance of redis with Envoy.

```bash
git clone git@github.com:CS2552F-DOSA/envoy_with_redis.git
```



### Run redis prod and redis test

```bash
# Run redis prod with envoy
cd envoy_with_redis/examples/redis
docker-compose pull
docker-compose up --build -d

# Run redis test with envoy
cd ../redis-test
docker-compose pull
docker-compose up --build -d
```

### Test the connectivity for redis test and redis prod

```bash
# Test for redis prod with envoy
$ redis-cli -h localhost -p 1999 set foo foo
OK
$ redis-cli -h localhost -p 1999 set bar bar
OK
$ redis-cli -h localhost -p 1999 get foo
"foo"
$ redis-cli -h localhost -p 1999 get bar
"bar"

# Test for redis test with envoy
$ redis-cli -h localhost -p 1998 set foo foo-test
OK
$ redis-cli -h localhost -p 1998 set bar bar-test
OK
$ redis-cli -h localhost -p 1998 get foo
"foo-test"
$ redis-cli -h localhost -p 1998 get bar
"bar-test"
```




### Stop redis prod and redis test

```bash
# Stop redis prod with envoy
cd ../redis
docker-compose down

# Stop redis test with envoy
cd ../redis-test
docker-compose down
```


