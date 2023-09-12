FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

ENV APP_ROOT /code
ENV DEBUG False

RUN mkdir /code;
RUN apt-get update && \
    apt-get install -y \
        unzip \
        libglib2.0-0 \
        libnss3 \
        libgconf-2-4 \
        libfontconfig \
        wget \
        gnupg \
        gcc && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    wget -O /tmp/chromedriver-linux64.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip && \
    unzip /tmp/chromedriver-linux64.zip chromedriver-linux64/chromedriver -d /usr/local/bin/ && \
    rm /tmp/chromedriver-linux64.zip && \
    chmod +x /usr/local/bin/chromedriver-linux64/chromedriver

WORKDIR ${APP_ROOT}

RUN mkdir /config
ADD requirements.txt /config/
RUN pip install --no-cache-dir -r /config/requirements.txt

ADD . ${APP_ROOT}