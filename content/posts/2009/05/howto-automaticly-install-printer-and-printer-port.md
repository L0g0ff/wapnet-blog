---
_edit_last: "1"
author: thomasf
categories:
  - programmeren
date: "2009-05-05T21:16:48+00:00"
guid: https://blog.wapnet.nl/?p=191
parent_post_id: null
post_id: "191"
title: 'Howto: Automaticly install printer and printer port'
url: /2009/05/howto-automaticly-install-printer-and-printer-port/

---
First create a port:
`
cscript %windir%\system32\prnport.vbs -a -s localhost -r IP_10.31.32.100 -h 10.31.32.100 -o raw -n 9100
`

Then create a printer:
`
rundll32 printui.dll,PrintUIEntry /if /b "Some Printer Name" /f C:\DEV\pcl5e_5c\P52KHAL.inf /r "IP_10.31.32.100" /m "Canon iR 3100C EUR PCL5c"
`

For more info try the /? commands
