FROM python:3.6
MAINTAINER Yann Piquet <yann.piquet@epitech.eu>

COPY src/requirements.txt /requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

ADD src /app
WORKDIR /app

ENV PYTHONUNBUFFERED True

EXPOSE 8887

CMD gunicorn -w 1 --threads 1 -b 0.0.0.0:8887 wsgi