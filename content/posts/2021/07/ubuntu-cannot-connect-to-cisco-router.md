---
author: thomasf
categories:
  - cisco
  - linux
date: "2021-07-23T13:34:04+00:00"
guid: https://blog.wapnet.nl/?p=1929
parent_post_id: null
post_id: "1929"
title: Ubuntu cannot connect to Cisco Router
url: /2021/07/ubuntu-cannot-connect-to-cisco-router/

---
Please follow these steps if you cannot can connect to a router. For example

```
ssh someusername@blog.wapnet.nl
```

Output

```
Unable to negotiate with blog.wapnet.nl port 22: no matching key exchange method found. Their offer: diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1,diffie-hellman-group1-sha1
```

use the -o parameter

```
ssh -o KexAlgorithms=+diffie-hellman-group1-sha1 someusername@blog.wapnet.nl
```

Output:

```
Unable to negotiate with blog.wapnet.nl port 22: no matching cipher found. Their offer: aes128-cbc,3des-cbc,aes192-cbc,aes256-cbc
```

and add the -c parameter

```
ssh -o KexAlgorithms=+diffie-hellman-group1-sha1 -c aes256-cbc  someusername@blog.wapnet.nl
```

and you are connected :)

```
The authenticity of host 'blog.wapnet.nl' can't be established.
RSA key fingerprint is SHA256:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```
