FROM python:slim

# RUN apt-get update && apt-get install pipenv nodejs

RUN pip install django django-3-jet django-tailwind requests bs4
