FROM alpine
LABEL authors="Herrmandel"

RUN apk add --no-cache bash

WORKDIR /classifierApp

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/classifierApp/entrypoint.sh" ]
CMD ['run']