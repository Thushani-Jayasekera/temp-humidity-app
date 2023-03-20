FROM python:alpine3.17

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8002

ENTRYPOINT ["python", "app.py"]