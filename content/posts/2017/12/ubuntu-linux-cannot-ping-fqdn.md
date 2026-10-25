---
_edit_last: "1"
_thumbnail_id: "1778"
author: thomasf
categories:
  - linux
cover:
  alt: dns
  image: /wp-content/uploads/2017/12/dns.png
date: "2017-12-16T22:00:55+00:00"
dsq_thread_id: "6357034157"
guid: https://blog.wapnet.nl/?p=1776
parent_post_id: null
post_id: "1776"
title: Ubuntu Linux cannot ping FQDN
url: /2017/12/ubuntu-linux-cannot-ping-fqdn/

---
Because this is the fifth time I fixed this issue I write a blog about it...

Microsoft uses `.local` as the recommended root of internal domains, and serves them via _unicast_ dns. Linux uses `.local` as the root of _multicast_ dns. If you're stuck on a broken MS network like this, reconfigure your linux multicast DNS to use a different domain like .alocal.

To do this, add a `domain-name=.alocal` line to the `[server]` section of `/etc/avahi/avahi-daemon.conf`, then restart avahi-daemon: `sudo service avahi-daemon restart`.

```
[server]
domain-name=.alocal

```

You may need to flush the DNS, mDNS and resolver cache, as well as restart your web browsers to clear their internal cache.

Source: [http://www.lowlevelmanager.com/2011/09/fix-linux-dns-issues-with-local.html](http://www.lowlevelmanager.com/2011/09/fix-linux-dns-issues-with-local.html)
