# agri-app-user-app-service

Use below command to build docker image for Humidity User App Service compatible with RPI
```
docker build --platform=linux/arm/v7 -t dhaura/agri-app-ua:latest -f Dockerfile .
```

Push to the DockerHub repo
```
docker push dhaura/agri-app-ua:latest
```
