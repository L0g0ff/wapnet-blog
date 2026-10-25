---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
date: "2012-07-28T11:00:22+00:00"
dsq_thread_id: "5136179061"
guid: https://blog.wapnet.nl/?p=947
parent_post_id: null
post_id: "947"
title: '[Ubuntu 12.04] Install ATI Video Drivers'
url: /2012/07/ubuntu-12-04-install-ati-videodrivers/

---
1) First, check the software sources, then paste this command into the terminal:

```
sudo apt-get install build-essential cdbs dh-make dkms execstack dh-modaliases fakeroot
```

2) If you have a 64 bit system, do this step:

```
sudo apt-get install ia32-libs-multiarch:i386 lib32gcc1 libc6-i386
cd /usr
sudo ln -svT lib /usr/lib64
```

3) Paste these commands into the terminal to create a new folder and download your driver:

```
cd ~/
mkdir catalyst12.4
cd catalyst12.4/
wget http://www2.ati.com/drivers/linux/amd-driver-installer-12-4-x86.x86_64.run
chmod +x amd-driver-installer-12-4-x86.x86_64.run
```

4-A) IF you have Intel HD graphics AND discrete ATI GPU, then do this(and reboot):

```
sudo ./amd-driver-installer-12-4-x86.x86_64.run
```

4-B) IF you have just the ATI Graphics card, then do this (like in video), it WILL take a while:

```
sh amd-driver-installer-12-4-x86.x86_64.run --buildpkg Ubuntu/precise
sudo dpkg -i fglrx*.deb
```

5)Overwrite the /etc/X11/xorg.conf file(anyway):

```
sudo amdconfig --initial -f
```

6) Force the use of the new xorg.conf file:

```
sudo amdconfig --input=/etc/X11/xorg.conf --tls=1
```

7)Reboot the computer, to verify your installation, follow the 8th step, otherwise you're Done.

8) To verify your installation, in terminal type:

```
fglrxinfo
```

9) OPTIONAL - you can try this for fun, in terminal type:

```
fgl_glxgears
```

Original source: [http://www.youtube.com/watch?v=52JRCddtZLk](http://www.youtube.com/watch?v=52JRCddtZLk)
