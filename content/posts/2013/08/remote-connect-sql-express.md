---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - sql
date: "2013-08-12T12:51:42+00:00"
dsq_thread_id: "5771804080"
guid: https://blog.wapnet.nl/?p=1304
parent_post_id: null
post_id: "1304"
title: Remote connect SQL Express
url: /2013/08/remote-connect-sql-express/

---
1. Start SQL Server Surface Area Configuration > Remote connections
1. [![SQL-Surface](/wp-content/uploads/2013/08/SQL-Surface.png)](/wp-content/uploads/2013/08/SQL-Surface.png)
1. Select "using both TCP/IP and named pipes"
1. Start "SQL Server Configuration Manager"
1. Find out the dynamic port
1. [![SQL-dynamicPort](/wp-content/uploads/2013/08/SQL-dynamicPort.png)](/wp-content/uploads/2013/08/SQL-dynamicPort.png)
1. Now connect to the SQL server from a remote server:
1. HOSTNAMESERVER\\MSSQL$SQLEXP\_VIM,49382
1. [![sql-connect](/wp-content/uploads/2013/08/sql-connect.png)](/wp-content/uploads/2013/08/sql-connect.png)
