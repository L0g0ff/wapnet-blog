---
_edit_last: "1"
author: thomasf
categories:
  - uncategorized
date: "2008-12-04T14:40:43+00:00"
dsq_thread_id: "5161420565"
guid: https://blog.wapnet.nl/?p=153
parent_post_id: null
post_id: "153"
title: Enable EWF after Norton Ghost Restore
url: /2008/12/enable-ewf-after-norton-ghost-restore/

---
To deal with the failed ewf function after Norton Ghost cloning,
you should keyin the command below

C:\\rundll32 ewfdll.dll,ConfigureEwf
Notice: the "ConfigureEwf" parameter is casesensitive.

Then the ewf will re-initialized after rebooting.
Check the state, by using check command like C:\\ewfmgr C:

Source: http://www.pcreview.co.uk/forums/thread-523966.php
