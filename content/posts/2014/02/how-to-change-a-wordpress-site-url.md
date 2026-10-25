---
_edit_last: "1"
author: thomasf
categories:
  - wordpress
date: "2014-02-07T22:47:00+00:00"
dsq_thread_id: "5161540465"
guid: https://blog.wapnet.nl/?p=1499
parent_post_id: null
post_id: "1499"
title: How to change a Wordpress site URL
url: /2014/02/how-to-change-a-wordpress-site-url/

---
Sometimes you may need to change the URL of your WordPress site.

For example, it is a common practice to develop the new version of your site in a subfolder and when it is ready to move it into your root directory.

WordPress, however, relies on its URL settings to work correctly.

This means that if you simply move your files and database it will not work properly.

The URL settings are located in the application database. Fortunately, direct database modification can be avoided by using a nice function provided by the WordPress developers named "update\_option".

Simply add these lines to the functions.php file of your theme:

```
update_option('siteurl','http://www.new-site-address.com');
update_option('home','http://www.new-site-address.com');
```

 [![wordpress-change-url](/wp-content/uploads/2014/02/wordpress-change-url.png)](/wp-content/uploads/2014/02/wordpress-change-url.png)

Then simply load your site from its new location - it should work just fine.

Note that after you run your site once and you make sure it works you should delete those lines from your functions.php file. The settings are already stored in your database and should not be modified each time your site is loaded.

Source (sorry ordinary copy/past): [http://www.siteground.com/tutorials/wordpress/change-url.htm](http://www.siteground.com/tutorials/wordpress/change-url.htm)
