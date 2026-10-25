---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - linux
date: "2010-12-07T13:22:40+00:00"
dsq_thread_id: "5140350272"
guid: https://blog.wapnet.nl/?p=489
parent_post_id: null
post_id: "489"
title: CentOS / Fedora / Red Hat Guest OS Hangs During Boot (VMWare)
url: /2010/12/centos-fedora-red-hat-guest-os-hangs-during-boot-vmware/

---
When the boot process hangs during the following:

> Creating root device.
> Mounting root filesystem.
> kjournald starting.  Commit interval 5 seconds
> EXT3-fs: mounted filesystem with ordered data mode.
> Setting up other filesystems.
> Setting up new root fs
> no fstab.sys, mounting internal defaults
> Switching to new root and running init.
> unmounting old /dev
> unmounting old /proc
> unmounting old /sys
> INIT: version 2.86 booting
> Welcome to  CentOS release 5 (Final)
> Press 'I' to enter interactive startup.

Do the follwing:

1. Start the server with an rescue cd and access (chroot) the disk
1. Give the following command:

> mv hwclock hwclock.original echo "exit 0" > hwclock chmod 755 hwclock

Now restart the server. The problem cause an error with the clock. For more info see: [http://www.virtuatopia.com/index.php/Xen\_CentOS/Fedora/Red\_Hat\_Guest\_OS\_Hangs\_During\_Boot](http://www.virtuatopia.com/index.php/Xen_CentOS/Fedora/Red_Hat_Guest_OS_Hangs_During_Boot)
