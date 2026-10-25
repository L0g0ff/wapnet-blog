---
_oembed_7f852c7d50e8b5467afed5b0b247c9d3: <iframe title="Nvidia Fuck You! (Linus Torvalds) My thoughts exactly" width="840" height="473" src="https://www.youtube.com/embed/i2lhwb_OckQ?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
_oembed_18a8ee373c5da0c2a2312f915c1d2396: <iframe title="Screen Tearing Test" width="840" height="473" src="https://www.youtube.com/embed/MfL_JkcEFbE?feature=oembed" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
_oembed_time_7f852c7d50e8b5467afed5b0b247c9d3: "1626787575"
_oembed_time_18a8ee373c5da0c2a2312f915c1d2396: "1626787575"
_thumbnail_id: "1919"
author: thomasf
categories:
  - gaming
  - linux
  - video
cover:
  alt: Screenshot_20210527_235205
  image: /wp-content/uploads/2021/05/Screenshot_20210527_235205.png
date: "2021-05-27T22:01:11+00:00"
guid: https://blog.wapnet.nl/?p=1910
parent_post_id: null
post_id: "1910"
title: Fix Screen Tearing in Linux
url: /2021/05/fix-screen-tearing-in-linux/

---
It cost me a lot of time to troubleshoot the screen tearing. So I want to share my solution for everyone with the same frustrating tearing issues. My private setup is a Lenovo Ideapad (gaming) with Nvidia and Intel (Prime) GPU. I use the laptop screen and an external 24" HDMI display.

In Windows 10 everything goes smooth but when I switch my dual boot to Linux than the frustrations begin.

I tried a lot of different Linux distributions (Fedora, Solus, Ubuntu, Pop\_OS!, Arch Linux, OpenSuse, and Zorin OS) and I try KDE Plasma, Gnome, and Budgie a lot of hacks for all these systems to get a smooth Linux GUI without screen tearing or other lag.

But I don't like manual modifications/hacks to get the Nvidia setup smooth. Especially the proprietary Nvidia drivers can break your system easily. So this fix is easy to remember and easy to switch if you want the power saver back to full and use the Intel driver instead of the Nvidia one.

## Important, choose your display!

What you have to keep in mind when you have a lot of screen tearing is to make a decision. Use your laptop display **or** external display. You can fix both displays but not at the same time in a smooth way. If I found a solution in the feature I will post it on my blog. But in the meanwhile, I use only one screen at the same time.

This procedure is for Ubuntu 20.04 LTS but it will work for other distributions for sure.

## Install the driver

After a fresh ubuntu installation, Nvidia and HDMI do not work as they should be. So, kick off the first command and reboot.

`$ sudo ubuntu-drivers autoinstall`

And reboot!  

## Configure Nvidia driver Part I

Now configure the Nvidia/Intel prime in on-demand mode. So you can do further configuration in the nvidia-settings gui

`$ sudo prime-select on-demand`

- And reboot again
- Now start Nvidia settings and switch to NVIDIA (Performance Mode)

{{< figure src="/wp-content/uploads/2021/05/image.png" alt="" caption="" >}}

- Click save and..... reboot!

## Turn off one display

Go to your KDE or Gnome display settings and turn off one display. KDE saves these settings so when you plug out the HDMI cable afterward KDE will activate your laptop display. And of course, when you plug in your HDMI cable next time he will turn off your laptop display.

{{< figure src="/wp-content/uploads/2021/05/image-2.png" alt="" caption="" >}}

## Configure Nvidia driver Part II

These steps are optional but needed for a better performance.

- Start nvidia-settings > GPU 0 > PowerMixer
- Change the Preffered Mode to "Prefer Maximum Performance"

{{< figure src="/wp-content/uploads/2021/05/image-3.png" alt="" caption="" >}}

## Last but not least: Firefox hardware rendering

For some compatibility reasons, hardware rendering in Firefox is turned off by default. So you have to enable it.

- about:config
- Set layers.acceleration.force-enabled to true

{{< figure src="/wp-content/uploads/2021/05/image-1.png" alt="" caption="" >}}

- Quit Firefox and restart it

## Some debug information

I always use this YouTube video to check if the screen tearing is varnished completely

https://youtu.be/MfL\_JkcEFbE

When you want to see if your have the right drivers loaded, use this command:

`$ lspci -k | grep -EA3 'VGA|3D|Display'`

{{< figure src="/wp-content/uploads/2021/05/image-4.png" alt="" caption="" >}}

And you can start an application with max video power with this command. Change gears to your own program off course. But I like gears because you can see the FPS realtime (see the screen what a differance ;) )

`$ __NV_PRIME_RENDER_OFFLOAD=1 glxgears`

{{< figure src="/wp-content/uploads/2021/05/image-9.png" alt="" caption="" >}}

With `nvidia-smi ` you can see if nvidia is running the application

{{< figure src="/wp-content/uploads/2021/05/image-8.png" alt="" caption="" >}}

Enjoy your tearing free Linux :)

/edit

Hahaha I saw this video today :) Exactly my thoughts

{{< youtube i2lhwb\_OckQ >}}
