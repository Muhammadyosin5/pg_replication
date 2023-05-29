FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV MYPATH=/home/app/code
RUN apk add --update py-pip

WORKDIR $MYPATH
# RUN pip install -r requirements.txt
RUN pip install fastapi uvicorn psycopg2-binary
COPY . $MYPATH


EXPOSE 8000