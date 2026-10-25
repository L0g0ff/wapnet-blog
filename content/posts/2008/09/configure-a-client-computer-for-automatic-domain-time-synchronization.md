---
_edit_last: "1"
author: thomasf
categories:
  - windows
date: "2008-09-22T11:40:58+00:00"
dsq_thread_id: "5272165564"
guid: https://blog.wapnet.nl/?p=44
parent_post_id: null
post_id: "44"
title: Configure a client computer for automatic domain time synchronization
url: /2008/09/configure-a-client-computer-for-automatic-domain-time-synchronization/

---
Some computers that are joined to a domain are configured to synchronize from a manual time source. Use the following procedure to configure a client computer that is currently synchronizing with a manually specified computer, to automatically synchronize time with the domain hierarchy.

![note](http://i.technet.microsoft.com/cc758905.note.gif)NoteFor more information about the **w32tm** command, type **w32tm /?** at a command prompt or see [Windows Time Service Tools and Settings](http://go.microsoft.com/fwlink/?LinkId=42984) on the Microsoft Web site (http://go.microsoft.com/fwlink/?LinkId=42984).

**Administrative Credentials**

To perform this procedure, you must be a member of the Administrators group on the local computer. To perform this procedure from a remote computer, you must be a member of the Domain Admins group.

**To configure a client computer for automatic domain time synchronization**

1. Open a Command Prompt.
1. Type the following command and then press ENTER: **w32tm /config /syncfromflags:domhier /update**
1. Type the following command and then press ENTER: **net stop w32time**
1. Type the following command and then press ENTER: **net start w32time**

**Administrative Credentials**

To perform this procedure locally on the PDC emulator, you must be a member of the Administrators group. To perform this procedure from a remote computer, you must be a member of the Domain Admins group.

**To configure the Windows Time service on the PDC emulator**

1. Open a Command Prompt.
1. Type the following command to display the time difference between the local computer and a target computer, and then press ENTER:

**w32tm /stripchart /computer:** _target_ **/samples:** _n_ **/dataonly** Value Definition_target_Specifies the DNS name or IP address of the NTP server that you are comparing the local computer's time against, such as time.windows.com._n_Specifies the number of time samples that will be returned from the target computer to test basic NTP communication.
1. Open UDP port 123 for outgoing traffic if needed.
1. Open UDP port 123 (or a different port you have selected) for incoming NTP traffic.
1. Type the following command to configure the PDC emulator and then press ENTER:

**w32tm /config /manualpeerlist:** _peers_ **/syncfromflags:manual /reliable:yes /update**

where _peers_ specifies the list of DNS names and/or IP addresses of the NTP time source that the PDC emulator synchronizes from. For example, you can specify time.windows.com. When specifying multiple peers, use a space as the delimiter and enclose them in quotation marks.
1. **w32tm /config /manualpeerlist:** _time.windows.com_ **/syncfromflags:manual /reliable:yes /update**
