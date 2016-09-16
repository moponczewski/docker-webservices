FROM alpine:latest
MAINTAINER moponczewski "markus@oponczewski.de"

COPY . /app
WORKDIR /app

RUN apk add --update \
		python \
		python-dev \
		py-pip \
		build-base \
	&& pip install -r requirements.txt 


ENTRYPOINT ["python"]
CMD ["date-app.py"]

#RUN apt-get update -y && apt-get install -y \
#    python-pip \
#    python-dev \
#    build-essential \
#    fortunes \
#    cowsay \
#    curl \
#    iputils-ping
# RUN apt-get clean
# RUN pip install -r requirements.txt
