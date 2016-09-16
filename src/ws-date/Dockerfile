FROM alpine:latest
MAINTAINER moponczewski

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
