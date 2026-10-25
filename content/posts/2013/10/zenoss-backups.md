---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
_thumbnail_id: "1423"
author: thomasf
categories:
  - linux
cover:
  alt: zenoss
  image: /wp-content/uploads/2013/10/zenoss.png
date: "2013-10-17T08:10:47+00:00"
dsq_thread_id: "5172606328"
guid: https://blog.wapnet.nl/?p=1416
parent_post_id: null
post_id: "1416"
title: Zenoss Backups
url: /2013/10/zenoss-backups/

---
Create a zenoss user cron

`sudo crontab -u zenoss -e`

Use this lines to backup every day 10 AM.

`HISTFILE=/home/zenoss/.bash_history
HOME=/home/zenoss
INSTANCE_HOME=/opt/zenoss
LD_LIBRARY_PATH=/opt/zenoss/lib
LOGNAME=zenoss
MAIL=/var/spool/mail/zenoss
PATH=/opt/zenoss/bin:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:/home/zenoss/bin
PWD=/home/zenoss
PYTHONPATH=/opt/zenoss/lib/python
USER=zenoss
ZENHOME=/opt/zenoss
30 10 * * * /opt/zenoss/bin/zenbackup -v10`

Note: When I not put the variables to the cron I get this error:
`ERROR: $ZENHOME is not set.
This is usually caused by executing this command as root rather than as the zenoss user. Either define $ZENHOME or run this command as a different user.`

Because I can't find a nice solution on the internet I fix it to add the SET lines to the cron.

Create a cleanup job

`sudo crontab -e`

Use this line to cleanup the backups every sunday 12 AM

`00 12 * * 7 root /usr/bin/find /opt/zenoss/backups -mtime +30 -type f -exec rm \{\} \;`
