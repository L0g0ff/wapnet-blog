---
_edit_last: "1"
author: thomasf
categories:
  - exchange
date: "2009-05-27T12:21:40+00:00"
dsq_thread_id: "5137070269"
guid: https://blog.wapnet.nl/?p=193
parent_post_id: null
post_id: "193"
title: Microsoft Exchange 2007 Powershell Commands
url: /2009/05/microsoft-exchange-2007-powershell-commands/

---
**Remove a public folder database** `Remove-PublicFolderDatabase -Identity "\\ "` **Change the Default Public Folder Database for a Mailbox Database** `Set-MailboxDatabase -Identity "Mailbox Database" -PublicFolderDatabase "PublicFolderDB1"` **Move all public folder replica's** `MoveAllReplicas.ps1 –Server Server1 –NewServer Server2 ` **Set Postmaster Address** `Set-TransportServer -ExternalPostmasterAddress ` **Upgrade Email Address Policy** `Set-EmailAddressPolicy "Default Policy" -IncludedRecipients AllRecipients` **View Public Folder Client Permissions** `Get-PublicFolderClientPermission -Identity "\Marketing" | fl ` **Change Autodisover website settings** `Set-AutodiscoverVirtualDirectory "servername\Autodiscover (Default Web Site)" -InternalUrl
http://server.domain.com -ExternalUrl https://autodiscover.mydomain.com` **Create a new certificate** `New-ExchangeCertificate -DomainName "external.maildomain.com"` **Enable certificate** `Enable-ExchangeCertificate "the number you get from the certificates once it
is generated" with out the quotes` **Give a user access to a Top Public Folder and all sub folders** `AddUsersToPFRecursive.ps1 -TopPublicFolder "\Sales" -User "David" -Permission Reviewer` **Give a user access to a Public Folder** `Add-PublicFolderClientPermission -Identity "\Marketing\West Coast" -AccessRights PublishingEditor -User Kim` **Replace the permissions of a user with new permissions** `ReplaceUserPermissionOnPFRecursive.ps1 -Server "SERVER01" -TopPublicFolder "\Marketing" -User "Kim" -Permissions PublishingEditor` **Replace the permissions of a user with new a new user on all sub folders** `ReplaceUserWithUserOnPFRecursive.ps1 -TopPublicFolder "\Sales" -UserOld "David" -UserNew "Kim"` **Remove the permissions of a user on a folder and all sub folders** `RemoveUserFromPFRecursive.ps1 -Server "SERVER01" -TopPublicFolder -"\Sales\Oregon" -User "David"` **Remove the permissions of a user from a Public Folder** `Remove-PublicFolderClientPermission -Identity "Sales\West Coast\Oregon" -User David -AccessRights CreateItems` **Mail enable Public Folder** `Enable-MailPublicFolder -Identity "\My Public Folder"` **Force Edge server synchronisation**
Run the following command on the Transport server
`Start-EdgeSynchronization` **Remove forwarding address with PowerShell - All users** `Get-Mailbox | Where {$_.ForwardingAddress -ne $null} | Set-Mailbox -ForwardingAddress $null -DeliverToMailboxAndForward $false` **Set Mailforwarder on a mailbox** `Set-Mailbox -Identity John -DeliverToMailboxAndForward $true -ForwardingAddress jose@contoso.com This e-mail address is being protected from spambots. You need JavaScript enabled to view it `
