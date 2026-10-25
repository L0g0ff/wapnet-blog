---
_edit_last: "1"
author: thomasf
categories:
  - windows
date: "2010-02-26T10:07:12+00:00"
guid: https://blog.wapnet.nl/?p=358
parent_post_id: null
post_id: "358"
title: Windows Vista/2008 your user profile was not loaded correctly
url: /2010/02/windows-vista2008-your-user-profile-was-not-loaded-correctly/

---
After you removed the C:\\users\\someprofile\ you get the error "your user profile was not loaded correctly". To fix this start regedit go to: HKLM\\Software\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList search the currupted profile and remove the key.
