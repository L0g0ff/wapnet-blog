---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - windows
date: "2010-11-03T21:19:33+00:00"
dsq_thread_id: "5138757509"
guid: https://blog.wapnet.nl/?p=447
parent_post_id: null
post_id: "447"
title: Sysprep error Windows 2008 r2 and Windows 7
url: /2010/11/sysprep-error-windows-2008-r2-and-windows-7/

---
You can only run sysprep twice. If you get an error the 3rd time follow these steps to fix it:

> 1.     Change the following Registry key value of **GeneralizationState** to 7.
>
> **HKLM\\System\\Setup\\Status\\SysprepStatus**
>
> 2.     Run 'msdtc -uninstall' and 'msdtc -install' to repair the DTC installation.
>
> 3.     Then re-run sysprep again and see if the issue is resolved.
