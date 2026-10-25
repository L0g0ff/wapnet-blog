---
author: thomasf
categories:
  - linux
date: "2025-04-01T16:38:09+00:00"
guid: https://blog.wapnet.nl/?p=2237
parent_post_id: null
post_id: "2237"
title: NCDU Shell tool with GUI for cleanup your disk
url: /2025/04/ncdu-shell-tool-with-gui-for-cleanup-your-disk/

---
When managing disk space, having a quick and efficient tool at your fingertips can be a game-changer. Enter **ncdu**—a lightweight, terminal-based disk usage analyzer that provides an interactive and visual overview of your file system directly from the command line.

## What Is ncdu?

ncdu (NCurses Disk Usage) is a command-line utility that scans your directories and files to show you exactly where your disk space is being used. With its ncurses-based interface, ncdu offers an intuitive way to navigate through large file systems, making it easier to identify and clean up space hogs.

{{< figure src="/wp-content/uploads/2025/04/image.png" alt="" caption="" >}}

## Key Features

- **Interactive Interface:** ncdu’s interface allows you to navigate your file system interactively, making it simple to explore directories and drill down into the details.
- **Fast Scanning:** It quickly scans directories and provides a detailed breakdown of disk usage, saving you time compared to traditional methods.
- **Simple Navigation:** With easy-to-use keyboard commands, you can move through the file hierarchy, delete unwanted files, and even sort directories by size.

{{< figure src="/wp-content/uploads/2025/04/image-1.png" alt="" caption="" >}}

## How to Get Started

### Installation

ncdu is available in many package managers. Here’s how to install it on some popular platforms:

- **Debian/Ubuntu:** `sudo apt-get install ncdu`
- **Fedora:** `sudo dnf install ncdu`
- **Arch Linux:** `sudo pacman -S ncdu`

If you’re on macOS and have installed ncdu via Homebrew, remember that the binary might be in a user-specific directory. To run it as sudo, you might need to use the full path:

```
sudo /usr/local/bin/ncdu

```

or preserve your environment with:

```
sudo -E ncdu

```

### Using ncdu

Once installed, simply run:

```
ncdu

```

By default, ncdu will scan the current directory. To scan a specific directory, specify its path:

```
ncdu /path/to/directory

```

Within the interface, you can navigate using arrow keys, view the size of directories and files, and even delete files directly by pressing the `d` key.

## Why Use ncdu?

For developers, system administrators, or anyone looking to keep their system tidy, ncdu is an invaluable tool. Its blend of speed, simplicity, and interactive design makes it ideal for quickly identifying large files and unnecessary clutter on your system.

In a world where disk space is precious, ncdu helps you maintain control and ensure your system runs smoothly without the hassle of sifting through countless files manually.

Happy disk cleaning!
