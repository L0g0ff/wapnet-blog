---
_edit_last: "1"
author: thomasf
categories:
  - networking
  - windows
date: "2010-07-28T14:20:55+00:00"
dsq_thread_id: "5214611483"
guid: https://blog.wapnet.nl/?p=385
parent_post_id: null
post_id: "385"
tags:
  - officescan
  - trend-micro
  - trendmicro
title: TrendMicro Officescan 10 on Windows 2008 R2
url: /2010/07/trendmicro-officescan-10-on-windows-2008-r2/

---
When you install Officescan 10 on a Windows 2008 R2 server you get 2 errors:

1. When you login to the webconsole you get the error: Your OfficeScan Session has timed out. Please log in again
1. When you use the remote installerr you get the error: Incorrect parameter in the initialization file

You can fix this problem by change the NTFS rights (Everyone/modify) on the maps.

C:\\Program Files (x86)\\Trend Micro\\OfficeScan\\PCCSRV\\TEMP
C:\\Program Files (x86)\\Trend Micro\\OfficeScan\\PCCSRV\\Web\_OSCE\\Web\_console

Please TrendMicro fix your installer!
