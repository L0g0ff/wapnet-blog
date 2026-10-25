---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
date: "2012-10-01T20:55:15+00:00"
dsq_thread_id: "5333087064"
guid: https://blog.wapnet.nl/?p=992
parent_post_id: null
post_id: "992"
title: Archlinux install UAR package (Arch User Repository)
url: /2012/10/archlinux-install-uar-package-arch-user-repository/

---
Some packages are not in the default repositories you can install these on a alternative way.

First install the base development tools:

```
#pacman -S base-devel
#pacman -S wget
#pacman -S sudo
```


Go to [https://aur.archlinux.org](https://aur.archlinux.org) and find you package
Find the tarball, right click it and copy link location
Wget the package (example nemo-fm) and install the package

```
$cd ~
$wget https://aur.archlinux.org/packages/ne/nemo-fm/nemo-fm.tar.gz
$tar xvzf nemo-fm.tar.gz
$cd nemo-fm
$makepkg -s
$sudo pacman -U nemo-fm-1.0.2-1-i686.pkg.tar.xz
```


Have fun :)
