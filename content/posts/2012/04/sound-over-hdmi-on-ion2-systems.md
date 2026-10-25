---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - kodi
date: "2012-04-07T09:42:03+00:00"
dsq_thread_id: "5136178919"
guid: https://blog.wapnet.nl/?p=834
parent_post_id: null
post_id: "834"
title: Sound over HDMI on ION2 systems
url: /2012/04/sound-over-hdmi-on-ion2-systems/

---
1\. Connect to your box with SSH or SAMBA.

2\. Type the following:

> cp ~/.config/asound.conf.sample/asound.conf\_double-xs35gt.sample ~/.config/asound.conf

3\. In XBMC, go to System > Audio and make the following configuration:

> Audio output = HDMISpeaker configuration = 7.1 (or the what your receiver is capable of)Audio output device = custom
> Custom audio device = plughw:1,7
>
> Passthrough output device = custom
> Custom passthrough device = plughw:1,7

4\. Reboot the system
