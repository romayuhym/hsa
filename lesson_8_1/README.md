# Transactions, Isolations, Locks

## Isolation levels, read phenomena, and locks

### Postgresql

|                  | Dirty reads | Lost updates | Non-repeatable reads | Phantoms |
|------------------|-------------|--------------|----------------------|----------|
| Serializable     | -           | -            | -                    | -        |
| Repeatable Read  | -           | -            | -                    | -        |
| Read Committed   | -           | -            | +                    | +        |
| Read Uncommitted | -           | +            | +                    | +        |

### Percona

https://www.percona.com/blog/2021/02/11/various-types-of-innodb-transaction-isolation-levels-explained-using-terminal/

|                  | Dirty reads | Lost updates | Non-repeatable reads | Phantoms |
|------------------|-------------|--------------|----------------------|----------|
| Serializable     | -           | -            | -                    | -        |
| Repeatable Read  | -           | -            | -                    | +        |
| Read Committed   | -           | -            | +                    | +        |
| Read Uncommitted | +           | +            | +                    | +        |


## Setup

```mysql
create table users(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    age int,
    PRIMARY KEY (id)
) ENGINE=InnoDB;

TRUNCATE users;

INSERT INTO users (id, name, age) VALUES (1, 'Ann', 20);
INSERT INTO users (id, name, age) VALUES (2, 'Tom', 25);

SELECT * FROM users;

SET autocommit=0;

SELECT @@transaction_ISOLATION;

SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
# OR
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
# OR
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
# OR
SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

## Dirty reads

| Transaction 1                       | Transaction 2                           |
|-------------------------------------|-----------------------------------------|
| SELECT age FROM users WHERE id = 1; |                                         |
|                                     | UPDATE users SET age = 21 WHERE id = 1; |
| SELECT age FROM users WHERE id = 1; |                                         |
|                                     | ROLLBACK;                               |

## Lost updates

| Transaction 1                           | Transaction 2                                              |
|-----------------------------------------|------------------------------------------------------------|
|                                         | SET  SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED; |
| UPDATE  users SET age = 40 WHERE id =1; |                                                            |
|                                         | UPDATE  users SET age = 21 WHERE age = 40;                 |

## Non-repeatable reads

| Transaction 1                     | Transaction 2                           |
|-----------------------------------|-----------------------------------------|
| SELECT * FROM users WHERE id = 1; |                                         |
|                                   | UPDATE users SET age = 21 WHERE id = 1; |
|                                   | COMMIT;                                 |
| SELECT * FROM users WHERE id = 1; |                                         |
| COMMIT;                           |                                         |


## Phantom reads

| Transaction 1                                     | Transaction 2                                            |
|---------------------------------------------------|----------------------------------------------------------|
| SELECT  * FROM users WHERE age BETWEEN 10 AND 30; |                                                          |
|                                                   | INSERT INTO users (id, name, age) VALUES (3, 'Bob', 27); |
| SELECT  * FROM users WHERE age BETWEEN 10 AND 30; |                                                          |
| UPDATE users SET age = 28 WHERE id = 3;           |                                                          |
| SELECT  * FROM users WHERE age BETWEEN 10 AND 30; |                                                          |
