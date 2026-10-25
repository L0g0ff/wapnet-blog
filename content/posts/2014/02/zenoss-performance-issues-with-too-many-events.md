---
_edit_last: "1"
_wp_old_slug: zenoss-performance-issue-with-too-many-events
author: thomasf
categories:
  - linux
  - monitoring
  - networking
date: "2014-02-03T10:23:36+00:00"
dsq_thread_id: "5140503210"
guid: https://blog.wapnet.nl/?p=1490
parent_post_id: null
post_id: "1490"
title: 'Zenoss: Performance issues with too many events'
url: /2014/02/zenoss-performance-issues-with-too-many-events/

---
When you have too many events in your zenoss environment the zenoss webinterface will be very sloooooooow. And you get all kind of errors:

- Script don't respond
- Connection refused. Check zeneventserver status on deamons
- A zenoss error has occurred

When you start top you see alot of java executables when you click on the Infrastructure zenoss button. Java sometimes take 350% CPU.

`java -Djetty.host=localhost -server -XX:+HeapDumpOnOutOfMemoryError -DZENOSS_COMMAND=zeneventserver -DZENHOME=/opt/zenoss -Djetty.home=/opt/zenoss -Djetty.logs=/opt/zenoss/log -Dlogback.configurationFile=/opt/zenoss/etc/zeneventserver/logback.xml -Xmx1024m -DZENOSS_DAEMON=y -jar /opt/zenoss/lib/jetty-start-7.5.3.v20111011.jar --config=/opt/zenoss/etc/zeneventserver/jetty/start.config --ini=/opt/zenoss/etc/zeneventserver/jetty/jetty.ini --pre=etc/zeneventserver/jetty/jetty-logging.xml`

I've read a lot of zenoss documentation on the internet but didn't   found a nice article to get rid of all the events. So here is an article how I fixed it.

Basic steps:

1. Backup Zenoss
1. Stop zenoss
1. Create a new zeneventserver database
1. Remove zeneventserver content
1. Restore the zenoss backup
1. Start zenoss
1. Enjoy your fast zenoss :)

Detailed steps:

- ssh zenoss host
- Switch zenoss user

`# su zenoss`

- Create backup:

`$ /opt/zenoss/bin/zenbackup -v10`

- Stop Zenoss service

`$ zenoss stop`

- edit  the zeneventserver script

`nano /opt/zenoss/bin/zeneventserver-create-db`

- Search for root and add the root password

[![root-password](/wp-content/uploads/2014/02/root-password.png)](/wp-content/uploads/2014/02/root-password.png)

- Run the script

`$ zeneventserver-create-db --force --dbtype=mysql`

- Clear the zeneventserver folder

`rm -rf $ZENHOME/var/zeneventserver/*`

Now some tricky part. Zenoss change some MySQL passwords when you do a restore.  This result in a access denied for user zenoss@localhost during a restore. There is a fix for this problem. Reset the zenoss@'localhost' and zenoss@'%' MySQL passwords before you do a restore.

First get the current mysql from the global.conf file (yellow). This password is the password you need for the restore.

`$nano /opt/zenoss/etc/global.conf` [![global.conf](/wp-content/uploads/2014/02/global.conf_.png)](/wp-content/uploads/2014/02/global.conf_.png)

Tip: Too check the password (encrypted). You can do the same after you change the password:

`$ mysql -uroot -p` `mysql> select * from mysql.user;` [![mysql-encrypted](/wp-content/uploads/2014/02/mysql-encrypted.png)](/wp-content/uploads/2014/02/mysql-encrypted.png)

Now reset the password

`SET PASSWORD FOR 'zenoss'@'localhost' = PASSWORD('BEagPxxxxxxxxxxxxxxx');` `SET PASSWORD FOR 'zenoss'@'%' = PASSWORD('BEagPxxxxxxxxxxxxxxx');`

When you check the permissions now you see another encryption:

`$ mysql -uroot -p` `mysql> select * from mysql.user;`

(I don't have an image example because this is an production enviroment)

**Optional:** To check the zenoss user permissions:

`mysql> SELECT user, host, db, select_priv, insert_priv, grant_priv FROM mysql.db;` [![mysql-permissions](/wp-content/uploads/2014/02/mysql-permissions.png)](/wp-content/uploads/2014/02/mysql-permissions.png) **Optional:** When you still have errors or the above rights ain't good try these two MySQL scripts:
`
mysql> CREATE USER 'zenoss'@'%' IDENTIFIED BY 'some_pass';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'zenoss'@'localhost'
-> WITH GRANT OPTION;
` `mysql> CREATE USER 'zenoss'@'%' IDENTIFIED BY 'some_pass';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'zenoss'@'localhost'
-> WITH GRANT OPTION;
`

Ok, now everting is set do a restore. The -v stands for verbose and with the no-eventsdb you don't restore all the events. That's exactly what we want

`zenrestore --file=/opt/zenoss/backups/zenbackup_2014013 -v --no-eventsdb`

Now start zenoss

`$zenoss start`

That's it.  Enjoy the performance and set some parameters that your events ain't that big any more in the future.

Source: [http://www.nickyeates.com/technology/zenoss/useful\_commands\_zenoss4](http://www.nickyeates.com/technology/zenoss/useful_commands_zenoss4) Source: [http://community.zenoss.org/docs/DOC-3048](http://community.zenoss.org/docs/DOC-3048)
