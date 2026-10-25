---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - kodi
  - media-center
date: "2012-04-01T16:10:36+00:00"
dsq_thread_id: "5142407908"
guid: https://blog.wapnet.nl/?p=825
parent_post_id: null
post_id: "825"
title: XBMCBuntu boot problem when TV is turned off (Nvidia)
url: /2012/04/xbmcbuntu-boot-problem-when-tv-is-turned-off-nvidia/

---
When I boot my XBMC box and don't turn my TV on before the boot XBMC was not succesfully. After some digging and googling I found the solution.

1. On your XBMCBuntu device press **ALT+CRTL+F1**
1. login with user xbmc, pass xbmc
1. type **sudo su -**
1. type **killall Xorg**
1. press **ALT+CRTL+F7**
1. login with user xbmc, pass xbmc and **select XBMCBuntu**
1. Now press the button on the left bottom (or press the windows/command key)
1. Select System Tools > Nvidia X Server Settings
1. click on DFP-0, DFP-1 or whatever then click "Acquire EDID.."
1. Save it as **edid.bin** in your **/home/xbmc/** folder
1. Now make an ssh connection from another PC to your XBMC box
1. Example linux/osx: **ssh 192.168.1.12 -l xbmc** for windows try [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
1. Make yourself root **sudo su -**
1. Password **xbmc**
1. Type: **cat /var/log/Xorg.0.log \| grep "Assigned Display Device: DFP-"**
1. Keep the DFP-X number in mind
1. Make a backup of your X.org config **cp /etc/X11/xorg.conf /etc/X11/xorg.conf.orig**
1. open the xorg.conf **nano /etc/X11/xorg.conf**
1. Delete all the lines with **ctrl+k**(multiple times)
1. Now paste the new config:

```
Section "Device"
    Identifier     "nvidia"
    Driver         "nvidia"
    Option         "DynamicTwinView" "False"
    Option         "NoFlip" "false"
    Option         "NoLogo" "true"
    Option         "ConnectToAcpid" "0"
    Option         "FlatPanelProperties" "Scaling = Native"
    Option         "ModeValidation" "NoVesaModes, NoXServerModes"
    Option         "ConnectedMonitor" "DFP-1"
    Option         "CustomEDID" "DFP-1:/home/xbmc/edid.bin"
EndSection

Section "Screen"
    Identifier     "screen"
    Device         "nvidia"
    DefaultDepth    24
    Option         "ColorRange" "Full"
    SubSection     "Display"
        Depth       24
        Modes      "1280x720"
    EndSubSection
EndSection

Section "Extensions"
    Option         "Composite" "false"
EndSection

Section "InputDevice"
    Identifier     "Mouse0"
    Driver         "mouse"
    Option         "Protocol" "auto"
    Option         "Device" "/dev/input/event4"
    Option         "Emulate3Buttons" "true"
    Option         "Emulate3Timeout" "70"
    Option         "SendCoreEvents" "true"
    Option         "ZAxisMapping" "4 5"
EndSection

Section "ServerFlags"
    Option         "AllowEmptyInput" "false"
EndSection
```

- Change the DFP-X number in the config if you have another number then DFP-1
- press CTRL+O to safe the file
- Type **shutdown -h now** to turn the XBMC box of
- Turn of the TV and turn your XBMC box on
- Test if everything works fine now :)

If this works for you please leave a comment below :)

[Source URL](http://openelec.tv/forum/67-display/14675-howto-fix-hdmi-resolution-problems-when-your-openelec-box-was-turned-on-while-the-tv-was-off?limit=20&start=20#21288) [Config URL](http://paste2.org/p/1953620)
