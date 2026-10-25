---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
  - networking
date: "2012-01-26T13:21:19+00:00"
dsq_thread_id: "5171447709"
guid: https://blog.wapnet.nl/?p=784
parent_post_id: null
post_id: "784"
tags:
  - snmp
title: Configure SNMP Linux
url: /2012/01/configure-snmp-linux/

---
Be careful so do a backup of the snmpd config file.

```
[root@linux ~]# mv /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.org
```

Create a new config file.

```
[root@linux ~]# nano /etc/snmp/snmpd.conf
```

```
rocommunity  public IPMonitorServer
syslocation  "Webserver, WAPNET"
syscontact  some@email.com
```

Start the snmpd service and set the snmp stratup at boot on

```
[root@linux ~]# /etc/init.d/snmpd start
```

```
[root@linux ~]# chkconfig snmpd on
```
