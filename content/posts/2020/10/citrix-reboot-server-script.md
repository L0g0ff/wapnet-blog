---
_thumbnail_id: "1866"
author: thomasf
categories:
  - citrix
cover:
  alt: Shell
  image: /wp-content/uploads/2020/10/Shell.png
date: "2020-10-15T20:41:55+00:00"
guid: https://blog.wapnet.nl/?p=1859
parent_post_id: null
post_id: "1859"
title: Citrix reboot server script
url: /2020/10/citrix-reboot-server-script/

---
This Citrix script will reboot all the servers with the tags SomeTag or SomeOtherTag and are in maintenance mode. Have fun!


```powershell
$machines=Get-BrokerMachine | Where-Object {($_.Tags -eq "SomeTag" -or $_.Tags -eq "SomeOtherTag") -and ($_.InMaintenanceMode -eq "True")}
Foreach($machine in $machines)
{New-BrokerHostingPowerAction -Action Restart -MachineName $machine.Machinename}
```

