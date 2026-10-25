---
_thumbnail_id: "1974"
author: thomasf
categories:
  - networking
  - windows
cover:
  alt: 140px-Wireshark_icon.svg
  image: /wp-content/uploads/2021/11/140px-Wireshark_icon.svg_.png
date: "2021-11-05T11:23:12+00:00"
guid: https://blog.wapnet.nl/?p=1973
parent_post_id: null
post_id: "1973"
title: Windows network package capture without installing anything (on the server)
url: /2021/11/windows-network-package-capture-without-installing-anything-on-the-server/

---
I like Wireshark. But I don't like to install software on a server for troubleshooting purposes. Especially when you need software like PCAP to sniff some network data.

But what you can do is capture data data with netsh, copy the data to your workstation, convert the data so you can read it with wireshark and do you thing.

# Capture the data

Run this command to capture the data (elevated command prompt)

```
netsh trace start capture = yes ipv4.address = x.x.x.x
```

And stop the capture when you are done

```
netsh trace stop
```

Copy the files to you computer

# Convert the capture

Download the etl2pcapng converter from the MS Github repo: [https://github.com/microsoft/etl2pcapng](https://github.com/microsoft/etl2pcapng)

Convert the data

```
etl2pcapng.exe NetTrace.etl out.pcapng
```

You can open the out.pcapng file and do you thing.

{{< figure src="/wp-content/uploads/2021/11/afbeelding-6.png" alt="" caption="" >}}

Happy Troubleshooting!
