FROM ubuntu:latest

# install python and  psycopg2 dependencies
RUN apt-get update
RUN apt-get upgrade -y \
 && apt-get install -y python3 python3-pip

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./eastwood /srv/www/eastwood
WORKDIR /srv/www/eastwood

RUN pip3 install -r requirements.txt