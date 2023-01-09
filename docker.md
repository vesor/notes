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
    

## x11docker

Run official ubuntu:18.04 docker, then apt install ubuntu-desktop. Commit docker as my_docker, then exit.

    ./x11docker --sudouser -- "--privileged -v /media/data:/media/data -v /media/weizhe/carlab:/media/weizhe/carlab" my_docker:18.04 xterm

    NOTE: "--sudouser" to fix "sudo" error (you still need to apt install sudo first)
    "--privileged" to fix "permission denied" error even use sudo.
    use "xterm" instead of "gnome-terminal" because "gnome-terminal" seems not compatible.

    ./x11docker --sudouser --clipboard --hostdisplay -- "--privileged -v /media/data:/media/data -v /media/weizhe/carlab:/media/weizhe/carlab --network none" my_docker:18.04 xterm
    
    NOTE: "--clipboard" to allow share clipboard
    "--hostdisplay" to use host xwindow display directly
    "--network none" to prevent docker access network


## docker shell can't display chinese

docker exec -it b18f56aa1e15 env LANG=C.UTF-8 /bin/bash 

## docker for remote debug

https://zhuanlan.zhihu.com/p/80099904

## connect to remote docker in vscode (better than using ssh server in docker)

create tunnel to remote docker daemon:

ssh -NL localhost:23750:/var/run/docker.sock username@remote_server

then tell vscode by modify docker.host in settings:

tcp://localhost:23750

install vscode docker extension, then you can see docker containers


## find docker container by host PID

    pstree -sg <PID>

    docker ps -q | xargs docker inspect --format '{{.State.Pid}}, {{.Name}}' | grep "^%PID%"

