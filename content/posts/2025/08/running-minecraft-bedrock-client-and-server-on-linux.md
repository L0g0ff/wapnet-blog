---
_thumbnail_id: "2253"
author: thomasf
categories:
  - android
  - linux
cover:
  alt: minecraft
  image: /wp-content/uploads/2025/08/minecraft.jpg
date: "2025-08-22T21:09:12+00:00"
guid: https://blog.wapnet.nl/?p=2252
parent_post_id: null
post_id: "2252"
title: Running Minecraft Bedrock Client and Server on Linux
url: /2025/08/running-minecraft-bedrock-client-and-server-on-linux/

---
Running a local Minecraft Bedrock server on Linux is perfect for playing with your kids on the same network. Minecraft Bedrock is incredibly fun for family gaming sessions, and setting up your own server gives you complete control over the experience.

## Setting Up the Server

Use the excellent `itzg/minecraft-bedrock-server` Docker container. Create a folder e.g. minecraft and in that folder the file `docker-compose.yml`:

```
services:
  bds:
    image: itzg/minecraft-bedrock-server
    environment:
      EULA: "TRUE"
    ports:
      - "19132:19132/udp"
    volumes:
      - ./data:/data
    stdin_open: true
    tty: true

```

Then create a folder **data** and start your server with:

```
docker compose up -d

```

## Installing the Client

Install the Minecraft client using Flatpak:

```
flatpak install io.mrarm.mcpelauncher

```

**Note**: You'll need a paid Microsoft/Mojang Android version.

## Adding Custom Maps

Download amazing community maps from [CurseForge](https://www.curseforge.com/minecraft-bedrock/maps/). These come as `.mcworld` files.

To install a map:

1. **Extract the world**: Rename `.mcworld` to `.zip` and unzip it in `data/worlds/`
1. **Configure the server**: Edit `data/server.properties` and set the level name. For example: `level-name=Island Survival with 30 Trial Chambers`
1. **Restart**: `docker compose restart`

The world folder name must match exactly what you put in `level-name`.

## Connect and Play

Your server will be discoverable in the "LAN Games" section of Minecraft Bedrock. Kids can easily join from tablets, phones, or other computers on your network.

This setup is perfect for controlled, family-friendly gaming where you have full control over the world and can enjoy quality time together exploring amazing community-created maps!

Happy gaming :)
