---
author: thomasf
categories:
  - linux
  - synology
date: "2021-02-10T20:39:11+00:00"
guid: https://blog.wapnet.nl/?p=1887
parent_post_id: null
post_id: "1887"
title: 504 Gateway Timeout on Synology NAS
url: /2021/02/504-gateway-timeout-on-synology-nas/

---
Looks familiar?

{{< figure src="/wp-content/uploads/2021/02/nginx.png" alt="" caption="" >}}

I want to move this blog to my own NAS because I have plenty enough bandwidth and with [Cloudflare](/2018/02/howto-configure-cloudflare-for-wordpress/) as reverse proxy it is secure enough also (and I like to hobby off course ;) ).

I tried to use the Duplicator WordPress plugin to make a dump of my website and do a restore in the Synology Webstation. But during the database restore in step 2 every time I was getting a 504 gateway timeout after a minute (exactly 60 seconds).

What I could have done was a manual (ftp & database) copy and restore the files. But I was sure I was getting other errors in the future when I had to update WordPress or other plugins. So fixing this timeout issue was the only solution.

On different places on the internet, I found that I had change the Nginx site settings. So I put the timeout settings in the associated "/etc/nginx/conf.d/ _site_.conf" and restart Nginx and restore the database Nginx was still was failing.

```
    proxy_connect_timeout 600s;
    proxy_send_timeout 600s;
    proxy_read_timeout 600s;
    send_timeout 600s;
```

Then I'll try to put these lines in the "/etc/nginx/nginx.conf" but when I restart the nginx the settings were overwritten and my changes are gone.

Every time you restart, Nginx Synology make use of a file "/usr/syno/share/nginx/nginx.mustache" to create a new nginx.conf file. I change the lines in that file and \*boom\* everything was working :)

So TLDR;

```
sudo su -
vim /usr/syno/share/nginx/nginx.mustache

#add these lines
    send_timeout                  600s;
    proxy_connect_timeout         600s;
    proxy_send_timeout            600s;
    proxy_read_timeout            600s;

synoservice --restart nginx
```

If you want to see the current Nginx config

```
nginx -T
```

Have fun :)
