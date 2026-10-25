---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - exchange
date: "2011-02-08T15:04:57+00:00"
dsq_thread_id: "6348433790"
guid: https://blog.wapnet.nl/?p=482
parent_post_id: null
post_id: "482"
title: Renew Self-Signed SSL Exchange 2007
url: /2011/02/renew-self-signed-ssl-exchange-2007/

---
I had to renew an expired self signed SSL certificate that i have on Exchange 2007 box today, and found the SSL clone trick interesting and did the job for me. So here's the howto:

Using the Exchange Management Shell run the following commands:

> Get-ExchangeCertificate -DomainName server.yourdomain.com (copy the thumbprint of the expired SSL)
> Get-ExchangeCertificate -Thumbprint <old thumbprint> \| New-ExchangeCertificate
>
> Now you can go to IIS and select your new created SSL certificate (this SSL have the same name as the old SSL one)
>
> [![](/wp-content/uploads/2010/12/IIS.png)](/wp-content/uploads/2010/12/IIS.png)

You might need to reboot IIS or any other service you enabled this SSL for.
