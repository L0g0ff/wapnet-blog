---
author: thomasf
categories:
  - firefox
  - linux
  - networking
date: "2022-09-18T19:13:06+00:00"
guid: https://blog.wapnet.nl/?p=2072
parent_post_id: null
post_id: "2072"
title: Use TOR proxy with any linux command
url: /2022/09/use-tor-proxy-with-any-linux-command/

---
There is an easy way to use the The Onion Router for any command under linux

First install TOR and proxychains4

```
$ sudo apt install tor proxychains4
```

You can configure proxychains.conf but the default config is good :)

```
$ sudo nano /etc/proxychains.conf
```

Then start the tor service

```
$ sudo systemctl start tor
```

And check your ip:

```
$ proxychains4 curl ifconfig.me
```

You can use any command you want. So if you want your firefox browser over tor:

```
$ proxychains4 firefox
```

To refresh your TOR IP simply restart the TOR service

Happy proxying :)
