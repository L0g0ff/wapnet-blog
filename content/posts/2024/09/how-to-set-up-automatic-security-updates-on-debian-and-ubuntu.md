---
_thumbnail_id: "2215"
author: thomasf
categories:
  - uncategorized
cover:
  alt: A_powerful_superhero,_wearing_a_red_cape_and_blue_
  image: /wp-content/uploads/2024/09/A_powerful_superhero_wearing_a_red_cape_and_blue_.jpg
date: "2024-09-18T13:56:12+00:00"
guid: https://blog.wapnet.nl/?p=2214
parent_post_id: null
post_id: "2214"
tags:
  - linux
  - ubuntu
title: How to Set Up Automatic Security Updates on Debian and Ubuntu
url: /2024/09/how-to-set-up-automatic-security-updates-on-debian-and-ubuntu/

---
Keeping your Ubuntu server secure and up-to-date is crucial to minimizing the risk of vulnerabilities. One effective way to ensure timely patching of critical security issues is to enable automatic updates using `unattended-upgrades`. Here’s how to configure it step by step.

Cronjob Onliner (every sunday 3.00AM):

```
# Check current cronjobs
sudo crontab -l

# Add cronjob for weekly updates with reboot (Sunday 3:00 AM)
(sudo crontab -l; echo "0 3 * * 0 /usr/bin/apt-get update && DEBIAN_FRONTEND=noninteractive /usr/bin/apt-get --assume-yes upgrade && $(whereis -b reboot | cut -d' ' -f2)") | sudo crontab -

# Verify
sudo crontab -l
```

Or the real deal :)

TLDR;

`sudo apt install unattended-upgrades
sudo dpkg-reconfigure unattended-upgrades
sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
sudo nano /etc/apt/apt.conf.d/20auto-upgrades`

#### Step 1: Install `unattended-upgrades`

First, you need to install the package that handles automatic updates. You can do this by running the following command:

```
sudo apt install unattended-upgrades
```

This will install the necessary package to automate the upgrade process.

#### Step 2: Configure `unattended-upgrades`

Once the package is installed, you need to configure it. Run the following command to launch the configuration process:

```
sudo dpkg-reconfigure unattended-upgrades
```

During this process, you’ll be asked whether you want to enable automatic updates. Make sure to select "Yes" to enable it.

#### Step 3: Adjust Configuration Files

To further customize the behavior of automatic updates, you can modify some configuration files.

1. Open the main configuration file to specify which packages to automatically update:

```
   sudo nano /etc/apt/apt.conf.d/50unattended-upgrades
```

In this file, you can select specific origins or repositories from which packages should be updated, such as security updates.

1. Open another configuration file to control the frequency of updates:

```
   sudo nano /etc/apt/apt.conf.d/20auto-upgrades
```

In this file, you can specify the interval for how often the system should check for updates. It typically looks something like this:

```
   APT::Periodic::Update-Package-Lists "1";
   APT::Periodic::Unattended-Upgrade "1";
```

These settings indicate that the package list is updated daily, and the system performs unattended upgrades once a day as well.

#### Conclusion

With these steps, you’ve successfully set up automatic security updates on your Ubuntu server. This will help keep your system secure without needing constant manual intervention. While this is a good practice for keeping your server updated, it's always important to regularly check logs and ensure everything runs smoothly.
