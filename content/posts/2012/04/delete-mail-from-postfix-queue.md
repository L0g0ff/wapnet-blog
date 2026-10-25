---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - linux
date: "2012-04-27T12:18:46+00:00"
dsq_thread_id: "5349304034"
guid: https://blog.wapnet.nl/?p=863
parent_post_id: null
post_id: "863"
title: Delete mail from postfix queue
url: /2012/04/delete-mail-from-postfix-queue/

---
The old command won't work anymore on my ubuntu server because of the error: _tail: cannot open \`+2' for reading: No such file or directory_
OLD Command:

> `
> # mailq | tail +2 | grep -v '^ *(' | awk  'BEGIN { RS = "" } { if ($8 == "user@example.com" && $9 == "") print $1 } ' | tr -d '*!' | postsuper -d -
> `

NEW Command:

> `
> # mailq | tail -n +2 | grep -v '^ *(' | awk  'BEGIN { RS = "" } { if ($7 == "user@example.com") print $1 } ' | tr -d '*!' | postsuper -d -
> `

Tnx to: [i8n1](http://i8n1.blogspot.com/2010/03/deleting-pesky-emails-that-are-in.html)

The above script only work for a specific email adres. Use the following script for bulk remove mail


```perl
#!/usr/bin/perl

$REGEXP = shift || die "no email-adress given (regexp-style, e.g. bl.*\@yahoo.com)!";

@data = qx</usr/sbin/postqueue -p>;
for (@data) {
if (/^(\w+)(\*|\!)?\s/) {
$queue_id = $1;
}
if($queue_id) {
if (/$REGEXP/i) {
$Q{$queue_id} = 1;
$queue_id = "";
}
}
}

#open(POSTSUPER,"|cat") || die "couldn't open postsuper" ;
open(POSTSUPER,"|postsuper -d -") || die "couldn't open postsuper" ;

foreach (keys %Q) {
print POSTSUPER "$_\n";
};
close(POSTSUPER);
```


For example, delete all queued messages from or to the domain called fackspamdomain.com, enter:


```
./postfix-delete.pl fackspamdomain.com
```


You can alos use


```
./postfix-delete.pl fackspam
```


Or an IP


```
./postfix-delete.pl 83.160.69.66
```


Source: [http://www.cyberciti.biz/tips/howto-postfix-flush-mail-queue.html](http://www.cyberciti.biz/tips/howto-postfix-flush-mail-queue.html)
