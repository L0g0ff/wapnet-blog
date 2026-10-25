---
_edit_last: "1"
author: thomasf
categories:
  - linux
date: "2008-10-06T10:48:27+00:00"
dsq_thread_id: "5164883153"
guid: https://blog.wapnet.nl/?p=77
parent_post_id: null
post_id: "77"
title: Linux Filemon
url: /2008/10/linux-filemon/

---
It is possible to achieve similar functionality to filemon with a linux 2.6.1 or newer kernel.
what you need to do is the following:
1\. Make sure that syslog doesn't log kern.debug to a file(check /etc/syslog.conf). if it does, disable it temporarily (better), or stop syslog altogether (worse, because you will eliminate one possible cause of the disk activity)
2\. type:
echo 1 > /proc/sys/vm/block\_dump
3\. in bash, type (modify to fit your favourite shell):
while true; do dmesg -c; sleep 1; done;

This effectively gives you a realtime live view of all disk activity
note that if you didn't dmesg -c since you booted, dmesg might contain a lot of info in the buffer, so let it barf everything onto the screen before attempting to actually read it.

remember to restore things back to the way they were when you are done:
1\. echo 0 > /proc/sys/vm/block\_dump
2\. restore syslog activity and/or kern.debug logging

Enjoy!
