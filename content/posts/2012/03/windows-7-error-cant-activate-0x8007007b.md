---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - windows
date: "2012-03-08T19:32:47+00:00"
dsq_thread_id: "5136178891"
guid: https://blog.wapnet.nl/?p=808
parent_post_id: null
post_id: "808"
title: Windows 7 error can't activate 0x8007007B
url: /2012/03/windows-7-error-cant-activate-0x8007007b/

---
After a clean windows 7 installation with [Novicorp WintoFlash](/2012/01/easiest-way-to-install-windows-bartpe-xp-2003-vista-7-or-8-on-a-usb-flash-drive/ "Easiest way to install Windows BartPE, XP, 2003, Vista, 7 or 8 on a USB flash drive") of  could not activate correctly. I'll get error the error: 0x8007007B

The easiest way to fix this problem is re-register the Windows key with the following steps:

1. Click on the Start Button and type: **CMD**(into the 'Search programs and files' field in the Start Menu)
1. The Start Menu will show 'CMD.exe',
1. Right-click the CMD.exe file and select Run As Administrator.
1. In the CMD window, type: **slmgr.vbs -ipk <type your product key here>**
1. To activate windows after changing the key, type: **slmgr.vbs -ato**
