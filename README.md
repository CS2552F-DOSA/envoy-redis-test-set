# envoy_with_redis

## Running 2 instance of redis with Envoy.

```bash
git clone git@github.com:CS2552F-DOSA/envoy_with_redis.git
```



### Run

```bash
cd envoy_with_redis/examples/redis1
docker-compose pull
docker-compose up --build -d

cd envoy_with_redis/examples/redis2
docker-compose pull
docker-compose up --build -d
```

### Test

```bash
$ redis-cli -h localhost -p 1999 set foo foo
OK
$ redis-cli -h localhost -p 1999 set bar bar
OK
$ redis-cli -h localhost -p 1999 get foo
"foo"
$ redis-cli -h localhost -p 1999 get bar
"bar"


$ redis-cli -h localhost -p 1998 set foo foo2
OK
$ redis-cli -h localhost -p 1998 set bar bar2
OK
$ redis-cli -h localhost -p 1998 get foo
"foo2"
$ redis-cli -h localhost -p 1998 get bar
"bar2"
```




### Stop

```bash
cd envoy_with_redis/examples/redis1
docker-compose down

cd envoy_with_redis/examples/redis2
docker-compose down
```


