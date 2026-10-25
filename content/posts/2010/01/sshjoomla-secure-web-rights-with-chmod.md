---
_edit_last: "1"
author: thomasf
categories:
  - linux
date: "2010-01-24T22:47:50+00:00"
guid: https://blog.wapnet.nl/?p=340
parent_post_id: null
post_id: "340"
title: SSH/Joomla secure web rights with chmod
url: /2010/01/sshjoomla-secure-web-rights-with-chmod/

---
Hi,

2 easy commands to secure your Joomla site:

> cd /var/www/somewebdir/
> find . -type f -exec chmod 644 {} \\;
> find . -type d -exec chmod 755 {} \\;
