---
author: thomasf
categories:
  - exchange
date: "2008-02-14T15:24:36+00:00"
dsq_thread_id: "5357500402"
guid: https://blog.wapnet.nl/?p=16
parent_post_id: null
post_id: "16"
tags:
  - "2003"
  - disaster
  - eseutil
  - exchange
  - fix
  - recovery
title: Exchange 2003 Disaster recovery
url: /2008/02/exchange-2003-disaster-recovery/

---
With a good backup in hand and Exchange databases and logfiles on different hard drives, it is no problem to recover from an Exchange disaster.Just restore the data from backup and initiate a roll forward of the transaction logs. Well done, the Exchange information store goes online.

But what should you do when your backup isn't readable or you don't have a backup? Here's how these tools come to play.

**Before you start:**

- Make sure that the databases are really not startable
- Check the Application log for Exchange events that can tell you the cause of the failure
- Make a backup of the database
- Restart the server so that a soft recovery can be done

**ESEUTIL /P parameters**

ESEUTIL /p repairs a corrupted or damaged database. Ensure that you have a minimum of 20% free disc capacity in association to the Exchange database size.

> [![](http://www.msexchange.org/img/upl/image0201109064642009.jpg)](http://www.msexchange.org/img/upl/image0201109064642009.jpg)**Figure 9:** ESEUTIL repair modus

 **Example:**

> ESEUTIL /P „c:\\program files\\exchsrvr\\mdbdata\\priv1.edb“ /Se:\\exchsrvr\\mdbdata\\priv1.stm /Te:\\tempdb.edb

This command will repair the database PRIV1.EDB. If you have no .STM file, you can create one with ESEUTIL /CREATESTM. Read more about this [here](http://support.microsoft.com/default.aspx?scid=kb;en-us;555146).

After running ESEUTIL, you can open a detailled logfile called >database<.integ.raw to see the results.

As a last Step run ISINTEG –fix -test alltests. You can read more about ISINTEG later in this article.

**Note:** Sometimes you must run the fix over and over again till it fix all problems. Its like a defrag of a harddrive

Source: [http://www.msexchange.org/tutorials/Exchange-ISINTEG-ESEUTIL.html](http://www.msexchange.org/tutorials/Exchange-ISINTEG-ESEUTIL.html)
