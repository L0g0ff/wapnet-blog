---
_thumbnail_id: "2103"
author: thomasf
categories:
  - android
cover:
  alt: empty-battery
  image: /wp-content/uploads/2023/02/empty-battery.jpg
date: "2023-02-22T09:55:30+00:00"
guid: https://blog.wapnet.nl/?p=2099
parent_post_id: null
post_id: "2099"
title: Debug and Fix Android battery drain (system_server)
url: /2023/02/debug-and-fix-android-battery-drain-system_server/

---
I previously write an article about a logd battery drain: [/2021/11/android-logd-battery-drain/](/2021/11/android-logd-battery-drain/)

But you can also have an system\_server battery drain. With some easy debug steps you can find the root cause of this drain.

- First install ADB
- Put your phone in development mode
- Start "adb shell"
- Start "top"

If you have an high system\_server CPU than check the PID.

Note: In my screenshot it is already fixed. But this was 30~35% CPU

{{< figure src="/wp-content/uploads/2023/02/image-1.png" alt="" caption="" >}}

In my case the PID is 1756. So now we can check logcat to find out what the reason is of the high CPU.

logcat \| grep 1756

{{< figure src="/wp-content/uploads/2023/02/image-2.png" alt="" caption="" >}}

In this example you see signal is eating some CPU

{{< figure src="/wp-content/uploads/2023/02/image-3.png" alt="" caption="" >}}

With this information you can remove all the apps that is eating your CPU. In my case these apps drained my battery:

- Spotify
- Teams
- MS Drive
- Oneplus Weather

Happy debugging :)
