FROM ubuntu:latest
MAINTAINER moponczewski "markus@oponczewski.de"
RUN apt-get update -y && apt-get install -y \
    python-pip \
    python-dev \
    build-essential \
    fortunes \
    cowsay \
    curl \
    iputils-ping

RUN apt-get clean

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]

CMD ["fort-app.py"]
