---
_edit_last: "1"
author: thomasf
categories:
  - linux
date: "2013-12-28T13:57:30+00:00"
dsq_thread_id: "5160233101"
guid: https://blog.wapnet.nl/?p=1474
parent_post_id: null
post_id: "1474"
title: IPtables howto
url: /2013/12/iptables-howto/

---
_I copy/paste this howto from the debian wiki @ [https://wiki.debian.org/iptables](https://wiki.debian.org/iptables) and add this to my blog to for fast finding the best iptables article on the net._ Iptables provides packet filtering, network address translation (NAT) and other packet mangling.

Two of the most common uses of iptables is to provide firewall support and NAT.

Configuring iptables manually is challenging for the uninitiated. Fortunately, there are many configuration tools (wizards) available to assist: e.g., [fwbuilder](http://packages.debian.org/fwbuilder "DebPkg"), [bastille](http://packages.debian.org/bastille "DebPkg"), [ferm](http://packages.debian.org/ferm "DebPkg") ([wiki page](https://wiki.debian.org/ferm)), [ufw](http://packages.debian.org/ufw "DebPkg") (Uncomplicated Firewall, from Ubuntu).

## Viewing current configuration

See what rules are already configured. Issue this command:

```
 iptables -L
```

The output will be similar to this:

```
 Chain INPUT (policy ACCEPT)
 target     prot opt source               destination

 Chain FORWARD (policy ACCEPT)
 target     prot opt source               destination

 Chain OUTPUT (policy ACCEPT)
 target     prot opt source               destination
```

This allows anyone access to anything from anywhere.

## Storing iptables rules in a file

Note: there is a package designed to help with this: [iptables-persistent](http://packages.debian.org/iptables-persistent "DebianPkg")

Let's tighten that up a bit by creating a test iptables file:

```
 nano /etc/iptables.test.rules
```

In this file enter some basic rules:

```
*filter

# Allows all loopback (lo0) traffic and drop all traffic to 127/8 that doesn't use lo0
-A INPUT -i lo -j ACCEPT
-A INPUT ! -i lo -d 127.0.0.0/8 -j REJECT

# Accepts all established inbound connections
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allows all outbound traffic
# You could modify this to only allow certain traffic
-A OUTPUT -j ACCEPT

# Allows HTTP and HTTPS connections from anywhere (the normal ports for websites)
-A INPUT -p tcp --dport 80 -j ACCEPT
-A INPUT -p tcp --dport 443 -j ACCEPT

# Allows SSH connections
# THE -dport NUMBER IS THE SAME ONE YOU SET UP IN THE SSHD_CONFIG FILE
-A INPUT -p tcp -m state --state NEW --dport 30000 -j ACCEPT

# Now you should read up on iptables rules and consider whether ssh access
# for everyone is really desired. Most likely you will only allow access from certain IPs.

# Allow ping
-A INPUT -p icmp -m icmp --icmp-type 8 -j ACCEPT

# log iptables denied calls (access via 'dmesg' command)
-A INPUT -m limit --limit 5/min -j LOG --log-prefix "iptables denied: " --log-level 7

# Reject all other inbound - default deny unless explicitly allowed policy:
-A INPUT -j REJECT
-A FORWARD -j REJECT

COMMIT
```

That may look complicated, but look at each section at a time. You will see that it simply shuts all ports except the ones we have allowed - which in this case are ports 80 and 443 (the standard web browser ports) and the SSH port defined earlier.

Activate these new rules:

```
 iptables-restore < /etc/iptables.test.rules
```

And see the difference:

```
 iptables -L
```

Now the output tells us that only the ports defined above are open. All the others are closed.

Once you are happy, save the new rules to the master iptables file:

```
 iptables-save > /etc/iptables.up.rules
```

To make sure the iptables rules are started on a reboot we'll create a new file:

```
 nano /etc/network/if-pre-up.d/iptables
```

or in the the if-up.d if the if-pre-up.d not work

```
nano /etc/network/if-up.d/iptables
```

Add these lines to it:

```
 #!/bin/bash
 /sbin/iptables-restore < /etc/iptables.up.rules
```

The file needs to be executable so change the permissions:

```
 chmod +x /etc/network/if-pre-up.d/iptables
```
