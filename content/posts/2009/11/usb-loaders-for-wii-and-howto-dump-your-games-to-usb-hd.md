---
_edit_last: "1"
author: thomasf
categories:
  - wii
date: "2009-11-29T21:47:11+00:00"
dsq_thread_id: "5136177886"
guid: https://blog.wapnet.nl/?p=277
parent_post_id: null
post_id: "277"
title: USB Loaders for Wii (and howto dump your games to USB HD)
url: /2009/11/usb-loaders-for-wii-and-howto-dump-your-games-to-usb-hd/

---
My Wii has a lot of troubles readings copied disk. I think this is because of a crappy modchip. I will recommend everyone a softmod instead of an chip. If you have hardware troubles with your softmod you can remove all the softmod installations and go back to nintendo and let them repair your harware.

This weekend I've connected an old external USB IDE disk to my Wii and dumped  all my ISO's, Game Copies and original DVD's  to the disk. Now every thing works fine :D

What you need:

1\. A Wii that's already softmodded with the CIOS 249 Rev 14 (<< tested)
2\. An external IDE disk (I had al lot of trouble with an new 2,5" WD SATA Disk.
3\. Configurable USB Loader for dump your DVD's ([Download](/wp-content/uploads/2009/11/Cfg_USB_Loader_48.zip))
4\. WBFS Manager ([http://wbfsmanager.codeplex.com/](http://wbfsmanager.codeplex.com/))
5\. USB Loader GX ([http://usbloadergx.koureio.net/downloads](http://usbloadergx.koureio.net/downloads))

The steps:

1\. Download, Install and Run the WBFS Manager on your Windows pc
2\. Attach a dedicated USB disk to your pc
3\. Format the disk with the WBFS Manager to the WBFS (filesystem)
4\. You can extract some downloaded ISO's to your USB disk now
5\. Connect your USB disk in the left -or- down USB port on your Wii
6\. Start the USB Loader GX on your Wii trough the homebrew channel
7\. When disk the is mount correctly you can run the games now. If you need the 002 fix you can set this in the load settings of the specific game.

When you want to complete your collection with all your Wii DVD's:

1\. Extract the Configurable USB Loader files to your SD
2\. Start the Configurable USB Loader via the homebrew channel
3\. Press the + button on the Wiimote
4\. Press the A button after the disk is read
5\. Have patience :)

Now you can play the games with the one of the two USB loaders.

Some Video's and screenshots:

1\. WBFS Manager
[![WBFSManager20](/wp-content/uploads/2009/11/WBFSManager20.jpg)](/2009/11/usb-loaders-for-wii-and-howto-dump-your-games-to-usb-hd/wbfsmanager20/)
2\. USB Loader GX


3\. Configurable USB Loader
