---
_thumbnail_id: "2037"
author: thomasf
categories:
  - linux
  - windows
cover:
  alt: angif-boot-up-your-computer
  image: /wp-content/uploads/2022/03/angif-boot-up-your-computer.gif
date: "2022-03-06T19:29:24+00:00"
guid: https://blog.wapnet.nl/?p=2035
parent_post_id: null
post_id: "2035"
title: Repair Debian boot after Windows update
url: /2022/03/repair-debian-boot-after-windows-update/

---
Today I update my dual boot system and unfortunately my Debian OS wasn't booting anymore. The root cause was that Windows decide to reclaim the EFI boot.

The fix is quite easy.

Type `mountvol P: /S`

Check the EFI boot partition data

{{< figure src="/wp-content/uploads/2022/03/image.png" alt="" caption="" >}}

And fix your boot the this command:

`bcdedit.exe /set {bootmgr} path \EFI\Debian\grubx64.efi`

As you can see in the screenshot, this also work for EndeavourOS and Ubuntu and probably for a lot other Linux EFI boot systems.

Happy booting!
