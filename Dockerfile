# pull the official base image
FROM python:3.9.7

# set work directory
WORKDIR /app

# set environment variables
# don't create __pycache__/* files
ENV PYTHONDONTWRITEBYTECODE 1

# output straight to terminal
ENV PYTHONUNBUFFERED 1

# copy project
COPY . /app

# install dependencies
RUN python -m pip install --upgrade pip 
RUN python -m pip install -r requirements.txt

# install server
RUN python -m pip install gunicorn==20.1.0

# make startup script executable
RUN chmod +x start_docker.sh
EXPOSE 80

CMD ["./start_docker.sh"]
