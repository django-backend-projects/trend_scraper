FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

ADD requirements.txt /requirements.txt

RUN apt-get update && \
    apt-get install -y \
        libglib2.0-0 \
        libnss3 \
        libgconf-2-4 \
        libfontconfig

RUN pip install virtualenvwrapper
RUN python3 -m venv /venv
RUN /venv/bin/pip install -U pip
RUN /venv/bin/pip install --no-cache-dir -r /requirements.txt
