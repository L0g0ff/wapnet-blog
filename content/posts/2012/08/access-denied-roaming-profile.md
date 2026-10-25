---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - windows
date: "2012-08-14T09:48:48+00:00"
dsq_thread_id: "5136179213"
guid: https://blog.wapnet.nl/?p=961
parent_post_id: null
post_id: "961"
title: Access Denied Roaming Profile
url: /2012/08/access-denied-roaming-profile/

---
By default the Roaming profile is only accessible for the owner (end-user) and the system account. I found a post on the internet with a workaround to access the profile without problems to the end user.

Using two tools, the first is **SubInAcl.exe** available from [Microsoft (download)](http://www.microsoft.com/downloads/details.aspx?FamilyID=E8BA3E56-D8FE-4A91-93CF-ED6985E3927B), and the second is **cacls.exe** which you should already have by default in Windows.

These first two commands will give the local administrators group ownership of the user’s folder and everything underneath. NOTE: This will not change any existing permissions.

```
SubInAcl /subdirectories D:\Profile\User.Name /setowner=Administrators
SubInAcl /subdirectories D:\Profile\User.Name\*.* /setowner=Administrators
```

This second command will give the local administrators group full access to the user’s foldercacls

```
D:\Profile\User.Name /T /E /C /G Administrators:F
```


[Source Article](http://marckean.wordpress.com/2009/06/18/access-denied-to-roaming-profiles/)
