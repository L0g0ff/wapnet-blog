---
_edit_last: "1"
_thumbnail_id: "1518"
author: thomasf
categories:
  - linux
cover:
  alt: dialog-question
  image: /wp-content/uploads/2014/04/dialog-question.png
date: "2014-04-08T14:12:40+00:00"
dsq_thread_id: "5147167943"
guid: https://blog.wapnet.nl/?p=1517
parent_post_id: null
post_id: "1517"
tags:
  - file-monitor
  - malware
  - monitor
  - process
  - virus
title: Linux find out what a process is doing
url: /2014/04/linux-find-out-what-a-process-is-doing/

---
1. start top
1. lsof -p <pid>
1. strace -p <pid>
1. ltrace -p <pid>

Happy debugging :D
