---
author: thomasf
categories:
  - powershell
  - windows
date: "2022-05-10T09:55:46+00:00"
guid: https://blog.wapnet.nl/?p=2063
parent_post_id: null
post_id: "2063"
title: Configure WSUS client with Powershell and Regedit
url: /2022/05/configure-wsus-client-with-powershell-and-regedit/

---
My use case for a customer was to configure WSUS for a couple of DMZ servers. The DMZ servers are not domain-joined. So I create a PowerShell script to configure the registry so I can easily deploy the settings to the servers.

You can use this script also for non domain-joined servers

```
# Script for WSUS configuration on non-domain joined servers

# First stop the Windows service
Get-Service -name wuauserv | stop-service

# Variables
$registryPath = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate"
$name1 = "TargetGroup"
$value1 = "Production"
$name2 = "WUServer"
$value2 = "http://wsus.domain.local:8530"
$name3 = "WUStatusServer"
$value3 = "http://wsus.domain.local:8530"
$name4 = "DoNotConnectToWindowsUpdateInternetLocations"
$value4 = "1"
$name5 = "TargetGroupEnabled"
$value5 = "1"
$registryPathAU = "HKLM:\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU"
$nameAU1 = "AUOptions"
$valueAU1 = "3"
$nameAU2 = "UseWUServer"
$valueAU2 = "1"

# Inject registry
IF(!(Test-Path $registryPath))
{
    New-Item -Path $registryPath -Force | Out-Null
    New-ItemProperty -Path $registryPath -Name $name1 -Value $value1 -Force | Out-Null
    New-ItemProperty -Path $registryPath -Name $name2 -Value $value2 -Force | Out-Null
    New-ItemProperty -Path $registryPath -Name $name3 -Value $value3 -Force | Out-Null
    New-ItemProperty -Path $registryPath -Name $name4 -Value $value4 -PropertyType DWORD -Force | Out-Null
    New-ItemProperty -Path $registryPath -Name $name5 -Value $value5 -PropertyType DWORD -Force | Out-Null
}
ELSE
{
    New-ItemProperty -Path $registryPath -Name $name1 -Value $value1 -Force | Out-Null
    New-ItemProperty -Path $registryPath -Name $name2 -Value $value2 -Force | Out-Null
    New-ItemProperty -Path $registryPath -Name $name3 -Value $value3 -Force | Out-Null
    New-ItemProperty -Path $registryPath -Name $name4 -Value $value4 -PropertyType DWORD -Force | Out-Null
    New-ItemProperty -Path $registryPath -Name $name5 -Value $value5 -PropertyType DWORD -Force | Out-Null
}
IF(!(Test-Path $registryPathAU))
{
    New-Item -Path $registryPathAU -Force | Out-Null
    New-ItemProperty -Path $registryPathAU -Name $nameAU1 -Value $valueAU1 -PropertyType DWORD -Force | Out-Null
    New-ItemProperty -Path $registryPathAU -Name $nameAU2 -Value $valueAU2 -PropertyType DWORD -Force | Out-Null
    }
ELSE
{
    New-ItemProperty -Path $registryPathAU -Name $nameAU1 -Value $valueAU1 -PropertyType DWORD -Force | Out-Null
    New-ItemProperty -Path $registryPathAU -Name $nameAU2 -Value $valueAU2 -PropertyType DWORD -Force | Out-Null
}

# Start the Windows service
Get-Service -name wuauserv | start-service

# Find updates and report to the WSUS server
$updateSession = new-object -com "Microsoft.Update.Session"; $updates=$updateSession.CreateupdateSearcher().Search($criteria).Updates
Start-sleep -seconds 10
wuauclt /detectnow
wuauclt /reportnow
c:\windows\system32\UsoClient.exe startscan
```

I save this file on the WSUS server itself at `http://wsus.domain.local:8530/script.txt` so I can download and run it from the DMZ environment.

```
invoke-webrequest -uri http://wsus.domain.local:8530/script.txt -outfile script.ps1
.\script.ps1
```

Happy updating :)
