#FROM alpine
#LABEL authors="Herrmandel"

#RUN apk add --no-cache bash

#WORKDIR /classifierApp

#COPY entrypoint.sh .
#RUN chmod +x entrypoint.sh

#ENTRYPOINT ["/classifierApp/entrypoint.sh" ]
#CMD ['run']

FROM python:3.12
LABEL authors="Herrmandel"

ADD liveClassifier.py .

#RUN brew install python-tk
RUN pip3 install SpeechRecognition numpy transformers torch tensorflow

CMD ["python", "./liveClassifier.py"]