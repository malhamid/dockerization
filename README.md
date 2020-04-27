# A simple example of how to dockerize a Python microservice

### To build the docker image: 
docker build -t app/echo-service:1.0 .

### To run the docker image: 
docker run -p 8000:8080 app/echo-service:1.0

