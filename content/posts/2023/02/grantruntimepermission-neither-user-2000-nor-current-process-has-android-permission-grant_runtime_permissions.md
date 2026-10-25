---
author: thomasf
categories:
  - android
date: "2023-02-22T08:49:32+00:00"
guid: https://blog.wapnet.nl/?p=2095
parent_post_id: null
post_id: "2095"
title: 'grantRuntimePermission: Neither user 2000 nor current process has android.permission.GRANT_RUNTIME_PERMISSIONS'
url: /2023/02/grantruntimepermission-neither-user-2000-nor-current-process-has-android-permission-grant_runtime_permissions/

---
I'll was getting this issue when I try to install BetterBatteryStats on my Oneplus device.

{{< figure src="/wp-content/uploads/2023/02/image.png" alt="" caption="" >}}

There are 3 things to do if you want to fix this:

1. Enable Developer mode
1. Disable Permission Monitoring (dutch: _Machtigingscontrole uitschakelen_). You can find this setting in the debugger options somewhere near the bottom.
1. You need to force quit the batteryBatteryStats app (or reboot the phone)

Then you can set the permissions:

```
adb -d shell pm grant com.asksven.betterbatterystats android.permission.BATTERY_STATS
adb -d shell pm grant com.asksven.betterbatterystats android.permission.DUMP
adb -d shell pm grant com.asksven.betterbatterystats android.permission.PACKAGE_USAGE_STATS
adb -d shell settings put global hidden_api_policy 1
```
