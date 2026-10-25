---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - kodi
  - linux
date: "2012-06-19T21:30:30+00:00"
dsq_thread_id: "5153903251"
guid: https://blog.wapnet.nl/?p=930
parent_post_id: null
post_id: "930"
title: XBMC (XBMCBuntu) ContextMenu option Logitech Harmony
url: /2012/06/xbmc-xbmcbuntu-contextmenu-option-logitech-harmony/

---
With my Logitech Harmony 300 I didn't have the ContextMenu _(right click_ or _c keyboard)_ option. This action is essential when you want to change some movie information. If I use my XBMC Android app I had the title (= ContextMenu) option so I thought that it must be possible do the same with my logitech harmony. After some searching and debugging I find a solution.

The steps:

1. login to your xbmc with **ssh xbmc@IPXBMC**
1. **cp /usr/share/xbmc/system/keymaps/keyboard.xml /home/xbmc/.xbmc/userdata/keymaps/keyboard.xml**(never hack the original file, that can be overwritten when you do an update)
1. **nano** **/home/xbmc/.xbmc/userdata/keymaps/keyboard.xml**
1. Add this line between the other keyboard shurtcuts **<asterisk>ContextMenu</asterisk>**
1. Save the file (CTRL + W) and restart your xbmc to reload the keyboard.xml config

[![](/wp-content/uploads/2012/06/remote.png)](/wp-content/uploads/2012/06/remote.png)

Now you can login to the [www.myharmony.com](http://www.myharmony.com) website and configure the **asterisk (\*)** key to the **List** button on your remote. Sync your remote with an USB key and your ContextMenu option is ready for use :)

If you have some trouble finding out which buttons you can use, the best way is enabling the debugging option in your XBMC. Go to the system settings of your XBMC and enable debugging mode. Then make a ssh connection to your XBMC and type **tail -f /home/xbmc/.xbmc/temp/xbmc.log** to see realtime output.

If you send some remote (IR) actions you can capture the output and if you want to change the action you can edit the keyboard.xml.

[![](/wp-content/uploads/2012/06/debug.png)](/wp-content/uploads/2012/06/debug.png)

If this helps you please leave a comment. Happy hacking :D
