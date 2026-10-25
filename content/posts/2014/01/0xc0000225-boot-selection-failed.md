---
_edit_last: "1"
author: thomasf
categories:
  - windows
date: "2014-01-30T09:31:55+00:00"
dsq_thread_id: "5140165355"
guid: https://blog.wapnet.nl/?p=1486
parent_post_id: null
post_id: "1486"
title: 0xc0000225 - Boot selection failed because a required device is inaccessible
url: /2014/01/0xc0000225-boot-selection-failed/

---
When you run Acronis version 10 on a Windows 2008 R2 you get the error "0xc0000225 - Boot selection failed because a required device is inaccessible.

To fix this problem:

1. Boot Windows 2008 R2 CD
1. Select repair
1. Run command line
1. Now run these commands

**Bootrec /fixmbr** **Bootrec /fixboot** **Bootrec /rebuildbcd**

Reboot the server and your windows is running again.

Source: [http://www.qliktips.com/2012/11/fix-windows-8-boot-issue.html](http://www.qliktips.com/2012/11/fix-windows-8-boot-issue.html)
