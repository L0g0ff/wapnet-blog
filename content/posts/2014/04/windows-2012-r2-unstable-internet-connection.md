---
_edit_last: "1"
_wp_old_slug: windows-2012-r2-unstable-downloads
author: thomasf
categories:
  - cisco
  - networking
  - windows
date: "2014-04-24T12:30:43+00:00"
dsq_thread_id: "5136530692"
guid: https://blog.wapnet.nl/?p=1532
parent_post_id: null
post_id: "1532"
title: Windows 2012 R2 unstable internet connection
url: /2014/04/windows-2012-r2-unstable-internet-connection/

---
I had 2x HP DL 380 G6 servers with Windows 2012 R2 whit the same problem. When I start a download (I try a lot of different sites) the download drops and fluctuate. When I connect my laptop or another server on the same cable the download is stable. So my conclusion was the onboard nic.

What I tried:

- Update latest HP SSP (2014\_2)
- Update firmware NIC
- Update driver NIC
- Update Windows (patches)
- change all the default nic settings like disable tcp offload for example
- Try another switch

Bandwidth during download:

[![hp ethernet](/wp-content/uploads/2014/04/hp-ethernet.jpg)](/wp-content/uploads/2014/04/hp-ethernet.jpg)

I thought the problem must be the NIC so I added an intel pro to my server with the same result :(

Then I found the command **netsh interface tcp show global**

Output:

```
C:\Windows\system32>netsh interface tcp show global
Querying active state...

TCP Global Parameters
----------------------------------------------
Receive-Side Scaling State          : enabled
Chimney Offload State               : disabled
NetDMA State                        : disabled
Direct Cache Access (DCA)           : disabled
Receive Window Auto-Tuning Level    : enabled
Add-On Congestion Control Provider  : none
ECN Capability                      : enabled
RFC 1323 Timestamps                 : disabled
Initial RTO                         : 3000
Receive Segment Coalescing State    : enabled
Non Sack Rtt Resiliency             : disabled
Max SYN Retransmissions             : 2

```

I dived in to these settings and I found the "Receive Window Auto-Tuning Level on enabled". So I disabled the setting with:

**netsh int tcp set global autotuninglevel=disabled**

After that setting the network connection to the internet was stable :)

[![fixed](/wp-content/uploads/2014/04/fixed.png)](/wp-content/uploads/2014/04/fixed.png)

I found an article on the net that Cisco PIX IOS 8.0 doesn't support "TCP Window Scaling". Source: [http://www.cisco.com/c/en/us/support/docs/security/ios-firewall/71613-iosfw-tcp-scaling-ts.html](http://www.cisco.com/c/en/us/support/docs/security/ios-firewall/71613-iosfw-tcp-scaling-ts.html)

So I use the workaround to disable the Automatic Windows Scaling in Windows because I can't update our old PIX.

Problem solved :D
