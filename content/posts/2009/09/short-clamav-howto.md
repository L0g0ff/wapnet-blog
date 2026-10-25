---
_edit_last: "1"
author: thomasf
categories:
  - linux
date: "2009-09-16T09:45:26+00:00"
dsq_thread_id: "5656311277"
guid: https://blog.wapnet.nl/?p=222
parent_post_id: null
post_id: "222"
title: Short ClamAV Howto
url: /2009/09/short-clamav-howto/

---
1\. Install Clamav with your favorite packet manager

> #apt-get install clamav

2\. Update ClamAV Database

> #freshclam

3\. Scan your server and only list infected files

> #clamscan / -r -i
