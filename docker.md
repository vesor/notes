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
    
