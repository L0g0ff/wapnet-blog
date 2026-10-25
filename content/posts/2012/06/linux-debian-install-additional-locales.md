---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
date: "2012-06-28T08:59:58+00:00"
guid: https://blog.wapnet.nl/?p=939
parent_post_id: null
post_id: "939"
title: '[Linux] Debian install additional locales'
url: /2012/06/linux-debian-install-additional-locales/

---
`#dpkg-reconfigure locales`

Now select you locale (for NL choose nl\_NL.UTF8).
Then select a default (or none for default system locale).

If you use the locale for apache restart your apache

`#/etc/init.d/apache2 restart`

Now you can define your locate trough you php config files.

More info: [http://wiki.debian.org/Locale](http://wiki.debian.org/Locale)
