---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - android
date: "2011-03-19T00:32:54+00:00"
dsq_thread_id: "5136177857"
guid: https://blog.wapnet.nl/?p=554
parent_post_id: null
post_id: "554"
title: 'Android 2.2: Install all apps to SD (even the unsupported apps)'
url: /2011/03/android-2-2-install-all-apps-to-sd-even-the-unsupported-apps/

---
Because a lot of android phones have a really small disk (NAND) you must move all the apps manually to SD. You can automate this with an tool on the marked (easy way).

1. Search for **modinstalllocation** in the marked
1. download and install this.
1. Start the tool and set the value on **2 external**

The _hard_ way:

1. Connect the phone using the android SDK. (If you don't know how, you can use my tutorial [/2011/03/windows-7-x64-android-sdk-example-connect-htc-desire/](/2011/03/windows-7-x64-android-sdk-example-connect-htc-desire/))
1. Now start cmd
1. change folder to C:\\Program Files (x86)\\Android\\android-sdk\\platform-tools
1. Now run the following command:

> adb shell pm setInstallLocation 2

Note: For both options you're phone don't have to be rooted  ;)
