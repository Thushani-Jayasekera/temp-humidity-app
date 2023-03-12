# agri-app-temperature-reader-service

Use below command to build docker image for Temperature Reader Service compatible with RPI
```
docker build --platform=linux/arm/v7 -t dhaura/agri-app-tr:latest -f Dockerfile .
```

Push to the DockerHub repo
```
docker push dhaura/agri-app-tr:latest
```
