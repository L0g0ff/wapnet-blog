---
_thumbnail_id: "2024"
author: thomasf
categories:
  - hardware
  - linux
cover:
  alt: signal-2022-02-11-091338_001
  image: /wp-content/uploads/2022/02/signal-2022-02-11-091338_001-e1644570709481.jpeg
date: "2022-02-11T09:12:22+00:00"
guid: https://blog.wapnet.nl/?p=2019
parent_post_id: null
post_id: "2019"
title: Corrupt SD Card Recovery
url: /2022/02/corrupt-sd-card-recovery/

---
A friend of mine came back from vacation where he had taken a lot of pictures. When he got back home a large part of his Micro SD card (exFAT partition) was no longer accessible so he missed a couple of weeks of his photos and videos. His Windows Operating System froze completely when it hit a rotten cluster during a file copy action. So we had to find another solution to get his files back.

The first step I tried was to get the data from the SD card via Linux with ddrescue. With ddrecue, you create and complete dump of the SD card (or the sdb1 partition only). So you can do the data recovery on the image file (backup1.img) and not on the already corrupted SD Card.

The command you can use is:

```
ddrescue -d /dev/sdb1 /media/thomas/backup1.img /media/thomas/backup1.mapfile
```

But Linux also had also trouble reading when I hit a bad cluster. The only thing I could do during the read issues was a physical disconnect of the USB adapter, reconnect the adapter and restart the ddrescue process. The reason of was that a dual SD card adapter was used:

Micro SD > SD > SD > USB

(spoiler ALERT!: **Never use multiple adapters for data recovery!!!**)

{{< figure src="/wp-content/uploads/2022/02/signal-2022-02-11-095241.jpeg" alt="" caption="" >}}

Because ddrescue has a mapfile it goes further where he was stopped the last time.

While debugging I wrote a simple loop that forced a "physical" disconnection of the USB adapter wait one sec and reconnect the devices without touching anything.

[Source of the USBReset](https://github.com/L0g0ff/usbreset)(fork)

This works but is a very very slow process. This will takes months to recover so I had to find another way.

```
#!/bin/bash
## Steps to Prepare:
# lsusb check card reader and change the /dev/bus
# Start script in usbreset folder
# Run as sudo
# mount disk (media / thomas)
while true
do
	echo "Let's try Again!"
	ddrescue -d /dev/sdb1 /media/thomas/4905eb31-1df4-49bb-bb75-ec4889641d20/backup1.img /media/thomas/4905eb31-1df4-49bb-bb75-ec4889641d20/backup1.mapfile
	sleep 1
	./usbreset /dev/bus/usb/001/004
	sleep 1
done
```

The funny thing is that it was Sinterklaas time and that my daughter had just received a vtech kiddy photo camera with a Micro SD to USB adapter included :D

{{< figure src="/wp-content/uploads/2022/02/signal-2022-02-11-091334%5F001-edited.jpeg" alt="" caption="" >}}

So I try new new adapter: Micro SD > USB and with success.

{{< figure src="/wp-content/uploads/2022/02/signal-2022-02-11-091338%5F001-edited.jpeg" alt="" caption="" >}}

And after almost 15 hours the result 99.98% rescued rate :)

{{< figure src="/wp-content/uploads/2022/02/signal-2022-02-11-091326%5F001.jpeg" alt="" caption="" >}}

During my search for a solution I found some interesting articles:

- [https://www.pandorarecovery.com/blog/recover-data-from-sd-card-on-linux/](https://www.pandorarecovery.com/blog/recover-data-from-sd-card-on-linux/)
- [https://www.technibble.com/guide-using-ddrescue-recover-data/](https://www.technibble.com/guide-using-ddrescue-recover-data/)
- [https://www.hamishmb.com/blog/tutorial-use-photorec-ddrescue-gui-recover-deleted-files/](https://www.hamishmb.com/blog/tutorial-use-photorec-ddrescue-gui-recover-deleted-files/)
- [https://ncrmnt.org/2017/05/12/data-recovery-sd-ddrescue-and-android/](https://ncrmnt.org/2017/05/12/data-recovery-sd-ddrescue-and-android/)
- [https://www.gnu.org/software/ddrescue/](https://www.gnu.org/software/ddrescue/)
- [https://gist.github.com/L0g0ff/3cd99199c820cb518d0c7eef1dd2c771](https://gist.github.com/L0g0ff/3cd99199c820cb518d0c7eef1dd2c771)

Happy recovering!
