---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - sql
date: "2008-02-20T16:19:32+00:00"
dsq_thread_id: "5303096554"
guid: https://blog.wapnet.nl/?p=18
parent_post_id: null
post_id: "18"
tags:
  - howto
  - log
  - shrink
  - sql
  - transaction
title: How to shrink a SQL Transaction Log
url: /2008/02/how-to-shrink-a-sql-transaction-log/

---
For 2005:
\-\-\\* you can get the logical log file name usingthe following command in Query Analizer:

```sql
exec "databaseName".dbo.sp_helpfile
```

Now execute the following command to shrink the database log to 200MB:

```sql
DBCC SHRINKFILE ("logicalLogFileName", 200)
BACKUP LOG "databaseName" WITH TRUNCATE_ONLY
DBCC SHRINKFILE ("logicalLogFileName", 200)
```

--if it doesn't work, run the two commands again.

--When done with that, do a full backup of your db as you will have broken your tlog backup chain.

For 2008+

```sql
USE databasename;
GO
-- Truncate the log by changing the database recovery model to SIMPLE.
ALTER DATABASE databasename
SET RECOVERY SIMPLE;
GO
-- Shrink the truncated log file to 1 MB.
DBCC SHRINKFILE (2, 1); -- here 2 is the file ID for trasaction log file,you can also mention the log file name (dbname_log)
GO
-- Reset the database recovery model.
ALTER DATABASE databasename
SET RECOVERY FULL;
GO
```

