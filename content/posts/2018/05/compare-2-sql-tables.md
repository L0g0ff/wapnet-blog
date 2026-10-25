---
_edit_last: "1"
author: thomasf
categories:
  - sql
date: "2018-05-15T14:37:01+00:00"
guid: https://blog.wapnet.nl/?p=1799
parent_post_id: null
post_id: "1799"
title: Compare 2 sql tables
url: /2018/05/compare-2-sql-tables/

---
A simple SQL compare is realy easy:

`select * from dbtest02.dbo.article
except
select * from dbtest01.dbo.article`

Source: [https://www.mssqltips.com/sqlservertip/2779/ways-to-compare-and-find-differences-for-sql-server-tables-and-data/](https://www.mssqltips.com/sqlservertip/2779/ways-to-compare-and-find-differences-for-sql-server-tables-and-data/)
