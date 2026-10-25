---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - vmware
date: "2012-04-24T15:49:23+00:00"
dsq_thread_id: "5140473647"
guid: https://blog.wapnet.nl/?p=859
parent_post_id: null
post_id: "859"
title: virtual ethernet card network adapter 1 is not supported
url: /2012/04/virtual-ethernet-card-network-adapter-1-is-not-supported/

---
I had the "error virtual ethernet card network adapter 1 is not supported" on a 64 bit Linux (ubuntu) virtual machine.

To fix this problem I shutdown the virtual machine, removed the NIC and add a new E1000 network card. Then I boot the server even everything was fine :)

[![](/wp-content/uploads/2012/04/vmware.png)](/wp-content/uploads/2012/04/vmware.png)
