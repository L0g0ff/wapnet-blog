---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - sql
  - windows
date: "2012-04-11T13:33:51+00:00"
dsq_thread_id: "5136178972"
guid: https://blog.wapnet.nl/?p=853
parent_post_id: null
post_id: "853"
tags:
  - rendering
title: SQL Reporting Services slow with Internet Explorer
url: /2012/04/sql-reporting-services-slow-with-internet-explorer/

---
When you access the reporting services over SSL you can have the problem that the reporting services GUI under IE is very slow.

The solution is quite simple: Login with the servername or domain name. E.g: SERVERNAME\\username

This problem exist under IE 8 and IE9 under Server 2008, 2008r2, Vista and Windows 7.
