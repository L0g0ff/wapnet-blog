---
_edit_last: "1"
_thumbnail_id: "1333"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
cover:
  alt: Securing-disk-drive
  image: /wp-content/uploads/2013/09/Securing-disk-drive.jpg
date: "2013-09-24T09:26:37+00:00"
dsq_thread_id: "5286635206"
guid: https://blog.wapnet.nl/?p=1328
parent_post_id: null
post_id: "1328"
title: Linux IO write disk test
url: /2013/09/linux-io-write-disk-test/

---
`dd bs=1M count=256 if=/dev/zero of=test conv=fdatasync`

if the results are too fast try:

`dd bs=1M count=1024 if=/dev/zero of=test conv=fdatasync`

Source: [http://romanrm.ru/en/dd-benchmark](http://romanrm.ru/en/dd-benchmark)
