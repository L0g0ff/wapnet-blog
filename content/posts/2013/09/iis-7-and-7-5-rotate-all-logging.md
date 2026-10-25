---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - iis
date: "2013-09-06T08:13:37+00:00"
dsq_thread_id: "5140037566"
guid: https://blog.wapnet.nl/?p=1313
parent_post_id: null
post_id: "1313"
title: IIS 7 and 7.5 rotate all logging
url: /2013/09/iis-7-and-7-5-rotate-all-logging/

---
- start powershell
- set-executionpolicy remotesigned
- Create a script with notepad


```
get-childitem -Path C:\inetpub\logs\LogFiles -recurse |
where-object {$_.lastwritetime -lt (get-date).addDays(-90)} |
Foreach-Object { del $_.FullName }
```


- Save the script @ c:\\scripts\\del\_old\_logs.ps1
- start cmd
- run: powershell.exe c:\\scripts\\del\_old\_logs.ps1  -noprofile -Noninteractive
- If you get a "child" question press A
- Start task scheduler
- Schedule the task
- program powershell
- c:\\scripts\\del\_old\_logs.ps1  -noprofile -Noninteractive

[![Sheduled Task](/wp-content/uploads/2013/09/Sheduled-Task.png)](/wp-content/uploads/2013/09/Sheduled-Task.png)

- Run the task wheter user is logged on or not
- Highest privileges **not needed**
