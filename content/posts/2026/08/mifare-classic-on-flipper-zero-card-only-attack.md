---
author: thomasf
categories:
  - linux
date: "2026-08-21T20:37:59+00:00"
guid: https://blog.wapnet.nl/?p=2306
parent_post_id: null
post_id: "2306"
title: 'MIFARE Classic on Flipper Zero: Card-Only Attack'
url: /2026/08/mifare-classic-on-flipper-zero-card-only-attack/

cover:
  image: /images/covers/mifare-classic-on-flipper-zero-card-only-attack.jpg
  alt: Handheld gadget reading an RFID access card with keys coming from a laptop
---
_For educational and research purposes only - only test systems you own or have explicit permission to test._

**The Goal**

I want to clone a MIFARE Classic 1K card with my Flipper Zero. 24 of 32 keys unknown, no reader access. Card-only attack because I don't want to go to the card reader to test ;-)

{{< figure src="/wp-content/uploads/2026/08/image-1.png" alt="" caption="" >}}


**The Rabbit Hole**

The tooling landscape is a graveyard:  
\- **FlipperNested** \- EOL since 2023  
\- **HardnestedRecovery** (PC) - silently skips every log line containing `dist`, which current firmware writes on _all of them_  
\- **FlipperNestedRecovery** (PC) - old log format, crashes on heap corruption  
\- **MFKey FAP** (on-device) - works, but slow and memory-hungry


Since most custom flipper firmwares integrated nested attacks into the NFC app, there's simply **no working PC tool for the new log format**. The community went on-device and never ported back. But the flipper device is slow when you need a CPU find all the potential keys.

**The Missing Piece**

[mfkey\_desktop\_cli](https://github.com/phntm-lab/mfkey_desktop_cli) \- multithreaded desktop recovery: pulls `.nested.log` from the Flipper, cracks on all CPU cores, uploads candidate dictionaries back. Laptop does the math and the power, Flipper does the radio to find out the correct keys.

{{< figure src="/wp-content/uploads/2026/08/image.png" alt="" caption="" >}}

**The Catch**

My card has **static encrypted nonces** \- every auth returns the same nonce. Instead of one key per sector: **957,039 candidates**. The Flipper then verifies them against the card at ~60 keys/sec. Full run takes days; trimmed to the sectors you need: about an hour.

**Three Takeaways**

1\. Check the nonces first: identical `nt0` = static card = candidate explosion  
2\. Reader access beats everything - one tap gives mfkey32-grade nonces and usually a single key  
3\. The desktop tooling gap is real - the solver cores are open source, someone just needs to connect them

But if you try and error hard enough you always win :)

Happy hacking!
