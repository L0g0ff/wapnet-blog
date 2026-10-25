---
_thumbnail_id: "1999"
author: thomasf
categories:
  - git
  - networking
  - windows
cover:
  alt: 2021-12-01 12_04_15-file transfer at DuckDuckGo
  image: /wp-content/uploads/2021/12/2021-12-01-12_04_15-file-transfer-at-DuckDuckGo.png
date: "2021-12-01T11:05:50+00:00"
guid: https://blog.wapnet.nl/?p=1996
parent_post_id: null
post_id: "1996"
title: Git SFTP
url: /2021/12/git-sftp/

---
I was working for an elementary website of a friend of [mine](https://www.fl-hair.nl). I pushed the website to GitHub so it's was way easier to maintain the site.

But I thought it must be easier than transferring all the changes every time by an FTP program. So I found [git-ftp](https://github.com/git-ftp/git-ftp) and of course FTPS didn't work out of the box ;)

## Windows

What you have to do to enable GIT FTP (on Windows)

First start an ssh sessions from powershell

```
ssh username@SOMEHOSTNAME
```

This will add the public key to you known host. Otherwise you will get this error later

```
fatal:  Can't access remote 'sftp://SOMEUSER:***@SOMEHOSTNAME'. Network down? Wrong URL? exiting...
```

You can see this with the -vv parameter

```
git ftp init -vv
```

{{< figure src="/wp-content/uploads/2021/12/afbeelding.png" alt="" caption="" >}}

Now it's time to install git-ftp

- First go to **c:\\program files\\git**
- Then run git-bash as administrator

{{< figure src="/wp-content/uploads/2021/12/afbeelding-1.png" alt="" caption="" >}}

And install git-ftp (bin is an alias for program files)

```
$ curl https://raw.githubusercontent.com/git-ftp/git-ftp/master/git-ftp > /bin/git-ftp
$ chmod 755 /bin/git-ftp
```

No go to your project and enter these commands

```
git config git-ftp.user SOMEUSERNAME
git config git-ftp.url sftp://SOMEHOSTNAME/public/sites/SOMEWEBSITE/
git config git-ftp.password SOMEPASSWORD
git ftp init
```

And the next time you make a change you only have to do

```
git ftp push
```

## Linux (Debian)

For linux the steps are much easier.

First start an ssh sessions from bash

```
ssh username@SOMEHOSTNAME
```

This will add the public key to you known host. Otherwise you will a error later.

Now install ftp-git

```
$ sudo apt install git-ftp
```

No go to your project and enter these commands

```
git config git-ftp.user SOMEUSERNAME
git config git-ftp.url sftp://SOMEHOSTNAME/public/sites/SOMEWEBSITE/
git config git-ftp.password SOMEPASSWORD
git ftp init
```

And the next time you make a change you only have to do

```
git ftp push
```

When you get an errors like these:

```
zo 19 dec 2021 23:11:50 CET: Retrieving last commit from sftp://******:***@s*******/public/sites/*********/.
*   Trying *********:22...
* Connected to ******* (********) port 22 (#0)
* Found host ******** in /home/******/.ssh/known_hosts
* Set "ecdsa-sha2-nistp256" as SSH hostkey type
* Closing connection 0
curl: (79) Error in the SSH layer

zo 19 dec 2021 23:11:50 CET: fatal: Could not get last commit. Use 'git ftp init' for the initial push. Can't access remote 'sftp://******:***@********'. Network down? Wrong URL? exiting..
```

Then try the `--insecure` parameter

```
git ftp push -vv --insecure
```

Happy uploading :)
