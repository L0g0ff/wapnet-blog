---
_thumbnail_id: "2211"
author: thomasf
categories:
  - powershell
  - windows
cover:
  alt: settings
  image: /wp-content/uploads/2024/09/settings-e1725967277567.png
date: "2024-09-10T11:17:52+00:00"
guid: https://blog.wapnet.nl/?p=2210
parent_post_id: null
post_id: "2210"
title: 'Monitoring Event Logs in Windows with PowerShell: A Script for Recent Events'
url: /2024/09/monitoring-event-logs-in-windows-with-powershell-a-script-for-recent-events/

---
When managing a Windows environment, analyzing event logs is an essential part of troubleshooting. Windows logs a wide range of system, security, and application events, but sometimes specific problems can arise without easily accessible evidence. For example, when tracking down recent events, it can be cumbersome to manually check each log for relevant entries.

In this post, I’ll share a simple PowerShell script that extracts recent log entries across **all event logs**—not just the default System, Application, and Security logs. This script is particularly useful when you need to quickly review what’s been happening on your machine over the last 5 minutes.

### The Challenge

By default, most users only check System, Application, and Security logs. However, Windows maintains many other event logs that can provide critical information about drivers, devices, or even specific services. Accessing these logs manually via **Event Viewer** can be tedious and time-consuming. The goal here is to automate this process with PowerShell and make it easier to analyze logs from a specific timeframe—such as the last 5 minutes.

### The Solution: PowerShell Script

Below is the PowerShell script that retrieves recent events from all event logs and displays them in an easy-to-read format.

```
# Determine the time from 5 minutes ago
$TimeSpan = (Get-Date).AddMinutes(-5)# Fetch all event log names
$logNames = Get-WinEvent -ListLog *# Loop through each log and look for recent events
foreach ($logName in $logNames.LogName) {
    # Fetch the last 100 events, suppress errors if no events exist
    $events = Get-WinEvent -LogName $logName -MaxEvents 100 -ErrorAction SilentlyContinue# If there are events, filter by time
    if ($events) {
        $recentEvents = $events | Where-Object { $_.TimeCreated -gt $TimeSpan }# If recent events exist, display them
        if ($recentEvents) {
            Write-Host "Log: $logName" -ForegroundColor Cyan
            $recentEvents | Select-Object TimeCreated, Id, LevelDisplayName, Message | Format-Table -AutoSize
        }
    }
}

```

### How It Works

1. **Fetching Log Names**: The script starts by retrieving the names of all available event logs on your system using the following command:powershellCopy code `$logNames = Get-WinEvent -ListLog * ` This command lists every log, including ones that are not typically visible in the default Event Viewer console.
1. **Setting a Time Filter**: The script calculates the timestamp from 5 minutes ago by using `Get-Date` combined with the `AddMinutes()` method:powershellCopy code `$TimeSpan = (Get-Date).AddMinutes(-5) ` This value will be used to filter out any events that occurred before this time.
1. **Looping Through Logs**: The script then loops through each log fetched earlier:powershellCopy code `foreach ($logName in $logNames.LogName) { ` For each log, it pulls the last 100 events using `Get-WinEvent`. The `-ErrorAction SilentlyContinue` parameter is important here—it suppresses any errors if no events are found in a particular log, ensuring the script doesn't stop unexpectedly.
1. **Filtering by Time**: Once the events are retrieved, they are filtered by the timestamp:powershellCopy code `$recentEvents = $events | Where-Object { $_.TimeCreated -gt $TimeSpan } ` This ensures that only events created in the last 5 minutes are shown.
1. **Displaying the Results**: If any events match the filter, they are displayed in a neat table using `Format-Table`:powershellCopy code `$recentEvents | Select-Object TimeCreated, Id, LevelDisplayName, Message | Format-Table -AutoSize ` The table includes the time the event was created, its event ID, the level (such as Error, Warning, or Information), and the message content.

### Why This Matters

By gathering events from all logs, this script ensures that no critical logs are overlooked. Whether you’re troubleshooting a hardware issue, investigating network activity, or monitoring driver problems, reviewing **all logs** within a specific timeframe can give you a broader perspective on system behavior.

### Example Output

Here’s an example of what the output looks like when recent events are found:

```
Log: Application
TimeCreated        Id LevelDisplayName Message
-----------        -- ---------------- -------
9/10/2024 11:45 AM 1001 Error           Application error occurred...
9/10/2024 11:47 AM 2002 Warning         Warning: High CPU usage...

```

This provides a quick snapshot of recent system activity across various logs.

Happy scripting!
