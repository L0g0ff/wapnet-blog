---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - android
  - mobile
date: "2010-09-06T08:17:03+00:00"
dsq_thread_id: "5155146674"
guid: https://blog.wapnet.nl/?p=394
parent_post_id: null
post_id: "394"
title: How to root HTC Desire from from official 2.2 Froyo firmware
url: /2010/09/how-to-root-htc-desire-from-from-official-2-2-froyo-firmware/

---
Source: [http://www.android-tutorials.org/dev/?page\_id=78](http://www.android-tutorials.org/dev/?page_id=78)

I make some small additions because the original article was not very clear at the USB installation.

DONT USE THIS WITH HBOOT 0.83 or 0.93 SLCD DEVICES!!!
OTHERWISE YOUR PHONE WILL END UP WITH A DEAD SCREEN!

**Overview**

1. **Requirements**
1. **Step 1 – downgrade** (Video: [Step 1 on youtube](http://www.youtube.com/watch?v=VdWt65tUBVc))
1. **Step 2 – root with unrevoke recovery**
1. **Step 3 – repair /misc partition** (Video: [Step 3-4 on youtube](http://www.youtube.com/watch?v=T88G3px7Ztc))
1. **Step 4 – flash custom or stock rom**

Please follow this step-by-step tutorial to go back to HBOOT 0.80

**!!!! ROOTING / FLASHING / DOWNGRADING IS ALWAYS ON YOUR OWN RISK !!!!** **Attention:** This method will completely wipe your phone!!!

**Requirements**

1. Make a NEW Goldcard ([here](http://android.modaco.com/content/general-discussion/305672/creating-a-goldcard/#entry1233023)) depending on your device (branded or not)
It can be that your CID has changed so you have to make a new goldcard. You can try your existing card as well!
1. [MIRROR Download PB99IMG.zip (DE)](http://www.android-tutorials.org/dev/?page_id=30&did=2) [MIRROR by Shipped-Roms](http://shipped-roms.com/shipped/Bravo/PB99IMG_Bravo_HTC_WWE_1.21.405.2_Radio_32.36.00.28U_4.06.00.02_2_release_126984_signed_txt.zip) [MIRROR 2](http://files.bestblog.de/desire/PB99IMG_Bravo_HTC_WWE_1.21.405.2_Radio_32.36.00.28U_4.06.00.02_2_release_126984_signed_txt.zip) [MIRROR by AdamG (UK)](http://android.adamg.co.uk/bravo/roms/PB99IMG.zip)
1. Rename the downloaded file to **PB99IMG.zip** \[NOT zip.zip !!!\] and copy it to the root directory of your SD Card. (Just to your SD Card, NOT into any subdirectory!)
1. Download this [misc\_update.zip](http://www.android-tutorials.org/dev/?page_id=30&did=1) to repair your misc partition in Step 3 and copy it to your SD card as well.
1. Download your desired ROM (custom or stock whatever you like) and copy it to your SD Card. Don’t name it update.zip!

**Step 1 – downgrade** (Video: [Step 1 on youtube](http://www.youtube.com/watch?v=VdWt65tUBVc))

1. Shutdown your device
1. Hold volume DOWN and press power button
1. Wait until **PB99IMG.ZIP** was found and verfied. If that fails, check if you named the file the right way and it’s located in the root of your SD.
1. Press volume UP to start the update.
1. Wait until all steps are done. DON’T POWER OFF YOUR DEVICE!
1. After the downgrade progress has finished press volume UP to reboot.
1. When the phone has started mount SD card and REMOVE PB99IMG.zip
1. Unmount SD card and continue with the next step…

**Step 2 – root with unrevoke recovery**

1. Uninstall HTC Sync completely
1. Download unrevoke recovery [here](http://downloads.unrevoked.com/recovery/3.1/reflash_package.exe)
1. Enable USB debugging on your phone (under settings > applications > developments >USB Debugging).
1. Download the unrevoke recovery USB driver [here](http://www.unrevoked.com/recovery/android-usb-driver.zip)
1. Install the drivers when the phone is in debug mode
1. Install the drivers when the phone is in boot mode (shutdown > press volume down > power button)
1. Start unrevoke and follow the instructions
1. If unrevoke has finished you should be in custom recovery.

**Step 3 – repair /misc partition** (Video: [Step 3-4 on youtube](http://www.youtube.com/watch?v=T88G3px7Ztc))

1. You are still in custom recovery mode
1. Select ‘ _install zip from sdcard_‘ (Use Vol + and – to navigate and trackball)
1. Select ‘ _choose zip from sdcard_‘
1. Select ‘ _misc\_update.zip_‘ from SD und confirm it with yes. Maybe you have to scroll down till you can see the file!
1. After that your /misc partition should be repaired
1. Go Back to custom Recovery menu.

**Step 4 – flash custom or stock ROM**

1. You are still in custom recovery mode
1. Select ‘ _install zip from sdcard_‘ (Use Vol + and – to navigate and trackball)
1. Select ‘ _choose zip from sdcard_‘
1. Select your desired ROM Zip-file from SD und confirm it with yes. Maybe you have to scroll down till you can see the file!
1. After the flashing progress has finished use the back key and then select reboot. This may take some minutes.
1. Congratulations. Now you have a re-rooted HTC Desire with HBOOT 0.80
