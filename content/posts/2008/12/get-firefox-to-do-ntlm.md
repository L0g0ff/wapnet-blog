---
_edit_last: "1"
author: thomasf
categories:
  - uncategorized
date: "2008-12-23T14:10:23+00:00"
guid: https://blog.wapnet.nl/?p=162
parent_post_id: null
post_id: "162"
title: Get Firefox to do NTLM
url: /2008/12/get-firefox-to-do-ntlm/

---
Being a dedicated Firefox user, one of the few things that was still thwarting me was SharePoint.  We use SharePoint internally for a ton of stuff, and it was a drag to have to fall back to that other browser.  SharePoint pages look and work fine in Firefox, but I was having to reauthenticate on every single page, which really hindered my enjoyment of the experience.

I finally figured out how to get Firefox to do NTLM, which means I don’t have to deal with the authentication dialogs, thereby reducing my dependence on IE to one and only one application (Oddpost).

It’s not at all obvious how to make it work, and it took me a few tries.  You have to go to your Firefox address bar and type about:config.  This will bring up the internal config editor, which allows you to set all kinds of properties that influence Firefox’s behavior.  Look for the key called network.automatic-ntlm-auth.trusted-uris.  Set that key’s value to a comma separated list of servers you want NTLM auth for.  So if your internal SharePoint sites are on servers called Larry and Mo, use “larry,mo”.  You can also add the same value to the key network.negotiate-auth.trusted-uris.  It’s unclear to me if that second one is required, but I set it, and everything works.  Now SharePoint works like a champ, and authenticates automatically.

Source: [http://www.testingreflections.com/node/view/1365](http://www.testingreflections.com/node/view/1365)
