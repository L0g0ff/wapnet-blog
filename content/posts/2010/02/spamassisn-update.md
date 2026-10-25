---
_edit_last: "1"
author: thomasf
categories:
  - linux
date: "2010-02-26T08:56:44+00:00"
guid: https://blog.wapnet.nl/?p=352
parent_post_id: null
post_id: "352"
title: Spamassisn Update
url: /2010/02/spamassisn-update/

---
Update Deamon

> sa-update -D

Restart Service

> service spamassassin restart

Check version

> perl -MMail::SpamAssassin -e 'print $Mail::SpamAssassin::VERSION;'
