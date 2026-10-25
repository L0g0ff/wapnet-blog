---
_disable_fbc: ""
_edit_last: "1"
_thumbnail_id: "1662"
author: thomasf
categories:
  - windows
cover:
  alt: Closed-loop-marketing-blog
  image: /wp-content/uploads/2015/08/Closed-loop-marketing-blog.png
date: "2015-08-27T11:11:56+00:00"
dsq_thread_id: "5196259989"
guid: https://blog.wapnet.nl/?p=1659
parent_post_id: null
post_id: "1659"
title: Windows update is looping forever
url: /2015/08/windows-update-is-looping-forever/

---
On my windows 2008 r2 server, Windows update was running forever :(

[![Windows update - Fix - 2](/wp-content/uploads/2015/08/Windows-update-Fix-2.png)](/wp-content/uploads/2015/08/Windows-update-Fix-2.png)

I tried a lot of things but fixing the problem was really simple:

1. Go to [https://support.microsoft.com/en-us/kb/971058](https://support.microsoft.com/en-us/kb/971058)
1. Download the fixit
1. Run the fixit and follow the wizard

Then your problem will be fixed automatically :)

Still problems? Try this post: [http://superuser.com/questions/951960/windows-7-sp1-windows-update-stuck-checking-for-updates](http://superuser.com/questions/951960/windows-7-sp1-windows-update-stuck-checking-for-updates) **Note:** If you have a WSUS server and you still have problems to find windows updates you can try to temporary disable the WSUS client to change the registry key UseWUServer to dword:00000000
`
[HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU]
"UseWUServer"=dword:00000000
` [![Windows update - Fix](/wp-content/uploads/2015/08/Windows-update-Fix.png)](/wp-content/uploads/2015/08/Windows-update-Fix.png)
