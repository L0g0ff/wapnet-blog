---
author: thomasf
categories:
  - gaming
  - hardware
  - linux
date: "2025-02-28T22:25:25+00:00"
guid: https://blog.wapnet.nl/?p=2232
parent_post_id: null
post_id: "2232"
tags:
  - howto
  - linux
title: Creating a Shared Internet Connection for Gaming During Vacations
url: /2025/03/creating-a-shared-internet-connection-for-gaming-during-vacations/

---
## Why You Need This Quick WiFi Sharing Solution

When staying at holiday parks or vacation rentals, internet connectivity is often limited or unreliable. This can be frustrating when you want to enjoy some gaming time with your kids. The solution? Create your own WiFi sharing setup using two wireless interfaces – your laptop's built-in WiFi and a USB WiFi dongle.

## The Perfect Setup in 3 Simple Steps

Requirement: a working internet connection. In my case: LandalPremiumWifi

### Step 1: Create a Hotspot with Your Built-in WiFi

First, set up a hotspot using your laptop's built-in WiFi card. This creates a stable, local network for your gaming devices:

```
sudo nmcli device wifi hotspot con-name wapnet ssid wapnet band bg password 87654312
```

This command creates a hotspot named "wapnet" with the password "87654312" using the 2.4GHz band, which provides better range for your devices.

### Step 2: Connect the WiFi Dongle

Plug your USB WiFi dongle into your laptop. This second wireless interface will be used to connect to the holiday park's WiFi network.

### Step 3: Switch the Holiday Park's WiFi adapter

Use the WiFi dongle to connect to the holiday park's internet. Your now can use the dongle for internet access while your built-in WiFi card maintains the local hotspot for your gaming devices.

{{< figure src="/wp-content/uploads/2025/03/image.png" alt="" caption="" >}}

## Why This Method Works So Well

The key advantage of this approach is using your laptop's built-in network card (which typically has better performance) as your primary gaming network, while the USB dongle handles the potentially less reliable internet connection. This separation means:

- More stable local connections for gaming
- Better network control
- Reduced latency for local multiplayer games
- Single internet connection shared across all your devices

This setup is perfect for family gaming sessions during vacations when you need reliable connectivity without the hassle of connecting each device separately to potentially unstable holiday park WiFi.

And to remove the hotspot:

```
$ sudo nmcli connection delete wapnet
```

Happy gaming!
