FROM ubuntu:latest
MAINTAINER moponczewski
RUN apt-get update -y && apt-get install -y \
    python-pip \
    python-dev \
    build-essential \
    fortunes \
    cowsay \
    curl \
    iputils-ping

RUN apt-get clean

COPY ./docker.cow /usr/share/cowsay/cows

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]

CMD ["cow-app.py"]
