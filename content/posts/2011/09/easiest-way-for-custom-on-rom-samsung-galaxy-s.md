---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - android
  - windows
date: "2011-09-25T21:29:51+00:00"
dsq_thread_id: "5317010180"
guid: https://blog.wapnet.nl/?p=663
parent_post_id: null
post_id: "663"
title: Easiest way for custom on ROM Samsung Galaxy S
url: /2011/09/easiest-way-for-custom-on-rom-samsung-galaxy-s/

---
The Samsung Galaxy S default (aka stock) ROM has a good ROM but after some time the ROM become slower and slower. I will describe the steps for rooting the phone, backup the phone and install a nice cutom ROM.

I rooted a stock phone with android 2.3.3. Older versions can use this tutorial also. Newer versions maybe work.

I am not responsible when you brick your phone with this steps.

1. Turn on USB debugging mode on your phone (settings > programs > enable usb debugging)
1. Download and install the [samsung galaxy s drivers](http://drivers.softpedia.com/get/MOBILES/Samsung/)
1. Download [SuperOneClick](http://forum.xda-developers.com/showthread.php?t=803682) and extract it (e.g. c:\\android\\root\\)
1. Start SuperOneClick and press update
1. Now click root. SuperOneClick then must download an exploit to root your phone
1. After the software download the exploit close SuperOneClick
1. Go to the extracted directory e.g. c:\\android\\root\\devices\\samsung\\common\ and start odin.exe
1. All the default settings are fine. Click on PDA then select c:\\android\\root\\devices\\samsung\\gti9000\\CF-Root-XW\_NEE\_JVH-v3.2-CWM3RFS.tar
1. Start flashing

ok your phone is rooted now :) Now we want to backup the phone to SD so we can always back to stock settings

1. In your apps list there is a new program CWM recovery start these
1. Now make a full backup
1. After you have the full backup make a backup of all your contacts, sms, etc and download [MyBackup root](https://market.android.com/details?id=com.rerware.android.MyBackupRoot) at the marked (free) and make a backup of everything you want.

ok youre phone is rooted and we have a backup. Now we can install the ROM

1. Download a nice and stable ROM like [Darky ROM 10.2](http://www.darkyrom.com/community/index.php?threads/rom-darkyrom-v10-2-2-final-touchwiz-4.5124/) and put this file on the root of your SD card
1. Go to the market and download DarkyROM Tool
1. Now start the DarkyROM Tool go to the second tab and select all (important: delete user data must selected otherwise you get a very unstable ROM)
1. Go to the first tab and select flash rom. Select the file you've put on the SD card and flash it
1. The flashing take a minute of ten. After that the new rom is started and you think you have a new phone :)
1. Now download MyBackup root again and restore your call recordings, sms, phone numbers etc.

Enjoy :)

Youtube video for the DarkyROM flash:

[DarkyROM video](http://www.youtube.com/watch?v=qdcuF4V9Ewg)
