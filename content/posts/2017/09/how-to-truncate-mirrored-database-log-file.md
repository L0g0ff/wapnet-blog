---
_edit_last: "1"
_thumbnail_id: "1774"
author: thomasf
categories:
  - sql
cover:
  alt: viewer
  image: /wp-content/uploads/2017/09/viewer.png
date: "2017-09-28T09:23:15+00:00"
dsq_thread_id: "6176523369"
guid: https://blog.wapnet.nl/?p=1769
parent_post_id: null
post_id: "1769"
title: How to truncate Mirrored Database Log File
url: /2017/09/how-to-truncate-mirrored-database-log-file/

---
First backup your transaction logging:

1. Tasks > Backup [![](/wp-content/uploads/2017/09/sql3.jpg)](/wp-content/uploads/2017/09/sql3.jpg)
1. Select transactionlog backup en select a disk where to backup [![](/wp-content/uploads/2017/09/SQL2.jpg)](/wp-content/uploads/2017/09/SQL2.jpg)
1. Now check the status with **DBCC LOGINFO(DATABASENAME)**
1. Check if the last status record is 0 (zero)![](/wp-content/uploads/2017/09/SQL1-1.jpg)
1. When the status is 2 make another backup
1. When the status is 0 you can run: **DBCC SHRINKFILE(2)**

You can use this script also:
`Backup LOG DBNAME
TO DISK = 'C:\SQL_TMP\transactionlog.trn'
WITH STATS
GO
DBCC LOGINFO(DBNAME)
DBCC SHRINKFILE(2)`
