---
author: thomasf
categories:
  - linux
date: "2008-03-25T19:38:32+00:00"
dsq_thread_id: "5136177216"
guid: https://blog.wapnet.nl/?p=32
parent_post_id: null
post_id: "32"
title: 'Getlibs: Automatically solves dependencies for 32-bit programs on 64-bit'
url: /2008/03/getlibs-automatically-solves-dependencies-for-32-bit-programs-on-64-bit/

---
Today i found an real life / time saving debian/ubuntu tool. The name of the tool is getlibs. This tool automatically find the libs and install these. In the past I have search my ass off to find the correct debian libs. Now this problem is (hopefully) fixed 4ever! :D

**On 64-bit systems it downloads and installs libraries needed for 32-bit programs and 64-bit programs.**
**On 32-bit systems it downloads and installs libraries needed for 32-bit programs.**

Thank you to the following bug reporters: marararam ViRMiN Cabal elanthis BogusJoe NullHead mooball
Thank you to the following Beta Testers: Kilz BogusJoe NullHead
Special thanks to: RavanH

**To install or upgrade:** [http://www.boundlesssupremacy.com/Ca...etlibs-all.deb](http://www.boundlesssupremacy.com/Cappy/getlibs/getlibs-all.deb)
Download and double click the file to install.

\-\-\---

View the source without installing the package:
[http://www.boundlesssupremacy.com/Cappy/getlibs/getlibs](http://www.boundlesssupremacy.com/Cappy/getlibs/getlibs) **getlibs works on:**

- All Ubuntu and Debian systems
- Debian or Ubuntu based distributions (best to use the package name)

Tip: To install a 32-bit debian package for a program (not a library!) use

Code:

```
sudo dpkg -i --force-all package_name.deb
```

**Usage Examples:**

getlibs on a program to download all missing libraries:

Code:

```
getlibs /usr/bin/skype
```

\-\-\---

Use getlibs to install a 32-bit library using the library name:

Code:

```
getlibs -l libogg.so.0 libSDL-1.2.so.0
```

\-\-\---

Use getlibs to install a 32-bit library using the package name:

Code:

```
getlibs -p libqt4-core libqt4-gui
```

\-\-\---

Install a 32-bit library file (.deb):

Code:

```
getlibs -i ~/i386_library_1.deb
```

\-\-\---

Download and install a 32-bit library file (.deb):

Code:

```
getlibs -w http://mirrors.kernel.org/ubuntu/pool/main/s/sdl-image1.2/libsdl-image1.2_1.2.5-3_i386.deb
```

\-\-\---

**Other options:**

--apt-file : Uses apt-file to find the packagenames for libraries. The default uses packages.ubuntu.com. This is especially useful for non-ubuntu users.

--build : converts a 32-bit package to a 64-bit package and installs it. This will only install libraries from a 32-bit package into the correct place! This will not install any binaries from that package! This is very beta.

--savebuild : use with --build. Saves new 64-bit package to /home/$USER

--mirror or -m : Use the specified mirror to download from if one is not specified for package

--verbose : Extra output

--ldconfig : Runs ldconfig on directories where new libraries are installed

-64 : Will let apt-get install 64-bit packages for a 64-bit system

-32 : Left only for compatibility with getlibs v1. 32-bit library installation is the default for all systems.

--distro : can set as either Ubuntu or Debian. Ubuntu installs to /usr/lib32 and/or /lib32. Debian installs to /emul/ia32-linux/

--release : can set as hardy gutsy feisty edgy or dapper. Determines what web interface release is used in search.

Source: [http://ubuntuforums.org/showthread.php?t=474790](http://ubuntuforums.org/showthread.php?t=474790)
