---
_edit_last: "1"
_thumbnail_id: "1485"
author: thomasf
categories:
  - android
cover:
  alt: android-bricks-in-the-wall
  image: /wp-content/uploads/2014/01/android-bricks-in-the-wall.jpg
date: "2014-01-07T15:02:34+00:00"
dsq_thread_id: "5150919078"
guid: https://blog.wapnet.nl/?p=1483
parent_post_id: null
post_id: "1483"
title: HTC One "Un-Brick" steps
url: /2014/01/htc-one-un-brick-steps/

---
Steps to take if you have an bootloop after a wrong ROM update

Requirements:

1. First off all your device must be unlocked
1. HTC Sync manager (install it)@ [http://www.htc.com/www/software/htc-sync-manager/](http://www.htc.com/www/software/htc-sync-manager/)
1. [MiniSDK](http://goo.gl/T6InE) (extract to C:\\mini-sdk)
1. Download recovery image and place the file in C:\\mini-sdk\ @ [http://clockworkmod.com/rommanager](http://clockworkmod.com/rommanager)
1. [New ROM](http://android-revolution-hd.blogspot.nl/p/android-revolution-hd-mirror-site-var.html) and place the zip in C:\\mini-sdk

- Shutdown your phone to hold it in direct light and hold down the power button
- When the power is off hold down volume and press the power button
- Select fastboot
- Connect the device with your pc
- start cmd.exe

`cd c:\mini-sdk
fastboot flash recovery recovery-clockwork-6.0.3.1-m7.img
`

- select recovery on your phone and recovery-clockwork will start
- in clockwork recovery "activate ADB siteload"
- Now give this command from your pc

`
adb sideload Android_Revolution_HD-One_31.6.zip
`

- Follow the wizard on screen
