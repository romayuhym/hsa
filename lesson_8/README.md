# Индексы в InnoDB

## Setup

```mysql
CREATE TABLE customers
(
    id       int auto_increment,
    date_of_birth date not null,
    constraint data_pk primary key (id)
) ENGINE = InnoDB;

SELECT count(`id`) from `customers` where `date_of_birth` = '1997-01-13';
SELECT count(`id`) from `customers` where `date_of_birth` < '1997-01-13';
SELECT count(`id`) from `customers` where `date_of_birth` >= '1997-01-13' AND `date_of_birth` <= '2004-06-26';

CREATE INDEX users_birthday ON customers (date_of_birth) USING BTREE;
CREATE INDEX users_birthday_hash ON customers (date_of_birth) USING HASH;

SET GLOBAL innodb_flush_log_at_trx_commit = 2;
```

## Compare SELECT performance using different index

|                                                                                                                  | Without index | BTREE index | HASH index |
|------------------------------------------------------------------------------------------------------------------|---------------|-------------|------------|
| SELECT count(`id`) from `customers`  where `date_of_birth` = '1997-01-13';                                       | 11 s 966 ms   | 70 ms       | 74 ms      |
| SELECT count(`id`) from `customers`  where `date_of_birth` < '1997-01-13';                                       | 8 s 477 ms    | 5 s 943 ms  | 4 s 954 ms |
| SELECT count(`id`) from `customers`  where `date_of_birth` >= '1997-01-13'  AND `date_of_birth` <= '2004-06-2’6; | 12 s 884 ms   | 2 s 190 ms  | 1 s 434 ms |

## Compare INSERT performance using different innodb_flush_log_at_trx_commit value

```shell
siege -c100 -t30s http://localhost:8000/
```

|   | 10                  | 25                 | 50                 | 100                |
|---|---------------------|--------------------|--------------------|--------------------|
| 0 | Response time: 0.07 | Response time:0.17 | Response time:0.32 | Response time:0.51 |
| 1 | Response time:0.08  | Response time:0.18 | Response time:0.33 | Response time:0.64 |
| 2 | Response time:0.07  | Response time:0.16 | Response time:0.27 | Response time:0.55 |