FROM python:3.8-alpine

RUN apk add hping3 --update-cache --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing

COPY ./slowloris /slowloris
