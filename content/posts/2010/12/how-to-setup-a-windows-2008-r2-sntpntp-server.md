---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - windows
date: "2010-12-30T10:05:20+00:00"
dsq_thread_id: "5584372292"
guid: https://blog.wapnet.nl/?p=501
parent_post_id: null
post_id: "501"
title: How to Setup a Windows 2008 R2 SNTP/NTP Server
url: /2010/12/how-to-setup-a-windows-2008-r2-sntpntp-server/

---
When configured correctly, you can use the Windows Time (W32Time) service as an SNTP/NTP server for both windows and non-windows SNTP/NTP clients.

Here's how to do it:

1. Click **Start**, click **Run**, type regedit, and then click **OK**.
1. Locate and then click the following registry entry:

   > HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\W32Time\\Config\

1. In the right pane, right-click **AnnounceFlags**, and then click **Modify**.
1. In the **Edit DWORD Value** dialog box, under **Value data**, type 5, and then click **OK**.
1. Enable NTPServer.

   1. Locate and then click the following registry subkey:

      > HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\
      > Services\\W32Time\\TimeProviders\\NtpServer\

   - In the right pane, right-click **Enabled**, and then click **Modify**.
   - In the **Edit DWORD Value** dialog box, type 1 under **Value data**, and then click **OK**.

1. Exit Registry Editor.
1. At the command prompt, type the following command to restart the Windows Time service, and then press ENTER:

   > **net stop w32time && net start w32time**

This should get you setup with minimal registry hack impact.

Source: [http://bchavez.bitarmory.com/archive/2009/12/21/how-to-setup-a-windows-2008-r2-sntp-ntp-server.aspx](http://bchavez.bitarmory.com/archive/2009/12/21/how-to-setup-a-windows-2008-r2-sntp-ntp-server.aspx)
