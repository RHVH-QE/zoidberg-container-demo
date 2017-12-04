# Container module for zoidberg-ng 

## Build the container in sub-directory "container" under PROJECT DIR
```
docker build -t zoidberg:latest .
```

## Run the test demo with two accessible system(root/redhat) appended
```
python demo.py $system1_ip $system2_ip
```

## See the output logs with the exited container
```
docker ps -a
docker logs $container-id
```
