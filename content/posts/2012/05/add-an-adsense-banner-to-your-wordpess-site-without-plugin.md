---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - uncategorized
date: "2012-05-17T18:38:57+00:00"
dsq_thread_id: "5323111840"
guid: https://blog.wapnet.nl/?p=900
parent_post_id: null
post_id: "900"
title: Add an Adsense banner to your wordpess site without plugin
url: /2012/05/add-an-adsense-banner-to-your-wordpess-site-without-plugin/

---
1. Start a FTP program and connect to your wordpress website
1. Locate your funtions.php (wp-content\\themes\\theme\_name\\functions.php)
1. Edit the file and put the following code in your functions.php file:


```javascript
function showads() {
return '
<script type="text/javascript"><!--
google_ad_client = "ca-pub-3134535021136249";
google_ad_slot = "3483719222";
google_ad_width = 468; google_ad_height = 60;
// -->
</script>
<script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
';}
add_shortcode('banner', 'showads');
```

 1. Modify the client, slot, width and height values
1. Safe the file and overwrite the current

Now you can use the **\[banner\]** tag in your post to publish the banner:

\[banner\]
