---
author: thomasf
categories:
  - uncategorized
date: "2021-11-13T16:24:54+00:00"
guid: https://blog.wapnet.nl/?p=1987
parent_post_id: null
post_id: "1987"
title: Android LOGD battery drain
url: /2021/11/android-logd-battery-drain/

---
Pfff I've had a battery drain for weeks on my Oneplus device (you know that your phone battery drains faster than you would expect). But that drain was not visible in the android battery overview.

I had already installed an app (betterbattrystats) that give you more information about the drain. With betterbatterystats I found out that logd could be the issue, but logd is a log service so it should not be a root cause.

So I found out that you could just start a task manager (top) from the Android debug tools. What seems; the youtube music app was draining my battery. Even though I don't even use it. You can't delete that app either so I forced stopped it and now everything is quiet.

Really wtf; I am a tech guy and have to put in so much effort to figure this out. How many people don't have the same issues but just accept it?

# How can you fix this?

- First install ADB
- Put your phone in development mode
- Start top

```
adb shell top -m 20 -d 2
```

{{< figure src="/wp-content/uploads/2021/11/image.png" alt="" caption="" >}}

Here you can see the **logd** and the **com.google.and+**

To figure out what PID **9036** is

```
adb shell ps | grep 9036
```

{{< figure src="/wp-content/uploads/2021/11/image-1.png" alt="" caption="" >}}

And voila; the root cause.... Youtube music

So I turned off the Youtube app and now everything looks nice!

{{< figure src="/wp-content/uploads/2021/11/image-2.png" alt="" caption="" >}}

Please google don't hide you shitty services from the android battery overview!

Happy debugging!
