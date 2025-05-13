## Docker architecture

Docker uses a client-server architecture. The Docker talks to the Docker daemon which does the heavy lifting od builing, running and distributing you Docker containers.

![image](../images/docker-architecture.webp) <br>


### The Docker daemon
The Docker daemon `(dockerd)` listens for Docker API requests and manages Docker objects such as images containers networks and volumes A daemon can also communicate with other daemons to manage Docker services


### The Docker client
The Docker client `(docker)` is the primary way that many Docker userse interact with Docker. When you use commands such as `docker run` the client sends these commands to `dockerd`, which carries them out. The docker command uses the Docker API The Docker client can communicate with more than one daemon


### Docker registeries
A Docker registery stores Docker iamges. Docker Hub is a public registert that anyone can use, and Docker loolks for images on Docker Hub by default You can even run your own private registery.


### Docker Images
An imags is a read-only template with instruction for creating a Docker container. Often an image is based on another image, with some additional customization.


### Docker Container
A container is a runnable instance of an image. You can create start stop move delete a container using Docker API of CLI 


### Install Docker

1. Install Docker
2. run this command

```bash
sudo docker run -d -p 8080:80 docker/welcome-to-docker 
```