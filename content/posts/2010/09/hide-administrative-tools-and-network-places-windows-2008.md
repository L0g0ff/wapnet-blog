---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - windows
date: "2010-09-28T09:09:14+00:00"
dsq_thread_id: "5398503048"
guid: https://blog.wapnet.nl/?p=422
parent_post_id: null
post_id: "422"
title: Hide Administrative tools and network places Windows 2008
url: /2010/09/hide-administrative-tools-and-network-places-windows-2008/

---
By default on Windows 2008 R2 you cannot hide Administrative tools and Network places by default. You must create custom 2 policies:

**Network places** (This cannot be a user key, so you must restart the (client) server :( ):

> CLASS MACHINE
>
> CATEGORY !!Custom
>
> CATEGORY !!ExplorerExtras
>
> POLICY !!HideNetworkInExplorer
> KEYNAME "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\NonEnum"
> EXPLAIN !!HideNetworkInExplorer\_Help
> VALUENAME "{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}"
> VALUEON NUMERIC 1
> VALUEOFF NUMERIC 0
> END POLICY
>
> END CATEGORY
>
> END CATEGORY
>
> \[strings\]
> Custom="Custom Policies"
> ExplorerExtras="Windows Explorer Extra's"
> HideNetworkInExplorer="Hide Network Icon in Explorer 2008/Vista"
> HideNetworkInExplorer\_Help="Enable this one to hide the icon, disable or unconfigure to show it..."

If the you cannot use the policy you can fix it in the register with the following key:

> ﻿Windows Registry Editor Version 5.00
>
> \[HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\NonEnum\]
> "{F02C1A0D-BE21-4350-88B0-7367FC96EF3C}"=dword:00000001

 **Administrative tools**

> CLASS USER
> CATEGORY "Start Menu Administrative Tools(CustomADM)"
> POLICY "Remove Administrative Tools from Start Menu"
> EXPLAIN !!ADMHelp
> KEYNAME Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced
> PART !!ADM\_Configure DROPDOWNLIST REQUIRED
> VALUENAME "Start\_AdminToolsRoot"
> ITEMLIST
> NAME !!ADMoff VALUE NUMERIC 0 DEFAULT
> NAME !!ADMon VALUE NUMERIC 1
> END ITEMLIST
> END PART
> END POLICY
> END CATEGORY
>
> \[strings\]
> ADM\_Configure="Set the Administrative Tools to:"
> ADMoff="Hidden"
> ADMon="Visible"
>
> ; explains
> ADMhelp="Set Administrative Tools to be shown or hidden on the Start Menu. No need to delete the folder off your TS now! MMills - 30/03/10"
