---
_thumbnail_id: "1850"
author: thomasf
categories:
  - docker
cover:
  alt: wale
  image: /wp-content/uploads/2020/05/wale.png
date: "2021-09-15T06:55:46+00:00"
guid: https://blog.wapnet.nl/?p=1934
parent_post_id: null
post_id: "1934"
title: Some useful docker commands
url: /2021/09/some-useful-docker-commands/

---
Attach to a container

```
docker exec -i -t container_name /bin/bash
```

List images

```
docker image ls
```

List all existing containers

```
docker ps -a
```

Delete a image

```
docker image rm image_name
```

Delete all images

```
docker image rm $(docker images -a -q)
```

Stop a container

```
docker stop container_name
```

Stop all running containers

```
docker stop $(sudo docker ps -a -q)
```

Delete a container

```
docker rm container_name
```

Delete all containers

```
docker rm $(docker ps -a -q)
```

Display logs of a container

```
docker logs container_name
```
