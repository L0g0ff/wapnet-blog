---
_edit_last: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - networking
date: "2012-08-14T18:27:17+00:00"
dsq_thread_id: "5137637941"
guid: https://blog.wapnet.nl/?p=968
parent_post_id: null
post_id: "968"
title: Stub zone easy explained
url: /2012/08/stub-zone-easy-explained/

---
The difference between stub zone and secondary DNS zones...  It all relates to replication, efficiency and availability.

Think of it like this:
There are two cities, London and Manchester.
London has 100 people, each with a book full of information (so 100 books in total).
You are in Manchester and you want to be able to have access to the information in these "books".

There are two ways to do this as follows:
a) Another 100 people appear in London, they each make a copy of a book, and they each take their own car in order to drive to Manchester to meet you and give you the books. This causes a traffic jam due to the high number of people driving on the highway.

The above is secondary zone replication.

b) Instead of the above, you received the address of the 100 people in London. You need information in one of the books. You decide to take your car, and you drive to the address. You found the information you need, and you drive back to Manchester.

This example is a stub zone.

So think about it for a second.
In example A, the information is stored twice, both in London and Manchester, but the information requires a big highway to transport those 100 people, each in their individual cars, to your office in Manchester. Do you have a big enough highway to support this many people?
In example B, you don't need such a big highway because a massive number of people are not clogging the highway, each trying to bring a book to you, but instead you decide to go back to London to find the book you need.

So what do we gather from this?
In example A, you need a large highway (lots of bandwidth) to get the books from London to Manchester. But once the information is in Manchester, you can very quickly find the book you need.
In example B, you don't need a large highway to find the book in London, but you do need a RELIABLE highway. If this highway is closed, how do you get the book? And remember, since the books are not in Manchester, it will take longer for you to get the book (since you need to drive back and forth for it).

Hope this helps, first thing that came to my mind.

Thanks to [Shinigami](http://www.certforums.com/forums/network-infrastructure/44684-difference-between-secondary-stub-zones.html)
