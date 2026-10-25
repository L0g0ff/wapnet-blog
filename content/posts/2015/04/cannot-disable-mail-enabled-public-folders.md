---
_disable_fbc: ""
_edit_last: "1"
author: thomasf
categories:
  - uncategorized
date: "2015-04-09T13:43:00+00:00"
dsq_thread_id: "5156776694"
guid: https://blog.wapnet.nl/?p=1621
parent_post_id: null
post_id: "1621"
title: Cannot disable mail enabled public folders
url: /2015/04/cannot-disable-mail-enabled-public-folders/

---
### Output

```
    PS C:\Users\jfb> get-mailpublicfolder -Identity "bccp11-036"

    Alias                Identity
    -----                --------
    bccp11-036           matricis.local/Microsoft Exchange System Objects/Correspondance 81807753

    PS C:\Users\jfb> disable-mailpublicfolder -Identity "matricis.local/Microsoft Exchange
System Objects/Correspondance 81807753"

    Disable-MailPublicFolder : No existing 'PublicFolder' matches the following Identity: 'matricis.local/Microsoft Exchange System Objects/Correspondance 81807753'
    At line:1 char:25
    + disable-mailpublicfolder <<<<  -Identity "matricis.local/Microsoft Exchange System Objects/Correspondance 81807753"
        + CategoryInfo          : NotSpecified: (0:Int32) [Disable-MailPublicFolder], MapiOperationException
        + FullyQualifiedErrorId : 826D5700,Microsoft.Exchange.Management.MapiTasks.DisableMailPublicFolder

```

### Cause

I have resolved the issue, to solve this, we have to go into Active Directory Users and Computers. Under View, select Advanced Features. Now, under the /Microsoft Exchange System Objects folder, manually delete the Correspondance 81807753 object.

To prevent this, you have to mail-disable the public folder before deleting it from the public folders

[Source](http://serverfault.com/questions/296411/how-to-mail-disable-a-non-existing-public-folder-in-exchange-server)

### Tip:

If you want to quick find the old public folder use a custom AD search:

```
(&proxyaddresses=smtp:some@mail.nl)

```
