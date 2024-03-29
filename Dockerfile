# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

EXPOSE 12000
ARG API_KEY
ARG TOKEN
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV API_KEY=${API_KEY} 
ENV TOKEN=${TOKEN}

# Install pip requirements
COPY requirements.txt .

# UPDATE APT-GET
RUN apt-get update

# UPGRADE pip3
RUN pip3 install --upgrade pip

RUN python -m pip install -r requirements.txt

WORKDIR /iabot
COPY . /iabot
#COPY openssl.cnf /etc/ssl/openssl.cnf

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuseriabot && chown -R appuseriabot /iabot
USER appuseriabot

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "./iaBot.py"]
