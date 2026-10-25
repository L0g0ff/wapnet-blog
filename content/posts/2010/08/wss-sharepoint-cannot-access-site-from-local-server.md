---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - iis
  - windows
date: "2010-08-18T09:25:28+00:00"
dsq_thread_id: "5147460365"
guid: https://blog.wapnet.nl/?p=390
parent_post_id: null
post_id: "390"
title: WSS / Sharepoint Cannot access site from local server
url: /2010/08/wss-sharepoint-cannot-access-site-from-local-server/

---
You receive error 401.1 when you browse a Web site that uses Integrated Authentication and is hosted on IIS 5.1 or a later version

Solution : [http://support.microsoft.com/kb/896861](http://support.microsoft.com/kb/896861)

### Method 1: Specify host names (Preferred method if NTLM authentication is desired)

To specify the host names that are mapped to the loopback address and can connect to Web sites on your computer, follow these steps:

1. Set the DisableStrictNameChecking registry entry to 1. For more information about how to do this, click the following article number to view the article in the Microsoft Knowledge Base:

   [281308](http://support.microsoft.com/kb/281308) Connecting to SMB share on a Windows 2000-based computer or a Windows Server 2003-based computer may not work with an alias name

1. Click **Start**, click **Run**, type regedit, and then click **OK**.
1. In Registry Editor, locate and then click the following registry key:

   **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa\\MSV1\_0**

1. Right-click **MSV1\_0**, point to **New**, and then click **Multi-String Value**.
1. Type BackConnectionHostNames, and then press ENTER.
1. Right-click **BackConnectionHostNames**, and then click **Modify**.
1. In the **Value data** box, type the host name or the host names for the sites that are on the local computer, and then click **OK**.
1. Quit Registry Editor, and then restart the IISAdmin service.

or

### Method 2: Disable the loopback check (less-recommended method)

The second method is to disable the loopback check by setting the **DisableLoopbackCheck** registry key.

To set the **DisableLoopbackCheck** registry key, follow these steps:

1. Set the DisableStrictNameChecking registry entry to 1. For more information about how to do this, click the following article number to view the article in the Microsoft Knowledge Base:

   [281308](http://support.microsoft.com/kb/281308) Connecting to SMB share on a Windows 2000-based computer or a Windows Server 2003-based computer may not work with an alias name

1. Click **Start**, click **Run**, type regedit, and then click **OK**.
1. In Registry Editor, locate and then click the following registry key:

   **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Lsa**

1. Right-click **Lsa**, point to **New**, and then click **DWORD Value**.
1. Type DisableLoopbackCheck, and then press ENTER.
1. Right-click **DisableLoopbackCheck**, and then click **Modify**.
1. In the **Value data** box, type 1, and then click **OK**.
1. Quit Registry Editor, and then restart your computer.
