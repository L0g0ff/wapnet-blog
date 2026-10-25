---
_thumbnail_id: "2042"
author: thomasf
categories:
  - powershell
  - windows
cover:
  alt: windows-powershell-ise-icon
  image: /wp-content/uploads/2022/04/windows-powershell-ise-icon.png
date: "2022-09-20T13:15:14+00:00"
guid: https://blog.wapnet.nl/?p=2076
parent_post_id: null
post_id: "2076"
title: Update Windows Server with powershell
url: /2022/09/update-windows-server-with-powershell/

---
This is for 2016 server. But it will work for other versions of Windows

```
[Net.ServicePointManager]::SecurityProtocol += [Net.SecurityProtocolType]::Tls12
Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force
Set-PSRepository -Name "PSGallery" -InstallationPolicy Trusted
Install-Module PSWindowsUpdate -Confirm:$false
Set-PSRepository -Name "PSGallery" -InstallationPolicy Untrusted
Get-WindowsUpdate -AcceptAll -Install -AutoReboot
```

Happy Patching :)
