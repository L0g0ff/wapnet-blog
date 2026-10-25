---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
date: "2011-08-30T15:06:25+00:00"
dsq_thread_id: "5138619283"
guid: https://blog.wapnet.nl/?p=630
parent_post_id: null
post_id: "630"
title: Extending LVM disks in Linux using Vmware virtual disks
url: /2011/08/extending-lvm-disks-in-linux-using-vmware-virtual-disks/

---
All the credits go to Arjen Visser @ [http://www.dbvisit.com/forums/showthread.php?t=343](http://www.dbvisit.com/forums/showthread.php?t=343). I add his article and I edited a little because of some error I get and I a'm able to find it quickly the next time :)

Here is the current file system. It needs another 3Gb on the LogVol00 filesystem. The Linux system is a VMware virtual system with Virtual disks.


```
[root@dbvrac1 ~]# df -k
Filesystem 1K-blocks Used Available Use% Mounted on
/dev/mapper/VolGroup00-LogVol00
9127580 6692828 1971088 78% /
/dev/sda1 101086 12651 83216 14% /boot
none 596544 0 596544 0% /dev/shm
```


The partitions are as follows


```
[root@dbvrac1 ~]# sfdisk -s
/dev/sda: 10485760
/dev/sdb: 10485760
/dev/sdc: 10485760
/dev/sdd: 10485760
/dev/sde: 10485760
/dev/sdf: 10485760
```


First the Vmware virtual disks needs to increase. 13Gb is the new size. Shutdown the Vmware guest and resize the disk on the Vmware host:


```
# vmware-vdiskmanager -x 13GB dbvrac1.vmdk
Using log file /tmp/vmware-root/vdiskmanager.log
The old geometry C/H/S of the disk is: 1305/255/63
The new geometry C/H/S of the disk is: 1697/255/63
Disk expansion completed successfully.
```


Start up the Vmware guest again.
This has added space on the /dev/sda partition. This can be seen by running sfdisk -s again:


```
[root@dbvrac1 ~]# sfdisk -s
/dev/sda: 13631488
/dev/sdb: 10485760
/dev/sdc: 10485760
/dev/sdd: 10485760
/dev/sde: 10485760
/dev/sdf: 10485760
```


To use the space, a partition first has to be created on /dev/sda


```
[root@dbvrac1 ~]# ls -al /dev/sda*
brw-rw---- 1 root disk 8, 0 Jun 29 2009 /dev/sda
brw-rw---- 1 root disk 8, 1 Jun 29 2009 /dev/sda1
brw-rw---- 1 root disk 8, 2 Jun 29 2009 /dev/sda2
```


The new partition will be /dev/sda3.


```
[root@dbvrac1 /]# fdisk /dev/sda
```



```
Command (m for help): n
Command action
e extended
p primary partition (1-4)
p
Partition number (1-4): 3
First cylinder (1306-1697, default 1306):
Using default value 1306
Last cylinder or +size or +sizeM or +sizeK (1306-1697, default 1697):
Using default value 1697

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
Validate that the new partition has been created
```



```
[root@dbvrac1 ~]# ls -al /dev/sda*
brw-rw---- 1 root disk 8, 0 Jun 29 2009 /dev/sda
brw-rw---- 1 root disk 8, 1 Jun 29 2009 /dev/sda1
brw-rw---- 1 root disk 8, 2 Jun 29 2009 /dev/sda2
brw-rw---- 1 root disk 8, 2 Jun 29 2009 /dev/sda3
```



```
/dev/sda3 is the new partition.
Reboot to load the new partition into the kernel.Create a physical volume for LVM:
```



```
[root@dbvrac1 ~]# pvcreate /dev/sda3
Physical volume "/dev/sda3" successfully created
```


I had some problems and get the error:
Device /dev/sda3 not found (or ignored by filtering). To fix thix error:

```
Command (m for help): n
Command action
l logical (5 or over)
p primary partition (1-4)
l
First cylinder (6267-7832, default 6267):
Using default value 6267
Last cylinder or +size or +sizeM or +sizeK (6267-7832, default 7832):
Using default value 7832

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
Validate that the new partition has been created
```



```
[root@dbvrac1 ~]# ls -al /dev/sda*
brw-rw---- 1 root disk 8, 0 Jun 29 2009 /dev/sda
brw-rw---- 1 root disk 8, 1 Jun 29 2009 /dev/sda1
brw-rw---- 1 root disk 8, 2 Jun 29 2009 /dev/sda2
brw-rw---- 1 root disk 8, 2 Jun 29 2009 /dev/sda3
brw-rw---- 1 root disk 8, 2 Jun 29 2009 /dev/sda5
```


and then:

```
[root@dbvrac1 ~]# pvcreate /dev/sda5
Physical volume "/dev/sda5" successfully created
```


Add the new physical volume to the volume group:


```
[root@dbvrac1 ~]# vgextend VolGroup00 /dev/sda3
Volume group "VolGroup00" successfully extended
```


Extend the logical volume over the new space in the volume group.
Find out how much more space can be added:


```
[root@dbvrac1 ~]# vgdisplay
--- Volume group ---
VG Name VolGroup00
System ID
Format lvm2
Metadata Areas 2
Metadata Sequence No 4
VG Access read/write
VG Status resizable
MAX LV 0
Cur LV 2
Open LV 2
Max PV 0
Cur PV 2
Act PV 2
VG Size 12.88 GB
PE Size 32.00 MB
Total PE 412
Alloc PE / Size 315 / 9.84 GB
Free PE / Size 97 / 3.03 GB
VG UUID 7yenoW-lzsd-xK8a-j2Vj-qgty-TFXK-L0lhTL

There is 3.03Gb available.
Extend the volume:

[root@dbvrac1 ~]# lvextend -L+3.03G /dev/VolGroup00/LogVol00
Rounding up size to full physical extent 3.03 GB
Extending logical volume LogVol00 to 11.88 GB
Logical volume LogVol00 successfully resized
```

Resize the filesystem:

```
[root@dbvrac1 ~]# resize2fs /dev/VolGroup00/LogVol00
resize2fs 1.35 (28-Feb-2004)
/dev/VolGroup00/LogVol00 is mounted; can't resize a mounted filesystem!
```


Cannot use resize2fs as it is online. Use ext2online instead.

```
[root@dbvrac1 ~]# ext2online /dev/VolGroup00/LogVol00
ext2online v1.1.18 - 2001/03/18 for EXT2FS 0.5b
```


Check file system:


```
[root@dbvrac1 ~]# df -k
Filesystem 1K-blocks Used Available Use% Mounted on
/dev/mapper/VolGroup00-LogVol00
12256820 6695112 4940796 58% /
/dev/sda1 101086 12651 83216 14% /boot
none 596544 0 596544 0% /dev/shm

All done! Filesystem has increased from 9127580 to 12256820.
```


Original article: [http://www.dbvisit.com/forums/showthread.php?t=343](http://www.dbvisit.com/forums/showthread.php?t=343)
