---
_edit_last: "1"
_wp_old_slug: yumi-%e2%80%93-multiboot-usb-creator-windows
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
  - windows
date: "2011-09-30T06:37:56+00:00"
dsq_thread_id: "5137545656"
guid: https://blog.wapnet.nl/?p=676
parent_post_id: null
post_id: "676"
tags:
  - recovery
  - usb
  - yumi
title: YUMI – Multiboot USB Creator (Windows)
url: /2011/09/yumi-multiboot-usb-creator-windows/

---
YUMI (Your Universal Multiboot Installer), is the successor to MultibootISOs. It can be used to create a Multiboot USB Flash Drive containing multiple operating systems, antivirus utilities, disc cloning, diagnostic tools, and more. Contrary to MultiBootISO's which used grub to boot ISO files directly from USB, YUMI uses syslinux to boot extracted distributions stored on the USB device, and reverts to using grub to _Boot Multiple ISO files from USB_, if necessary.

Aside from a few distributions, all files are stored within the Multiboot folder, making for a nicely organized Multiboot Drive that can still be used for other storage purposes.

**Creating a YUMI Multiboot MultiSystem USB Flash Drive**
YUMI works much like Universal USB Installer, except it can be used to install more than one distribution to run from your USB. Distributions can also be uninstalled using the same tool!

[![](/wp-content/uploads/2011/09/YUMI-Multiboot-USB-Creator.png)](/wp-content/uploads/2011/09/YUMI-Multiboot-USB-Creator.png)**YUMI's Main Multiboot Boot Menu**  [![](/wp-content/uploads/2011/09/YUMI-Boot-Menu.png)](/wp-content/uploads/2011/09/YUMI-Boot-Menu.png)

## How to Create a MultiBoot USB Flash Drive

1. Run\* **YUMI-0.0.2.9.exe** following the onscreen instructions
1. Run the tool again to Add More ISOs/Distributions to your Drive
1. Restart your PC setting it to boot from the USB device
1. Select a distribution to Boot from the Menu and enjoy!

That's all there is to it. You should now be booting your favorite distributions from your custom Multi-Boot USB device!

**How It Works**: YUMI (Your Universal Multiboot Installer) enables each user to create their own custom Multiboot UFD containing only the distributions they want, in the order by which they are installed. A new distribution can be added to the UFD each time the tool is run.

If you run YUMI from the same location you store ISO downloads, they should be auto-detected (\*See Known Issues Below), eliminating the need to browse for each ISO.

**VERY IMPORTANT**: Windows Vista or 7 Installers will cause Ubuntu or any remix based on Ubuntu (I.E. Linux Mint) to hang during boot. A quick fix is to temporarily rename the Windows **SOURCES** folder found at the root of the USB device.

**Other Notes**: If MultibootISOs was previously used, you must reformat the drive and start over. YUMI uses Syslinux directly, and chainloads to grub only if necessary, so it is not compatible with the older Multiboot ISO tool. Although I do plan to add back the capabilities of MultibootISOs as time permits.

The distro uninstaller works great, but unlisted ISO's that have been added must currently be manually removed!

Source: [http://www.pendrivelinux.com/yumi-multiboot-usb-creator/](http://www.pendrivelinux.com/yumi-multiboot-usb-creator/)
