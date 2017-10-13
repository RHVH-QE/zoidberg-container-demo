# Container module for rhvh-auto-ng

## Build the container in sub-directory "container" under PROJECT DIR
```
docker build -t rhvh-auto-ng:latest .
```

## Run the test demo
```
python demo.py
```

## See the output logs with the exited container
```
docker ps -a
docker logs $container-id
```
