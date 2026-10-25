---
author: thomasf
categories:
  - uncategorized
date: "2008-02-18T22:41:08+00:00"
guid: https://blog.wapnet.nl/?p=17
parent_post_id: null
post_id: "17"
title: MCSA 2003 70-292 Tips & Trics
url: /2008/02/mcsa-2003-70-292-tips-trics/

---
Tips & Weetjes MCSA 2003:

1\. De PDC emulator (FSMO role) is verantwoordelijk voor de tijd sync. De handig weetje is dat je met het w32tm /config /syncfromflags:manual /manualpeerlist time\_source de tijd kan syncen.
2\. Voor de meest optimale werking van een Windows machine moet er minstends 5% vrije RAM zijn. Voor 512 mb komt dat dus op minstends 25.6.
3\. Perfmon: Memory - Pages/Sec mag niet hoger zijn dan 5 anders is het een memory probleem
4\. Perfmon: Logical Disk - Avg Disk Queue Length mag niet hoger zijn dan het aantal 2 + het aantal spindles in het systeem. Voor 1 schijf is dat dus 1 (schijf) + 2 (standaard) = 3 (max)
5\. Private houdt in beveiligde verbinding in
6\. WPAD = Web Proxy Auto Detect
7\. 80/20 Rule voor een 192.168.1.0/24 segment houdt in:
DHCP-A (80%)
192.168.1.10 192.168.1.254 Range
192.168.1.10 192.168.1.205 Excluded adresses

DHCP-B (20%)
192.168.1.10 192.168.1.254 Range
192.168.1.206 192.168.1.254 Exclude adresses
8\. Gereserveerde DHCP netwerk adressen zijn altijd met kleine letters en zonder tussenvoegsels
9\. System monitor:

Hardware Status Explenation Accepting Valeus
Memory : Pages/Sec pages between disk and ram 30 low
Memory: Page Faults/Sec OS not found page in RAM 40 old pc´s 150 new pc´s
Disk: Time
Disk Avg Disk Queue Length mag niet hoger zijn dan het aantal 2 + het aantal spindles in het              systeem
Processor: Time greater than 85 not always a problem
Processor Queue Length greater than 2 \* cpu´s = too much
