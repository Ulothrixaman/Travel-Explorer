FROM ubuntu:latest

RUN sudo apt update


#Install python3.10
RUN apt-get install -y python3.10 python3.10-dev python-pip

#Create app dire
WORKDIR /app

#Install Project Dependencies
RUN pip3 install --no-cache-dir

# Copy packages
