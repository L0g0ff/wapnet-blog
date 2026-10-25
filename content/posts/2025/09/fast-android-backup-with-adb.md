---
author: thomasf
categories:
  - android
  - linux
  - windows
date: "2025-09-22T06:55:49+00:00"
guid: https://blog.wapnet.nl/?p=2261
parent_post_id: null
post_id: "2261"
tags:
  - linux
title: Fast Android backup with ADB
url: /2025/09/fast-android-backup-with-adb/

cover:
  image: /images/covers/fast-android-backup-with-adb.jpg
  alt: Phone connected over USB to a laptop streaming photos, music and apps into a backup box
---
Want to create a full backup of your Android phone without root access? ADB (Android Debug Bridge) is your best friend. This method works on all Android versions and gives you complete control over what gets backed up.

## What You'll Need

- Android phone with USB debugging enabled
- Computer with ADB installed
- USB cable

## Setup

**1\. Install ADB:**

```
# Ubuntu/Debian
sudo apt install android-tools-adb

# Windows: Download Android SDK Platform Tools
# macOS: brew install android-platform-tools
```

**2\. Enable USB Debugging:**

- Go to Settings → About phone
- Tap "Build number" 7 times to unlock Developer options
- Go to Developer options → Enable "USB debugging"

## Creating the Backup

**Full backup:**

```
# All apps + system data
adb backup -all -system -shared

# Files from storage
adb shell "cd /sdcard && tar -cf - ." > sdcard_backup.tar
```

**Selective backup:**

```
# Specific app only
adb backup com.whatsapp

# System settings only
adb backup -system
```

## What Gets Backed Up?

**Included:**

- App data and settings
- System configuration
- WiFi passwords
- SMS messages (depending on app)

**Not included:**

- Photos/videos (use `adb pull` for these)
- Apps that block backup
- DRM-protected content

## Restoring

```
adb restore backup.ab
```

## Pro Tips

1. **Encrypt your backup:** Use a password during the backup process
1. **Test your backup:** Try restoring on a test device first
1. **Combine methods:** ADB + cloud sync for complete coverage

ADB backup isn't perfect, but it's the most comprehensive method without root. For critical data, I always recommend combining multiple backup strategies.
