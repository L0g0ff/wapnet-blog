---
_edit_last: "1"
author: thomasf
categories:
  - linux
date: "2010-07-08T07:37:39+00:00"
dsq_thread_id: "5288319474"
guid: https://blog.wapnet.nl/?p=378
parent_post_id: null
post_id: "378"
title: Create a second root account
url: /2010/07/create-a-second-root-account/

---
Sometimes you can't give someone the root password but you he/she must have root access. You can follow this steps to create a additional root account:
Add a new user:

**\# useradd newuser**

Set a password for the new user

**\# passwd newuser**

Once done, edit the 'passwd' file

**\# nano /etc/passwd**

set the UID:GUD bits to 0:0. Say for example the new user is 'newuser', the line should look like

**newuser:x:0:0::/home/newuser:/bin/bash**
﻿
