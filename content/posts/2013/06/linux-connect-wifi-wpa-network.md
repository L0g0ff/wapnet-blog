---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
date: "2013-06-06T21:30:52+00:00"
dsq_thread_id: "5319998701"
guid: https://blog.wapnet.nl/?p=1058
parent_post_id: null
post_id: "1058"
title: Linux connect WiFi / WPA network
url: /2013/06/linux-connect-wifi-wpa-network/

---
```
nano /etc/network/interfaces

auto wlan0
iface wlan0 inet dhcp
    wpa-ssid YOUR-SSID-HERE
    wpa-psk YOUR-PASSWORD-HERE
```
