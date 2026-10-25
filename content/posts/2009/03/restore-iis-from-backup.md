---
_edit_last: "1"
author: thomasf
categories:
  - iis
date: "2009-03-11T07:31:17+00:00"
dsq_thread_id: "5653781318"
guid: https://blog.wapnet.nl/?p=175
parent_post_id: null
post_id: "175"
tags:
  - iis
  - restore
title: Restore IIS from backup
url: /2009/03/restore-iis-from-backup/

---
- Give a IISRESET /STOP
- Browse to C:\\Windows\\System32\\Inetsrv\
- Rename the Histroy folder to History.old
- Rename the metabase.xml to metabase.xml.old
- Rename the mbschema.xml to mbschema.xml.old
- Place the following files from the backup: metabase.xml, mbschema.xml & Histrory to the C:\\Windows\\System32\\Inetsrv\ folder
- Giva a IISRESET /START
