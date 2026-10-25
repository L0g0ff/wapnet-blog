---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - windows
date: "2011-03-17T19:14:29+00:00"
dsq_thread_id: "5353000542"
guid: https://blog.wapnet.nl/?p=543
parent_post_id: null
post_id: "543"
title: Create Acer custom recovery CD
url: /2011/03/create-acer-custom-recovery-cd/

---
My neighbour give me his old laptop  because he have a lot of problems with it. But he gives me only one crappy unbooteble XP cd. After some searching I found on a CD2 Recover image file but the IMG / ghost  file was password protected. I will write down the steps here to create a new recovery cd.

What do you need:

1. Nlite (google)
1. Ghost explorer (Google)

Steps to extract the I386

1. First start Ghost explorer
1. Click File > open > select \*.\*
1. Browse to the CD and select the ACER\\IMAGE\ **WXPNLPER.IMG**
1. Password: **aim1r8**
1. Extract the I386 to a temp folder

Steps to create a CD

1. Start nlite
1. Import the i386 folder
1. When you missing some files you can use this url: [http://www.nu2.nu/download.php?sFile=wxp10.zip](http://www.nu2.nu/download.php?sFile=wxp10.zip)
1. Click on Unattended
1. Click on Bootable CD
1. Click on next twice
1. Insert a blank cd and direct burn it
