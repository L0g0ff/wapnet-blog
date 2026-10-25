---
_edit_last: "1"
author: thomasf
categories:
  - networking
date: "2008-10-13T14:09:59+00:00"
dsq_thread_id: "5354658864"
guid: https://blog.wapnet.nl/?p=116
parent_post_id: null
post_id: "116"
title: What Ports do I need to open on my Firewall?
url: /2008/10/what-ports-do-i-need-to-open-on-my-firewall/

---
August 20, 2008 by [Curtis Johnstone](http://ocsbuzz.wordpress.com/author/ocsbuzz/ "Posts by Curtis Johnstone")

The first question often asked when exposing OCS functionality to the Internet is “what ports do I need to open on my firewall?”.

The answer depends on which Edge functionality (and the associated Role), being exposed to the Internet.Below is a concise recap of the default Ports that need to be opened to expose specific OCS functionality to remote users (on the Internet).

**Edge Role**

**Functionality**

**External F/W Port**

**Internal F/W Port**

**Protocol**

Reverse Proxy

Address Book, File Download, etc…

443

443

HTTP(S)

Access

Remote IM and Presence, Federation, Public IM

443, 5061

5061

SIP/MTLS

Web Conferencing

External Web Conf Participation

443

8057

PSOM/MTLS

Audio/Video Conferencing

External A/V Conf Participation

443, 3478, 50,000-59,999

443, 5062, 3478

STUN

Chapter 2.3 of the [Office Communications Server 2007 Document: Edge Server Deployment Guide](http://www.microsoft.com/downloads/details.aspx?familyid=ED45B74E-00C4-40D2-ABEE-216CE50F5AD2&displaylang=en) provides more detail, including the associated Firewall policies.
