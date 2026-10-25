---
_thumbnail_id: "1984"
author: thomasf
categories:
  - networking
  - programmeren
  - windows
cover:
  alt: wyse
  image: /wp-content/uploads/2021/11/wyse.png
date: "2021-11-11T21:33:37+00:00"
guid: https://blog.wapnet.nl/?p=1977
parent_post_id: null
post_id: "1977"
title: DHCP Test Tool
url: /2021/11/dhcp-test-tool/

---
I had to check my DHCP configuration for a Dell Wyse Thin Client. But when you configure specific options like 161 and 162 you don't see that options in a Wireshark capture during a Windows DHCP request.

Luckily for us CyberShadow created a great tool to test some specific DHCP settings an he even make it open source: [https://github.com/CyberShadow/dhcptest](https://github.com/CyberShadow/dhcptest)

This DHCP tool have 2 great features:

1. You can do a request for specific DHCP option
1. You can send a vendor class so in my case I can pretend to be a Wyse Thin client.

# DHCP Request Option

This will only work when you have configured Global DHCP settings.

```
dhcptest.exe --query --request 161
```

{{< figure src="/wp-content/uploads/2021/11/afbeelding-8.png" alt="" caption="" >}}

# DHCP Vendor Class

First I had to figure what the vendor class was. I checked this on the DHCP server:

{{< figure src="/wp-content/uploads/2021/11/afbeelding-9.png" alt="" caption="" >}}

Or on a Thin client itself:

{{< figure src="/wp-content/uploads/2021/11/afbeelding-10.png" alt="" caption="" >}}

Then run this command:

```
dhcptest.exe --query --option "60=wyse-1000"
```

And you will get Vendor Specific Information in Hex.

{{< figure src="/wp-content/uploads/2021/11/afbeelding-11.png" alt="" caption="" >}}

You can do different things to translate the Hex into readable data.

1. Compile the open source yourself yourself and create a output in a string
1. Use a (online) hex convertor
1. Open wireshark during the capture. Wireshark will translate this for you :)

# Compile the tool

- Download the git repo

```
git clone https://github.com/CyberShadow/dhcptest.git
```

- Edit the file (add these 2 lines)

{{< figure src="/wp-content/uploads/2021/11/afbeelding-12.png" alt="" caption="" >}}

```
161 : DHCPOptionSpec("File Server", OptionFormat.str),
162 : DHCPOptionSpec("Root Path to the File Server", OptionFormat.str),
```

- Download DMD for Windows: [https://dlang.org/download.html](https://dlang.org/download.html)
- Install the DMD compiler
- Compile the dhcptest tool

```
dmd dhcptest.d
```

This will create a exe for you and will translate the Hex to readable format.

Happy sniffing!
