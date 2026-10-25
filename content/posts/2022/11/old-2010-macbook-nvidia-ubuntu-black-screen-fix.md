---
_thumbnail_id: "2092"
_wp_old_slug: old-2008-macbook-nvidia-ubuntu-black-screen-fix
author: thomasf
categories:
  - linux
  - osx
cover:
  alt: nvidia
  image: /wp-content/uploads/2022/11/nvidia.png
date: "2022-11-22T16:11:23+00:00"
guid: https://blog.wapnet.nl/?p=2090
parent_post_id: null
post_id: "2090"
title: Old 2010 Macbook Nvidia Ubuntu black screen fix
url: /2022/11/old-2010-macbook-nvidia-ubuntu-black-screen-fix/

---
All the credits are for Andreas @ [https://askubuntu.com/questions/264247/proprietary-nvidia-drivers-with-efi-on-mac-to-prevent-overheating/613573#613573](https://askubuntu.com/questions/264247/proprietary-nvidia-drivers-with-efi-on-mac-to-prevent-overheating/613573#613573)

Nvidia is always a pain in the ass on Linux. Especially with a old white 2010 macbook. I have black screen issues every time so I create this article so I can easy find it when I reinstall this laptop ;-)

First find the right identifiers.

We need both the IDs for the graphics card and the PCI-E bridge that it is connected to. Issue the following command in a shell:

```
~$ sudo lshw -businfo -class bridge -class display
pci@0000:00:00.0              bridge         MCP89 HOST Bridge
pci@0000:00:03.0              bridge         MCP89 LPC Bridge
pci@0000:00:0e.0              bridge         NVIDIA Corporation
pci@0000:00:15.0              bridge         NVIDIA Corporation
pci@0000:00:16.0              bridge         NVIDIA Corporation
pci@0000:00:17.0     >!!<     bridge         MCP89 PCI Express Bridge
pci@0000:04:00.0     >!!<     display        MCP89 GeForce 320M
```

Have a look at (1) the line saying display and (2) the line with bridge right before that display line. Write down the PCI-E bus ids (format XX:YY.Z) of the bridge device (here 00:17.0) and the display device (here 04:00.0) and remember which is which. **Note**: Those IDs may be different on your machine, depending on your Mac model and revision.

Create a GRUB script for setting the PCI-E registers during boot

Fire up a text editor with _sudo nano /etc/grub.d/01\_enable\_vga.conf_ and copy/paste the content below. Make sure to paste all 4 lines into that file! **Replace** _00:17.0_ with the PCI-E ID of your bridge device noted in step 1. **Replace** _04:00.0_ with the PCI-E ID of your display device noted in step 1.

```
cat << EOF
setpci -s "00:17.0" 3e.b=8
setpci -s "04:00.0" 04.b=7
EOF
```

Finally, make the created file executable and update your grub config files using the following **TWO** commands.

```
~$ sudo chmod 755 /etc/grub.d/01_enable_vga.conf
~$ sudo update-grub
```

Install Nvidia drivers and enjoy!
