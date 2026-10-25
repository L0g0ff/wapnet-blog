---
author: thomasf
categories:
  - linux
date: "2008-03-15T13:30:19+00:00"
guid: https://blog.wapnet.nl/?p=30
parent_post_id: null
post_id: "30"
title: 'Project: Linux on solid state flash laptop'
url: /2008/03/project-linux-on-solid-state-flash-laptop/

---
15-3-08

I want to create a new linux project. The laptop have a solit state flash drive with only 128mb ram.

The following must run:
\- Debian\\Ubuntu as main OS
\- Xwindow manager (Flux box, Enlightenment, ICEWM or XFCE)
\- PPTP VPN connections
\- Remote desktop program for Windows RDP

The main problem of solid state flash is that you can write the disk not forever. So the log & temporary files must be run in the RAM. I found the following solution:

_/etc/fstab_

```
tmp     /tmp            tmpfs   noexec,nosuid,rw,size=1024K     0       0
vartmp  /var/tmp        tmpfs   noexec,nosuid,rw,size=1024K     0       0
varlog  /var/log        tmpfs   noexec,nosuid,rw,size=2048K     0       0
```

17-03-08:

My Distro choice is DSL (damn small linux) because that is a very small distro including window manager.

The first big problem is that i have only a 64mb SSD disk. I must create 57mb for my "fragile" installation. A have 7 MB for my home & swap. I'll have try it without swap but DSL was very unstable on my laptop.

18-03-08

I found a solution ([DSL Create own CD(PDF)](/wp-content/uploads/2008/03/mkmydslhowto.pdf "DSL Create own CD")) to create a my own installation CD. When I re-mastering the distro I can add items. But soon I'll try this manner to strip the distribution to a smaller one :)

19-03-08

When I remastered the DS, I seen one big KNOPPIX file. Now I must rebuild te KNOPPIX enviroment instead of the DSL. The KNOPPIX file is like a ISO. I must mount the file before i can edit these.

I found the following steps on the internet:

_Uncompress the DSL-N \*.iso and 'unpack" the knoppix image_

_\# mkdir /ramdisk/image_
_\# mount /path-to-file/dsl-n-01RC4.iso /ramdisk/image -t iso9660 -o loop,ro_
_\# mkdir /ramdisk/unpack_
_\# mount /ramdisk/image/KNOPPIX/KNOPPIX /ramdisk/unpack -t iso9660 -o ro,loop=/dev/cloop50_

_Prepare a place to put the files for the re-mastered knoppix image_

_\# mkdir /ramdisk/source_
_\# mkdir /ramdisk/newcd_
_\# mkdir /ramdisk/newcd/KNOPPIX_
_\# cp -Rp /ramdisk/unpack/\* /ramdisk/source_
_\# cp -Rp /ramdisk/unpack/.bash\_profile /ramdisk/source_

_Copy additional files to be added to the new knoppix image_

_\# cp /path-to-file/file /ramdisk/source/path-to-file/file_
_\# etc etc_

_"Pack" the new knoppix image_

_\# mkisofs -R /ramdisk/source \| create\_compressed\_fs - 65536 > ramdisk/newcd/KNOPPIX/KNOPPIX_
I'll try the mount and this works :) So now I must find the big files and strip these. My following step is find a tool like KDirStat to find these files.
