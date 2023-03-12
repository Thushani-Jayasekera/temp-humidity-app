FROM python:alpine3.17

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8001

ENTRYPOINT ["python", "app.py"]