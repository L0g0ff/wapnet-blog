---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - osx
date: "2011-04-26T20:09:14+00:00"
dsq_thread_id: "5136178209"
guid: https://blog.wapnet.nl/?p=565
parent_post_id: null
post_id: "565"
title: 'OSX Finder: Sort Folder Before File'
url: /2011/04/osx-finder-sort-folder-before-file/

---
Here the trick to change this behavior under Finder.

1. Open Terminal.
1. Open InfoPlist.strings file using vi text editor as a root.
    sudo vi /System/Library/CoreServices/Finder.app/Contents/Resources/English.lproj/InfoPlist.strings

    (change English.lproj to your language)
1. Find below line:
    /\\* General kind strings \*/
    "Folder" = "Folder";
1. Do following change (by adding space before " Folder" word after equal sign).
    "Folder" = " Folder";
1. Save the InfoPlist.strings file by press \[esc\], type wq (mean write and quit vi) then press \[return\].
1. Close Terminal
1. Restart your Finder, right click on Finder icon while pressing the key\[option\] and select Relaunch your Finder.
1. [![](/wp-content/uploads/2011/04/finder-relaunch.jpg)](/wp-content/uploads/2011/04/finder-relaunch.jpg)
1. Open Finder and order by Kind.
1. [![](/wp-content/uploads/2011/04/finder-kind.jpg)](/wp-content/uploads/2011/04/finder-kind.jpg)
