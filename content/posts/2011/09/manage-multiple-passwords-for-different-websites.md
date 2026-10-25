---
_edit_last: "1"
author: thomasf
categories:
  - android
  - firefox
  - linux
  - osx
  - windows
date: "2011-09-23T23:59:46+00:00"
guid: https://blog.wapnet.nl/?p=654
parent_post_id: null
post_id: "654"
tags:
  - keepass
  - lastpass
  - password
  - security
title: Manage multiple passwords for different websites
url: /2011/09/manage-multiple-passwords-for-different-websites/

---
One of the worst things you can do on the internet is use the same password for different websites. When one of the webites is hacked or there is an bad sysadmin they can use your password to login your email or other sites to steal all your private information and worst case scenario your bank account.

Every self respected browser has an built-in password safer but when your computer/laptop is stolen or hacked by a mad person (in dutch we call them klootzakken ;) ) they can easily steal all your passwords. So don't use the built-in password safer (or [configure](http://luxsci.com/blog/master-password-encryption-in-firefox-and-thunderbird.html) a strong master password).

There are two great solutions for managing your passwords. One is a local and one is a cloud solution. I will describe them both so you can choose what is best for you.

**KeePass (local):**
KeePass is a great tool for managing your passwords. There is an built-in password generator, the passwords saved in one local encrypted file and you must always give up a master key to access the passwords. The tool is crossplatform (using .net/mono) and there are a lot of plugins, example; there is a browser plugin to replace the insecure built-in pass safer. The great thing about this tool is that is is an local tool so only you can access and manage the password files. If you want to share the password file on multiple places you can use dropbox to synchronise/centralise the password files.

[![](/wp-content/uploads/2011/09/keepass.png)](/wp-content/uploads/2011/09/keepass.png)**LastPass (cloud):** LastPass is also a great tool for managing your password especialy when you use multiple computers and different operating systems. LastPass replaces the default integrated browser password safer with his own. Your password stored localy and in the cloud and are encrypted. Without the master password it is not possible to automatic login or see your password. I like LastPass because tons of options and integration with all the operating systems and smartphones. The default settings are good but I recommend that you change the setting that the LastPass is logoff automaticly when you close the browser.

The only thing you must keep in mind that you password is in sync at LastPass (cloud) so you must trust the company.

[![](/wp-content/uploads/2011/09/lastpass.jpg)](/wp-content/uploads/2011/09/lastpass.jpg)**Keep in mind**
That using multiple random words password (example: _"correct battery horse staple"_) mostly of the time is better then using complex passwords ( _"Tr0ub4dor&3"_). This picture tells why:

[![](/wp-content/uploads/2011/09/password_strength.png)](/wp-content/uploads/2011/09/password_strength.png)**Last but not least**
**Always** use a BIOS password on a laptop. Most of the thief's are very dumb people and if they stole you laptop they cannot remove the BIOS password and your laptop is useless for them.
