---
_edit_last: "1"
_thumbnail_id: "1588"
author: thomasf
categories:
  - windows
cover:
  alt: why
  image: /wp-content/uploads/2015/02/why.png
date: "2015-02-03T22:27:27+00:00"
dsq_thread_id: "5296629129"
guid: https://blog.wapnet.nl/?p=1586
parent_post_id: null
post_id: "1586"
title: Why Virtual Box won't give me option to create 64 bits guests?
url: /2015/02/why-virtual-box-wont-give-me-option-to-create-64-bits-guests/

---
Try to turn hyper-v off

> bcdedit /set hypervisorlaunchtype off

and a reboot. To turn it back on:

> bcdedit /set hypervisorlaunchtype on

and reboot.
