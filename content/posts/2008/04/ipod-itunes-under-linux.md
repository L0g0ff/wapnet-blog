---
_edit_last: "1"
author: thomasf
categories:
  - ipod
  - linux
date: "2008-04-19T22:28:41+00:00"
dsq_thread_id: "5185862191"
guid: https://blog.wapnet.nl/?p=37
parent_post_id: null
post_id: "37"
title: iPod / iTunes under Linux
url: /2008/04/ipod-itunes-under-linux/

---
See this blog: [http://ipodvirtualos.blogspot.com/](http://ipodvirtualos.blogspot.com/)

### [This works](http://ipodvirtualos.blogspot.com/2007/11/this-works.html)

 [![](http://bp0.blogger.com/_WJfoaZV2G3g/Ryn7UCeRgYI/AAAAAAAAAAY/bqHaZCDaFBM/s200/Screenshot-VirtualBox+-+About.png)](http://bp0.blogger.com/_WJfoaZV2G3g/Ryn7UCeRgYI/AAAAAAAAAAY/bqHaZCDaFBM/s1600-h/Screenshot-VirtualBox+-+About.png)
After those failed methods I was sure about some necessary things:

- A Windows XP installation is required (for pc's), so I need an emulator.
- The emulator should support USB 2.0
- I want it free and legal (opinion)
- It should be stable and fast to work with

Finaly after using Google (again) I found an emulator that would do the job: VirtualBox. It's a free emulator with USB support and it runs remarkably faster than the VMWare Workstation. For people who run Compiz-Fusion: VirtualBox in fullscreen allows cube rotation while the cursor is on the VirtualBox-window. I haven't found a way to do this with VMWare...

This is how I did it:

First, to be able to access your USB-ports in VirtualBox you need to run the following command as superuser, or add his equivalent line in /etc/fstab :

> \# sudo mount -t usbfs none /proc/bus/usb

Now to download and install VirtualBox, visit

> http://www.virtualbox.org/wiki/Downloads

and download the package that fits your linux distribution and processor architecture. The packages are automatically installable with the GDebi Package Installer (for Ubuntu users).

After the installation read the users manual on

> http://www.virtualbox.org/download/UserManual.pdf

to find out how to create a new guest operation system. You should create a new Windows XP home/professional guest.(\*)

Once you have set up a new guest you should install Guest Additions to improve the functionality:

1. Start your guest OS and wait until it is completely booted
1. Go to the Device menu and take the last item: Install Guest Additions.
1. A wizard will start in your guest OS.
1. You will be prompted to restart your guest, so do this.

Then download and install iTunes 7.4 (or later):

> http://www.apple.com/itunes/download/

Plug in your iPod, and wait for iTunes to react.
If it doesn't, go to the Device menu, select USB Devices and click your iPod.
If your iPod is not in the list, you should plug in you iPod before you start VirtualBox.
