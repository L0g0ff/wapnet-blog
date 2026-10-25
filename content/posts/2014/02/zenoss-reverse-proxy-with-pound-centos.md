---
_edit_last: "1"
author: thomasf
categories:
  - linux
  - monitoring
  - security
date: "2014-02-27T14:38:16+00:00"
dsq_thread_id: "5181060033"
guid: https://blog.wapnet.nl/?p=1503
parent_post_id: null
post_id: "1503"
title: Zenoss reverse proxy with Pound (CentOS)
url: /2014/02/zenoss-reverse-proxy-with-pound-centos/

---
Zenoss don't support SSL certificates out-of-the-box. If you want to use an SSL connection to your zenoss monitor server the only thing you can do is use an reverse proxy. You can use this howto to install and configure a pound reverse proxy.

**Install pound with the EPEL**

Install the EPEL (more info about [EPEL](https://fedoraproject.org/wiki/EPEL)) repository with these commands:

```
su -c 'rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm'
```

```
yum update
```

Install pound

```
yum install pound
```

 **Install pound without the EPEL**

```
wget http://dl.fedoraproject.org/pub/epel/6/x86_64/Pound-2.6-2.el6.x86_64.rpm
rpm -ivh Pound-2.6-2.el6.x86_64.rpm
```

 **Configure Pound**

I had a lot of trouble because I used a real SSL certificate immediately. The cause was I dropped the SSL cert in the wrong linux folder. Best practice is first create a selfsigned SSL, test pound and then replace the selfsigned with a real SSL certificate.

```
cd /etc/ssl && openssl req -x509 -newkey rsa:1024 -keyout local.server.pem -out local.server.pem -days 365 -nodes
```

Configure Pound

```
nano /etc/pound.cfg
```

Config file:

```
User "pound"
Group "pound"
Control "/var/lib/pound/pound.cfg"
```

```
ListenHTTPS
Address 192.168.0.x
Port    443
Cert    "/etc/ssl/local.server.pem"
End
```

```
Service
BackEnd
Address 127.0.0.1
Port    8080
End
End
```

Now start the pound service

```
service pound start

```

**Change the Zenoss config the handle the HTTPS traffic**

```
nano /opt/zenoss/etc/zope.conf
```

Ad these 3 lines:

```
<cgi-environment>
HTTPS ON
</cgi-environment>

```

Restart zope

```
su - zenoss
restart zopectl

```

**Replace the selfsigned SSL with a wildcard SSL (optional)**

Create a PFX in windows. Tranfer the PFX to the Zenoss server and tranform the PFX to PEM (Linux certificate format). The command:

```
openssl pkcs12 -in validcertificate.pfx -out wilcard.domain.nl.pem -nodes
```

Now change the pound cert:

```
nano /etc/pound.cfg
```

```
ListenHTTPS
Address 192.168.0.x
Port    443
Cert    "/etc/ssl/wilcard.domain.nl.pem"
End
```

Restart the service

```
service pound restart
```

Source: [Enabling SSL in Zenoss 4.2 - Open Source Network Monitoring and Systems Management](https://community.zenoss.org/message/67923)
