---
_edit_last: "1"
author: thomasf
categories:
  - linux
date: "2008-09-18T08:34:08+00:00"
guid: https://blog.wapnet.nl/?p=43
parent_post_id: null
post_id: "43"
title: Mount FreeBSD disk in Linux
url: /2008/09/mount-freebsd-disk-in-linux/

---
This must work:

First:
Console: _**dmesg \|grep bsd**_

Second:
**_mkdir /mnt/ufs/_**

Then:
**_mount -r -t ufs -o ufstype=44bsd /dev/sda5 /mnt/ufs/_** where _/dev/sda5_ is one of the partition listed in dmesg
