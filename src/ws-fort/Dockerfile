FROM alpine:latest
MAINTAINER moponczewski "markus@oponczewski.de"

COPY . /app
WORKDIR /app

RUN apk add --update \
		python \
		python-dev \
		py-pip \
		build-base \
		fortune \
	&& pip install -r requirements.txt 


ENTRYPOINT ["python"]
CMD ["date-app.py"]
