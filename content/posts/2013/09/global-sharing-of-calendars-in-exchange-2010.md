---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - exchange
date: "2013-09-03T13:24:15+00:00"
dsq_thread_id: "5175451392"
guid: https://blog.wapnet.nl/?p=1311
parent_post_id: null
post_id: "1311"
title: Global sharing of calendars in exchange 2010
url: /2013/09/global-sharing-of-calendars-in-exchange-2010/

---
- Download the ExFolders tools
- Extract the tool
- Place the tool in de Exchange Bin folder
- Run the reg in the zip
- Run the tool
- Click File , and then click Connect
- Click Tools , and then click Set Calendar Permissions .
- In the new window, click Add , and then select Everyone . Click OK to confirm.
- Back in the Permissions window, click \\Everyone , and select the appropriate permissions that you want to add.
- Click OK to begin setting permissions. No warning screen will appear, permissions will be set immediately.
- When the Percentage complete box has reached 100, you can safely close the window. All permissions are set on everyone’s calendar.

If you get the error: _Error: Logged-on user does not have FullAccess to this mailbox" in ExFolders_ run the following cmdlet in the exchange shell:

Get-Mailbox \| Add-MailboxPermission -User \[username\] -AccessRights FullAccess –InheritanceType All
