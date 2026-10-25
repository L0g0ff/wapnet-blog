---
_edit_last: "1"
author: thomasf
categories:
  - linux
date: "2009-08-14T14:58:31+00:00"
dsq_thread_id: "5142675739"
guid: https://blog.wapnet.nl/?p=203
parent_post_id: null
post_id: "203"
title: NTP Troubleshooting
url: /2009/08/ntp-troubleshooting/

---
# Download and Install The NTP Package

Most RedHat and Fedora Linux software products are available in the RPM format. Downloading and installing RPMs isn't hard. If you need a refresher, Chapter 6, "[Installing Linux Software](/wiki/index.php/Quick_HOWTO_:_Ch06_:_Installing_Linux_Software "Quick HOWTO : Ch06 : Installing Linux Software")", has all the details.

When searching for the file, remember that the NTP RPM's filename usually starts with the word ntp followed by a version number as in ntp-4.1.2-5.i386.rpm.

# The /etc/ntp.conf File

The /etc/ntp.conf file is the main configuration file for Linux NTP in which you place the IP addresses of the stratum 1 and stratum 2 servers you want to use. Here are the steps to create a configuration file using a pair of sample Internet-based NTP servers:

1) First we specify the servers you're interested in:

```
server  otherntp.server.org    # A stratum 1 server at server.org
server  ntp.research.gov       # A stratum 2 server at research.gov
```

2) Restrict the type of access you allow these servers. In this example the servers are not allowed to modify the run-time configuration or query your Linux NTP server.

```
restrict otherntp.server.org   mask 255.255.255.255 nomodify notrap noquery
restrict ntp.research.gov      mask 255.255.255.255 nomodify notrap noquery
```

The mask 255.255.255.255 statement is really a subnet mask limiting access to the single IP address of the remote NTP servers.

3) If this server is also going to provide time for other computers, such as PCs, other Linux servers and networking devices, then you'll have to define the networks from which this server will accept NTP synchronization requests. You do so with a modified restrict statement removing the noquery keyword to allow the network to query your NTP server. The syntax is:

```
restrict 192.168.1.0 mask 255.255.255.0 nomodify notrap
```

In this case the mask statement has been expanded to include all 255 possible IP addresses on the local network.

4) We also want to make sure that localhost (the universal IP address used to refer to a Linux server itself) has full access without any restricting keywords:

```
restrict 127.0.0.1
```

5) Save the file and restart NTP for these settings to take effect. You can now configure other Linux hosts on your network to synchronize with this new master NTP server in a similar fashion.

# How To Get NTP Started

You have to restart the NTP process every time you make a change to the configuration file for the changes to take effect on the running process.

To get NTP configured to start at boot, use the line:

```
[root@bigboy tmp]# chkconfig ntpd on
```

To start, stop and restart NTP after booting, follow these examples:

```
[root@bigboy tmp]# service ntpd start
[root@bigboy tmp]# service ntpd stop
[root@bigboy tmp]# service ntpd restart
```

Testing And Troubleshooting NTP

After configuring and starting NTP, you should test it to make sure it is working. Here are some guidelines you can follow to get NTP working correctly.

## Verifying NTP is Running

To test whether the NTP process is running use the command

```
[root@bigboy tmp]# pgrep ntpd
```

You should get a response of plain old process ID numbers.

## Doing An Initial Synchronization

If the time on the local server is very different from that of its primary time server your NTP daemon will eventually terminate itself leaving an error message in the /var/log/messages file. You should run the ntpdate -u command to force your server to become instantly synchronized with its NTP servers before starting the NTP daemon for the first time. The ntpdate command doesn't run continuously in the background, you will still have to run the ntpd daemon to get continuous NTP updates.

Take a look at some sample output of the ntpdate command in which a server whose initial time was set to midnight, was correctly set to 8:03 am.

- The date was originally set to midnight which was verified by using the date command.

```
[root@smallfry tmp]# date
Thu Aug 12 00:00:00 PDT 2004
[root@smallfry tmp]#
```

- The ntpdate command is run three times to synchronize smallfry's clock to server 192.168.1.100, but it must be run while the ntpd process is stopped. So you'll have to stop ntpd, run ntpdate and then start ntpd again.

