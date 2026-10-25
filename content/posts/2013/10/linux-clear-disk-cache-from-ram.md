---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
_thumbnail_id: "1391"
author: thomasf
categories:
  - linux
cover:
  alt: tux_pc
  image: /wp-content/uploads/2013/10/tux_pc.gif
date: "2013-10-14T07:34:11+00:00"
guid: https://blog.wapnet.nl/?p=1406
parent_post_id: null
post_id: "1406"
title: Linux clear disk cache from RAM
url: /2013/10/linux-clear-disk-cache-from-ram/

---
Sometimes your memory is full and youu can find the reason. 99/100 times the cause is that all your RAM is used for disk cache. This is an standard linux feature. With this command you can free your disk cache.

`echo 3 | sudo tee /proc/sys/vm/drop_caches`

via [Experiments and fun with the Linux disk cache](http://www.linuxatemyram.com/play.html).
