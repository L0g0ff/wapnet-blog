---
_edit_last: "1"
_thumbnail_id: "1525"
author: thomasf
categories:
  - uncategorized
cover:
  alt: xi-logo-large
  image: /wp-content/uploads/2014/04/xi-logo-large.png
date: "2014-04-18T19:40:34+00:00"
dsq_thread_id: "5192135023"
guid: https://blog.wapnet.nl/?p=1523
parent_post_id: null
post_id: "1523"
title: Nagios Webinject errors
url: /2014/04/nagios-webinject-errors/

---
I installed a fresh copy of Nagios XI but the web transaction didn't work very well. I made some changes to fix the problems

The first status information error I had was: (null)

To fix this I installed perl-suidperl

```
yum install perl-suidperl

```

After that I get I new error: Return code of 255 is out of bounds![nagios return code of 255 is out of bounds](/wp-content/uploads/2014/04/nagios-return-code-of-255-is-out-of-bounds.png)

To fix this I changed the permissions of the  webinject folder and its files:

```
chown nagios:nagios /usr/local/nagiosxi/etc/components/webinject/
chown nagios:nagios /usr/local/nagiosxi/etc/components/webinject/*

```

Did was the trick.
