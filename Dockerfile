# pull the official base image
FROM python:3.9-alpine

# install bash
RUN apk add --upgrade bash

# create dir
RUN mkdir /app

# set work directory
WORKDIR /app

# set environment variables
# don't create __pycache__/* files
ENV PYTHONDONTWRITEBYTECODE 1

# output straight to terminal
ENV PYTHONUNBUFFERED 1

# copy requirements
COPY ./requirements.txt /app/requirements.txt

# install dependencies
RUN python -m pip install --upgrade pip 
RUN python -m pip install -r requirements.txt
RUN rm requirements.txt

# install server
RUN python -m pip install gunicorn==20.1.0

COPY ./docker-entrypoint.sh ./docker-entrypoint.sh

# make startup script executable
RUN chmod +x docker-entrypoint.sh
EXPOSE 80

# copy project
COPY . .

ENTRYPOINT [ "/bin/bash" ]
CMD [ "docker-entrypoint.sh" ]
