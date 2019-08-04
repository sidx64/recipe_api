FROM python:3.7-alpine
MAINTAINER sidx64

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

#RUN adduser -D user
#USER user
