---
_thumbnail_id: "2119"
author: thomasf
categories:
  - networking
  - windows
cover:
  alt: OpenSSH_logo
  image: /wp-content/uploads/2023/04/OpenSSH_logo.png
date: "2023-04-03T08:17:48+00:00"
guid: https://blog.wapnet.nl/?p=2110
parent_post_id: null
post_id: "2110"
title: 'NTP Error: the computer did not resync because no time data was available'
url: /2023/04/ntp-error-the-computer-did-not-resync-because-no-time-data-was-available/

---
When it comes to configuring your Primary Domain Controller (PDC) or local Network Time Protocol (NTP), you'll find a a lot of information online.

But in a nutshell this is what you have to do:

```
w32tm /config /manualpeerlist:"<IPTIMESERVER>,0x1" /syncfromflags:manual /reliable:yes /update
net stop w32time
net start w32time
w32tm /resync /rediscover
```

But if the timeserver isn't reliable you get the error:

{{< figure src="/wp-content/uploads/2023/04/image.png" alt="" caption="" >}}

The fix is really easy. Remove the `/reliable:yes` option

```
w32tm /config /manualpeerlist:"<IPTIMESERVER>,0x1" /syncfromflags:manual /update
```

And then after the `w32tm /resync /rediscover`:

{{< figure src="/wp-content/uploads/2023/04/image-1.png" alt="" caption="" >}}

Off course you only want to remove the `/reliable:yes` in a lab environment. Otherwise change the NTP server to a reliable one.
