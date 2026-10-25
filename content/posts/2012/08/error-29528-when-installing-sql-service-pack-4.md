---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - sql
date: "2012-08-01T22:01:35+00:00"
dsq_thread_id: "5136179119"
guid: https://blog.wapnet.nl/?p=956
parent_post_id: null
post_id: "956"
title: Error 29528 When Installing SQL Service Pack 4
url: /2012/08/error-29528-when-installing-sql-service-pack-4/

---
Today I had this problem for the second time. Last time it cost me 3 hours to find the solution. Now I find your article and I fixed it in 30 minutes :)

My Exact error was (summary.txt):
MSP Error: 29528  The setup has encountered an unexpected error while Setting Internal Properties. The error is: Fatal error during installation.

The workaround resolution involves the following steps:

**For a stand-alone installation of SQL Server 2005**

- Remove the following registry subkeys that store SID settings:
  - HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Microsoft SQL Server\\MSSQL. _X_\\Setup\\SQLGroup

  - HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Microsoft SQL Server\\MSSQL. _X_\\Setup\\AGTGroup

  - HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Microsoft SQL Server\\MSSQL. _X_\\Setup\\FTSGroup

  - HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Microsoft SQL Server\\MSSQL. _X_\\Setup\\ASGroup

**Note** In these registry subkeys, MSSQL. _X_ is a placeholder for the corresponding value on a specific system. You can determine MSSQL. _X_ on a specific system by examining the value of the MSSQLSERVER registry entry under the following registry subkey:

- Reinstall the SQL Server 2005 service pack or the SQL Server 2005 hotfix package.

For some reason, the local SIDs had been changed or removed or something and SQL just needed to figure out what was going on.

HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Microsoft SQL Server\\Instance Names\\SQL\

Official source: [http://www.conetrix.com/Blog/post/Error-29528-When-Installing-SQL-Server-Hotfix.aspx](http://www.conetrix.com/Blog/post/Error-29528-When-Installing-SQL-Server-Hotfix.aspx)
