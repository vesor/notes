Docker image compaitbility

    https://www.redhat.com/en/resources/container-image-host-guide-technology-detail



List all containers (only IDs)

    docker ps -aq

Stop all running containers

    docker stop $(docker ps -aq)

Remove all containers

    docker rm $(docker ps -aq)

Remove all images

    docker rmi $(docker images -q)

Run a container

    docker run -it --runtime=nvidia --rm tensorflow/tensorflow:1.13.1-gpu-py3
    docker run -itd --runtime=nvidia --rm -v /some/host/folder:/folder/in/container tensorflow/tensorflow:1.13.1-gpu-py3
    
    # -it means iteractive, -d means detach, --rm means remove after stop, -v maps folder with host
    # --runtime=nvidia is needed for nvidia-docker
    
    # create a new bash terminal of some running container
    docker exec -it <container id> /bin/bash

Commit container to some image:

    docker commit <container id> <image name> 

Docker for cuda:

If not using nvidia official docker.    
See https://github.com/NVIDIA/nvidia-docker/wiki/Usage#non-cuda-image    

Dockerfile:
    
    FROM your_image:latest
    ENV NVIDIA_VISIBLE_DEVICES all
    ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

Build new docker image:

    docker build --tag your_docker_name:your_tag .
    
    
List all remote tags:
(https://raw.githubusercontent.com/denilsonsa/small_scripts/master/docker_remote_tags.py)

    python3 docker_remote_tags.py tensorflow/tensorflow
    


