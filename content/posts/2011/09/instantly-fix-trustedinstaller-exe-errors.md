---
_edit_last: "1"
author: thomasf
categories:
  - windows
date: "2011-09-02T08:14:43+00:00"
dsq_thread_id: "5153524924"
guid: https://blog.wapnet.nl/?p=639
parent_post_id: null
post_id: "639"
title: Instantly Fix TrustedInstaller.exe Errors
url: /2011/09/instantly-fix-trustedinstaller-exe-errors/

---
# How to Disable TrustedInstaller.exe

TrustedInstaller.exe is the Windows Module Installer program used in the Windows Vista operating system. The process works in conjunction with Windows Integrated Update in Windows Vista. The program is known to run randomly and consume up to 100% of CPU causing dramatic slowdown in the performance of a Windows Vista computer. Trustedinstaller.exe holds the rights to some essential Windows Vista programs and applications, which means that trustedinstaller.exe gets blanket authority to do whatever is necessary and use as much of the system resources, CPU and RAM as needed.

After a program or application is trustedinstaller.exe approved, Windows Vista considers it as  an essential system resource and  Windows gives it as much CPU as required.

**How to Fix High CPU Usage Problem Caused by TrustedInstaller.exe** **Let’s have a look at some of the methods that you can use to resolve the issue:** _**Method 1: Clear Problem History**_

The following fix is intended for situations where trustedinstaller.exe causes problems due to the Problem Reports and Solutions history maintained in Windows Vista.

1. Go to _**Start**_ and then select _**Control** **Panel**_.
1. Turn on _**Classic** **View**_.
1. Select _**Problem Reports and Solutions**_.
1. Click _**Clear Solution and Problem History** in the left panel._
1. Confirm your decision.
1. Exit the Problems Reports and Solutions Window and Control Panel.

A variation to this fix is to click **Change** in the **Problems Reports and Solutions** Window. And then modify the configuration from _**Check for solutions automatically**_ setting to _**Ask me to check if a problem occurs**_.

**Method 2: Change Microsoft Update Startup Settings to Manual**

1. Go to _**Start**_ and then select _**Control** **Panel**._
1. Select _**Administrative** **Tools**_ and then select _**Services**_ **.**
1. Scroll down to _**Microsoft** **Update**,_ right-click on it and then select **Stop.**
1. Right-click on Microsoft Update again and select _**Properties**_.
1. On the **General** tab, set _**Startup** **type**_ as _**Manual**_.
1. Next, display the _**Recovery**_ tab.
1. Choose _**Take** **No** **Action**_ and click _**OK**_ for _**First** **Failure**_.
1. Exit the properties dialog box.
1. Bring up your _**Task** **Manager**_ by pressing on _**Ctrl** \+ **Alt** \+ **Del**_ or _**Ctrl** \+ **Shift** \+ **Esc**_ simultaneously.
1. On the **Processes** tab, look for and select _**trustedinstaller.exe**_.
1. Click _**End process**_ to kill _**trustedinstaller.exe**._

_**Method 3: Disable Automatic Update**_

1. Go to _**Start**_ and then select _**Control** **Panel**_.
1. Go to _**System** **and** **Maintenance**_.
1. Click **Turn _automatic_** _**update on or off** option_.
1. Next, depending on your preference choose one of the following options:

   - Never check for updates (not recommended)

   - Check for updates but let me choose whether to download and install them

   - Download updates but let me choose whether to install them
1. Click _**OK**_ to save your changes and exit the dialog box.

_**Method 4: Stop**_ **_the Windows Module Installer That Runs Trustedinstaller.exe_**

1. Click on _**Start**_,in the _**Start** **Search**_ box, type _**msconfig**_ and then press Enter.
1. Click **Continue** when **_User Account Control_** prompt is displayed.
1. In the **System Configuration** window that is displayed, open the **Services** tab.
1. Locate and clear the **Windows Module Installer** check box.
1. Click _**OK**_ save your changes and exit the dialog box.
1. Next, open **Services** window again and change the **Startup** **type** of **Windows Module Installer** to **Manual**.

_**Method 5: Install Windows Vista Service Pack 1**_

Source: [http://www.exe-error-fixes.com/disable-trustedinstallerexe/](http://www.exe-error-fixes.com/disable-trustedinstallerexe/)
