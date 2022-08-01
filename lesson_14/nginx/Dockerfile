FROM nginx:alpine

RUN apk update \
    && apk upgrade \
    && apk add --no-cache bash

COPY ./iptable.sh /usr/local/bin/iptable.sh
COPY ./nginx.conf /etc/nginx/nginx.conf

RUN chmod +x /usr/local/bin/iptable.sh && apk add --no-cache curl iptables
