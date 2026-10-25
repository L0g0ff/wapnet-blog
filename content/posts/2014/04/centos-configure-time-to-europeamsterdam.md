---
_edit_last: "1"
author: thomasf
categories:
  - uncategorized
date: "2014-04-18T21:14:58+00:00"
dsq_thread_id: "5177316086"
guid: https://blog.wapnet.nl/?p=1527
parent_post_id: null
post_id: "1527"
title: Centos Configure time to Europe/Amsterdam
url: /2014/04/centos-configure-time-to-europeamsterdam/

---
I always have some time issues in Linux. Here the howto:

Check the time

```
# date
Fri Mar 18 21:50:43 CET 2011
```

Install and configure NTP

```
# yum install ntp
# service ntpd stop
# ntpdate pool.ntp.org
# /etc/init.d/ntpd start
# chkconfig ntpd on
```

Configure the localtime

```
# cd /etc/
# ls -la |grep localtime
# /etc/localtime -> /usr/share/zoneinfo/Europe/Amsterdam
# ln -sf /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime
```

Configure the shell time

```
export TZ=CET
```
