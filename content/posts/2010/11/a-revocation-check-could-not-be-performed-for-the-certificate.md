---
_disable_fbc: ""
_edit_last: "1"
_wp_old_slug: ""
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - iis
  - windows
date: "2010-11-15T20:23:10+00:00"
dsq_thread_id: "5136177480"
guid: https://blog.wapnet.nl/?p=450
parent_post_id: null
post_id: "450"
title: A revocation check could not be performed for the certificate
url: /2010/11/a-revocation-check-could-not-be-performed-for-the-certificate/

---
_If this article helps you please consider a donation. I don't like adds on my blog._

When you get the RDP error "a revocation check could not be performed for the certificate" on a windows 7 workstation after you installed an SSL from a certification, you must disable enablecredsspsupport support. You can do this in the RDP file you are using. Open the \*.rdp file in notepad and add the following line:

_enablecredsspsupport:i:0_ [![](/wp-content/uploads/2010/11/notepad.png)](/wp-content/uploads/2010/11/notepad.png)

If you are using TSWeb you can add this to the RemoteApp section.

[![](/wp-content/uploads/2010/11/RemoteApps.png)](/wp-content/uploads/2010/11/RemoteApps.png)

You can check if the SSL work correctly when you click on the lock icon in the connection bar

You can also fix the problem itself by creating an SSL certificate trough the windows enterprise authority. Here are the steps:

_Resolution_
_=======================_ _To recover from the CA failure, we tried the following procedures:_ _Procedure A: recover the CA. In this procedure, we tried the following steps:_ _1\. setup a new Enterprise Root CA on a Windows Server 2008 Enterprise Edition box. The Steps of this procedure can be found at:_ _Install Active Directory Certificate Services_ _[http://technet.microsoft.com/en-us/library/cc947821(WS.10).aspx](http://technet.microsoft.com/en-us/library/cc947821%28WS.10%29.aspx)_ _Refer:_ _Active Directory Certificate Services Step-by-Step Guide_
_[http://technet.microsoft.com/en-us/library/cc772393(WS.10).aspx](http://technet.microsoft.com/en-us/library/cc772393%28WS.10%29.aspx)_ _2\. Configure the CA's CDP and AIA to publish the CRL and AIA to the Internet Address on your web server. We did this by creating a virtual directory mapping to the CA's share "CertEnroll". This can be done via the following step:_ _\- Logon to the IIS Server which holds the Web Service in your network._ _\- Run Inetmgr to open the IIS management console._
_\- Under the default web site, we created a new Virtual Directory called "CertEnroll" and mapped it to the "CertEnroll" share on the CA. At the same time, we manually specific the account for this connection ._
_\- Logon t o the CA and run "Certsrv.msc" to open the CA's management console._ _\- Right click on the CA and select Properties._
_\- Switch to "Extensions" tab._
_\- In the Extension list, select "CDP" and then add a new CDP points to the Address we just created in the IIS and checked the option to add this extension to issued certificates._
_\- In the Extension list, select "AIA" and perform similar steps as we did for CDP._ _Refer:_ _Configure CDP and AIA Extensions_
_[http://technet.microsoft.com/en-us/library/cc776904(WS.10).aspx](http://technet.microsoft.com/en-us/library/cc776904%28WS.10%29.aspx)_ _Procedure B: Recover the TS Gateway Certificate. In this procedure, we tried the following steps:_ _1\. Enable the SSL for the CA's web enrollment page via the following steps:_ _\- Open the MMC on the CA._ _\- Click File -> Add/Remove Snap-ins -> Certificates -> Computer -> Local Computer to load the local computer's certificate store._
_\- Right on the Certificates \| Personal \| Certificates to request a new certificate from the new CA. Since we need to enable the SSL for the web site, we requested the Domain Controller_ _Certificate Template as this templates contains the "Server Authentication" in application policy._
_\-  Open the IIS Management console on the CA via "Inetmgr" command._
_\- Open the Web site hold the CA's web enrollment._
_\- Click "Binding" and add a new binding for HTTPS and select the certificate we just requested._ _2\. Duplicate the Web Server certificate template._ _\- On the CA, run Certsrv.msc to open the CA's management console._ _\- Right click on certificate templates and select Duplicate to duplicate it and name it "TS Gateway"._
_\- Mark the key as "exportable" for this template._ _3\. Request the certificate for the TS Gateway:_ _\- Logon to the TS Gateway._ _\- Launch IE and access [https://ca-name/certsrv](https://ca-name/certsrv)._
_\- use the Advanced Request to request the "TS Gateway" certificate template and put the common name as the TS Gateway's virtual name "safari-1.bbe.k12.mn.us"._
_\- Install the certificate._
_\- Open the User's certificates store via the command "Certmgr.msc"._
_\- Right click the certificate we just requested and export it along with its private key to a PFX file._
_\- Launch IIS Management console via Inetmgr command._
_\- Right click on the Web site for TS Gateway and click "Server Certificates" to import the PFX file._
_\- Launch Server manager to open the TS Gateway's console and then configure the new certificate we just requested for the TS Gatway._ _Procedure C: recover the nodes in the TS Farm._ _1\. Request Certificates for the TS Farm nodes:_ _\- Logon to the TS Farm nodes._ _\- Launch IE and access [https://ca-name/certsrv](https://ca-name/certsrv)._
_\- use the Advanced Request to request the "TS Gateway" certificate template and put the common name as the TS Farm virtual name "safari-1.bbe.priv"._
_\- Install the certificate._
_\- Open the User's certificates store via the command "Certmgr.msc"._
_\- Right click the certificate we just requested and export it along with its private key to a PFX file._ _2\. Configure the Certificate for the TS nodes._ _\- Open the TS management console._ _\- Right click on the RDP interface to specify the new certificate for those nodes in the Properties page._ _More Information_ _==================================_ _For clients, they can access the TS Gateway and would receive a warning indicating the certificate is not trusted. They can check the certificate chain by click "view certificate". Meanwhile, they can also access the AIA directly  to download the Root CA's certificate and install it on the client: [http://domain-name/certenroll/Jaguar6.bbe.priv\_bbe-ca.crt](http://domain-name/certenroll/Jaguar6.bbe.priv_bbe-ca.crt)_ _If this article helps you please consider a donation. I don't like adds on my blog._
