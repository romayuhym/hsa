# Nginx Fine Tuning

## Setup 

```shell
docker-compose up -d
```

## Get image

```shell
curl --location --request GET 'http://127.0.0.1:8080/media/4456190.png'
```

## Refresh image

```shell
curl --location --request GET 'http://127.0.0.1:8080/media/4456190.png' \
--header 'secret-header: true'
```