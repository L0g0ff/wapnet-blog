---
_edit_last: "1"
author: thomasf
categories:
  - linux
date: "2008-08-06T18:45:11+00:00"
dsq_thread_id: "5241652840"
guid: https://blog.wapnet.nl/?p=41
parent_post_id: null
post_id: "41"
title: 'fsck.ext3: Unable to resolve'
url: /2008/08/fsckext3-unable-to-resolve/

---
Hi

I have installed Fedora Core 3 and on booting up it gives the error

fsck.ext3:Unable to resolve "LABEL=/"
An error occured during filesystem check
Dropping you to a shell, the system will reboot
when you leave shell

Ok I searched on the net regarding this...

My /etc/fstab had the following entries

LABEL=/ / ext3 defaults 1 1
LABEL=/var/log /var/log ext3 defaults 1 2
.....
....

My grub.conf had the following entries

title StorTrends iTX 2.0 (2.6.9-1.667smp)
root (hd0,0)
kernel /boot/vmlinuz-2.6.9-1.667smp ro root=LABEL=/ elevator=deadline vga=0x318 quiet
initrd /boot/initrd-2.6.9-1.667smp.img

\\*\\*\\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* \*\*
In maintenance mode i mounted the / in read - write mode
**mount -n -o remount,rw /**
