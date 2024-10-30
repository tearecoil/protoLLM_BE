# # Dockerfile

# # pull the official docker image
# FROM python:3.12.3

# # set work directory
# WORKDIR /app

# # set env variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # install dependencies
# # COPY ./requirements.txt /app/requirements.txt
# # RUN pip install -r /app/requirements.txt
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # copy project
# # COPY ./src/ /app/src
# COPY . .
# #expose the port
# EXPOSE 8000

#DOCKER FILE COPIED
# start from python base image
FROM python:3.12.3

# change working directory
WORKDIR /code

# add requirements file to image
COPY ./requirements.txt /code/requirements.txt

# install python libraries
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# add python code
COPY ./src/ /code/src/

# specify default commands
CMD ["fastapi", "run", "src/main.py", "--port", "80"]