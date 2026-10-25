---
_edit_last: "1"
_thumbnail_id: "1448"
author: thomasf
categories:
  - linux
cover:
  alt: spam
  image: /wp-content/uploads/2013/11/spam.png
date: "2013-11-12T10:58:33+00:00"
dsq_thread_id: "5139377989"
guid: https://blog.wapnet.nl/?p=1443
parent_post_id: null
post_id: "1443"
title: Show spam script on linux webserver
url: /2013/11/show-spam-script-on-linux-webserver/

---
Sometimes a website on a shared server is compromised by a hacker. Most of the time they use the website to spam the WWW around. It can be hard to find the specific script who is responsible for the spam. Here I will describe a method you can use to find and eliminate the script.

First stop postfix to stop the mail flood

`# service stop postfix
`

Now get the mailque and write down the message id (yellow)

`# mailq` [![mailq.png](/wp-content/uploads/2013/11/2013-11-12-11_44_26-Untitled-Paint.png)](/wp-content/uploads/2013/11/2013-11-12-11_44_26-Untitled-Paint.png)

Get the message header

`# postcat -vq A9CC9182699 |more ` [![message header](/wp-content/uploads/2013/11/message-header.png)](/wp-content/uploads/2013/11/message-header.png)

Now see the yellow text above. You have find the culprit. Now find the file location:

`# find /var/www/web/ -name *addwp.php*`

Eliminate the process and patch the website.

Delete the queue (USE THIS WITH CAUTION!!!!)

`# postsuper -d ALL`

And start postfix

`# service start postfix`

To find and kill a spamming perl script try this:

Find the process:

```
lsof -i :25
readlink -f /proc/{PID of process}/exe
kill PID
```

Check and delete the (sendmail) QUEUE:

```
cd /var/spool/mqueue/
ls
nano queue file
rm -f *
```

It can be very difficult to find a specific perl spam script because the path is not always visible. To find the script do a locate and isolate/rename the files.

```
locate *.pl |grep /var/www/
```

For more commands see my blog article: [/2014/04/linux-find-out-what-a-process-is-doing/](/2014/04/linux-find-out-what-a-process-is-doing/)

I found another nice tool to find suspicious scripts: [http://cbl.abuseat.org/findbot.pl](http://cbl.abuseat.org/findbot.pl)
