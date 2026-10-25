---
_edit_last: "1"
_thumbnail_id: "1545"
author: thomasf
categories:
  - networking
cover:
  alt: network slow
  image: /wp-content/uploads/2014/05/network-slow.jpg
date: "2014-05-08T06:54:13+00:00"
dsq_thread_id: "5152918183"
guid: https://blog.wapnet.nl/?p=1539
parent_post_id: null
post_id: "1539"
title: Build your own speedtest with iperf
url: /2014/05/build-your-own-speedtest-with-iperf/

---
When you have network performance issue's you often use speed test websites to check the network bandwidth. But mostly of the time you want to monitor the network bandwidth between two specific servers. There is a cross platform speed test utility you can use to monitor the bandwidth. The name of the tool is **iperf**

How it works:

- Download the tool: [http://iperf.fr/](http://iperf.fr/)
- Extract the tool in a folder and jump to the folder with the command line
- start the tool on the server with this command: **iperf -s**

[![iperf server](/wp-content/uploads/2014/05/iperf-server.png)](/wp-content/uploads/2014/05/iperf-server.png)

- Start the tool on the remote client **iperf -c IPSERVER -r**
- The tool first try an upload from the client and then a download from the client

[![iperf client](/wp-content/uploads/2014/05/iperf-client.png)](/wp-content/uploads/2014/05/iperf-client.png)

If you have any connection problems with iperf try temporary turn of you firewall on both server and client. You can also play with different window sizes with the **iperf -c IPSERVER -r -w 40000**

For a lot of tips and tricks (even a graphical interface called jperf) check: [http://openmaniak.com/iperf.php](http://openmaniak.com/iperf.php)

Happy troubleshooting :D
