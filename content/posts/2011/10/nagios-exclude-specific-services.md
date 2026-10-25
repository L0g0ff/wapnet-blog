---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - monitoring
date: "2011-10-28T12:40:36+00:00"
dsq_thread_id: "5141131482"
guid: https://blog.wapnet.nl/?p=717
parent_post_id: null
post_id: "717"
title: 'Nagios: exclude specific services'
url: /2011/10/nagios-exclude-specific-services/

---
With Nagios services check you want include all windows services with status automatic. But some services like the .NET or windows installer services stop sometimes and your monitor turns red. If you want to exclude specific services add this config to the NSC.ini file:

> alias\_service=checkServiceState CheckAll  exclude=sppsvc exclude=someotherservice exclude=ShellHWDetection
