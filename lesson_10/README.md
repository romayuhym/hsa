# Queues

```shell
siege -c100 -t30S http://localhost:8000/write
siege -c100 -t30S http://localhost:8000/read
```

## Compare

|            | write            | read             |
|------------|------------------|------------------|
| redis-rdb  | 734.66 trans/sec | 752.31 trans/sec |
| redis-aof  | 857.02 trans/sec | 879.14 trans/sec |
| beanstalkd | 666.71 trans/sec | 553.05 trans/sec |
