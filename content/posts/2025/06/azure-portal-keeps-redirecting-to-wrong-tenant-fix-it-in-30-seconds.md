---
author: thomasf
categories:
  - azure
date: "2025-06-16T07:12:33+00:00"
guid: https://blog.wapnet.nl/?p=2242
parent_post_id: null
post_id: "2242"
title: Azure Portal Keeps Redirecting to Wrong Tenant? Fix It in 30 Seconds
url: /2025/06/azure-portal-keeps-redirecting-to-wrong-tenant-fix-it-in-30-seconds/

---
## The Problem

Ever tried logging into your personal Azure account only to get redirected to your company tenant over and over again? Even after clearing cookies, trying incognito mode, and switching browsers, the redirect persists like a stubborn bug.

This happens because Azure remembers your email domain and automatically associates it with a business tenant—even when you have a personal account with the same domain. I recently ran into this exact issue when setting up a new Azure account, and after some experimenting, I found a bulletproof solution.

## The Solution (Works Every Time)

Copy these 4 URLs and open them **in this exact order** in the same browser tab:

```
1. https://account.microsoft.com/auth/complete-signout
1. https://login.microsoftonline.com/common/oauth2/v2.0/logout
1. https://login.live.com/logout.srf
1. https://portal.azure.com/?feature.settingsportalinstance=mpac
```

No need to close your browser, clear cache, or restart anything. Just click through these URLs sequentially.

## Why This Works

Each URL serves a specific purpose:

- **URL 1**: Signs you out of all Microsoft Account services
- **URL 2**: Clears your Azure AD session completely
- **URL 3**: Forces logout from Live services
- **URL 4**: Opens Azure Portal with the account selector forced

This approach works because you're clearing all possible session caches simultaneously and forcing Azure to present the account chooser instead of making assumptions about which tenant you want.

**Time saved: From hours of debugging to 30 seconds of clicking.** Sometimes the simplest solutions are the most effective.

Happy Logoff :P
