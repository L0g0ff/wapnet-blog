---
author: thomasf
categories:
  - linux
date: "2021-05-03T20:58:17+00:00"
guid: https://blog.wapnet.nl/?p=1904
parent_post_id: null
post_id: "1904"
title: Install Synology Drive Client on Solus Linux
url: /2021/05/install-synology-drive-client-on-solus-linux/

---
The current 3rth party repo is deprecated so I've created my own fork for version: 2.0.4-11112

```
sudo eopkg bi --ignore-safety https://raw.githubusercontent.com/L0g0ff/3rd-party/master/network/download/synology-drive-client/pspec.xml
sudo eopkg it synology-drive-client*.eopkg;sudo rm synology-drive-client*.eopkg

```

Have fun!
