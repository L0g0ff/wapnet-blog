---
_edit_last: "1"
author: thomasf
categories:
  - exchange
date: "2008-10-27T08:25:10+00:00"
guid: https://blog.wapnet.nl/?p=130
parent_post_id: null
post_id: "130"
title: Exchange 2007 Spam solution
url: /2008/10/exchange-2007-spam-solution/

---
To enable anti-spam functionality on a Hub Transport server

1. Run the following command:

[![](http://i.technet.microsoft.com/Global/Images/clear.gif) Copy Code](javascript:CopyCode('ctl00_rs1_mainContentContainer_ctl20other');)

```
./install-AntispamAgents.ps1
```

1. After the script has run, restart the Microsoft Exchange Transport service by running the following command:

[![](http://i.technet.microsoft.com/Global/Images/clear.gif) Copy Code](javascript:CopyCode('ctl00_rs1_mainContentContainer_ctl21other');)

```
Restart-Service MSExchangeTransport
```

1. Run the following command:

   ```
   ./install-AntispamAgents.ps1
   ```

1. After the script has run, restart the Microsoft Exchange Transport service by running the following command:

   ```
   Restart-Service MSExchangeTransport
   ```
