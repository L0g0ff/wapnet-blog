---
title: "Microsoft Teams on Android Without the Teams App"
date: 2026-10-27T12:00:00+01:00
url: /2026/10/microsoft-teams-on-android-without-the-teams-app/
author: Thomas Faddegon
categories:
  - android
  - mobile
tags:
  - howto
  - linux
cover:
  image: cover.jpg
  alt: A smartphone in a mustache-and-glasses disguise walks with a Linux penguin past a locked, guarded gate while showing a chat app
---
**The Goal**

I run /e/OS on my phone. No Google services, and I'd like to keep it that way. I still need Microsoft Teams for work chats, though. But I don't want the Teams app or Microsoft Authenticator on this phone.

On my Linux laptop, Teams in the browser works perfectly. So surely a browser on Android can do the same? Well... not out of the box.

**The Catch**

Teams on the web officially supports Linux desktop browsers, but [not mobile browsers](https://learn.microsoft.com/en-us/microsoftteams/teams-client-web). Open `teams.cloud.microsoft` on Android and you're sent to the app store.

My employer's tenant made it even more fun. Once I got past that, sign-in failed with error **530081**: *"You must use Microsoft Edge to access this resource."* That's a Conditional Access policy that only kicks in when you sign in from Android. From Linux the same account just works.

So the trick is simple: make the browser look like a Linux desktop. The hard part was finding a browser that does this reliably.

**What Didn't Work**

I tried a lot before I found something that works:

- **Native Alpha / WebSpace** (web app wrappers): these use the system WebView. On /e/OS that WebView is version 148 and comes with the ROM, so you can't update it separately. Teams loaded, but a fat *"Oops, app failed to init!"* overlay stayed on top.
- **IronFox** with Desktop site: worked by hand, but a home screen shortcut dropped back to mobile mode every time.
- **Brave**: Desktop site gets past the app redirect, but Brave on Android has no custom user agent setting, so I still hit the Edge error.

**The Winner: Cromite**

[Cromite](https://github.com/uazo/cromite) is a de-Googled Chromium fork (the successor of Bromite). It has its own up-to-date Chromium engine, so it doesn't depend on the system WebView. More importantly, it lets you set a **custom user agent** for both mobile and desktop mode.

**Step 1: Install Cromite**

Cromite has its own F-Droid repo, but that was unreachable for me. So I grabbed the APK from GitHub. Most current phones need the `arm64` version:

```
https://github.com/uazo/cromite/releases/latest/download/arm64_ChromePublic.apk
```

Grab `arm64_ChromePublic.apk`, **not** the `SystemWebView` APK. Cromite has a built-in updater; enable it on first start.

**Step 2: Pretend to Be Linux**

Go to **Settings → User Agent** and set the **mobile** user agent to a custom value:

```
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36
```

Keep the Chrome version close to Cromite's own version, so the user agent matches the engine underneath.

With just **Desktop site** turned on, Teams already worked. But you get the full desktop layout on a small screen. With the custom mobile user agent, Teams accepts the browser *and* still renders nicely for your screen size.

**Step 3: Open Teams**

```
https://teams.cloud.microsoft/
```

That's the new Teams URL. The old `teams.microsoft.com` still redirects to it. Sign in, and you're chatting. Add a home screen shortcut and it feels almost like an app.

**The Fine Print**

- No push notifications. Cromite deliberately has no Google Cloud Messaging, so you only see new messages when you open it.
- This works around a Conditional Access policy. Technically you just look like a Linux browser, which your tenant allows. But Microsoft or your admin can close that gap at any time, and your sign-ins show up in the logs as Linux. If you do this on a work account, check with your IT department first.
- Messaging works fine. I haven't tested calls and meetings.

**Three Takeaways**

1. "Unsupported browser" usually means "unsupported user agent". Teams works fine on mobile Chromium once it thinks it's on Linux.
2. On a de-Googled ROM, avoid anything that relies on the system WebView. Pick a browser with its own engine.
3. Read the error code. 530081 told me it was Conditional Access and not a broken browser, which saved a lot of guessing.

*Full disclosure: I figured this out together with my AI assistant. Fair to say we tried a few wrong turns before finding the right one.* 😉

Happy (app-free) chatting!
