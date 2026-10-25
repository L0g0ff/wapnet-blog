---
_thumbnail_id: "2107"
author: thomasf
categories:
  - networking
  - windows
cover:
  alt: snort3
  image: /wp-content/uploads/2023/03/snort3.webp
date: "2023-03-31T13:20:00+00:00"
guid: https://blog.wapnet.nl/?p=2106
parent_post_id: null
post_id: "2106"
title: TCPDump alternative Windows
url: /2023/03/tcpdump-alternative-windows/

---
Are you in a situation where you need to capture and analyze network traffic, but don't have Wireshark or TCPDump at your disposal? Don't worry, there's still a solution. Enter **pktmon**.

While it may not be the most sophisticated tool out there, pktmon is a viable option for monitoring traffic in real-time. With its lightweight and efficient design, you can quickly capture and analyze packets without the need for any additional software installations.

So, how exactly does pktmon work? It uses the Windows Filtering Platform (WFP) to capture network traffic at the packet level. This allows you to examine specific details about each packet, such as its source and destination address, protocol, and payload.

But what makes pktmon really stand out is its ability to filter traffic based on specific criteria. For example, you can use it to only capture traffic from a specific IP address, port, or protocol. This makes it a powerful tool for troubleshooting network issues or identifying potential security threats.

While pktmon may not be the most robust traffic monitoring tool out there, it's certainly a valuable option to have in your arsenal and its already installed :) So the next time you find yourself in need of capturing and analyzing network traffic, give pktmon a try - you might just be surprised by what it can do.

```
#start the traffic capture
pktmon start -c
#stop the traffic capture
pktmon stop
#convert the file so you can view it in notepad
pktmon etl2txt <etl file>
```

More info: [https://learn.microsoft.com/en-us/windows-server/networking/technologies/pktmon/pktmon-syntax](https://learn.microsoft.com/en-us/windows-server/networking/technologies/pktmon/pktmon-syntax)

Happy sniffing :)
