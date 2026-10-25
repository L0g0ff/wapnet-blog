---
_edit_last: "1"
author: thomasf
categories:
  - uncategorized
date: "2008-11-14T11:49:51+00:00"
guid: https://blog.wapnet.nl/?p=142
parent_post_id: null
post_id: "142"
title: Installeer een Joomla testomgeving onder Windows
url: /2008/11/installeer-een-joomla-testomgeving-onder-windows/

---
Hierbij de stappen om een website Joomla te ontwikkelen

1.    Download en installeer wampserver op je pc ([http://www.wampserver.com/en/download.php](http://www.wampserver.com/en/download.php)). Install locatie c:\\wamp\
2.    Start na de installatie de services:

[![](/wp-content/uploads/2008/11/joomla-1.jpg)](/wp-content/uploads/2008/11/joomla-1.jpg)

3.    Download joomla 1.5 full package: [http://www.joomla.org/download.html](http://www.joomla.org/download.html)
4.    Pak het zip bestand uit in op c:\\wamp\\www\
5.    Ga in je browser naar [http://localhost](http://localhost)
6.    Start phpmyadmin
7.    Maak een nieuwe database (nieuwe collatie) noem deze test
8.    Ga naar het begin scherm van phpmyadmin
9.    Klik op rechten en maak een nieuwe gebruiker en noem deze test met password test. Database staat op localhost en klik op start

[![](/wp-content/uploads/2008/11/joomla-2.jpg)](/wp-content/uploads/2008/11/joomla-2.jpg)

10.    Scroll naar beneden en geef op test en druk op start

[![](/wp-content/uploads/2008/11/joomla-3.jpg)](/wp-content/uploads/2008/11/joomla-3.jpg)

11.    Klik op selecteer alles en klik op start

[![](/wp-content/uploads/2008/11/joomla-4.jpg)](/wp-content/uploads/2008/11/joomla-4.jpg)

12.    Ga naar [http://localhost/joomla](http://localhost/joomla) en doorloop de wizard.
13.    Als de wizard succes verlopen is moet je even de installatie map hernoemen of verwijderen. Deze is te vinden op: c:\\wamp\\www\\installation

Plugins/Extensions kun je van [http://extensions.joomla.org/](http://extensions.joomla.org/) halen :) Succes
