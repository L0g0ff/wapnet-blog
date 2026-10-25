---
_edit_last: "1"
author: thomasf
categories:
  - windows
date: "2009-11-16T12:30:51+00:00"
guid: https://blog.wapnet.nl/?p=251
parent_post_id: null
post_id: "251"
title: Show 5 fsmo roles script
url: /2009/11/show-5-fsmo-roles-script/

---
> Set objRootDSE = GetObject("[LDAP://rootDSE](ldap://rootDSE/)")
>
> ' Schema Master
> Set objSchema = GetObject("LDAP://" &\_
> objRootDSE.Get("schemaNamingContext"))
> strSchemaMaster = objSchema.Get("fSMORoleOwner")
> Set objNtds = GetObject("LDAP://" & strSchemaMaster)
> Set objComputer = GetObject(objNtds.Parent)
> WScript.Echo "Forest-wide Schema Master FSMO: " &\_
> objComputer.Name
>
> Set objNtds = Nothing
> Set objComputer = Nothing
>
> ' Domain Naming Master
> Set objPartitions = GetObject("[LDAP://CN=Partitions](ldap://CN=Partitions/)," & \_
> objRootDSE.Get("configurationNamingContext"))
> strDomainNamingMaster = objPartitions.Get("fSMORoleOwner")
> Set objNtds = GetObject("LDAP://" & strDomainNamingMaster)
> Set objComputer = GetObject(objNtds.Parent)
> WScript.Echo "Forest-wide Domain Naming Master FSMO: " &\_
> objComputer.Name
>
> Set objNtds = Nothing
> Set objComputer = Nothing
>
> ' PDC Emulator
> Set objDomain = GetObject("LDAP://" &\_
> objRootDSE.Get("defaultNamingContext"))
> strPdcEmulator = objDomain.Get("fSMORoleOwner")
> Set objNtds = GetObject("LDAP://" & strPdcEmulator)
> Set objComputer = GetObject(objNtds.Parent)
> WScript.Echo "Domain's PDC Emulator FSMO: " & objComputer.Name
>
> Set objNtds = Nothing
> Set objComputer = Nothing
>
> ' RID Master
> Set objRidManager = GetObject("[LDAP://CN=RID](ldap://CN=RID/) Manager$,CN=System," & \_
> objRootDSE.Get("defaultNamingContext"))
> strRidMaster = objRidManager.Get("fSMORoleOwner")
> Set objNtds = GetObject("LDAP://" & strRidMaster)
> Set objComputer = GetObject(objNtds.Parent)
> WScript.Echo "Domain's RID Master FSMO: " & objComputer.Name
>
> Set objNtds = Nothing
> Set objComputer = Nothing
>
> ' Infrastructure Master
> Set objInfrastructure = GetObject("[LDAP://CN=Infrastructure](ldap://CN=Infrastructure/)," & \_
> objRootDSE.Get("defaultNamingContext"))
> strInfrastructureMaster = objInfrastructure.Get("fSMORoleOwner")
> Set objNtds = GetObject("LDAP://" & strInfrastructureMaster)
> Set objComputer = GetObject(objNtds.Parent)
> WScript.Echo "Domain's Infrastructure Master FSMO: " & objComputer.Name

Source: [http://www.thevortex.nl/index.php?option=com\_content&task=view&id=48&Itemid=29](http://www.thevortex.nl/index.php?option=com_content&task=view&id=48&Itemid=29)
