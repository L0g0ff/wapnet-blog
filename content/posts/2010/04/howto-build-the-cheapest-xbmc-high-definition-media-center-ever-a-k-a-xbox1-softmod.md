---
_edit_last: "1"
author: thomasf
categories:
  - hardware
  - media-center
  - xbox
date: "2010-04-22T14:31:13+00:00"
dsq_thread_id: "5136177728"
guid: https://blog.wapnet.nl/?p=369
parent_post_id: null
post_id: "369"
tags:
  - xbmc
  - xbox
title: 'Howto: Build the cheapest XBMC High Definition media center ever a.k.a. XBOX1 Softmod'
url: /2010/04/howto-build-the-cheapest-xbmc-high-definition-media-center-ever-a-k-a-xbox1-softmod/

---
What do you need?

1. [This ISO](/upload/XBOXHDMAKER.rar) (Custom XBOX HD Maker)
1. Auto installer deluxe (4.5 or higher) (Download: [http://aideluxe.com](http://aideluxe.com/))
1. Computer with an IDE connection
1. CD Burner
1. Screwdriver with a couple of tork plugs
1. Second-hand XBOX1 **with remote** ([http://marktplaats.nl](http://marktplaats.nl/) max €40)
1. XBOX1 component cable ([http://bol.com](http://bol.com/) €6, free shipping coupon @ [http://retailmenot.com](http://retailmenot.com/))

First download and burn the XBOX HD Maker and Auto installer Deluxe to a CD or DVD.

Then disconnect al the  IDE cables except the IDE CD player. Put the XBOX HD Maker CD in the computer. Start the pc and before the BIOS recognize the harddisk press the pause key. Now the boot process is on pause :-)

Now remove the rubber feeds under the xbox. Then remove all the six tork screws (2 screws are under a sticker). Remove the disk bay (screw are under the IDE cable) and remove the 4 disk screws.

Pull out the IDE cable from your XBOX DVD player. When you start the XBOX now you see a red light is blinking. This is gooood ;-)

Now you must connect a video/scart cable (a tv is not necessary but without the cable the xbox cannot start) and power on the XBOX, let the red light blink 3 times and then put the IDE cable from the XBOX hard disk as fast as possible. Now the disk is unlocked so we can flash that XBOX FATX DISK.

Connect the IDE cable from the computer to the disk (primary master is the best, otherwise you can use the secondary master). Then press on the spacebar to continue the boot process and the BIOS must recognize the XBOX disk.

The pc must boot from CD and start the XBOX HD Maker Linux Distribution. Follow the steps on the screen. You must wipe the disk completely and rebuild it and create a new key (option 6 or 7)

Now you can connect the newly build disk to the XBOX and connect the CD player again. Connect the scart to your tv and boot the XBOX from the auto installed deluxe (AID) CD.

Follow the steps on screen, first make a MS Backup, so AID can copy all the necessary files to the XBOX, then choose the softmod option with virtual C drive. Choose XBMC as the default dashboard.

After the installation you can put out the AID CD and boot the XBOX. Now XBMC is started directly.

To make the XBOX 720P compatible (1080 is also possible but the poorly 733Mhz processor  doesn’t like that kind of high resolutions :P ) connect the component cable to the XBOX. Then run the “Enigmah Video Mode Switcher”. You can launch this from the XBMC > Programs (if you don’t have programs you can enable this in the option screen). Set the video mode from PAL60 to NSTC. Then reboot the XBOX and start the MS dashboard (easiest way is from file explorer default.xbe on the C:\\). Now go to video and enable the 420 and 720 HD resolutions.

That’s it :)

Ps. The embedded AID XBOX media center is a little bit old. You can download a new build from: [http://www.sshcs.com/xbmc/](http://www.sshcs.com/xbmc/) or [http://t3ch.yi.se/](http://t3ch.yi.se/).
Ps2. The next time I i'll softmod a XBOX1 i will create a youtube video.

﻿
