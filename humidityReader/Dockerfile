FROM python:alpine3.17
WORKDIR /app

COPY microservice_humidity_r.py /app
COPY ./readings /app/readings

EXPOSE 8004

ENTRYPOINT ["python", "microservice_humidity_r.py"]