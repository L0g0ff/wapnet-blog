---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - cisco
  - networking
date: "2012-03-15T15:00:06+00:00"
dsq_thread_id: "5206707149"
guid: https://blog.wapnet.nl/?p=814
parent_post_id: null
post_id: "814"
title: Cisco router change access list (ACL)
url: /2012/03/cisco-router-change-access-list-acl/

---
- First check accesslist with **show run**
- Then check the dialer

> !
> interface Dialer1
> description Internet
> ip address negotiated
> **ip access-group 111 in**
> ip nat outside
> ip inspect list1 out
> ip virtual-reassembly

- Copy the access group line (bold) to notepad
- Now do a show run and copy the specific (111 in my case)  accesslist to notepad

> access-list 111 permit tcp any any established
> access-list 111 permit icmp any any administratively-prohibited
> access-list 111 permit icmp any any echo
> access-list 111 permit icmp any any echo-reply
> access-list 111 permit icmp any any packet-too-big
> access-list 111 permit icmp any any time-exceeded
> access-list 111 permit icmp any any traceroute
> access-list 111 permit icmp any any unreachable
> access-list 111 permit tcp any any eq ftp
> access-list 111 permit tcp any any eq www
> access-list 111 deny   ip any any log

- Now change the ACL with the new line (bold) still in notepad

> access-list 111 permit tcp any any established
> access-list 111 permit icmp any any administratively-prohibited
> access-list 111 permit icmp any any echo
> access-list 111 permit icmp any any echo-reply
> access-list 111 permit icmp any any packet-too-big
> access-list 111 permit icmp any any time-exceeded
> access-list 111 permit icmp any any traceroute
> access-list 111 permit icmp any any unreachable
> access-list 111 permit tcp any any eq ftp
> access-list 111 permit tcp any any eq www
> **access-list 111 permit tcp any any eq 443**
> access-list 111 deny   ip any any log

- now type **conf t**
- and type **interface dialer1**
- now temporary disable the accesslist with: **no ip access-group 111 in**
- type **exit** to exit the Dialer1 interface
- type **no access-list 111** to clear the current ACL
- Past the new modified ACL fro notepad to your router
- Type **interface dialer1**
- Type **ip access-group 111 in** to enable new new access lists
- Type **exit**
- Test the new rule
- Type **wr mem** to write the config from RAM to ROM
