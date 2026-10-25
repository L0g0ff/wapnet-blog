---
_edit_last: "1"
_wp_old_slug: exchange-2007-mapi-session-exceeded-the-maximum-of-32-objects-of-type-%e2%80%9csession%e2%80%9d
author: thomasf
categories:
  - exchange
date: "2008-10-06T11:20:09+00:00"
dsq_thread_id: "5161251905"
guid: https://blog.wapnet.nl/?p=81
parent_post_id: null
post_id: "81"
title: 'Exchange 2007: Mapi session exceeded the maximum of 32 objects of type “session”'
url: /2008/10/exchange-2007-mapi-session-exceeded-the-maximum-of-32-objects-of-type-session/

---
Error Message: “Mapi session “/o=Organization/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Recipients/cn=JohnSmith” exceeded the maximum of 32 objects of type “session”".
Source: MSExchangeIS
Event ID: 9646

On the client side, the user is unable to connect to Microsoft Exchange or getting this error:

Unable to open your default e-mail folders. The Microsoft Exchange Server computer is not available. Either there are network problems or the Microsoft Exchange Server is down for maintenance.

This usually happens when the user loses network connectivity while Outlook is still open. The Exchange server wasn’t able to close the sessions properly so they just stayed there even when they are not in use.

By default, Exchange only allows up to 32 MAPI (Outlook) sessions per user. To fix this problem, you must close some of the sessions.

What to do:

1. Download and extract Sysinternals’ TCPView (free) on the Exchange server
1. Open the Exchange Management Shell and type in the following command to get a list of all the opened sessions. Make a note of the IP Addresses:

_Get-LogonStatistics jsmith \| Sort-Object clientipaddress \| Format-Table username,clientipaddress,logontime_

1. Open Tcpview.exe on the server. Sort it by Remote Address, then sort it by Process.
1. Look for the IP Addresses from Step 2 in the Remote Address column (if you only see hostnames, go to Options -> uncheck Resolve Addresses) and close their connections for the store.exe process (right-click and choose Close Connection, you can select multiple connections by holding the Shift or Ctrl key)
1. Run the command from Step 2 again and you will see that the sessions disappeared. The user should now be able to connect to the Exchange server again.
