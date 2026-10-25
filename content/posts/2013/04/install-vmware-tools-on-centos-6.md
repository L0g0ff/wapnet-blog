---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
date: "2013-04-29T13:21:59+00:00"
dsq_thread_id: "5193805713"
guid: https://blog.wapnet.nl/?p=1034
parent_post_id: null
post_id: "1034"
title: Install VMware Tools on Centos 6
url: /2013/04/install-vmware-tools-on-centos-6/

---
This is a HOWTO for installing VMware Tools on Centos 6.x.

Update your system so the kernel headers/devel will match your system:

```
yum update
```

Install the VMware tools prerequisites:

```
yum install make gcc kernel-devel kernel-headers glibc-headers perl
```

Reboot the server:

```
shutdown -r now
```

Mount the VMware Tools CD (after inserting it into the VM)

```
mkdir /media/cdrom
mount /dev/cdrom /media/cdrom
```

Copy the install bundle from the CD and extract it.

```
cp /media/cdrom/VMware-Tools*.tar.gz /root
cd /root
tar xvfz VMwareTools*.tar.gz
```

Run the installer, default on all prompts works fine.

```
cd /root/vmware-tools-distrib
./vmware-install.pl
```

Reboot the server.

```
shutdown -r now
```

Source: [http://mondotech.blogspot.nl/2012/05/install-vmware-tools-on-rhel-6-centos-6.html](http://mondotech.blogspot.nl/2012/05/install-vmware-tools-on-rhel-6-centos-6.html)
