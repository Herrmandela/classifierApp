FROM alpine
LABEL authors="Herrmandel"

RUN apk add --no-cache bash


COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

ENTRYPOINT ["entrypoint.sh" ]