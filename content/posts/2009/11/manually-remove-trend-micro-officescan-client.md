---
_edit_last: "1"
author: thomasf
categories:
  - windows
date: "2009-11-04T18:36:45+00:00"
dsq_thread_id: "5142878186"
guid: https://blog.wapnet.nl/?p=247
parent_post_id: null
post_id: "247"
title: Manually Remove Trend Micro Officescan Client
url: /2009/11/manually-remove-trend-micro-officescan-client/

---
1. Go to Control Panel **Services (services.msc)**, and stop the following services:

   - OfficeScanNT Listener
   - OfficeScanNT RealTimeScan
   - OfficeScanNT Personal Firewall (if enabled)
1. Run **Registry Editor (regedit.exe)**.
1. Navigate to the following [registry key](http://www.mydigitallife.info/2008/07/18/how-to-manually-uninstall-trend-micro-officescan-corporate-edition-client/)

hive:

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services**

1. Delete the following keys (if available):
   - **Ntrtscan**
   - **Tmlisten**
   - **TmFilter**
   - **VSApiNt**
   - **TMPreFilter**
   - **TM\_CFW**
   - **OfcPfwSvc**
1. Navigate to the following registry hive:

**HKEY\_LOCAL\_MACHINE \\SOFTWARE\\TrendMicro**

or

**HKEY\_LOCAL\_MACHINE \\SOFTWARE \\Wow6432Node\\TrendMicro** (in [64-bit](http://www.mydigitallife.info/2008/07/18/how-to-manually-uninstall-trend-micro-officescan-corporate-edition-client/) Windows operating system)

1. Delete the following keys (if available):
   - **OfcWatchDog**
   - **Pc-cillinNTCorp** or **OfficeScanCorp** (depending on the client)
   - R **emoteAgent**
   - **PC-cillin**
   - **CFW**
1. Browse to the following registry key hive:

**HKEY\_LOCAL\_MACHINE \\SOFTWARE \\Microsoft\\Windows\\CurrentVersion\\Run**

1. Delete the **OfficeScanNT** Monitor key.
1. Navigate to the following registry key:

**HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall**

1. Delete the **OfficeScanNT** key.
1. Delete the OfficeScan program group ( **Trend Micro OfficeScan Client**) from the Windows **Start menu**.
1. Restart the computer.
1. Delete the directories that contain the **OfficeScan Client** program files, normally located inside **Program Files** folder.

Above steps work for OfficeScan 7.x client in Windows 2003/XP/2000/NT/Vista/2008 machine. For Trend Micro OfficeScan Corporate Edition (OSCE) – 5.58, OfficeScan Corporate Edition (OSCE) – 6.5, Client / Server / Messaging Suite for SMB – 2.0, follow these manual uninstallation steps instead.

1. Delete the **Trend Micro OfficeScan Client** program shortcut in **Start Menu**, by right click on it and then choose **Delete**.
1. Delete the installed files located in the **OfficeScan** folder under the **\\Program Files\\Trend Micro\\OfficeScan Client** directory.
1. Open the **Registry Editor (regedit)**.
1. Navigate to the following registry key:

**HKEY\_LOCAL\_MACHINE\\Software\\TrendMicro**

1. Delete the following keys:
   - **OfcWatchDog**
   - **PC-cillin**
   - **PC-cillinNTCorp**
1. Also delete the following registry hives:
   - **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run\\OfficeScanNT Monitor**
   - **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\OfficeScanNT**
   - **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\ntrtscan**
   - **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\tmfilter**
   - **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\tmlisten**
   - **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\TmPreFilter** (for Win2003)
   - **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\VSApiNt**
1. Right click on **[My Computer](http://www.mydigitallife.info/2008/07/18/how-to-manually-uninstall-trend-micro-officescan-corporate-edition-client/)**

, click **Manage** and then select **Device Manager**.

1. Enable the **Show Hidden Devices** option.
1. Remove the following hidden devices in **Non-Plug and Play Drivers** tree pertaining to OfficeScan (right-click and select Uninstall):

   - **Trend Micro VSAPI NT**
   - **Trend Micro FILTER**
   - **Common Firewall Driver**
   - **NTRTSCAN** (if available)
   - **TMLISTEN** (if available)
1. Restart the OfficeScan client machine.

Source: [http://www.mydigitallife.info/2008/07/18/how-to-manually-uninstall-trend-micro-officescan-corporate-edition-client/](http://www.mydigitallife.info/2008/07/18/how-to-manually-uninstall-trend-micro-officescan-corporate-edition-client/)
