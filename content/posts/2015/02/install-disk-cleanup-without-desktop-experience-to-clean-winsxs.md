---
_edit_last: "1"
_thumbnail_id: "1593"
author: thomasf
categories:
  - windows
cover:
  alt: Vacuum cleaner - Workers collection
  image: /wp-content/uploads/2015/02/software_cleanup.jpg
date: "2015-02-19T08:40:27+00:00"
dsq_thread_id: "5157738726"
guid: https://blog.wapnet.nl/?p=1592
parent_post_id: null
post_id: "1592"
title: Install Disk Cleanup without Desktop Experience to clean WinSXS
url: /2015/02/install-disk-cleanup-without-desktop-experience-to-clean-winsxs/

---
### For: Windows Server 2008 R2 (64-bit)

Copy the following files:

```
> copy C:\Windows\winsxs\amd64_microsoft-windows-cleanmgr_31bf3856ad364e35_6.1.7600.16385_none_c9392808773cd7da\cleanmgr.exe C:\Windows\System32\
```

English:

```
> copy C:\Windows\winsxs\amd64_microsoft-windows-cleanmgr.resources_31bf3856ad364e35_6.1.7600.16385_en-us_b9cb6194b257cc63\cleanmgr.exe.mui C:\Windows\System32\en-US\
```

Dutch:

```
> copy C:\Windows\winsxs\amd64_microsoft-windows-cleanmgr.resources_31bf3856ad364e35_6.1.7600.16385_nl-nl_72d752f33b5fc86a c:\Windows\System32\nl-NL\
```

Run the cleanmgr.exe:

```
> cleanmgr.exe
```
