---
_thumbnail_id: "2202"
author: thomasf
categories:
  - linux
cover:
  alt: edit disks
  image: /wp-content/uploads/2024/08/362257d9-a3b1-427d-ad92-d02201aa9b1c-e1725096849664.webp
date: "2024-08-31T09:28:20+00:00"
guid: https://blog.wapnet.nl/?p=2187
parent_post_id: null
post_id: "2187"
title: Extend Linux ext4 disk with cfdisk
url: /2024/08/extend-linux-ext4-disk-with-cfdisk/

---
There are times when you need to extend a disk to accommodate more data or improve performance. While using UI tools to extend disks can make the process easier and more intuitive, there are situations where these tools aren't available. In such cases, knowing how to extend a disk using command-line tools can be invaluable. This post will guide you through the process of extending a disk without the need for graphical interfaces like gparted.

## TLDR;

`swapoff /dev/sda5
cfdisk
resize2fs /dev/sda1
mkswap /dev/sda5`  
`swapon /dev/sda5
blkid /dev/sda5
nano /etc/fstab`  

## Full procedure

First check the current partition structure with `lsblk`

{{< figure src="/wp-content/uploads/2024/08/image-7.png" alt="" caption="" >}}

As you can see you have 65G total but only 15GB on /

Start `cfdisk`

{{< figure src="/wp-content/uploads/2024/08/image.png" alt="" caption="" >}}


As you can see I cannot extend the disk because of the swap partition. So disable the swap first:

`sudo swapoff /dev/sda5`  

Then start cfdisk to remove the extended and the swap partitions and extend the /dev/sda1

{{< figure src="/wp-content/uploads/2024/08/image-1.png" alt="" caption="" >}}

In my case I reseverd 1GB for the new swap.

Then create a new extended `/dev/sda2` (max size) partition and within the extended partition a new swap partition `/dev/sda5`

{{< figure src="/wp-content/uploads/2024/08/image-2.png" alt="" caption="" >}}

Change the type of the swap partition to `82 Linux Swap / Solaris`

{{< figure src="/wp-content/uploads/2024/08/image-3.png" alt="" caption="" >}}

{{< figure src="/wp-content/uploads/2024/08/image-4.png" alt="" caption="" >}}

So the partition structure looks like:

{{< figure src="/wp-content/uploads/2024/08/image-5.png" alt="" caption="" >}}

Give a write and exit the cfdisk tool

Now you can extend the /dev/sda1 partition with: `resize2fs /dev/sda1`

{{< figure src="/wp-content/uploads/2024/08/image-8.png" alt="" caption="" >}}

As you can see the partition is extended. Now can can reactivate your swap partition

First check the current status

{{< figure src="/wp-content/uploads/2024/08/image-9.png" alt="" caption="" >}}

Enter the commands:

- `mkswap /dev/sda5`
- `swapon /dev/sda5`  

And as you can see the swap is actived

{{< figure src="/wp-content/uploads/2024/08/image-10.png" alt="" caption="" >}}

last thing you need to do is change the fsab to when the system reboots everything still works ;)

Get the UUID with `blkid /dev/sda5`

{{< figure src="/wp-content/uploads/2024/08/image-11.png" alt="" caption="" >}}

Edit the fstab file: ` nano /etc/fstab` and change the UID to the new ID

{{< figure src="/wp-content/uploads/2024/08/image-12.png" alt="" caption="" >}}

That's all. Happy resizing :)
