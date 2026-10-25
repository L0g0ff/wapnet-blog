---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - android
  - osx
date: "2011-05-18T22:05:11+00:00"
dsq_thread_id: "5136178238"
guid: https://blog.wapnet.nl/?p=576
parent_post_id: null
post_id: "576"
tags:
  - android-sdk-fastboot
  - fastboot-mac
  - fastboot-mac-download
  - fastboot-osx
title: Setup ADB and Fastboot with Android SDK on Mac OSX
url: /2011/05/setup-adb-and-fastboot-with-android-sdk-on-mac-osx/

---
\[banner\]

#### Download Android SDK (original article @ [http://androidtricks.net/setup-adb-and-fastboot-android-sdk-mac-osx-18](http://androidtricks.net/setup-adb-and-fastboot-android-sdk-mac-osx-18))

Download and extract Android SDK from [http://developer.android.com/sdk/index.html](http://developer.android.com/sdk/index.html "http://developer.android.com/sdk/index.html") to your desktop

Browse to Tools and double click "android". It will open up a terminal window and load the SDK.

[![](/wp-content/uploads/2011/05/1.png)](/wp-content/uploads/2011/05/1.png)

#### Install packages

Here go to "Available Packages" and select what you want to download. I selected everything. Wait for the packages to download and install.

[![](/wp-content/uploads/2011/05/2.png)](/wp-content/uploads/2011/05/2.png)

#### Set the Path

Next you need to update the **PATH** for **tools/** and **platform-tools/** folder. To do this you need to edit your **~/.bash\_profile** (create it if you don't already have one). Add the following two lines

**export PATH=${PATH}:/Users/(username)/Desktop/android-sdk/tools**
**export PATH=${PATH}:/Users/(username)/Desktop/android-sdk/platform-tools**  [![](/wp-content/uploads/2011/05/3.png)](/wp-content/uploads/2011/05/3.png)

#### Download Fastboot

Now go to [http://developer.htc.com/adp.html](http://developer.htc.com/adp.html "http://developer.htc.com/adp.html") scroll to the middle of the page and **download Fastboot binary for OSX**. Because HTC host no longer the fastboot binary you can [**download**](/wp-content/uploads/2011/05/fastboot-mac.zip) the version on my blog. Unzip it and place it in **/tools/** [![](/wp-content/uploads/2011/05/4.png)](/wp-content/uploads/2011/05/4.png)

Now your all set for ADB and Fastboot

Tnx [http://androidtricks.net/](http://androidtricks.net/) for the article!

To check if your fastboot works you can start your terminal and cd **/Users/(username)/Desktop/android-sdk/tools** then run **./fastboot-mac devices** [![](/wp-content/uploads/2011/05/console2.png)](/wp-content/uploads/2011/05/console2.png)

When you some output you are connected. Happy modding!! :) _Note: please check the comments for more feedback_

\[banner\]
