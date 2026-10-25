---
_edit_last: "1"
author: thomasf
categories:
  - windows
date: "2011-08-17T12:44:05+00:00"
dsq_thread_id: "5221821068"
guid: https://blog.wapnet.nl/?p=619
parent_post_id: null
post_id: "619"
title: Easiest way to delete old files
url: /2011/08/easiest-way-to-delete-old-files/

---
For specific files
`FORFILES /P "C:\MyPath\" /S /M log*.xml /D -30 /C "cmd /c del @file"`

For files and subfolders:
`FORFILES /P "C:\MyPath\" /S /D -30 /C "cmd /c IF @isdir == TRUE rd /S /Q @path"`
