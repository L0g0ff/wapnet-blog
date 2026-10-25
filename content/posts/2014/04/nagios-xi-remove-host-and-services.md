---
_edit_last: "1"
_thumbnail_id: "1525"
author: thomasf
categories:
  - linux
  - monitoring
cover:
  alt: xi-logo-large
  image: /wp-content/uploads/2014/04/xi-logo-large.png
date: "2014-04-23T21:27:51+00:00"
dsq_thread_id: "5137548264"
guid: https://blog.wapnet.nl/?p=1530
parent_post_id: null
post_id: "1530"
title: Nagios xi remove host and services
url: /2014/04/nagios-xi-remove-host-and-services/

---
Run each of the following scripts from:

/usr/local/nagiosxi/scripts

cd /usr/local/nagiosxi/scripts/

./nagiosql\_delete\_service.php –-config=LOC\_MASShost\_1

After the services have successfully been deleted, the host can be removed as well:

./nagiosql\_delete\_host.php –-host=LOC\_MASShost\_1

Once the host is removed, the new configuration can be applied and verified by running the reconfigure\_nagios.sh

./reconfigure\_nagios.sh
