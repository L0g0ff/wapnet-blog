---
_edit_last: "1"
_wp_old_slug: exchange-2007-%e2%80%93-out-of-office-autodiscover-troubleshooting
author: thomasf
categories:
  - exchange
date: "2010-10-27T20:03:20+00:00"
dsq_thread_id: "5240682638"
guid: https://blog.wapnet.nl/?p=443
parent_post_id: null
post_id: "443"
tags:
  - autodiscover
  - error-1013
  - error-500
title: Exchange 2007 – Out-of-Office / Autodiscover troubleshooting
url: /2010/10/exchange-2007-out-of-office-autodiscover-troubleshooting/

---
If you have some trouble with Out-of-Office / Autodiscover  Exchange try the following to fix the problems:

 Remove Autodiscover and EWS virtual directories from the default website with the following commands

> Remove-WebServicesVirtualDirectory
>
> Remove-AutodiscoverVirtualDirectory

If you can't remove them because of some error use the metebase explorer (google) and follow these steps:

> 1\. Install it on your Exchange Server
> 2\. Run it as Administrator
> 3\. Browse to Wssv --> 1 --> Root --> Autodiscover
> 4\. Dont delete it first, rename it to whatever...
> 5\. Check Metabase Explorer and IIS Management to make sure your new Autodiscover Application is listed.
> 6\.  Delete old renamed directory in Metabase explorer...

 Create the EWS and Autodiscover again

> New-WebServicesVirtualDirectory -WebsiteName "Default Web Site" -Internalurl "[https://server.domain.local/EWS/Exchange.asmx](https://server.domain.local/EWS/Exchange.asmx)" -ExternalUrl "[https://server.domain.local/EWS/Exchange.asmx](https://server.domain.local/EWS/Exchange.asmx)"
>
> New-AutoDiscoverVirtualDirectory -websitename "Default Web Site" -WindowsAuthentication $true -DigestAuthentication $false -Internalurl "[https://server.domain.local/EWS/Exchange.asmx](https://server.domain.local/EWS/Exchange.asmx)" -ExternalUrl "[https://server.domain.local/EWS/Exchange.asmx](https://server.domain.local/EWS/Exchange.asmx)"

 Give an IIS reset.

Check with these commands if the EWS and Autodiscover works:

1\. Past the internal URL in your browser. A certificate error may occur, and there must be come a login windows. After you login with some authenticated user you must see a XML file.
2\. Try the following CMDlets for more information. Esspecialy the output from Test-Outlookwebservices is very important .

> Test-OutlookWebServices \|fl
> Get-webservicesvirtualdirectory \|fl

3\. Start Outlook as Exchange user, press down crtl, click with the right mouse button on the Outlook icon and click on test automatic email configuration.

If you get an error 500, error 1013 or some web application error check the IIS authentication rights:

[![](/wp-content/uploads/2010/10/out-of-office.png)](/wp-content/uploads/2010/10/out-of-office.png)
Now it must work!
