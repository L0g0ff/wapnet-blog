---
_edit_last: "1"
_thumbnail_id: "1448"
author: thomasf
categories:
  - linux
cover:
  alt: spam
  image: /wp-content/uploads/2013/11/spam.png
date: "2014-05-21T12:55:38+00:00"
dsq_thread_id: "5142770526"
guid: https://blog.wapnet.nl/?p=1554
parent_post_id: null
post_id: "1554"
title: Find spam script
url: /2014/05/find-spam-script/

---
## THIS IS AN ORDINARY COPY/PAST FROM http://cbl.abuseat.org because I can't find a source link and this is a nice article!

We have detected that this IP is NATting for, or is infected itself, with a Linux (or possibly some other Unix-like system such as FreeBSD) PHP spam mailing script. Occasionally Windows servers are infected as well.

We do not know how the malware got installed onto the machine, but we know a lot of what it does. The main thing we've seen it doing is sending staggering large volumes of email spam. But it can do a lot more than that, and that is the real danger.

NEW Of late some of these infections are facilitiated by a [SSH Rootkit](http://cbl.abuseat.org/sshvuln.html) called "ebury". See the link for more detail.

In most cases, this IP address would be that of a shared hosting environment. If you are a customer of this environment, you will almost certainly not be able to do anything about it, only the administrators of the hosting environment itself can. Please contact your administrators, and refer them to this page.

If the administrators are reluctant to do anything please try to convince them, because there is nothing you can do to fix this problem.

## For the System Administrators

Your task is to find the current problem, fix it, and prevent it from happening again.

### Finding the problem by network activity: Linux/FreeBSD etc

One way of finding the user that is infected and spewing spam is to use the "lsof" (list open files) utility. "lsof" is available for most versions of UNIX-like systems such as Linux as part of the official distribution, but may not be installed by default. So first, make sure you have it installed. On many systems such as Ubuntu, you can install it by:

```
sudo apt-get install lsof

```

Once lsof is installed, you can issue the following command

```
sudo lsof -i | grep smtp

```

You may see a number of lines, such as (example.com takes the place of your machine's name):

```
sendmail- 18520 root  3u IPv4 3016693 0t0 TCP *:smtp (LISTEN)
sendmail   4401 mail 13u IPv4 8742322 0t0 TCP example.com:42177->mail1.hotmail.com:smtp (ESTABLISHED)
exim       6348 mail  3u IPv4 210565067 0t0 TCP *:smtp (LISTEN)
find       4403  foo 13u IPv4 8742322 0t0 TCP example.com:42176->mtain-dk.r1000.mx.aol.com:smtp (ESTABLISHED)

```

The first line, for example, is your sendmail mail software "LISTEN"ing (as userid root) for inbound email connections - this is normal. The second line is sendmail "caught" at the moment of sending an email (as userid "mail") from your machine to a hotmail server - that is also perfectly normal. You may see similar lines with "exim" or "postfix" or "smtpd" or "qmail" instead of sendmail - all depending on what mail server you run - example - the third line is an Exim listener. The important thing that indicates that it's normal is that the userid is "mail" or "mailman" or something like that - **NOT** an ordinary user.

The fourth line is a program called "find", running under userid "foo" making a connection to an AOL server.

It's examples like the fourth line you're looking for - it tells you the userid of the infected user. In this case it also indicates that the infection is masquerading as the program "find". There will often be more than one of these.

Simply killing these processes is **NOT** enough, because they will often restart on their own. You will need to find whether these are started by a cron job owned by that user, or, spawned through your web server, or started from a ssh login. Find and delete the program - often a PHP or Perl script. In some cases, however, the program deletes itself as soon as it starts. The "find" example above is a Linux binary executable that contains an encrypted perl script. Since this was first written, it now sometimes masquerades as "mail" or "ntpd". Assume it could be anything. You will also need to find out how the script got installed on your machine - often through Joomla, Wordpress, Cpanel or Plesk security holes, or ftp upload and secure it.

**WARNING** Just because you didn't find a line like the "foo" line above doesn't mean the machine is not infected! It just means that the machine is not sending email at the instant lsof was run. If you don't see a line like the "foo" line, we suggest that you run the lsof command multiple times. Example:

```
while true
do
    sudo lsof -i | grep smtp
    sleep 10
done

```

### Finding the problem by finding the script: Linux/FreeBSD

Try the [findbot.pl](http://cbl.abuseat.org/findbot.pl) program. It's a relatively straight-forward Perl script that will find most of the malicious scripts that we are aware of. The beginning of the file contains instructions on how to use it. If you are not the administrator of the system, it will not work for you.

Many of these infections start themselves running, and then delete themselves from disk. Which means you won't be able to find it. Check your ftp and SSH logs for suspicious files and logins. This is why it's so important to prevent it happening again.

### Finding the problem by network activity: Windows

The Windows environment is rather less developed for finding these things than UNIX-like systems. However, we can recommend the tcpview tool, so please see [tcpview/tcpconn](http://cbl.abuseat.org/advanced.html#tcpview) in our advanced section.

### Finding the problem by logs: (Mostly) Linux/FreeBSD

Most of these scripts are quite good at hiding their presence. Some of them start up, and them remove the on-disk copy, so there's nothing to see. None of them volunteer where they are, so samples don't help. Most of these scripts bypass your mail server software, so there is nothing to see in the mail logs or queues.

However, they all do need to get on your system somehow, and that often leaves logs. If you can find those log records, often that will help you identify the infected user and find the malicious files (if they are still there).

Generally speaking, these are the ways malicious scripts get onto a system:

- Web sites often make FTP or SSL available so their customers can upload content or log in to manage their web pages. If the customer's computer is compromised with a keylogger, it means that the criminal can upload anything they want. You can usually see this activity in your FTP or SSL logs - look for uploads of .php or .pl files, lots of oddly named files, access from a large variety of IP addresses, etc. If you do find something like this, it's important to get the user to change their password, and do virus scans of their computers.
- Check your web server for large quantities of requests to the same PHP or CGI or Perl file, or POST commands, etc... This can reveal where the infection is, and often how it got there.
- Most CMSes, in particular, Plesk, CPanel, Wordpress and Joomla quite simply have severe security holes being found in them, seemingly daily, and hosted environments are often reluctant to keep up to date with their patching. You may never find a reasonable explanation of how the malicious software got there

### Preventing it Happening Again

- Make absolutely certain that ALL CMS software (Joomla, Cpanel, Wordpress, Plesk etc) is kept up to date at all times. Do not let your users make any excuses for not doing so.
- Make it impossible for such infections (and they will happen again) to spam the world by implementing the blocking of email sent direct from the machine without going through your mail server.Some of your customers may believe that they need to be allowed to do this. The best answer for them is to configure their software to relay it through the mail server software on the machine or to an external smart-host.

  For blocking: With Cpanel you can use ConfigServer Security Firewall (CSF). It's free. CSF has the "SMTP\_BLOCK" configuration option - turn it on.

  Basic Cpanel, there's also "WHM SMTP Tweak" would should also help.

  The following is an equivalent for non-Cpanel installations - it permits local mail submission and blocks external mail submission:

  ```
  iptables -A OUTPUT -d 127.0.0.1 -p tcp -m tcp --dport 25 -j ACCEPT
  iptables -A OUTPUT -p tcp -m tcp --dport 25 -m owner --gid-owner mail -j ACCEPT
  iptables -A OUTPUT -p tcp -m tcp --dport 25 -m owner --gid-owner mailman -j ACCEPT
  iptables -A OUTPUT -p tcp -m tcp --dport 25 -m owner --uid-owner root -j ACCEPT
  iptables -A OUTPUT -p tcp -m tcp --dport 25 -j REJECT --reject-with icmp-port-unreachable

  ```

  The above permits users to send mail via a local mail server, permits local mail server software (running under userid root, or gid mail or mailman) to send email to the Internet, but prevents any ordinary user making direct SMTP connections to the Internet. You may have to adjust this for Qmail or Exim. Check which userids are used. Note that the iptables settings will probably be lost next time you reboot. The iptables commands should be installed into a system init script.

  If you're using cPanel and APF, APF by default will wipe out iptables rules you enter manually leaving the server vulnerable. If you are using APF, you should make the above change via APF and that will take care of reissuing the commands upon reboot or reset.
- Do you really need PHP script support? CGI support? PHP mail functions? Turn off the ones you don't need. Some people, for example, turn off CGIs, and PHP "fsocketopen" or "exec" functions in the PHP ini files (either for the whole site, or individual environments), and manage to inhibit many infections.
- Some of these scripts get installed into /tmp. If /tmp is a separate file system, you can stop it being used by malicious scripts by adjusting the /etc/fstab file to mount /tmp with the "noexec" and "nosuid" flags. This means that the O/S will not run programs that are in the /tmp directory nor treat them as setuid.
- Turn off customer FTP if you don't need it. Note that some CMS packages install FTP with anonymous FTP turned on by default. This is ALWAYS a bad idea, so make sure "anonymous login" is turned off.
- It is necessary to force password changes on those users whose web sites have been compromised. If you can't tell exactly which users have been compromised, it's strongly recommended you change all passwords.
