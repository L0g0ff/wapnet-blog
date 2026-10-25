---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - windows
date: "2011-10-03T20:50:27+00:00"
dsq_thread_id: "5136178434"
guid: https://blog.wapnet.nl/?p=682
parent_post_id: null
post_id: "682"
tags:
  - corrupt
  - file-missing
  - system
  - windows-xp
title: '[WINXP] \WINDOWS\SYSTEM32\CONFIG\SYSTEM missing or corrupt'
url: /2011/10/winxp-windowssystem32configsystem-missing-or-corrupt/

---
If you get the error \\WINDOWS\\SYSTEM32\\CONFIG\\SYSTEM missing or corrupt you can follow these steps to fix this problem:

[![](/wp-content/uploads/2011/10/windows-system-missing-or-corrupt.png)](/wp-content/uploads/2011/10/windows-system-missing-or-corrupt.png)

- Boot a linux distribution of your choice. I prefer Ubuntu
- Mount your windows partition
- If exist rename (or move) the corrupt file \\WINDOWS\\SYSTEM32\\CONFIG\\SYSTEM to \\WINDOWS\\SYSTEM32\\CONFIG\\SYSTEM.old
- Now open the folder "system volume information\\restore (with some numbers)\\RP (with a number)\\snapshot.
- Copy the file \_REGISTRY\_MACHINE\_SYSTEM to \\WINDOWS\\SYSTEM32\\CONFIG\\\_REGISTRY\_MACHINE\_SYSTEM
- Rename \\WINDOWS\\SYSTEM32\\CONFIG\\\_REGISTRY\_MACHINE\_SYSTEM to \\WINDOWS\\SYSTEM32\\CONFIG\\SYSTEM
- Restart the computer and you will see Windows is starting again :)
- Now point to start > programs > accessories > system tools > system restore
- Restore your windows a couple of days earlier

If you don't restore you windows you must manually fix the file permissions. Everything looks fine but if you see your event viewer you see a lot of (networking) profile troubles.

You can do the same trick with

\_REGISTRY\_USER\_DEFAULT
\_REGISTRY\_MACHINE\_SECURITY
\_REGISTRY\_MACHINE\_SOFTWARE
\_REGISTRY\_MACHINE\_SYSTEM
\_REGISTRY\_MACHINE\_SAM

MS Support article: [http://support.microsoft.com/kb/307545](http://support.microsoft.com/kb/307545)
My inspiration for this article: [http://forum.computeridee.nl/showthread.php?t=48294](http://forum.computeridee.nl/showthread.php?t=48294) (Dutch)
