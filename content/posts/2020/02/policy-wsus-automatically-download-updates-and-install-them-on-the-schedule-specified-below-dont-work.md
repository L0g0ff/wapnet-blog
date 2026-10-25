---
author: thomasf
categories:
  - windows
date: "2020-02-04T14:43:51+00:00"
guid: https://blog.wapnet.nl/?p=1835
parent_post_id: null
post_id: "1835"
title: 'Policy WSUS: "Automatically download updates and install them on the schedule specified below" don''t work...!!!?!'
url: /2020/02/policy-wsus-automatically-download-updates-and-install-them-on-the-schedule-specified-below-dont-work/

---
So I configure a "configure automatic updates" policy for testing purposes but the auto-update and installation won't work. The main cause....? Lack of patience ;-)

How this Policy works ([source](https://social.technet.microsoft.com/Forums/exchange/en-US/52ac4f34-dfee-4eae-bda9-6f8087a83173/wsus-auto-download-and-schedule-install)):

_The Windows Update Agent periodically checks the WSUS server for updates. Updates it finds, it reports state for: Installed, Not Installed, Not Applicable. If a "Not Installed" update is approved and available, the WUA queues the installation files for download if the Configure Automatic Updates policy is set to AUOption '3' or '4'._

_The download occurs via Background Intelligent Transfer Service (BITS) subsequent to the WUA finding the update as available for download._

_When the download of the update is completed, the WUA does one of two things:_

- _If the Configure Automatic Updates policy is set to AUOption '4', then the WUA will schedule the update for installation at the scheduled time. This scheduled installation does NOT require access to the WSUS server to be conducted._
- _If the Configure Automatic Updates policy is not set to AUOption '4', then the update will be retained on the client computer until a user launches the Windows Update applet from Control Panel and initiates the installation._

So bottom line; the updates must first be downloaded on the client and ONLY then will Windows apply the "Automatically download updates and install them on the schedule specified" action

To force a client ([source](http://pleasework.robbievance.net/howto-force-really-wsus-clients-to-check-in-on-demand/)):

`$updateSession = new-object -com  "Microsoft.Update.Session";  $updates=$updateSession.CreateupdateSearcher().Search($criteria).Updates
Start-sleep -seconds 10
wuauclt /detectnow
wuauclt /reportnow
c:\windows\system32\UsoClient.exe startscan`

After this commands BITS will download the updates and prepare the installation. When you start Windows update you can see the available update

{{< figure src="/wp-content/uploads/2020/02/image.png" alt="" caption="" >}}

The default of the WSUS communication check-in (report and detect) is 22 hours. If you don't want to wait so long you can change the "automatic updates detection frequency" to every hour (do not to this every hour on production policies!)

{{< figure src="/wp-content/uploads/2020/02/image-2.png" alt="" caption="" >}}

And now wait till the magic happens :)

{{< figure src="/wp-content/uploads/2020/02/image-1.png" alt="" caption="" >}}

Last but now least. When you change setting in the "configure automatic updates" policy you can trigger the client with powershell so you don't have to reboot the client

```
gpupdate /force
net stop wuauserv
net start wuauserv
(new-object -Comobject Microsoft.Update.AutoUpdate).Detectnow()
```

You get get more information about Windows update log with the command.

`Get-WindowsUpdateLog`

Happy updating!

OK... Even with all the tips. Sometimes you need rename the software distribition folder also so I present to you: The PLZ GIVE ME \*\*\*\*\*\*\* UPDATES NOW SCRIPT!!!! ( **runas admin**)

```
gpupdate /force
Start-sleep -seconds 10
Stop-Service -Name BITS, wuauserv -Force
Remove-Item "$env:SystemRoot\SoftwareDistribution\" -Recurse -Force -ErrorAction SilentlyContinue
Start-Service -Name BITS, wuauserv
$updateSession = new-object -com "Microsoft.Update.Session"; $updates=$updateSession.CreateupdateSearcher().Search($criteria).Updates
Start-sleep -seconds 10
wuauclt /detectnow
wuauclt /reportnow
(New-Object -ComObject Microsoft.Update.AutoUpdate).DetectNow()
```
