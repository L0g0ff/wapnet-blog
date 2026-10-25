---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
  - windows
date: "2011-07-18T18:22:11+00:00"
dsq_thread_id: "5143296908"
guid: https://blog.wapnet.nl/?p=591
parent_post_id: null
post_id: "591"
tags:
  - nagios
  - parseresponse
  - webinject
title: Troubleshoot (Nagios) Webinject
url: /2011/07/troubleshoot-nagios-webinject/

---
There is a very nice GUI tool to troubeshoot webinject scripts. You can download the tool @ [http://www.webinject.org/download.html](http://www.webinject.org/download.html) for Windows and Linux.

After you extract or install the tool you can change the **globalhttplog** line in the config.xml file to: **<globalhttplog>yes</globalhttplog>** so you get the full debug log.

Note: I found a small memory bug in the GUI when you use the **parseresponse** parameter in your scripts. To workaround this issue the best you can do is restart the tool (file > restart) before you test the scripts.

[![](/wp-content/uploads/2011/07/screenshot_gui_status_win.jpg)](/wp-content/uploads/2011/07/screenshot_gui_status_win.jpg)
