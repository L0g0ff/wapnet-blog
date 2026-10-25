---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - linux
date: "2010-10-08T22:09:04+00:00"
dsq_thread_id: "5136177944"
guid: https://blog.wapnet.nl/?p=429
parent_post_id: null
post_id: "429"
title: Install Meego on Dell Mini 9 with Wireless support
url: /2010/10/install-meego-on-dell-mini-9-with-wireless-support/

---
By default Meego 1.0 does not support the wireless broadcom chipset from the dell mini 9. I will explain how you can install Meego as netbook OS for your mini 9 with wireless :)

- First download [Meego](http://meego.com/downloads)
- Then use [Win32DiskImager.exe](https://wiki.ubuntu.com/Win32DiskImager) to create a bootable USB stick with the Meego image
- Install Meego
- Use the following procedure to fix the wireless:

> **Instructions (tnx LostLogic @ [Dell Forum](http://www.mydellmini.com/forum/dell-mini-9-discussion/21116-meego-mini9.html)):**
> Go to the applications tab, and type Terminal. Launch it
>
> $ sudo yum install rpmdevtools
> $ sudo yum groupinstall "Development Tools"
> $ sudo yum install kernel-netbook-devel
>
> Restart the notbook after the kernel is installed.
>
> Download the 32-bit package from this site and put it in your home/download dir
> [Broadcom.com - 802.11 Linux STA driver](http://www.broadcom.com/support/802.11/linux_sta.php)
>
> $ cd Downloads
> $ mkdir hybrid\_wl
> $ cd hybrid\_wl
> $ tar xvzf /home/YOURUSERNAME/Downloads/hybrid-portsrc-x86\_32-v5.60.48.36.tar.gz
> $ make clean
> $ make
>
> You might get a warning during the make build. Don't worry, it won't affect the later steps!
>
> $ modprobe lib80211
> $ sudo insmod wl.ko
>
> Welcome to WiFi MeeGo!
>
> We might want the driver to load every time we boot up MeeGo, so let's do the following!
> $ sudo cp wl.ko /lib/modules/\`uname -r\`/kernel/drivers/net/wireless
> $ sudo depmod -a
