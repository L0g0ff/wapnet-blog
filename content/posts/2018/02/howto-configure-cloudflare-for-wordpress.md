---
_edit_last: "1"
_thumbnail_id: "1794"
author: thomasf
categories:
  - networking
  - wordpress
cover:
  alt: cloudflare-logo
  image: /wp-content/uploads/2018/02/cloudflare-logo.jpg
date: "2018-02-25T22:17:57+00:00"
guid: https://blog.wapnet.nl/?p=1780
parent_post_id: null
post_id: "1780"
title: 'Howto: Configure cloudflare for wordpress'
url: /2018/02/howto-configure-cloudflare-for-wordpress/

---
My web hosting company don't support subdomain SSL certificates. And because Google's Chrome in July is required HTTPS on all websites (otherwise you get an error your website isn't safe) I had some deadline to make my blog HTTPS. Cloudflare is a nice reverse proxy solution and the basic plan is free to use also.

So what I did was create a cloudflare account and put my website behind it. After I did that I forced the HTTPS and voila my website was HTTPS. The steps you must take.

> _Note: this trick will also work if you want to use cloudflare as a reverse proxy to prevent DDoS, to optimize your site security, hide your hosting party backend and make your website a lot faster. If you use a raspbery Pi for example at your home location you can put cloudflare between the visitor and your home IP and save you a lot of trouble._

- If you use the wordfence plugin also be sure your PHP version is higher than 5.6. Otherwise you get some errors and conflicts ([more info](https://wordpress.org/support/topic/csrf-token-not-found-cloudflare-and-wordfence/))
- Go to cloudflare an create an account
- Configure your DNS

[![](/wp-content/uploads/2018/02/cloudflare-DNS-e1519597486214.jpg)](/wp-content/uploads/2018/02/cloudflare-DNS.jpg)

- (temporary) disable your DNSSEC at you domain if that is enabled (cloudflare cannot succesfully transfer your DNS otherwise). For me I had to create a ticket with my domain register company
- Cloudflare give you 2 new name servers. Ask your domain registry company to change these DNS name servers if you can change it by yourself

[![](/wp-content/uploads/2018/02/cloudflare-nameservers.jpg)](/wp-content/uploads/2018/02/cloudflare-nameservers.jpg)

- After a succesfull DNS nameserver change cloudflare shows in the portal everything is ok:

[![](/wp-content/uploads/2018/02/cloudflare-complete.jpg)](/wp-content/uploads/2018/02/cloudflare-complete.jpg)

- Now install the [wordpress cloudflare plugin](https://wordpress.org/plugins/cloudflare/)
- Fill in your username and API key.
- You can find the Global API key in your cloudflare profile @ [https://www.cloudflare.com/a/profile](https://www.cloudflare.com/a/profile)

[![](/wp-content/uploads/2018/02/cloudflare-api.jpg)](/wp-content/uploads/2018/02/cloudflare-api.jpg)

- Optimize your cloudflare for wordpress in the cloudflare wordpress plugin and enable HTTPS rewrites

[![](/wp-content/uploads/2018/02/cloudflare-optimize-wordpress.jpg)](/wp-content/uploads/2018/02/cloudflare-optimize-wordpress.jpg)[![](/wp-content/uploads/2018/02/cloudflare-http-rewrites.jpg)](/wp-content/uploads/2018/02/cloudflare-http-rewrites.jpg)

- Now edit your url in the settings >general in your wordpress

[![](/wp-content/uploads/2018/02/https-wapnet-blog.jpg)](/wp-content/uploads/2018/02/https-wapnet-blog.jpg)

- And finaly go to cloudflare and enable always uses HTTPS under crypto

[![](/wp-content/uploads/2018/02/always-use-https.jpg)](/wp-content/uploads/2018/02/always-use-https.jpg)

Now everything is done and your website is fully HTTPS at the frontend (with automatic HTTP > HTTPS URL rewrites). Because my backend don't have an SSL certificate all the data between cloudflare and my hosting company is still unencrypted. So this is a nasty workaround but you don't have any problem with Chrome HTTPS problems in the near future anymore.
