---
_disable_fbc: ""
_edit_last: "1"
_wp_old_slug: remove-windows-2008-r2-winsxs-windows-update
author: thomasf
categories:
  - windows
date: "2016-06-06T12:37:13+00:00"
dsq_thread_id: "5222964833"
guid: https://blog.wapnet.nl/?p=1684
parent_post_id: null
post_id: "1684"
title: Remove Windows 2008 r2 WinSXS "Windows Update" files
url: /2016/06/remove-windows-2008-r2-winsxs-windows-update-files/

---
copy C:\\Windows\\winsxs\\amd64\_microsoft-windows-cleanmgr\_31bf3856ad364e35\_6.1.7600.16385\_none\_c9392808773cd7da\\cleanmgr.exe to **%systemroot%\\System32**

copy C:\\Windows\\winsxs\\amd64\_microsoft-windows-cleanmgr.resources\_31bf3856ad364e35\_6.1.7600.16385\_en-us\_b9cb6194b257cc63\\cleanmgr.exe.mui to **%systemroot%\\System32\\en-Us**

Run cmd > cleanmgr and remove all the nasty update files!

After I cleaned up the server I had to stop the windows installer service (trustedinstaller.exe) to remove the c:\\windows\\logs\\cbs\\CBS.log (6GB file) manually. Maybe a restart of the server do the same but I cannot test it on a production environment.

Have fun!

Source: [https://support.appliedi.net/kb/a110/how-to-enable-the-disk-cleanup-tool-on-windows-server-2008-r2.aspx](https://support.appliedi.net/kb/a110/how-to-enable-the-disk-cleanup-tool-on-windows-server-2008-r2.aspx)
