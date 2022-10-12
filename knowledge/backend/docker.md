It works on my machine
- files missing
- Version mismatch

Docker: 
- package everything that app needs tor run.
- Run many apps side by side.
- Each app is independent

Virtual machine: Slow, resource-intensive, heavy-weight
Kernel(Inside OS): Manages all applications and hardware resources

DockerHub: registry for docker images. Github for Git. Can push and pull.
A Docker image: a read-only template that contains a set of instructions for creating a container that can run on the Docker platform.


Commands:
Build image first time: `docker build -t hello-docker .`
Show all images: `docker image ls` or `docker images`
Run docker: `docker run hello-docker`
