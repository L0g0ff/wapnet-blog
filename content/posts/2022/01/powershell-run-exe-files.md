---
author: thomasf
categories:
  - powershell
date: "2022-01-01T17:22:14+00:00"
guid: https://blog.wapnet.nl/?p=2013
parent_post_id: null
post_id: "2013"
title: Powershell run *.exe files
url: /2022/01/powershell-run-exe-files/

---
There are 2 ways to run an executable within powershell without any errors

`$exe = 'C:\scripts\Everything.exe'
$param1 = '-reindex'
& $exe $param1`

Or with a --% attribute

`C:\windows\system32\sc.exe --% qc bits`
