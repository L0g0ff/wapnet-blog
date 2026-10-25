---
_disable_fbc: ""
_edit_last: "1"
_thumbnail_id: "1575"
_wp_old_slug: install-chrome-with-atch-linux
author: thomasf
categories:
  - linux
cover:
  alt: arch-mini
  image: /wp-content/uploads/2014/08/arch-mini.png
date: "2014-08-15T22:35:22+00:00"
dsq_thread_id: "5136256129"
guid: https://blog.wapnet.nl/?p=1561
parent_post_id: null
post_id: "1561"
title: Install chrome with Arch Linux
url: /2014/08/install-chrome-with-arch-linux/

---
In Windows I like Firefox more than chrome because everything is already "Google". But Google chrome has a nice stable and fast flash plugin built-in and so I need a chrome browser in Linux.... Because I'm testing Arch Linux (Antergos actually ) and Google don't have arch packages I found a way to install it automatically for me with the AUR repository. **$yaourt -S google-chrome** More info about the yaourt ( **Y** et **A** n **O** ther **U** ser **R** epository **T** ool):

## Using yaourt

You can install packages (including [AUR](https://wiki.archlinux.org/index.php/AUR "AUR") packages) with

```
$ yaourt packagename

```

or

```
$ yaourt -Sa packagename

```

You can update your system including AUR packages with:

```
$ yaourt -Syua
```
