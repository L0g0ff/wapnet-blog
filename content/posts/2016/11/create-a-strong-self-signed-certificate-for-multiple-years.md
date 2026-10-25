---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
_thumbnail_id: "1748"
author: thomasf
categories:
  - networking
  - security
  - windows
cover:
  alt: certificate_icon
  image: /wp-content/uploads/2016/11/certificate_icon.jpg
date: "2016-11-12T16:52:15+00:00"
dsq_thread_id: "5298859182"
guid: https://blog.wapnet.nl/?p=1744
parent_post_id: null
post_id: "1744"
title: Create a strong self-signed certificate for multiple years
url: /2016/11/create-a-strong-self-signed-certificate-for-multiple-years/

---
If you follow these steps you can create a self signed certificate with the following specifications:

- Wildcard certificate
- SHA256 hash
- 10 years
- 2048 bits public key
- Client and server verification
- Sha1 fingerprint

**Be aware that self-signed certificates can manipulate by a man-in-the-middle. You should not use this in critical production environments.**

Please use windows 10 powershell in admin mode. Otherwise you will get errors


```
New-SelfSignedCertificate -certstorelocation cert:\localmachine\my -dnsname *.domain.local -NotBefore $([datetime]::now.AddDays(-15)) -NotAfter $([datetime]::now.AddDays(3560))
```


Now export the certificates. Before you copy/paste change the thumbprint with the thumbprint you get from the above command.


```
$CertPassword = ConvertTo-SecureString -String "YourPassword" -Force –AsPlainText
Export-PfxCertificate -Cert cert:\LocalMachine\My\C6B46CEB7D3A40DB08E78B19FEDD3A24EA7A7919 -FilePath C:\test.pfx -Password $CertPassword
Export-Certificate -Cert Cert:\LocalMachine\My\C6B46CEB7D3A40DB08E78B19FEDD3A24EA7A7919 -FilePath C:\tstcert.cer
```


Now you can import the PFX with IIS and bind the certificate in IIS.
And import the \*.CER in your MMC > Certificates > Computer account > trusted root Certification authority > Certificates

Have fun with your certificate the next 10 years :D

[![command-prompt-powershell](/wp-content/uploads/2016/11/Command-Prompt-powershell.png)](/wp-content/uploads/2016/11/Command-Prompt-powershell.png)[Inspiration](http://woshub.com/how-to-create-self-signed-certificate-with-powershell/)
