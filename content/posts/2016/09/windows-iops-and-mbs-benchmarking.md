---
_disable_fbc: ""
_edit_last: "1"
_thumbnail_id: "1699"
author: thomasf
categories:
  - hardware
  - sql
  - windows
cover:
  alt: overheating_computer
  image: /wp-content/uploads/2016/09/Overheating_Computer.jpg
date: "2016-09-11T10:05:08+00:00"
dsq_thread_id: "5136185696"
guid: https://blog.wapnet.nl/?p=1696
parent_post_id: null
post_id: "1696"
title: Windows IOPS and MB/s benchmarking
url: /2016/09/windows-iops-and-mbs-benchmarking/

---
You have bought een new system and the first thing what you want to do is check the disk performance (ehhh that's always the first thing I want to know :P )

There  is one tool I always use: [ATTO Disk Benchmark](https://www.attotech.com/disk-benchmark/) [![disk-benchmark](/wp-content/uploads/2016/09/disk-benchmark.png)](/wp-content/uploads/2016/09/disk-benchmark.png)

This is a very nice tool to quickly see how fast your troughput is of your new system.

But sometimes you want to check your IOPS. Then you can use another nice microsoft commandline benchmark tool [DiskSpd](https://gallery.technet.microsoft.com/DiskSpd-a-robust-storage-6cd2f223)

You can use this parameter to benchmark:
`
diskspd -b8K -d30 -o4 -t8 -h -r -w25 -L -Z1G -c20G testfile.dat
`

This example command line will run a 30 second random I/O test using a 20GB test file located on the T: drive, with a 25% write and 75% read ratio, with an 8K block size. It will use eight worker threads, each with four outstanding I/Os and a write entropy value seed of 1GB. It will save the results of the test to a text file called DiskSpeedResults.txt. This is a pretty good set of parameters for a SQL Server OLTP workload.

Example:

[![diskspd](/wp-content/uploads/2016/09/DiskSpd.png)](/wp-content/uploads/2016/09/DiskSpd.png)[Orginal article](http://sqlperformance.com/2015/08/io-subsystem/diskspd-test-storage)

If you get errors like:

`Results for timespan 1:
*******************************************************************************
The test was interrupted before the measurements began. No results are displayed.
Error generating I/O requests`

Or file creation errors like " **Error opening file: testfile.dat**" please try to replace the minus "-" characters with your keyboard. Sometimes your browser copy the wrong character.

Happy benchmarking :D
