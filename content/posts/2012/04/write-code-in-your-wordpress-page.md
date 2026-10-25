---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - wordpress
date: "2012-04-27T12:32:42+00:00"
dsq_thread_id: "5347396618"
guid: https://blog.wapnet.nl/?p=869
parent_post_id: null
post_id: "869"
title: Write code in your wordpress page
url: /2012/04/write-code-in-your-wordpress-page/

---
\[banner\]

Sometimes you want to put code in your wordpress blog. The beste way to write code is switch to switch to HTML and put the <code> and </code> tags to your post.

Example with <code>:

> `
> mailq | tail -n +2 | grep -v '^ *(' | awk  'BEGIN { RS = "" } { if ($7 == "user@example.com") print $1 } ' | tr -d '*!' | postsuper -d -
> `

Example withoute <code>:

> mailq \| tail -n +2 \| grep -v '^ \*(' \| awk  'BEGIN { RS = "" } { if ($7 == "user@example.com") print $1 } ' \| tr -d '\*!' \| postsuper -d -

You will see that some characters won't display correctly if you don't use the code tag.

Another/better way to publish code is using the "SyntaxHighlighter Evolved" plugin.

Example:

```
mailq | tail -n +2 | grep -v '^ *(' | awk 'BEGIN { RS = "" } { if ($7 == "user@example.com") print $1 } ' | tr -d '*!' | postsuper -d -
```


And if you need special characters in your post try these:

```
< = &lt;
> = &gt;
/ = &#47;
] = &#93;
[ = &#91;
" = &#34;
' = &#39;
```


And if you want to use a code language try these


```sql
your code here
```


The following languages are supported:

 actionscript3
 bash
 clojure
 coldfusion
 cpp
 csharp
 css
 delphi
 erlang
 fsharp
 diff
 groovy
 html
 javascript
 java
 javafx
 matlab (keywords only)
 objc
 perl
 php
 text
 powershell
 python
 r
 ruby
 scala
 sql
 vb
 xml

SQL script Example:

```sql
USE database;
SELECT * FROM Persons
WHERE City='Sandnes'
```


Last but not least. DO NOT USE THE VISUAL VIEW :) Visual will scramble your code.

\[banner\]
