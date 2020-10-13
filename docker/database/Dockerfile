FROM mysql:latest as setup-stage

LABEL maintainer="c@carterlandis.com"
LABEL version="0.1.0"

ENV MYSQL_ROOT_PASSWORD "th2020adminpassword"
ENV MYSQL_DATABASE "tigerhacks_api"
ENV MYSQL_PASSWORD "th2020adminpassword"
ENV MYSQL_USER "th2020admin"

FROM setup-stage as generate-schema

COPY ./schema/ /docker-entrypoint-initdb.d/

EXPOSE 3306