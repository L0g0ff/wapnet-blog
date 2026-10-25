---
author: thomasf
categories:
  - linux
  - networking
date: "2020-02-01T17:38:42+00:00"
guid: https://blog.wapnet.nl/?p=1833
parent_post_id: null
post_id: "1833"
title: Create a local TCP port for a remote server on a ubuntu/debian server
url: /2020/02/create-a-local-tcp-port-for-a-remote-server-on-a-ubuntu-debian-server/

---
You can do this stuff with netcat and inetd

apt-get install openbsd-inetd (netcat is installed by default)

nano /etc/inetd.conf

LOCALIP:443 stream tcp nowait root /bin/nc nc REMOTEIP 443

/etc/init.d/openbsd-inetd restart

Have fun!
