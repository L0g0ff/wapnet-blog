---
_edit_last: "1"
author: thomasf
categories:
  - security
date: "2015-02-08T15:45:16+00:00"
dsq_thread_id: "5136407914"
guid: https://blog.wapnet.nl/?p=1589
parent_post_id: null
post_id: "1589"
title: Brute force example MD5 password using hashcat
url: /2015/02/brute-force-example-md5-password-using-hashcat/

---
`hashcat -n 2 -m 0 -a 3 --pw-min 9 hashfile.txt ?l?l?l?l?l?l?l?l?l?l`

-n = 2 threads
-m 0 = md5
--pw-min 9 = minimal 9 characters
hashfile.txt = is txt file where the hash is located
`?l?l?l?l?l?l?l?l?l?l` = lowercase password

Have fun!
