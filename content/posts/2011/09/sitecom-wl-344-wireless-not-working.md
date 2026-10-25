---
_edit_last: "1"
author: thomasf
categories:
  - linux
date: "2011-09-10T00:12:45+00:00"
dsq_thread_id: "5246338851"
guid: https://blog.wapnet.nl/?p=645
parent_post_id: null
post_id: "645"
tags:
  - "11.04"
  - linux
  - ubuntu
title: Sitecom WL-344 wireless not working
url: /2011/09/sitecom-wl-344-wireless-not-working/

---
The solutions is block the rt2800usb

> echo 'blacklist rt2800usb' \| sudo tee -a /etc/modprobe.d/blacklist.conf

restart, and try this

> echo 'install rt2870sta modprobe --ignore-install rt2870sta ; /bin/echo "0df6 0040" > /sys/bus/usb/drivers/rt2870/new\_id' \| sudo tee /etc/modprobe.d/rt2870sta.conf
> sudo modprobe rt2870sta
> dmesg \| egrep 'rt28\|usb\|Phy'
> iwconfig
> sudo iwlist scan

(the first Line allocate the Chipset-ID to the driver rt2870sta)

If the solution works, activiate it automatically by a new udev-Rule

> sudo gedit /etc/udev/rules.d/10-wlan.rules

Insert the following code and save the file

> # UDEV-Rule for Sitecom WL-344 ID 0df6:0040
>
> SUBSYSTEM=="usb", SYSFS{idVendor}=="0df6", SYSFS{idProduct}=="0040", RUN+="/sbin/modprobe rt2870sta"

Activate it (or restart)

> sudo service udev reload

Credits: flash63
Source: [http://ubuntuforums.org/showthread.php?t=1514196](http://ubuntuforums.org/showthread.php?t=1514196)
