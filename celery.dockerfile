FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

ENV APP_ROOT /code
ENV DEBUG False

RUN mkdir /code;
RUN apt-get install gcc

WORKDIR ${APP_ROOT}

RUN mkdir /config
ADD requirements.txt /config/
RUN pip install --no-cache-dir -r /config/requirements.txt

ADD . ${APP_ROOT}