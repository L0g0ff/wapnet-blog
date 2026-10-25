---
_edit_last: "1"
author: thomasf
categories:
  - sql
date: "2009-01-14T20:05:47+00:00"
guid: https://blog.wapnet.nl/?p=170
parent_post_id: null
post_id: "170"
title: mysql restore (under Windows)
url: /2009/01/mysql-restore-under-windows/

---
Hi,

If you want to use mysqldump to back up the database, you can enter the full path when typing the command, or add the path c:\\wamp\\bin\\mysql\\mysql5.0.51b\\bin to the System variable PATH in Control Panel - System - Advanced - Environment Variables - System variables.

You can make a backup from the command line or a scheduled task in Windows like this, assuming that myusername and mypassword have access to the database mydatabase:

mysqldump -umyusername -pmypassword mydatabase > mydatabase.sql

You can restore the database using the mysql command from the command line:

mysql -umyusername -pmypassword -D mydatabase < mydatabase.sql

More info from the command line:
mysql --help \| more
