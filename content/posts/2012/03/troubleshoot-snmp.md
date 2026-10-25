---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
  - networking
date: "2012-03-07T12:47:20+00:00"
dsq_thread_id: "5322987476"
guid: https://blog.wapnet.nl/?p=803
parent_post_id: null
post_id: "803"
title: Troubleshoot SNMP
url: /2012/03/troubleshoot-snmp/

---
If you want to know what a specific SNMP value must be, snmpwalk is your friend :)

> snmpwalk -v1 -c _<snmp community name>_ -On _<ip server>_ 1.3

 [Download SNMPWALK for windows](http://www.snmpsoft.com/freetools/snmpwalk.html)
