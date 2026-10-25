---
_disable_fbc: ""
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - iis
date: "2016-08-25T13:50:41+00:00"
dsq_thread_id: "5258568659"
guid: https://blog.wapnet.nl/?p=1300
parent_post_id: null
post_id: "1300"
title: IIS Log Analyzer
url: /2016/08/iis-log-analyzer/

---
Download [Log Parser 2.2](http://www.microsoft.com/en-us/download/details.aspx?id=24659) from the microsoft site. After the installation [google](https://www.google.nl/search?q=Log+Parser+2.2+iis+examples) is your friend

Example

Hits on a particular page by IP address


```
LogParser -i:IISW3C "SELECT c-ip, COUNT(*) As Hits FROM C:\WINDOWS\system32\LogFiles\temp\*.log WHERE EXTRACT_FILENAME(cs-uri-stem) = 'default.aspx' AND sc-status = '200' GROUP BY c-ip Order by Hits DESC" -o:DataGrid
```


Another great way to analyse log files is the tool: [Log Parser Studio.](https://gallery.technet.microsoft.com/Log-Parser-Studio-cd458765) With this tool you can easy query loggings with a GUI:

[![2016-08-25 15_49_33-How To_ Move Music from iPod to PC in 5 Easy Steps](/wp-content/uploads/2013/07/2016-08-25-15_49_33-How-To_-Move-Music-from-iPod-to-PC-in-5-Easy-Steps.png)](/wp-content/uploads/2013/07/2016-08-25-15_49_33-How-To_-Move-Music-from-iPod-to-PC-in-5-Easy-Steps.png)
