---
_disable_fbc: ""
_edit_last: "1"
_thumbnail_id: "1633"
author: thomasf
categories:
  - hardware
  - osx
cover:
  alt: disk
  image: /wp-content/uploads/2015/04/disk.png
date: "2015-04-29T21:38:38+00:00"
dsq_thread_id: "5137253011"
guid: https://blog.wapnet.nl/?p=1630
parent_post_id: null
post_id: "1630"
title: Fix Intel SSD 320 problem on a Macbook
url: /2015/04/fix-intel-ssd-320-problem-on-a-macbook/

---
From one day to another my Intel 320 SSD was not visible anymore. So I download Ubuntu 14.04 boot it and start gparted.  Then I saw no SSD disk in my disk selection :(

[![ubuntu-disk-missing](/wp-content/uploads/2015/04/ubuntu-disk-missing.png)](/wp-content/uploads/2015/04/ubuntu-disk-missing.png)

So I download the Intel firmware tool and boot it and then I get a BAD\_CTX and a disk with 0GB :(

[![bad_ctx](/wp-content/uploads/2015/04/bad_ctx.png)](/wp-content/uploads/2015/04/bad_ctx.png)

After some google'ing on the BAD\_CTX I saw this was an known issue. The only way to fix this was completely secure erase your disk and so all your data on the disk is gone ARRRRGGGGG!!!!!!!!!!!!!!!!!!!!!!!!!!

I found a lot information how to secure erase the disk but finding some mac / apple specific articles was a lot more painful.

So I tried a lot of things and fixing the problem is quite easy if you know the steps. So I explain this for you so it cost you only one evening to fix this :P

First go to [https://partedmagic.com/](https://partedmagic.com/) and buy and download parted magic ISO ($9). Now burn the parted magic ISO to a CD.

Then boot the parted magic. If you don't know how to boot from a CD or USB with mac you must press the "option (alt) key" immediately after you press the power button and select the disk.

If parted magic is started, start secure erase and follow the wizard to accomplish this step. If you disk is frozen use the sleep key in the wizard to change the state to "not frozen".

After the disk is completely erased shutdown the computer.

Now download the [Intel SSD drive firmware update tool](https://downloadcenter.intel.com/download/18363/Intel-Solid-State-Drive-Firmware-Update-Tool) and burn it to a CD. Then boot the tool and update your disk firmware.

Then reinstall your OSX. For the people who use time machine is very easy to get the latest status back to your pc.

I know one thing for sure. This was my latest Intel SSD...

If I helped you please help me to supporting this blog without any advertising.

{{< paypal-donation >}}

Some extra info:
[CNET outdated article](http://www.cnet.com/how-to/how-to-securely-erase-an-ssd-drive/) [Secure erase article from Parted Magic](http://partedmagic.com/secure-erase/) [Nice blog about this issue and fix it with a standard PC](https://trikks.wordpress.com/2013/06/20/battling-the-intel-320-bad_ctx-bug-again/)
