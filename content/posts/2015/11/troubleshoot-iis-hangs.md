---
_disable_fbc: ""
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
_thumbnail_id: "1671"
author: thomasf
categories:
  - iis
cover:
  alt: slow-moving-websites-sign
  image: /wp-content/uploads/2015/11/slow-moving-websites-sign1.jpg
date: "2015-11-04T14:22:08+00:00"
dsq_thread_id: "5327719587"
guid: https://blog.wapnet.nl/?p=1665
parent_post_id: null
post_id: "1665"
title: Troubleshoot IIS hangs
url: /2015/11/troubleshoot-iis-hangs/

---
I've created a batch file which find out what was hanging my .NET application.


```
:loop
CLS
time /t >>crappy_site_log.txt
%windir%\system32\inetsrv\appcmd list requests /elapsed:5000 >>crappy_site_log.txt
ping -n 4 127.0.0.1
GOTO loop
```


This command logs every request above the 5 seconds.

[![IIS-debug](/wp-content/uploads/2015/11/IIS-debug.png)](/wp-content/uploads/2015/11/IIS-debug.png)

This idea came from: [https://www.leansentry.com/Guide/IIS-AspNet-Hangs](https://www.leansentry.com/Guide/IIS-AspNet-Hangs)
