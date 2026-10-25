---
_edit_last: "1"
author: thomasf
categories:
  - linux
  - networking
  - programmeren
date: "2010-01-12T21:54:47+00:00"
dsq_thread_id: "5136177914"
guid: https://blog.wapnet.nl/?p=313
parent_post_id: null
post_id: "313"
title: Migrate my Joomla 1.0.15 to 1.5.x
url: /2010/01/migrate-my-joomla-1-0-15-to-1-5-x/

---
Yes, I know... My Joomla site is very old. In this article I will write down all my migration steps. The best practise is to create a development environment. I download and install a Debian 5.0 (lenny) OS and installed all the common LAMP, SSH, Samba, PHPMyadmin & ImageMagick  packages. Then:

1. I Copy the content of my site to my development environment
1. Edit the joomla configuration.php file and change my physical paths
1. Upload my database
1. Check all my joomla modules
1. set 777 permisions for easy testing ;)
1. I know from earlier testing that mine Joomla template is not compatible with 1.5. So I download and install Artisteer 2 to create a new template. This software works so easy I created the template with my girlfriend ;) ([download torrent](http://thepiratebay.org/torrent/5252382/Artisteer_2.3.0.23023___Crack_Loader___VirusFree___Working))
1. My Biggest concern is the community builder component and the forum. This are the most important modules so I will upgrade them first.
1. Backup administrator/components/com\_comprofiler/ **ue\_config.php**, remove the CB module and reinstall the latest versions. (note: latest CB have 1.5.10 native support)
1. My Fireboard version is aleady to the latest version (1.0.5 RC2) :D
1. Now I will install the migrator tools and follow the 5 migration steps @ [http://docs.joomla.org/Migrating\_from\_1.0.x\_to\_1.5\_Stable](http://docs.joomla.org/Migrating_from_1.0.x_to_1.5_Stable)
1. I have installed the migrator and the fireboard ETL's. After that I create A SQL Dump. Now I must create a new 1.5 install and import everything.
1. Note: You can now download your SQL dump file and upload it into your Joomla! 1.5 installation to continue the process. Don't forget to select migration and use the prefix 'jos\_' (this migrator rewrites your prefix to jos\_ even if the sites prefix is different).
1. I found a small community builder howto @ [http://www.alledia.com/blog/joomla-15/migrating-to-joomla-15/](http://www.alledia.com/blog/joomla-15/migrating-to-joomla-15/)
1. \\* Step 1: Export the Community Builder database tables from 1.0
    \\* Step 2: Download administrator / components / com\_profiler / ue\_config.php
    \\* Step 3: Install CB on the 1.5 site:
    \\* Step 4: Delete the CBt database tables on 1.5 and import the old tables from 1.0
    \\* Step 5: Upload the old ue\_config.php to administrator / components / com\_profiler / ue\_config.php
1. For expose I can install the latest version. The copy the ../components/com\_expose/expose/img and xml folders to the new site. That as very easy :)
1. For the CB Profile pictures I copy images/comprofiler to the new site.
1. .. to be continued

Template fix:

Extensions > Module manager > Top Menu (or any other menu, e.g. Main Menu) > click to Edit this module > select Position = **user3**. Save the configuration and go to the frontpage. You should see your Artisteer style applied to the menu items.

And first assign another default template and then your template

http://thepiratebay.org/torrent/5252382/Artisteer\_2.3.0.23023\_\_\_Crack\_Loader\_\_\_VirusFree\_\_\_Working
