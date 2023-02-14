FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

#ENV C_FORCE_ROOT true

#ENV APP_USER myapp
ENV APP_ROOT /code
ENV DEBUG True

RUN mkdir /code;

WORKDIR ${APP_ROOT}

RUN mkdir /config
ADD requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#USER ${APP_USER}
ADD . ${APP_ROOT}
