---
_edit_last: "1"
author: thomasf
categories:
  - linux
date: "2008-10-06T10:50:30+00:00"
guid: https://blog.wapnet.nl/?p=79
parent_post_id: null
post_id: "79"
title: Linux TCPDump Apache
url: /2008/10/linux-tcpdump-apache/

---
tcpdump "tcp port 80 and (((ip\[2:2\] - ((ip\[0\]&0xf)<<2)) - ((tcp\[12\]&0xf0)>>2)) != 0)"

easier command:

tcpdump -i eth0 not port 22
