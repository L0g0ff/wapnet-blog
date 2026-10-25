---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - sql
date: "2011-04-22T13:26:18+00:00"
guid: https://blog.wapnet.nl/?p=560
parent_post_id: null
post_id: "560"
title: How to identify your SQL Server version and edition
url: /2011/04/how-to-identify-your-sql-server-version-and-edition/

---
> ```
> SELECT SERVERPROPERTY('productversion'), SERVERPROPERTY ('productlevel'), SERVERPROPERTY ('edition')
> ```
