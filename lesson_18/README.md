# Lesson 18

## Master

``` sql
CREATE USER 'slave'@'%' IDENTIFIED BY 'password';
GRANT REPLICATION SLAVE ON *.* TO 'slave'@'%';
FLUSH PRIVILEGES;

USE mydb;
FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
UNLOCK TABLES;

create table customers(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    address varchar(255),
    age int,
    PRIMARY KEY (id)
);
```

## Database dump

```shell
docker exec -i mysql_m mysqldump -u root -p111 mydb > mydb.sql
docker exec -i mysql_s1 mysql -u root -p111 mydb < ./mydb.sql
```

## Slave

``` sql
CHANGE MASTER TO MASTER_HOST='172.22.0.2', MASTER_USER='slave',
MASTER_PASSWORD='password',MASTER_LOG_FILE = 'mysql-bin-master.000005',
MASTER_LOG_POS = 1413;
START SLAVE;
SHOW SLAVE STATUS;
```

### Troubleshooting

Authentication plugin 'caching_sha2_password' reported error:Authentication require secure connection
```shell
mysql -u slave -ppassword -h 172.22.0.2 -P3306 --get-server-public-key
```

## Try to turn off mysql-s1

After stopping mysql_s1, mysql_s2 stopped synchronizing data with error.
```
Relay log read failure: Could not parse relay log event entry. 
The possible reasons are: the master's binary log is corrupted 
(you can check this by running 'mysqlbinlog' on the binary log), 
the slave's relay log is corrupted (you can check this by running 
'mysqlbinlog' on the relay log), a network problem, the server was 
unable to fetch a keyring key required to open an encrypted relay 
log file, or a bug in the master's or slave's MySQL code. If you 
want to check the master's binary log or slave's relay log, you 
will be able to know their names by issuing 'SHOW SLAVE STATUS' 
on this slave.
```
After starting mysql_s1 - the data started to be synchronized on mysql_s1. 
mysql_s2 was still in error. After restarting mysql_s2, the data began to 
synchronize on mysql_s2.

## Try to remove a column in  database on slave node

If remove last column all right.
If remove not the last column - the replica stops synchronizing data with error:
```
Coordinator stopped because there were error(s) in the worker(s). 
The most recent failure being: Worker 1 failed executing transaction 
'ANONYMOUS' at master log mysql-bin-master.000006, end_log_pos 28227746. 
See error log and/or performance_schema.replication_applier_status_by_worker 
table for more details about this failure or others, if any.
```
