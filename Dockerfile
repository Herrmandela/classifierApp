FROM python:3.12
LABEL authors="Herrmandel"

RUN apk add --no-cache bash

WORKDIR /classifierApp

COPY entrypoint.sh .
RUN chmod +x liveClassifier.py

ENTRYPOINT ["/classifierApp/liveClassifier.py" ]
CMD ['run']