---
_edit_last: "1"
author: thomasf
categories:
  - networking
  - windows
date: "2008-10-15T21:00:15+00:00"
guid: https://blog.wapnet.nl/?p=120
parent_post_id: null
post_id: "120"
title: Terminal server memory solutions
url: /2008/10/terminal-server-high-memory-solutions/

---
Many terminalservers have an memory problem. You easily can write a fix for it with a simple but powerful Windows 2003 server resource kit tool.

- First download the [resource kit](http://www.microsoft.com/downloads/details.aspx?FamilyID=9D467A69-57FF-4AE7-96EE-B18C4790CFFD&displaylang=en)

- Then copy empty.exe from the resource kit to c:\\scripts\\freemem or something

- Write a batch file c:\\scripts\\freemem\\freemem.bat

Example batch file:

> @echo off
>
> c:\\scripts\\freemem\\empty.exe iexplore.exe
> c:\\scripts\\freemem\\empty.exe outlook.exe
> c:\\scripts\\freemem\\empty.exe winword.exe

Run this script every 30 minutes en you have al lot of extra memory to spent :)

Also add the /PAE to your boot.ini to get 700mb extra (if you have 4 gig of ram). See [this support article](http://support.microsoft.com/kb/283037/)

Good luck!
