---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - exchange
  - iis
  - windows
date: "2010-12-16T14:41:07+00:00"
dsq_thread_id: "5136177796"
guid: https://blog.wapnet.nl/?p=494
parent_post_id: null
post_id: "494"
title: Install Thawte SSL Webserver or Wildcard (the Quick way)
url: /2010/12/install-thawte-ssl-webserver-or-wildcard-the-quick-way/

---
After you successfully installed a web or wildcard SSL certificate you must follow some extra steps.

- First [download this zip](/wp-content/uploads/2010/12/ThawteSSLCA.zip) with 2 SSL certificates
- Extract the zip e.g. C:\\install\\ssl
- Start > run > mmc > file> add/remove snap in > certificates > local computer >computer account > Intermediate Certification Authorities > right click certificates > import

Then disable the old certificate

- Expand Trusted Root Certification Authorities > certificates
- Locate this certificate:

> Common Name – thawte Primary Root CA
> Expiry Date – 17th July 2036
> Thumbprint – 91 c6 d6 ee 3e 8a c8 63 84 e5 48 c2 99 29 5c 75 6c 81 7b 81

- disable it completely

When the SSL not exist, please follow this steps:

- [Download this zip](/wp-content/uploads/2010/12/2036root.zip)
- Install it here: Trusted Root Certification Authorities > certificates
- Disable the certificate

I used this website as source: [http://www.ripley.za.net/howto/it\_howto/ssl-web-server-or-wildcard-certificate-issued-after-june-26-2010-not-trusted-after-installation-on-microsoft-iis/](http://www.ripley.za.net/howto/it_howto/ssl-web-server-or-wildcard-certificate-issued-after-june-26-2010-not-trusted-after-installation-on-microsoft-iis/)
