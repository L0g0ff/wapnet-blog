---
_edit_last: "1"
_syntaxhighlighter_encoded: "1"
Hide OgTags: "0"
Hide SexyBookmarks: "0"
author: thomasf
categories:
  - vmware
date: "2013-04-08T22:39:33+00:00"
dsq_thread_id: "5137079854"
guid: https://blog.wapnet.nl/?p=1024
parent_post_id: null
post_id: "1024"
title: Force shutdown or kill a stuck VMWare virtual machine
url: /2013/04/force-shutdown-or-kill-a-stuck-vmware-virtual-machine/

---
Sometimes when a LUN is full a VM cannot shutdown properly

- Make a SSH connection to the host where the VM running at
- Login as root
- list all running VM's


```
# vmware-cmd -l
```


- Get the current state


```
# vmware-cmd /vmfs/volumes/<UUID>/<VMDIR>/<VMNAME>.vmx getstate
```


- Output:


```
[root@esx ~]# vmware-cmd /vmfs/volumes/<UUID>/<VMDIR>/<VMNAME>.vmx getstate
getstate() = stuck
```


- Now you know for sure the status is stuck you can kill the VM


```
ps auxwww |grep -i <VMNAME>.vmx</span>
```


- Output:


```
root 3093 0.0 0.3 2016 860 ? S< Jul30 0:17 /usr/lib/vmware/bin/vmkload_app /usr/lib/vmware/bin/vmware-vmx -ssched.group=host/user -# name=VMware ESX Server;version=3.5.0;licensename=VMware ESX Server;licenseversion=2.0 build-158874; -@ pipe=/tmp/vmhsdaemon-0/vmx569228e44baf49d1; /vmfs/volumes/49392e30-162037d0-17c6-001f29e9abec/<VMDIR>/<VMNAME>.vmx
```


- The code right after root is the PID you must kill.
- First try only kill


```
#kill 3093
```


- Wait 30 seconds and try a getstate again:


```
# vmware-cmd /vmfs/volumes/<UUID>/<VMDIR>/<VMNAME>.vmx getstate
```


- If the state is "off" your ready. If the state is still stuck try the following:


```
#kill -9 3093
```


- Wait 30 seconds and see the state is "off" now.

If the state is still "stuck" migrate all VM's to another host en reboot the host.

When the VM is off by the kill command HA (High Availability) will power on the host automaticly. Now power down the server during the boot trough the VMWare GUI. If the VM is off try to remove snapshots, (re) move disks, or fix the thing who cause the crash.

Source: [VMware KB 1004340](http://kb.vmware.com/selfservice/microsites/search.do?language=en_US&cmd=displayKC&externalId=1004340)

```

```
