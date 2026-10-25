---
_thumbnail_id: "2042"
author: thomasf
categories:
  - powershell
  - programmeren
cover:
  alt: windows-powershell-ise-icon
  image: /wp-content/uploads/2022/04/windows-powershell-ise-icon.png
date: "2022-04-02T08:03:39+00:00"
guid: https://blog.wapnet.nl/?p=2040
parent_post_id: null
post_id: "2040"
title: Add Powershell 7 to your Powershell ISE
url: /2022/04/add-powershell-7-to-your-powershell-ise/

---
I find this code snippet [somewhere on the internet](http://eddiejackson.net/lab/2021/05/22/powershell-add-ise-support-for-current-powershell-version-core/) and I like it :)

{{< figure src="/wp-content/uploads/2022/04/afbeelding.png" alt="" caption="" >}}

Just open ISE and paste these code and you are ready to rock!

```
$ErrorActionPreference= 'silentlycontinue'
$psISE.CurrentPowerShellTab.AddOnsMenu.Submenus.Clear()
$psISE.CurrentPowerShellTab.AddOnsMenu.Submenus.Add("Switch to PowerShell 7", {
        function New-OutOfProcRunspace {
            param($ProcessId)

            $ConnInfo = New-Object -TypeName System.Management.Automation.Runspaces.NamedPipeConnectionInfo -ArgumentList @($ProcessId)
            $DefaultType = [System.Management.Automation.Runspaces.TypeTable]::LoadDefaultTypeFiles()

            $Runspace = [System.Management.Automation.Runspaces.RunspaceFactory]::CreateRunspace($ConnInfo, $Host, $Default)

            $Runspace.Open()
            $Runspace
        }

        $PowerShell = Start-Process PWSH -ArgumentList @("-NoExit") -PassThru -WindowStyle Hidden
        $Runspace = New-OutOfProcRunspace -ProcessId $PowerShell.Id
        $Host.PushRunspace($Runspace)
}, "ALT+F5") | Out-Null

$psISE.CurrentPowerShellTab.AddOnsMenu.Submenus.Add("Switch to PowerShell 5", {
    $Host.PopRunspace()

    $ChildProc = Get-CimInstance -ClassName win32_process | where {$_.ParentProcessId -eq $Pid}
    $ChildProc | ForEach-Object { Stop-Process -Id $_.ProcessId }

}, "ALT+F6") | Out-Null
```

Happy coding!
