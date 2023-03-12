# agri-app-humidity-reader-service

Use below command to build docker image for Humidity Reader Service compatible with RPI
```
docker build --platform=linux/arm/v7 -t dhaura/agri-app-hr:latest -f Dockerfile .
```

Push to the DockerHub repo
```
docker push dhaura/agri-app-hr:latest
```
