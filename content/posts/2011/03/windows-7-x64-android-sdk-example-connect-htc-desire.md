---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - android
date: "2011-03-19T00:17:06+00:00"
dsq_thread_id: "5136178030"
guid: https://blog.wapnet.nl/?p=549
parent_post_id: null
post_id: "549"
title: 'Windows 7 x64 Android SDK - Example: Connect HTC Desire'
url: /2011/03/windows-7-x64-android-sdk-example-connect-htc-desire/

---
I had some troubles with the Android SDK so I will explain the steps you must take to connect your phone from your pc

Preparation:

1. Download the Android SDK
1. Turn on your USB debugging mode (On the device, go to the home screen, press MENU, select Applications > Development, then enable USB debugging)

Steps:

1. Install the Android SDK
1. During the install ask to download and install the Java SDK
1. Continue the installation when you have installed the Java SDK
1. Start the (Android) SDK Manager and download all the default packages. Note: when you start the SDK Manager in the future always start the shortcut with administrator permissions. (right click > runas admin)
1. Now download the USB drivers with the SDK Manager
1. [![](/wp-content/uploads/2011/03/sdk.png)](/wp-content/uploads/2011/03/sdk.png)
1. Now start notepad as administrator and open "C:\\Program Files (x86)\\Android\\android-sdk\\extras\\google\\usb\_driver\\android\_winusb.inf"
1. Now add some x64 code to the 32bits inf file

> \[Google.NTamd64\]
> ; HTC Desire
> %SingleAdbInterface%        = USB\_Install, USB\\VID\_0BB4&PID\_0C87
> %CompositeAdbInterface%     = USB\_Install, USB\\VID\_0BB4&PID\_0C87&MI\_01

1. Example:
1. [![](/wp-content/uploads/2011/03/sdk2.png)](/wp-content/uploads/2011/03/sdk2.png)
1. Now connect your phone with an USB cable (usb debuging mode must be turned on) open your device manager and update the android device with the modified driver.
1. [![](/wp-content/uploads/2011/03/devicemanager.png)](/wp-content/uploads/2011/03/devicemanager.png)
1. Now you can start cmd and use the adb util to manager your phone. Some example if you want to change your default install location for all apps to SD (even the app that not support this feature)
1. [![](/wp-content/uploads/2011/03/adb.png)](/wp-content/uploads/2011/03/adb.png)

If your phone are other phone rather than HTC Desire, you have to change the Hardware ID (e.g. USB\\VID\_0BB4&PID\_0C87) to be your phone’s ID. You can get this ID by

\- Right-click on the My computer -> properties.
\- Click on Device Manager.
\- Find the phone in the list on left-hand. (Should be some warning mark if you don’t have driver for it)
\- Right click on ADB -> Properties -> Detail
\- Change the drop-down box to Hardware ID. This is where your phone USB ID is keep. Use this ID to put in the android\_winusb.inf as described above.

Note: for 32bits computers use: \[Google.NTx86\]
Note: for 64bits computers use: \[Google.NTamd64\]

Happy debugging :)

(pfff crappy wordpress editor ;))
