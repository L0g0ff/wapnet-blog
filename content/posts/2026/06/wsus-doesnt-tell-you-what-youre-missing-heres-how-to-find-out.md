---
_oembed_83f4dc64d5eb16c46428d03715f1cdf5: '{{unknown}}'
author: thomasf
categories:
  - windows
date: "2026-06-16T19:36:05+00:00"
guid: https://blog.wapnet.nl/?p=2301
parent_post_id: null
post_id: "2301"
title: WSUS Doesn't Tell You What You're Missing - Here's How to Find Out
url: /2026/06/wsus-doesnt-tell-you-what-youre-missing-heres-how-to-find-out/

cover:
  image: /images/covers/wsus-doesnt-tell-you-what-youre-missing-heres-how-to-find-out.jpg
  alt: Server next to a checklist where a magnifying glass reveals missed update boxes
---
If you manage Windows updates through WSUS, you've probably been there: a server is missing patches, you dig into it, and it turns out the product category was never enabled in WSUS. No warning, no report - it just silently never synced those updates.

The frustrating part is that WSUS has no built-in way to tell you which product categories your clients actually need. You can see what's subscribed, but not what you're missing. It doesn't know what's installed on your clients unless you've already told it to care.

I went looking for a smart solution that didn't require SCCM, Intune, or clients reaching out to the internet. Turns out Microsoft already ships the answer: `wsusscn2.cab`.

## What is wsusscn2.cab?

It's a signed cabinet file published by Microsoft that contains the full catalog of security-related updates. The Windows Update Agent (WUA) on any Windows machine can use it to scan locally - no internet connection needed on the client, no WSUS query. It figures out what's applicable based on what's actually installed.

This means you can point it at any client and get back a list of every product category that has outstanding updates, including ones you never subscribed to in WSUS.

## The Script

Download `wsusscn2.cab` once — either directly on the client or from the WSUS server and copy it over:

[https://catalog.s.download.windowsupdate.com/microsoftupdate/v6/wsusscan/wsusscn2.cab](https://catalog.s.download.windowsupdate.com/microsoftupdate/v6/wsusscan/wsusscn2.cab)

Then run this as administrator on the client:

```
#Requires -RunAsAdministrator

$cabPad = "C:\Temp\wsusscn2.cab"
New-Item -ItemType Directory -Force -Path "C:\Temp" | Out-Null

if (-not (Test-Path $cabPad)) {
    Write-Host "Downloading wsusscn2.cab (~700 MB)..."
    Invoke-WebRequest `
        -Uri "https://catalog.s.download.windowsupdate.com/microsoftupdate/v6/wsusscan/wsusscn2.cab" `
        -OutFile $cabPad -UseBasicParsing
}

Write-Host "Scanning... this takes 10 to 30 minutes."

$mgr      = New-Object -ComObject Microsoft.Update.ServiceManager
$svc      = $mgr.AddScanPackageService("Offline Sync Service", $cabPad)
$session  = New-Object -ComObject Microsoft.Update.Session
$searcher = $session.CreateUpdateSearcher()
$searcher.ServerSelection = 3
$searcher.ServiceID       = [string]$svc.ServiceID

$result = $searcher.Search("IsInstalled=0")

Write-Host "`nProduct categories with outstanding updates on this machine:`n"
$result.Updates | ForEach-Object {
    $u = $_
    $u.Categories | Where-Object Type -eq "Product"
} | Select-Object -ExpandProperty Name -Unique | Sort-Object | ForEach-Object {
    Write-Host "  - $_"
}
```

### How It Works

The WUA COM object normally talks to either Windows Update or your WSUS server. By setting ServerSelection = 3 and pointing it to a local service backed by the cab file, it scans entirely offline. It runs the same applicability rules it always does — checking installed software, versions, and hotfixes - but against the catalog in the cab instead of a live server.

One important caveat: this has to run locally on the machine. The WUA COM object doesn't work correctly over PowerShell remoting, so Invoke-Command won't cut it here.

What To Do With the Output

You'll get a list like this:

- .NET Framework
- Microsoft Edge
- Microsoft Office 2019
- Windows Server 2016

{{< figure src="/wp-content/uploads/2026/06/image.png" alt="" caption="" >}}

Cross-reference that with your WSUS product subscriptions (Options → Products and Classifications). Anything on this list that isn't checked in WSUS is a gap - those updates are never being offered to your clients.

Run the script on a few representative machines (a file server, an app server, a workstation) and you'll quickly get a complete picture of what your environment actually needs.

Happy patching!
