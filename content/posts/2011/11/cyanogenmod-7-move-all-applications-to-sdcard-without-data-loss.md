---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - android
  - linux
date: "2011-11-23T20:37:24+00:00"
dsq_thread_id: "5136178663"
guid: https://blog.wapnet.nl/?p=731
parent_post_id: null
post_id: "731"
title: Cyanogenmod 7 move all applications to sd card without data loss
url: /2011/11/cyanogenmod-7-move-all-applications-to-sdcard-without-data-loss/

---
I have an HTC Desire phone. I like the phone but there is one big problem; the NAND (internal storage) is way to small. I installed a lot of ROM's but the last time I install Cyanogenmod 7.1 with the "Launcher 7" and I did a lot of customization I don't want to reinstall my phone.

There is an crappy android workaround to move some of your apps to the SD card but when you connect/mount your phone to your pc you cannot start these apps and if you disconnect some of the settings are ruined.

So I searched the internet and read a lot of articles to find the best method to repartition my SD card and move the application and dalvik cache to my SD card. So I wrote this tutorial so you can move all the apps to your phone without any data loss also.

What do you need:

1. Cyanogenmod 7
1. S2E (free on the android marked)
1. App 2 SD free (android marked)
1. Linux operating system with Gparted or Gparted live CD

The steps

1. Shutdown the phone and put out your SD card
1. Make a backup of your SD card
1. Run GParted and make a primary FAT32 partiton and 1 GB (or more) EXT3 partition. Because I have an 16GB SD card I make a 2GB EXT3 partition. You can check a Gparted youtube tutorial here: [http://www.youtube.com/watch?v=6z1Tu9l8WNc](http://www.youtube.com/watch?v=6z1Tu9l8WNc)
1. Now copy your backup back to the SD card and place the SD in to the phone
1. Start the phone and start S2E
1. Select Applications, Dalvik cache and Download cache
1. Press the menu button and reboot the phone
1. Have some patience now (5min-10min)
1. Now start the phone and start apps 2 sd
1. Press the "On SD Card" tab, press menu and press move all apps
1. Now press on the **move to phone button** for every app you haved placed to the SD card.

Because  you have place the /data/app folder to the EXT3 partition (/sd-ext/app) you do not move the app to your phone but to your EXT3 partition :)

If this article helps you, please leave a comment below :)
