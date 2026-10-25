---
_edit_last: "1"
author: thomasf
categories:
  - uncategorized
date: "2013-11-02T14:27:22+00:00"
dsq_thread_id: "5136405287"
guid: https://blog.wapnet.nl/?p=1435
parent_post_id: null
post_id: "1435"
title: Automatically download series with RSS (ShowRSS) and Synology
url: /2013/11/automatically-download-series-with-rss-showrss-and-synology/

---
I want the latest tvseries series automatically downloaded. There are plugins like couchpotato and sickbeard. Problem with these tools is that you must (semi) hack your synology nas to get this working.

Synology has the option to download automatically trough RSS. So I did a dive in to this option and I worked it out for you ;)

What do you need:

- Synology NAS
- ShowRSS account @ [http://showrss.info](http://showrss.info) (free)
- Some tv series that you like

After you create an account at [http://showrss.info](http://showrss.info) select the series you want to download and click "Add to my list"

[![showrss series overview](/wp-content/uploads/2013/11/showrss-series-overview.png)](/wp-content/uploads/2013/11/showrss-series-overview.png)

After that click on the feeds button and select the type of RSS you want to generate. I like HD versions and I also want to download a proper repack when the first edition have some audio and video problems

[![showrss generate rss](/wp-content/uploads/2013/11/showrss-generate-rss.png)](/wp-content/uploads/2013/11/showrss-generate-rss.png)

Click on generate and copy the RSS feed URL. (If you want to test the url and you use Firefox it looks like the feed is empty but when you use chrome instead you see the output.)

[![showrss copy url](/wp-content/uploads/2013/11/showrss-copy-url.png)](/wp-content/uploads/2013/11/showrss-copy-url.png)

Now login to your Synology NAS and open the download station. Click on RSS feeds and then on the blue plus button

[![synology add rss](/wp-content/uploads/2013/11/synology-add-rss.png)](/wp-content/uploads/2013/11/synology-add-rss.png)

Paste the RSS feed URL in to the field and **don't** press the download automatically option

[![synology add rss url](/wp-content/uploads/2013/11/synology-add-rss-url.png)](/wp-content/uploads/2013/11/synology-add-rss-url.png)

Now click on the download filter tab an click add. Fill in these fields:

[![synology save location](/wp-content/uploads/2013/11/synology-save-location.png)](/wp-content/uploads/2013/11/synology-save-location.png)

Now when the new tv series releases on the bittorent network your download started automatic .

Have fun and don't forget to click the donate button on the ShowRSS site if your like their website.
