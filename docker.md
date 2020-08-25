Running DIGITS on Nvidia Docker

    nvidia-docker run -v <path to data>:/data/ -p 5000:5000 nvidia/digits:latest

List all containers (only IDs)

    docker ps -aq

Stop all running containers

    docker stop $(docker ps -aq)

Remove all containers

    docker rm $(docker ps -aq)

Remove all images

    docker rmi $(docker images -q)

Run bash on a container

    docker exec -it 1c76f7912221 /bin/bash
    
List all remote tags:
(https://raw.githubusercontent.com/denilsonsa/small_scripts/master/docker_remote_tags.py)

    python3 docker_remote_tags.py tensorflow/tensorflow
    
