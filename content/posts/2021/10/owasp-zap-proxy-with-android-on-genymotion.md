---
_thumbnail_id: "1959"
author: thomasf
categories:
  - android
  - linux
  - networking
cover:
  alt: pexels-marta-branco-1194713
  image: /wp-content/uploads/2021/10/pexels-marta-branco-1194713-e1635255492929.jpg
date: "2021-10-26T13:30:48+00:00"
guid: https://blog.wapnet.nl/?p=1941
parent_post_id: null
post_id: "1941"
title: OWASP ZAP Proxy with Android on Genymotion
url: /2021/10/owasp-zap-proxy-with-android-on-genymotion/

---
It can be fun to reverse engineer some android applications. I think it's better to do this on your workstation instead of your phone because it's way more flexible and you don't ruin your phone when you break things ;)

In my case, I use Debian 11. But of course, you can do this with any OS.

# Requirements

- An app you want to debug
- OWASP ZAP Proxy
- Genymotion
- NPM
- APK Export (Android App)

# OWASP ZAP Proxy

I use the snap package for ZAP because it's easy to install and you've always the latest version.

```
$ sudo snap install zaproxy --classic
```

Start ZAP and export the dynamic certificate (tools > options)

{{< figure src="/wp-content/uploads/2021/10/image-1.png" alt="" caption="" >}}

- Click on the save button an place the file somewhere on your disk.

You can check if the OWASP ZAP is running with:

```
$ netstat -tulpen | grep 8080
tcp6       0      0 127.0.0.1:8080          :::*                    LISTEN      1000       89190      14016/java
```

# Genymotion

Now the proxy is in place it's time to install genymotion for the android emulation. First install virtualbox.

Install virtualbox APT keys

```
$ wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo apt-key add -
$ wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | sudo apt-key add -
```

Edit the /etc/apt/sources file and add this line:

```
deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian bullseye contrib

```

Update the repo and install virtualbox

```
$ sudo apt-get update
$ sudo apt-get install virtualbox-6.1

```

- Now go the the genymotion website and download the latest bin file

{{< figure src="/wp-content/uploads/2021/10/image-2.png" alt="" caption="" >}}

- Make the file executable and run the installer

```
$ chmod +x genymotion-3.2.1-linux_x64.bin
$ ./genymotion-3.2.1-linux_x64.bin
```

- Follow the wizards, create an genymotion account and create a new virtual device. In my example I used a google Pixel 3 with Android 10.

{{< figure src="/wp-content/uploads/2021/10/image-3.png" alt="" caption="" >}}

Now it's time to configure the proxy within the android device!

# Configure proxy in Android

Start the created virtual genymotion android device and copy the certificate file we create earlier with a simple drag and drop.

{{< figure src="/wp-content/uploads/2021/10/image-5.png" alt="" caption="" >}}

{{< figure src="/wp-content/uploads/2021/10/image-4.png" alt="" caption="" >}}

- Now we can can configure the proxy in the wifi settings.
- Go to settings > search for certificate and install the certificate.

{{< figure src="/wp-content/uploads/2021/10/image-6.png" alt="" caption="" >}}

{{< figure src="/wp-content/uploads/2021/10/image-7.png" alt="" caption="" >}}

Edit the wifi connection, add the proxy and restart the wifi.

- Edit the Wifi
- Go to the advance options
- Set the proxy to Manual
- The IP is always: **10.0.3.2** _This is the "localhost" setting for the genymotion host server_
- Port **8080**

{{< figure src="/wp-content/uploads/2021/10/image-8.png" alt="" caption="" >}}

When you (re)connect the the wifi you have the accept the proxy error (but this is a good thing).

{{< figure src="/wp-content/uploads/2021/10/image-9.png" alt="" caption="" >}}

{{< figure src="/wp-content/uploads/2021/10/image-11.png" alt="" caption="" >}}

Now you will see all the traffic. But only the traffic for the apps who respect the android HTTP\_PROXY settings. So this is what you can do when an app don't respect this setting:

# Rebuild the APK with APK-MITM

Now everything is in place. So the last thing we need to do is rebuild the APK file so we can proxing all the network traffic. So:

- First export the APK file trough the [APK Export](https://play.google.com/store/apps/details?id=com.ses.app.apkexport)
- Place the APK somewhere on your disk
- Install npm (at least version 14)

```
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
$ sudo apt-get install nodejs npm
```

- Install java

```
$ sudo apt install openjdk-17-jre openjdk-17-jdk
```

- And rebuild the APK

```
$ npx apk-mitm SomeAppName.apk
```

{{< figure src="/wp-content/uploads/2021/10/image-13.png" alt="" caption="" >}}

# And here we go!

Everything is in place now. So the only thing you have to do is drag & drop the **\*-patched.apk** file to genymotion, install this file and you are fully in control :)

{{< figure src="/wp-content/uploads/2021/10/image-14.png" alt="" caption="" >}}

Happy hacking!
