---
_thumbnail_id: "1518"
author: thomasf
categories:
  - linux
cover:
  alt: dialog-question
  image: /wp-content/uploads/2014/04/dialog-question.png
date: "2020-02-01T17:27:58+00:00"
guid: https://blog.wapnet.nl/?p=1831
parent_post_id: null
post_id: "1831"
title: How to keep processes running after ending ssh session
url: /2020/02/how-to-keep-processes-running-after-ending-ssh-session/

---
- ssh into the remote machine
- start tmux by typing tmux into the shell
- start the process you want inside the started tmux session
- leave/detach the tmux session by typing Ctrl+b and then d
