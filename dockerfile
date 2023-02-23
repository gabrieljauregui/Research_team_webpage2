# base image
FROM python:3.12-rc-slim-buster

# set working directory
WORKDIR /Research_team_project

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get -y install postgresql \
    && apt-get -y install python3-dev \
    && apt-get -y install libpq-dev \
    && apt-get clean

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . /django_project

# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]
 