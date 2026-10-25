---
_edit_last: "1"
author: thomasf
categories:
  - windows
date: "2016-10-13T19:41:16+00:00"
dsq_thread_id: "5281772960"
guid: https://blog.wapnet.nl/?p=1709
parent_post_id: null
post_id: "1709"
title: 'BSOD Domain Controller STOP: c00002e2 Directory Services could not start'
url: /2016/10/bsod-domain-controller-stop-c00002e2-directory-services-could-not-start/

---
Today our domain controller had a very bad day and had a bootloop after a reboot. I used recording software to capture the blue screen error: **STOP: c00002e2 Directory Services could not start**

Then we found a nice article to fix this issue. We had a second working domain controller so if you have the same setup you can use this how to, to fix this problem also. All the credits go to [dbutch1976](https://social.technet.microsoft.com/profile/dbutch1976/?ws=usercard-mini)

1. Restart the server and press F8 key, select Directory Services restore mode.
1. Log in with the local administrator username and password (hope you remember what you set it to!).
1. Type cd \\windows\\system32
1. type NTDSUTIL
1. type activate instance NTDS
1. type files
1. If you encounter an error stating that the Jet engine could not be initialized exit out of ntdsutil.
1. type cd\
1. type md backupad
1. type cd \\windows\\ntds
1. type copy ntds.dit c:\\backupad
1. type cd \\windows\\system32
1. type esentutl /g c:\\windows\\ntds\\ntds.dit
1. This will perform an integrity check, (the results indicate that the jet database is corrupt)
1. Type esentutl /p   c:\\windows\\ntds\\ntds.dit
1. Agree with the prompt
1. type cd \\windows\\ntds
1. type move \*.log c:\\backupad   (or just delete the log files)

This should complete the repair.  To verify that the repair has worked successfully:

1. type cd \\windows\\system32
1. type ntdsutil
1. type activate instance ntds
1. type files        (you should no longer get an error when you do this)
1. type info       (file info should now appear correctly)

Source: [https://social.technet.microsoft.com/Forums/windowsserver/en-US/771b97ad-4e1c-4e7c-8617-91601224dd7f/server-core-2008-r2-blue-screen?forum=winserverManagement](https://social.technet.microsoft.com/Forums/windowsserver/en-US/771b97ad-4e1c-4e7c-8617-91601224dd7f/server-core-2008-r2-blue-screen?forum=winserverManagement)
