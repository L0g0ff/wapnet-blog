---
_thumbnail_id: "2139"
author: thomasf
categories:
  - programmeren
cover:
  alt: excel-work
  image: /wp-content/uploads/2023/08/excel-work.jpg
date: "2023-08-30T09:45:49+00:00"
guid: https://blog.wapnet.nl/?p=2138
parent_post_id: null
post_id: "2138"
title: vlookup with powershell
url: /2023/08/vlookup-with-powershell/

---
I want to use the vlookup excel function within powershell and without data manipulation of the CSV itself. So I wrote a script to import a CSV, find some data and compare these data

```
$CSV = Import-Csv -Path C:\Users\user\some.csv

$trigger = $CSV| Where-Object {$_."Primary Description"  -like "some string with a computername"}
$result = $CSV| Where-Object {$_."Primary Description"  -like "another string with a computername"}

$triggerComputer = foreach ($i in $trigger) {($i."Primary Description" -split " ")[5]}
$resultComputer = foreach ($i in $result) {($i."Primary Description" -split " ")[5]}

Compare-Object $triggerComputer $resultComputer
```

Have fun!
