FROM python:slim

# RUN apt-get update && apt-get install pipenv nodejs

WORKDIR /app
ADD requirements.txt /app
RUN pip install -r requirements.txt
