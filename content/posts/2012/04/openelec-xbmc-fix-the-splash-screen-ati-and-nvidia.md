---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - kodi
date: "2012-04-07T09:54:15+00:00"
dsq_thread_id: "5216918014"
guid: https://blog.wapnet.nl/?p=839
parent_post_id: null
post_id: "839"
title: OpenElec XBMC Fix the splash screen ATI and NVidia
url: /2012/04/openelec-xbmc-fix-the-splash-screen-ati-and-nvidia/

---
If your OpenELEC machine says "could not open framebuffer no such file or directory" when you turn it on, follow this to get the splash screen working.

The splash screen is much prettier than some plain text in the corner of the screen, so follow this to get your splash working.

You'll need:

- SSH access to your OpenELEC machine
- Nano installed; for versions 0.7 and above, you'll need to install the nano add-on from System > Addons > Get Addons > OpenELEC.tv > Programs > nano and click install.

OK, let's begin. Open an SSH session to your OpenELEC machine then at the prompt, type:

```
mount -o remount,rw /flash
```

This allows read/write access to the configuration file we need to access.

Next, type:

```
nano /flash/extlinux.conf
```

This will open up a terminal-based text editor called nano. It's very easy to use, so move your cursor to the end of the following line:

```
APPEND boot=LABEL=System disk=LABEL=Storage quiet
```

and add the following text:

for NVIDIA:

```
vga=792
```

for ATI:

```
vga=0x323
```

If you are using NVIDIA your line should read:

```
APPEND boot=LABEL=System disk=LABEL=Storage quiet vga=792
```

If you are using ATI your line should read:

```
APPEND boot=LABEL=System disk=LABEL=Storage quiet vga=0x323
```

Now, type \[CTRL\] and X to exit. You'll be prompted to save the file - just hit \[ENTER\] to save the file.

You should be back at the prompt now, so just type exit to close the prompt

```
exit
```

Reboot your OpenELEC box and you should now see the splash screen.
