---
_thumbnail_id: "1970"
author: thomasf
categories:
  - networking
  - windows
cover:
  alt: remote-desktop-rdp-mstsc-icon
  image: /wp-content/uploads/2021/11/remote-desktop-rdp-mstsc-icon.png
date: "2021-11-04T21:57:29+00:00"
guid: https://blog.wapnet.nl/?p=1963
parent_post_id: null
post_id: "1963"
title: Slow initial RDP connection
url: /2021/11/slow-initial-rdp-connection/

---
For me, this was a pain in the ass for a long time. When I connect to a Windows server through RDP/RDS it sometimes takes more than 2 minutes to connect to a server. Today after some waiting, and waiting and some more waiting I did a deep dive with Wireshark to figure out why it was so slow.

# My setup

- Azure domain joined Windows 10 device (Laptop)
- Connection over a Cisco Anyconnect VPN
- Remote Desktop Manager (Devolutions)
- Native RDP client
- MremoteNG

# Remote VS local

I know for sure the issue should be in my setup. Because when I connect first to a jump host (RDP) and then connect to other domain-joined servers everything was connected almost immediately after I put in my user credentials.

# What to do (TL;DR)

There are four things you have to modify to speed up the initial remote desktop connection speed:

1. Disable SSL / TLS1.0
1. Disable Netbios on the VPN network adapter
1. Disable automatic proxy settings in Windows
1. Change the credential to domain.local\\admin or admin@domain.local instead of domain\\admin

# Disable SSL / TLS1.0

No, you don't have to negotiate what protocol you have to use to connect a server. Use TLS1.2 or I don't want to connect with you ;) So:

### How to

- Start > Run > Regedit
- Go to: `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols\TLS 1.0\Client`
- If the TLS 1.0 and Client folders doesn't exists create these keys
- Create a 32 DWORD value with the name `Enabled`
- Value data: `0` (Hex)
- Restart the client

{{< figure src="/wp-content/uploads/2021/11/afbeelding-1.png" alt="" caption="" >}}

# Disable Netbios on the VPN adapter

What I was seeing in my Wireshark capture is that RDP was trying to broadcast to get information over NETBIOS. You have a DNS server so you don't need a legacy broadcast protocol! Unfortunately, I don't have any screenshot of the capture but you can always check yourself ;-)

### How to

Change the VPN Adapter and reboot the computer:

{{< figure src="/wp-content/uploads/2021/11/afbeelding.png" alt="" caption="" >}}

# Disable the proxy

After connection to a server with RDP and you enter the credentials Windows is trying constantly to WPAD.domain.local to autoconfigure itself. WPAD stands for **Web Proxy Auto-Discovery** and I think you never want to autoconfigure a MITM ehh proxy device. You always want to have full control of your device. So, disable this to speed up the connection and make your device more secure.

{{< figure src="/wp-content/uploads/2021/11/afbeelding-3.png" alt="" caption="" >}}

### How to

- Go to settings
- Search for proxy
- Switch the Automatically detect settings to **Off**
- Restart Windows

{{< figure src="/wp-content/uploads/2021/11/afbeelding-2.png" alt="" caption="" >}}

# Change the login name

I found out that this is the most annoying and time consuming one. I always use DOMAIN\\User when I connect to a server. But this is what happens:

{{< figure src="/wp-content/uploads/2021/11/afbeelding-4.png" alt="" caption="" >}}

Kerberos is doing a DNS query on `_kerberos._tcp.dc._msdcs.domain.domain.tld` and of course he will never can find that double domain A record. But if you change the logon name to domain.tld\\admin or admin@domain.tld Kerberos will find the A record and connects immediately :)

{{< figure src="/wp-content/uploads/2021/11/afbeelding-5.png" alt="" caption="" >}}

# Kerberos

And even now it's possible to tune the Kerberos authentication further and fix the last `KRB5KDC_ERR_PREAUTH_REQUIRED` error you can see in the screenshot. Maybe next time but for now I'm happy with the initial connection speed :)

Happy hack ehh... connecting!
