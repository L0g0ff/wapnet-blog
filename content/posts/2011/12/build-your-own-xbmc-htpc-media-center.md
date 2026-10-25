---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - media-center
date: "2011-12-01T21:49:00+00:00"
dsq_thread_id: "5136178749"
guid: https://blog.wapnet.nl/?p=734
parent_post_id: null
post_id: "734"
tags:
  - howto
  - htpc
  - media-center
  - openelec
  - xbmc
  - zotac-zbox
title: Build your own embedded XBMC HTPC
url: /2011/12/build-your-own-xbmc-htpc-media-center/

---
Earlier I wrote an [article](/2010/04/howto-build-the-cheapest-xbmc-high-definition-media-center-ever-a-k-a-xbox1-softmod/ "Howto: Build the cheapest XBMC High Definition media center ever a.k.a. XBOX1 Softmod") how to build a cheap XBMC media center with a XBOX1. But nowadays you want a high definition media center and XVID and DIVX isn't acceptable anymore on your full HD television. So I read a lot of information how to make an nice media streamer like the popcorn hour, ac rayon and xstreamer but then highly customizable .

I choose for XBMC because it is highly customizable and there are tons of addons, plugins, script, skins, fanart, visualizations. XBMC is a media streamer so it's recommended that all your downloaded music, photo's, tv series and movies are on a NAS (network attached storage) device. If you want there are NZB and torrent plugins and you can download the software to the local disk but I don't use any of these methods. XBMC is also in almost every language and the GUI for normal use is girlfriend, wife and kids friendly ;)

Because the software is highly customizable and it's always in development you get sometimes some unstable situations when you change some config settings. I can live with that but if you want a very stable product maybe you can better look further to an out-of-the-box product like the AC Ryan.

Also the software isn't for noobs. If you don't like to spent hours to tweaking the software how YOU want it please buy a product like the Popcorn Hour or AC Ryan that isn't customizable.

But for normal use the software is stable and you will very often surprised by the tricks and the nice performance of the XBMC.

XBMC is open source and cross platform. There are official builds for OSX, Windows, Linux, iPAD, Apple TV and more ports still coming. The build I choose is OpenELEC. I choose for OpenELEC because that is an embedded linux distribution optimized for XBMC only. The software is compiled for all the common hardware platforms. The boot time is 30 seconds with SD (with SSD 5 sec) and the installation is very easy and I explain here how you can install the XBMC OpenELEC software.

The hardware I use is a Zotac ZBOX ID41, 2 GB RAM (Kingston ValueRAM KVR1333D3S9/2G) and a 4GB SD class 2 card. If you have an Android or Apple smartphone (or tablet)  you can download the "XBMC remote" app for remote. So you don't need to buy a remote.  Total costs 200,- euro. That is very cheap for a full hd media center :)

What do you need to build this system:

1. Zotac ZBOX
1. 2 GB of RAM
1. 4GB SD card
1. Tabled or smartphone for remote (xbmc remote app installed)
1. 256mb or higher USB stick for the installation
1. OpenELEC ION x86\_64 build ([link](http://openelec.tv/get-openelec))
1. HDMI cable
1. USB keyboard
1. [Putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
1. UTP Network cable and network connection (wireless also supported)

Hardware:
[![](/wp-content/uploads/2011/12/1.jpg)](/wp-content/uploads/2011/12/1.jpg)

Unboxed:
[![](/wp-content/uploads/2011/12/2.jpg)](/wp-content/uploads/2011/12/2.jpg)

First you need to do is build in the RAM. You can loosen the screws just with your hands.

[![](/wp-content/uploads/2011/12/3.jpg)](/wp-content/uploads/2011/12/3.jpg)

Now open the cover
[![](/wp-content/uploads/2011/12/5.jpg)](/wp-content/uploads/2011/12/5.jpg)

Build in the memory
[![](/wp-content/uploads/2011/12/7.jpg)](/wp-content/uploads/2011/12/7.jpg) and \*click\* [![](/wp-content/uploads/2011/12/8.jpg)](/wp-content/uploads/2011/12/8.jpg)

Close the cover and connect the ZBOX with the HDMI cable to the TV

[![](/wp-content/uploads/2011/12/10.jpg)](/wp-content/uploads/2011/12/10.jpg) Turn on the ZBOX to see if you get a boot error (and the memory is working correctly)
[![](/wp-content/uploads/2011/12/11.jpg)](/wp-content/uploads/2011/12/11.jpg)

Ok, now we create the bootable OpenELEC USB stick to install the software. Because these steps are very good

documented by OpenELEC please follow these steps: [http://openelec.tv/find-help/documentation/installation](http://openelec.tv/find-help/documentation/installation)

Now insert the SD card, USB stick and the keyboard into the Zotac ZBOX and press the power button. The setup will start.

[![](/wp-content/uploads/2011/12/17.jpg)](/wp-content/uploads/2011/12/17.jpg)[![](/wp-content/uploads/2011/12/18.jpg)](/wp-content/uploads/2011/12/18.jpg)

Setup:

[![](/wp-content/uploads/2011/12/22.jpg)](/wp-content/uploads/2011/12/22.jpg) Press ok and then quick install

[![](/wp-content/uploads/2011/12/23.jpg)](/wp-content/uploads/2011/12/23.jpg)

Choose the SD card and then OK

[![](/wp-content/uploads/2011/12/24.jpg)](/wp-content/uploads/2011/12/24.jpg)

Now the setup will start. This will take 3 minutes.

[![](/wp-content/uploads/2011/12/25.jpg)](/wp-content/uploads/2011/12/25.jpg)

After the setup is done you can restart the device. The first time boot takes 2 minutes and than you have the most EPIC Media Center you can have:

[![](/wp-content/uploads/2011/12/27.jpg)](/wp-content/uploads/2011/12/27.jpg)

Now you must install 2 fixes. One for the [sound over HDMI](/2012/04/sound-over-hdmi-on-ion2-systems/) and one to [fix the splash screen](/2012/04/openelec-xbmc-fix-the-splash-screen-ati-and-nvidia/).

For both fixes you need [putty](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) and a little linux knowledge. Open the system preferences to see the IP adres. (If you use wireless please configure this first).

[![](/wp-content/uploads/2011/12/31.jpg)](/wp-content/uploads/2011/12/31.jpg)

Now connect with putty. User **"root**", password is " **openelec**" and apply the fixes. After you applied the fixes with SSH/Putty you can change the sound settings within XBMC. But if you don't it work also :P

[![](/wp-content/uploads/2011/12/33.jpg)](/wp-content/uploads/2011/12/33.jpg)

Bye bye good old XBOX. After eight years of loyal service, I will miss you ;-)

[![](/wp-content/uploads/2011/12/28.jpg)](/wp-content/uploads/2011/12/28.jpg)

I hope you enjoyed this review if you have some questions feel free to ask :)

[XBMC / OpenELEC Features](http://www.youtube.com/watch?v=DY-I5MWA7CE)

[XBMC Remote and how to configure](http://www.youtube.com/watch?v=IhrWepWmiDo)
