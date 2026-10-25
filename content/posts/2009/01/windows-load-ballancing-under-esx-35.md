---
_edit_last: "1"
author: thomasf
categories:
  - uncategorized
date: "2009-01-06T14:10:56+00:00"
guid: https://blog.wapnet.nl/?p=168
parent_post_id: null
post_id: "168"
title: Windows load Ballancing under ESX 3.5
url: /2009/01/windows-load-ballancing-under-esx-35/

---
Recently I have setup a NLB IIS site with 2 VM’s in a DRS/HA cluster.  Because of this using unicast mode was not an option (we need to be able to vMotion the virtual machines).  Multicast is also the way VMware recommends setting it up.  From VMware’s site:

> **Note:** VMware recommends configuring the cluster to use NLB multicast mode even though NLB unicast mode should function correctly if you complete these steps. This recommendation is based on the possibility that the settings described in these steps might affect VMotion operations on virtual machines. Also, unicast mode forces the physical switches on the LAN to broadcast all NLB cluster traffic to every machine on the LAN. If you plan to use NLB unicast mode, you must run all members of the NLB cluster on the same virtual switch.

The other problem with unicast mode is you have to disable RARP for either the virtual switch or the port group:

![](http://kb.vmware.com/Platform/Publishing/images/1556_1.png)

The other thing you need to do if using multicast mode, is add a static ARP entry in your switch for the MAC address of the NLB cluster, which is found under the cluster properties in NLB manager.  For a Cisco switch, from config mode:

> arp <ip of nlb cluster> <mac of nlb cluster> arpa

Source: [http://www.2putts4par.com/2008/01/31/windows-nlb-on-vmware-esx/](http://www.2putts4par.com/2008/01/31/windows-nlb-on-vmware-esx/)
