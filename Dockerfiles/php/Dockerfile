FROM php:7.4-fpm-alpine

ADD https://github.com/mlocati/docker-php-extension-installer/releases/latest/download/install-php-extensions /usr/local/bin/

RUN chmod +x /usr/local/bin/install-php-extensions && sync && \
    install-php-extensions pgsql pdo_pgsql zip opcache xdebug @composer \
    && echo -e "opcache.memory_consumption=128\n\
    opcache.interned_strings_buffer=8\n\
    opcache.max_accelerated_files=4000\n\
    opcache.revalidate_freq=60\n\
    opcache.enable_cli=1\n\
    opcache.enable=1\n" >> /usr/local/etc/php/conf.d/docker-php-ext-opcache.ini \
    && echo -e "xdebug.mode = debug\n\
    xdebug.client_host = host.docker.internal\n\
    xdebug.start_with_request = yes\n" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini

RUN apk add --update nodejs npm \
    && npm install --global yarn

WORKDIR /var/www/engular