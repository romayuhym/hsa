# Balancing

Request from US

```json
{"heder":"US","hello":"world","server":"US2"}
{"heder":"US","hello":"world","server":"US1"}
```

Request from US server us1 and us2 down

```json
{"heder":"US","hello":"world","server":"BACKUP"}
```

Request from Ukraine

```json
{"heder":"UA","hello":"world","server":"UK"}
```

Request from Ukraine server uk down

```json
{"heder":"UA","hello":"world","server":"BACKUP"}
```

Request from Germany

```json
{"heder":"DE","hello":"world","server":"REST"}
```

Request from Ukraine server rest down

```json
{"heder":"DE","hello":"world","server":"BACKUP"}
```
