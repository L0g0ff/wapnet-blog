---
_edit_last: "1"
_oembed_7f8b1cd11557f8e2545a475379e77346: '{{unknown}}'
_wp_old_slug: ""
author: thomasf
categories:
  - programmeren
date: "2011-08-24T10:06:22+00:00"
dsq_thread_id: "5330314833"
guid: https://blog.wapnet.nl/?p=522
parent_post_id: null
post_id: "522"
tags:
  - regex
title: Regular Expressions Example
url: /2011/08/regular-expressions-example/

---
If you want to use regular expressions to know if some numerical value is higher then 199 use the following code:

> **^\\d{1,2}$\|^\[1\]\\d\\d$**

Explanation:

^          = String begins with

\\d         = numerical string (character 0-9)

{1,2}    = minimal 1 maximum 2 numerical characters

$          = end script

\|           = OR (to bind 2 regular expressions)

^          = begins with

\[1\]        = first character = 1 (if you want to go till 299 it may be \[1-2\])

\\d\\d      = the next 2 character must be numerical strings

$          = end

For 399 the parameter can be:

> **^\\d{1,2}$\|^\[1,2,3\]\\d\\d$**

or

> **^\\d{1,2}$\|^\[1-3\]\\d\\d$**

Nice freeware regex tool: [http://www.radsoftware.com.au/regexdesigner/](http://www.radsoftware.com.au/regexdesigner/)

Lot of samples: [http://www.regular-expressions.info/examples.html](http://www.regular-expressions.info/examples.html)

Online test: [http://www.regexplanet.com/simple/index.html](http://www.regexplanet.com/simple/index.html)

Very nice online test tool: [https://regex101.com/](https://regex101.com/)

Hope this helps :)
