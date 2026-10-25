---
_edit_last: "1"
_thumbnail_id: "1466"
author: thomasf
categories:
  - exchange
cover:
  alt: schedule
  image: /wp-content/uploads/2013/12/schedule.png
date: "2013-12-03T14:36:49+00:00"
dsq_thread_id: "5138288399"
guid: https://blog.wapnet.nl/?p=1465
parent_post_id: null
post_id: "1465"
title: Room Mailbox - Your meeting request was declined
url: /2013/12/room-mailbox-your-meeting-request-was-declined/

---
When you reschedule appointments in a roombox you can get this error:

`Your meeting request was declined.
It didn't specify an end date. The end date must be before x/x/xxxx.`

To fix this start the Exchange Management Shell and set this commands:

`get-CalendarProcessing  * |fl |findstr Roombox
set-CalendarProcessing "Roommailbox" -EnforceSchedulingHorizon $false
set-CalendarProcessing "Roommailbox" -BookingWindowInDays 1080`

After this cmdlet you can schedule the appointments more than the default 180 days.