```
[root@smallfry tmp]# service ntpd stop
[root@smallfry tmp]# ntpdate -u 192.168.1.100
Looking for host 192.168.1.100 and service ntp
host found : bigboy.my-site.com
12 Aug 08:03:38 ntpdate[2472]: step time server 192.168.1.100 offset 28993.084943 sec
[root@smallfry tmp]# ntpdate -u 192.168.1.100
Looking for host 192.168.1.100 and service ntp
host found : bigboy.my-site.com
12 Aug 08:03:40 ntpdate[2472]: step time server 192.168.1.100 offset 2.467652 sec
[root@smallfry tmp]# ntpdate -u 192.168.1.100
Looking for host 192.168.1.100 and service ntp
host found : bigboy.my-site.com
12 Aug 08:03:42 ntpdate[2472]: step time server 192.168.1.100 offset 0.084943 sec
[root@smallfry tmp]# service ntpd start
[root@smallfry tmp]#
```

- The date is now corrected.

```
[root@smallfry tmp]# date
Thu Aug 12 08:03:45 PDT 2004
[root@smallfry tmp]#
```

## Determining If NTP Is Synchronized Properly

Use the ntpq command to see the servers with which you are synchronized. It provided you with a list of configured time servers and the delay, offset and jitter that your server is experiencing with them. For correct synchronization, the delay and offset values should be non-zero and the jitter value should be under 100.

```
[root@bigboy tmp]# ntpq -p
```

Here is some sample output of the command:

```
     remote          refid       st t when poll reach  delay   offset   jitter
==============================================================================
-jj.cs.umb.edu   gandalf.sigmaso  3 u   95 1024  377  31.681  -18.549    1.572
milo.mcs.anl.go  ntp0.mcs.anl.go  2 u  818 1024  125  41.993  -15.264    1.392
-mailer1.psc.edu ntp1.usno.navy.  2 u  972 1024  377  38.206   19.589   28.028
-dr-zaius.cs.wis ben.cs.wisc.edu  2 u  502 1024  357  55.098    3.979    0.333
+taylor.cs.wisc. ben.cs.wisc.edu  2 u  454 1024  347  54.127    3.379    0.047
-ntp0.cis.strath harris.cc.strat  3 u  507 1024  377 115.274   -5.025    1.642
*clock.via.net   .GPS.            1 u  426 1024  377 107.424   -3.018    2.534
ntp1.conectiv.c  0.0.0.0         16 u    - 1024    0   0.000    0.000  4000.00
```

## Your Linux NTP clients cannot Synchronize Properly

A telltale sign that you haven't got proper synchronization is when all the remote servers have jitter, delay and reach values of 0. In some older versions of Fedora, the jitter values will be 4000.

```
    remote           refid      st t when poll reach   delay   offset  jitter
=============================================================================
LOCAL(0)        LOCAL(0)        10 l    -   64    7    0.000    0.000   0.008
ntp-cup.externa 0.0.0.0         16 u    -   64    0    0.000    0.000   0.000
snvl-smtp1.trim 0.0.0.0         16 u    -   64    0    0.000    0.000   0.000
nist1.aol-ca.tr 0.0.0.0         16 u    -   64    0    0.000    0.000   0.000
```

This could be caused by the following:

- Older versions of the NTP package that don't work correctly if you use the DNS name for the NTP servers. In these cases you will want to use the actual IP addresses instead.
- A firewall blocking access to your Stratum 1 and 2 NTP servers. This could be located on one of the networks between the NTP server and its time source, or firewall software such as iptables could be running on the server itself.
- The notrust nomodify notrap keywords are present in the restrict statement for the NTP client. In some versions of the Fedora Core 2's implementation of NTP, clients will not be able to synchronize with a Fedora Core 2 time server unless the notrust nomodify notrap keywords are removed from the NTP client's restrict statement.

In this example the restrict statement has only the client network defined without any keywords and the configuration line that works with other NTP versions has been commented out:

```
# -- CLIENT NETWORK -------
#restrict 172.16.1.0 mask 255.255.255.0 notrust nomodify notrap
restrict 172.16.1.0 mask 255.255.255.0
```
