---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
  - osx
date: "2011-12-07T20:59:42+00:00"
guid: https://blog.wapnet.nl/?p=764
parent_post_id: null
post_id: "764"
title: locate command for OSX
url: /2011/12/locate-command-for-osx/

---
Locate is a great unix/linux util that you can use for fast file searching.

enable locate (search command database) this takes 10 minutes the first ime. But it is a background process.

> sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.locate.plist

Updatedb (search db)

> sudo /usr/libexec/locate.updatedb

find a specific file

> locate file
