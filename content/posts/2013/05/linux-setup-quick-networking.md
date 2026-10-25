---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
date: "2013-05-21T20:56:09+00:00"
dsq_thread_id: "5366078037"
guid: https://blog.wapnet.nl/?p=1040
parent_post_id: null
post_id: "1040"
title: Linux setup quick networking
url: /2013/05/linux-setup-quick-networking/

---
> ifconfig eth0 192.168.1.222/24 up
>
> route add default gw 192.168.1.1
>
> echo nameserver 8.8.8.8 > /etc/resolv.conf
>
> update-rc.d networking defaults
