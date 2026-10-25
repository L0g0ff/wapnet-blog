---
_thumbnail_id: "1850"
author: thomasf
categories:
  - hardware
  - linux
  - monitoring
  - security
cover:
  alt: wale
  image: /wp-content/uploads/2020/05/wale.png
date: "2020-05-12T21:49:06+00:00"
guid: https://blog.wapnet.nl/?p=1847
parent_post_id: null
post_id: "1847"
title: Install Pihole on Synology with docker
url: /2020/05/install-pihole-on-synology-with-docker/

---
Unfortunately, there isn't a pihole addon in the Synology package center. But you can build your pihole in a docker container instead :)

The reason you must use docker-compose instead of the Synology docker package itself is that you want to bridge net NIC of your Synology and place the pihole direct in your network. You cannot do this with the GUI.

## The steps:

- Install docker with the package center
- Activate SSH
- Download de image pihole/pihole:latest
- Login with ssh
- type vi docker-compose.yaml
- Paste the content from the docker-compose.yaml example into the vi
- Change the IP adressen to your own network
- Type :wr to save the file
- Type :q to quit vi
- Type "sudo docker-compose up"
- Have fun!

## Docker-compose.yaml Example

```
# Note: 192.168.123.xxx is an example network, you must update all these to match your own.

version: '2'

services:
  pihole:
    container_name: pihole
    image: pihole/pihole:latest
    hostname: pihole
    domainname: localhost             # <-- Update
    mac_address: d0:ca:ab:cd:ef:01
    cap_add:
      - NET_ADMIN
    networks:
      pihole_network:
        ipv4_address: 192.168.123.199   # <-- Update
    dns:
      - 127.0.0.1
      - 1.1.1.1
    ports:
      - 443/tcp
      - 53/tcp
      - 53/udp
      - 67/udp
      - 80/tcp
    environment:
      ServerIP: 192.168.123.199                 # <-- Update (match ipv4_address)
      VIRTUAL_HOST: pihole.localhost            # <-- Update (match hostname + domainname)
      WEBPASSWORD: "justarondompassword"        # <-- Add password (if required)
    restart: unless-stopped

networks:
  pihole_network:
    driver: macvlan
    driver_opts:
      parent: ovs_eth0
    ipam:
      config:
        - subnet: 192.168.123.0/24            # <-- Update
          gateway: 192.168.123.1              # <-- Update
          ip_range: 192.168.123.192/28        # <-- Update
```

When you want to update the docker container, all you have to do is:

s **udo docker-compose down**

and

**sudo docker-compose up**

A good article I used to figure everything out is: [http://tonylawrence.com/posts/unix/synology/free-your-synology-ports/](http://tonylawrence.com/posts/unix/synology/free-your-synology-ports/)
