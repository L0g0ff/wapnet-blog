---
_disable_fbc: ""
_edit_last: "1"
_thumbnail_id: "1680"
author: thomasf
categories:
  - linux
  - networking
  - security
cover:
  alt: SSL-Certificate-how-to-secure-your-web-site
  image: /wp-content/uploads/2015/12/SSL-Certificate-how-to-secure-your-web-site.jpg
date: "2015-12-21T16:16:00+00:00"
dsq_thread_id: "5144606227"
guid: https://blog.wapnet.nl/?p=1677
parent_post_id: null
post_id: "1677"
title: Convert PFX to PEM and upload the certificate to Plesk
url: /2015/12/convert-pfx-to-pem-and-upload-the-certificate-to-plesk/

---
Export the Private Key:
`
# openssl pkcs12 -in filename.pfx -nocerts -out key.pem
`
Remove the password from the SSL certificate (unencrypted is needed for plesk):
`
# openssl rsa -in key.pem -out server.key
`
Export the certificate:
`
# openssl pkcs12 -in filename.pfx -clcerts -nokeys -out cert.pem
`

Now upload the certificate:

[![ssl-thawte](/wp-content/uploads/2015/12/SSL-thawte.png)](/wp-content/uploads/2015/12/SSL-thawte.png)

And bind the certificate in your hosting settings:

[![SSL-PII](/wp-content/uploads/2015/12/SSL-PII.png)](/wp-content/uploads/2015/12/SSL-PII.png)
