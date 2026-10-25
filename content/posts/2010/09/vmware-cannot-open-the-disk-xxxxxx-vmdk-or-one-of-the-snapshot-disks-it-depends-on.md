---
_edit_last: "1"
_wp_old_slug: vmware-%e2%80%9ccannot-open-the-disk-%e2%80%98xxxxxx-vmdk%e2%80%99-or-one-of-the-snapshot-disks-it-depends-on-%e2%80%9d
author: thomasf
categories:
  - vmware
date: "2010-09-13T09:12:33+00:00"
dsq_thread_id: "5150434925"
guid: https://blog.wapnet.nl/?p=408
parent_post_id: null
post_id: "408"
title: VMware “Cannot open the disk ‘XXXXXX.vmdk’ or one of the snapshot disks it depends on.”
url: /2010/09/vmware-cannot-open-the-disk-xxxxxx-vmdk-or-one-of-the-snapshot-disks-it-depends-on/

---
Source: [http://www.ardamis.com/2009/11/20/vmware-cannot-open-the-disk-xxxxxx-vmdk-or-one-of-the-snapshot-disks-it-depends-on/](http://www.ardamis.com/2009/11/20/vmware-cannot-open-the-disk-xxxxxx-vmdk-or-one-of-the-snapshot-disks-it-depends-on/)

From time to time, I want to copy just the minimum files for a VMware virtual machine: the two .vmdk files and the .vmx file. After moving those files to a new location or deleting a snapshot file, attempting to boot the virtual machine returns the following error message:

Cannot open the disk ‘XXXXXX.vmdk’ or one of the snapshot disks it depends on.
Reason: The system cannot find the file specified.

I’ve found that following the steps below fixes the problem and allows me to boot the virtual machine as it existed at the time of creation. DO NOT USE these steps if you need to retain any changes to the machine:

Open the \*.vmx file in a text editor and find the line that refers to the old snapshot file, which will look something like:
scsi0:0.fileName = “XXXXXX-000002.vmdk”
or
ide0:0.fileName = “XXXXXX-000002.vmdk”

Change the value to the filename of the ~1kb .vmdk file (which happens to be the same as the name of the VM). For example, if your virtual machine was named “Windows XP Professional”, the line would read:

scsi0:0.fileName = “Windows XP Professional.vmdk”

Power on the VM. It should boot normally, but because the snapshot file is missing, the machine will boot to an earlier state.
