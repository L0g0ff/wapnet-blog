---
_edit_last: "1"
author: thomasf
categories:
  - vmware
date: "2010-02-25T08:49:34+00:00"
dsq_thread_id: "5272066407"
guid: https://blog.wapnet.nl/?p=349
parent_post_id: null
post_id: "349"
title: Configure Jumbo Frames in esx 4 Vsphere
url: /2010/02/configure-jumbo-frames-in-esx-4-vsphere/

---
**Jumbo Frames !!!!!!**

-\> Lets understand what’s Jumbo Frames first and how it benefits us ...

- **Jumbo frames** are Ethernet frames with more than 1,500 bytes of payload (MTU). Conventionally, jumbo frames can carry up to 9,000 bytes of payload.

- Jumbo Frames allow ESX Server to send larger frames out onto the physical network. The network must support Jumbo Frames end‐to‐end for Jumbo Frames to be effective.

- iSCSI with jumbo frames gives better or rather much better performance .If you are getting sluggish performance then try enabling jumbo frames

So let’s activate it, I have used Jumbo frames only with SW initiator not HW one so if some can comment on how it works on HW it would be in for a great benefit.

Most probably you might have your VMkernel setup with 1500 MTU so we need to delete it and start over again. Its recommend to start from 0 but if you wish you can enable the jumbo frames on the fly, it won't throw any errors.

In my case vSwitch1 was used as VMkernel for iscsi.

**Step  1:**
\[root@esx sysconfig\]# _esxcfg-vswitch -d vSwitch1_ **Step 2:**

Then I went ahead and did a listing

\[root@esx sysconfig\]# _esxcfg-vswitch -l_
Switch Name    Num Ports   Used Ports  Configured Ports  MTU     Uplinks
vSwitch0       32          3           32                9000    vmnic0

PortGroup Name      VLAN ID  Used Ports  Uplinks
VM Network          0        0           vmnic0
Service Console     0        1           vmnic0

As it can be seen no VMkernel

Then lets start the stuff .........

**Step 3:**

Add a vSwitch

\[root@esx sysconfig\]#  _esxcfg-vswitch -a vSwitch1_ **Step 4:**

List it....
\[root@esx sysconfig\]#  _esxcfg-vswitch -l_
Switch Name    Num Ports   Used Ports  Configured Ports  MTU     Uplinks
vSwitch0       32          3           32                9000    vmnic0
PortGroup Name      VLAN ID  Used Ports  Uplinks
VM Network          0        0           vmnic0
Service Console     0        1           vmnic0
Switch Name    Num Ports   Used Ports  Configured Ports  MTU     Uplinks
vSwitch1       64          1           64                1500
PortGroup Name      VLAN ID  Used Ports  Uplinks

**Step 5:**
Lets set the jumbo frames AKA MTU

_If you wish you can execute the below command on the fly to your vSwitch without deleting it_\[root@esx sysconfig\]# **_esxcfg-vswitch -m 9000 vSwitch1_**
List it to see the diference
\[root@esx sysconfig\]#  _esxcfg-vswitch -l_
Switch Name    Num Ports   Used Ports  Configured Ports  MTU     Uplinks
vSwitch0       32          3           32                9000    vmnic0
PortGroup Name      VLAN ID  Used Ports  Uplinks
VM Network          0        0           vmnic0
Service Console     0        1           vmnic0
Switch Name    Num Ports   Used Ports  Configured Ports  MTU     Uplinks
vSwitch1       64          1           64                9000
PortGroup Name      VLAN ID  Used Ports  Uplinks
As it can be seen MTU is now 9000 not 1500

**Step 6 :**
Lets assign a NIC to the newly created vSwitch
\[root@esx sysconfig\]# _esxcfg-vswitch -L vmnic1 vSwitch1_
The result
\[root@esx sysconfig\]# _esxcfg-vswitch -_ l
Switch Name    Num Ports   Used Ports  Configured Ports  MTU     Uplinks
vSwitch0       32          3           32                9000    vmnic0
PortGroup Name      VLAN ID  Used Ports  Uplinks
VM Network          0        0           vmnic0
Service Console     0        1           vmnic0
Switch Name    Num Ports   Used Ports  Configured Ports  MTU     Uplinks
vSwitch1       64          2           64                9000    vmnic1
PortGroup Name      VLAN ID  Used Ports  Uplinks
**Step 7:**
Lets give it a port group
\[root@esx sysconfig\]#  _esxcfg-vswitch -A VMkernel vSwitch1_ **Step 8:**

Lets see Whether we got desired output
\[root@esx sysconfig\]#  _esxcfg-vswitch -l_
Switch Name    Num Ports   Used Ports  Configured Ports  MTU     Uplinks
vSwitch0       32          3           32                9000    vmnic0
PortGroup Name      VLAN ID  Used Ports  Uplinks
VM Network          0        0           vmnic0
Service Console     0        1           vmnic0
Switch Name    Num Ports   Used Ports  Configured Ports  MTU     Uplinks
vSwitch1       64          2           64                9000    vmnic1
PortGroup Name      VLAN ID  Used Ports  Uplinks
VMkernel            0        0           vmnic1
**Step 9:**

Now lets give it IP
\[root@esx sysconfig\]#  _esxcfg-vmknic -a -i 192.168.0.11 -n 255.255.255.0 -m 9000 VMkernel_
Hmm the output is ........
\[root@esx sysconfig\]#  _esxcfg-vswitch -l_
Switch Name    Num Ports   Used Ports  Configured Ports  MTU     Uplinks
vSwitch0       32          3           32                9000    vmnic0
PortGroup Name      VLAN ID  Used Ports  Uplinks
VM Network          0        0           vmnic0
Service Console     0        1           vmnic0
Switch Name    Num Ports   Used Ports  Configured Ports  MTU     Uplinks
vSwitch1       64          3           64                9000    vmnic1
PortGroup Name      VLAN ID  Used Ports  Uplinks
VMkernel            0        1           vmnic1
Property of vmknic
\[root@esx sysconfig\]#  _esxcfg-vmknic -l_
Interface  Port Group/DVPort   IP Family IP Address                              Netmask         Broadcast       MAC Address       MTU     TSO MSS   Enabled Type
vmk0       VMkernel            IPv4      192.168.0.11                            255.255.255.0   192.168.0.255   00:XX:83:91:23:14 9000    65535     true    STATIC

Source: [http://moizzy.blogspot.com/2010/02/configure-jumbo-frames-in-esx-4-for.html](http://moizzy.blogspot.com/2010/02/configure-jumbo-frames-in-esx-4-for.html)
