---
_edit_last: "1"
_thumbnail_id: "1617"
author: thomasf
categories:
  - linux
  - windows
cover:
  alt: usb
  image: /wp-content/uploads/2015/04/usb.png
date: "2015-04-08T14:29:23+00:00"
dsq_thread_id: "5151001251"
guid: https://blog.wapnet.nl/?p=1614
parent_post_id: null
post_id: "1614"
title: Clone HP ThinState Capture USB stick (or any other USB disk)
url: /2015/04/clone-hp-thinstate-capture-usb-stick/

---
The ThinState USB disk is split into 2 partitions. And the second partition isn't accessible in Windows so it was very hard to build a stick from scratch. There are a lot of Windows USB clone tools but because I had to clone the ThinState 16GB to a 8GB stick also, it was impossible to do it from my windows workstation. But when some things get more difficulty what do you do? Use Linux :)

### The Easy way (same USB stick size or bigger):

```
$sudo dd if=/dev/sdb of=/dev/sdc bs=512
```

### The "Hard" way (clone to smaller USB):

First resize the partitions with gparted to the minimum size. Then find out the last sector of the /dev/sdb2 (where sdb2 is my USB stick)

```
$sudo fdisk -u -l /dev/sdb
```

Output:

```
Disk /dev/sdb: 14,9 GiB, 16026435584 bytes, 31301632 sectors
Units: sectors of 1 * 512 = 512 bytes

Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disklabel type: dos Disk identifier: 0x6a60ab98

Device     Boot   Start     End Sectors Size Id Type
/dev/sdb1 *       2048 2099199 2097152   1G b W95 FAT32
/dev/sdb2       2099200 14131199 12032000 5,8G 7 HPFS/NTFS/exFAT
```

Now use dd with sector 12032000 + 1.

```
dd if=/dev/sdb of=/home/myusername/usbimage.img count=12032001
```

and write the \*.img file back to your new USB stick:

```
dd if=/home/myusername/usbimage.img of=/dev/sdb
```
