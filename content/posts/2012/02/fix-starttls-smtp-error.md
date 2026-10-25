---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - exchange
date: "2012-02-28T10:20:14+00:00"
dsq_thread_id: "5137904900"
guid: https://blog.wapnet.nl/?p=799
parent_post_id: null
post_id: "799"
title: Fix  STARTTLS SMTP error
url: /2012/02/fix-starttls-smtp-error/

---
**Error:**

Microsoft Exchange could not find a certificate that contains the domain name exchange.global-e.nl in the personal store on the local computer. Therefore, it is unable to support the STARTTLS SMTP verb for the connector Outbound Ex 2010 with a FQDN parameter of exchange.global-e.nl. If the connector's FQDN is not specified, the computer's FQDN is used. Verify the connector configuration and the installed certificates to make sure that there is a certificate with a domain name for that FQDN. If this certificate exists, run Enable-ExchangeCertificate -Services SMTP to make sure that the Microsoft Exchange Transport service has access to the certificate key.

**Cause:**

Problem is that you have configured a wrong (not matching)  SSL certificate on your send/recieve connector.

**Fix:**

- Start the Exchange Powershell
- Get-ExchangeCertificate
- Copy the good thumbprint
- Enable-ExchangeCertificate -Services SMTP
- Paste the good thumbprint

More information:

[http://blog.ronnypot.nl/?p=271](http://blog.ronnypot.nl/?p=271) [http://smtpport25.wordpress.com/2009/03/19/renewing-the-certificate-in-client-access-servers/](http://smtpport25.wordpress.com/2009/03/19/renewing-the-certificate-in-client-access-servers/)
