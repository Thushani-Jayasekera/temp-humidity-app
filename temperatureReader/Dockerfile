FROM python:alpine3.17
WORKDIR /app

COPY ./readings /app/readings
COPY microservice_temp_r.py /app


EXPOSE 8003

ENTRYPOINT ["python", "microservice_temp_r.py"]