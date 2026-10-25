---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - windows
date: "2011-11-10T08:17:02+00:00"
dsq_thread_id: "5136178579"
guid: https://blog.wapnet.nl/?p=722
parent_post_id: null
post_id: "722"
title: Create a BartPE bootable USB stick
url: /2011/11/create-a-bartpe-bootable-usb-stick/

---
\[banner\]

**Requirements:**
\- USB Stick
\- BartPE CD (or BartPE source)
\- Download Bootable USB-Drive Utility @ [http://www.911cd.net/forums//index.php?showtopic=21702](http://www.911cd.net/forums//index.php?showtopic=21702)
\- Download WinUSB\_FULL Patcher @ [http://www.megaupload.com/?d=AEC0GAMM](http://www.megaupload.com/?d=AEC0GAMM) **Steps:**
1\. Extract Bootable USB-Drive
2\. Open Config\_SourcePath.cmd
3\. REM set SourcePath="..\\BartPE"
4\. set SourceCD=G: where G: the cd-rom drive is with the BartPE CD
5\. Start BOOTABLE\_USB-DRIVE.cmd
6\. Format and create the USB drive
7\. Close the utillity en extract de WinUSB\_FULL Patcher
8\. Run the patcher on the USB drive (root)

The patcher patch the ntdetect.com file. When you don't run the patcher you will get a 0x0000007b BSOD when you boot from the BartPE USB.

[![](/wp-content/uploads/2011/11/Bootable_USB-Drive.cmd_.jpg)](/wp-content/uploads/2011/11/Bootable_USB-Drive.cmd_.jpg)

\[banner\]
