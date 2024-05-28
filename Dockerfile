#FROM alpine
#LABEL authors="Herrmandel"

#RUN apk add --no-cache bash

#WORKDIR /classifierApp

#COPY entrypoint.sh .
#RUN chmod +x entrypoint.sh

#ENTRYPOINT ["/classifierApp/entrypoint.sh" ]
#CMD ['run']

FROM ubuntu as builder

FROM python:3.12

LABEL authors="Herrmandel"
LABEL org.opencontainers.image.source=https://github.com/Herrmandela/classifierApp
LABEL org.opencontainers.image.description="ClassifierAPP"
LABEL org.opencontainers.image.licenses=MIT

RUN apt-get update &&\
    apt-get -y install sudo

RUN useradd -ms /bin/bash docker && echo "docker:docker" |chpasswd && adduser docker sudo

#allow sudo w/o password + add sudoies
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER docker

USER root

WORKDIR /home/docker

COPY . .

#RUN brew install python-tk
RUN sudo apt-get install apt-utils
RUN sudo apt-get update && apt-get install -y\
    python3-tk

# pip install dependencies
RUN pip install -- upgrade pip; \
    pip3 install -r requirements.txt

RUN mkdir /.local; mkdir /.local/share; chmod 777 /.local; chmod 777 /.local/share
ADD liveClassifier.py .

ENV DISPLAY=:0

CMD ["python", "./liveClassifier.py"]