---
author: thomasf
categories:
  - uncategorized
date: "2024-05-27T20:00:10+00:00"
guid: https://blog.wapnet.nl/?p=2174
parent_post_id: null
post_id: "2174"
title: NixOS and Sway
url: /2024/05/nixos-and-sway/

---
Currently, I am experimenting with NixOS and Sway. NixOS is a Linux operating system that allows you to build and manage your system using a single configuration file. Sway is a tiling window manager designed for Wayland, offering a dynamic and efficient workspace.

This article is a work in progress. I plan to share my setup and configuration details, but for now, this article serves as a draft to document my journey.

I am aware of tools like flakes and Home Manager, but my current goal is to explore and understand NixOS without using these mechanisms.

## Sway

### Config displays

Use `wdisplays`. This is a nice graphical tool for wayland to configure and outline your displays

Use `swaymsg -t get_outputs` to get all the display settings

#### Example config for 3 displays

```
# Config eDP-1
output eDP-1 {
    mode 2256x1504@59.999Hz
    pos 5247 0
    scale 1.375
    scale_filter linear
    transform normal
    max_render_time off
    adaptive_sync disabled
}

# Config DP-3
output DP-3 {
    mode 1920x1080@60.000Hz
    pos 8808 0
    scale 1.0
    scale_filter nearest
    transform normal
    max_render_time off
    adaptive_sync disabled
}

# Config DP-4
output DP-4 {
    mode 1920x1080@60.000Hz
    pos 6888 0
    scale 1.0
    scale_filter nearest
    transform normal
    max_render_time off
    adaptive_sync disabled
}

# Workspace assign
workspace 1 output eDP-1
workspace 2 output DP-4
workspace 3 output DP-3
```

### Terminal (foot)

Configure the font

```
$ touch ~/.config/foot/foot.ini
$ nano ~/.config/foot/foot.ini

[main]
font = monospace:size=14
```

### Sway shortcuts (cheatsheet)

- `Mod + w` = Tabbed view
- `Mod + e` = Normal view
- `Mod + w` = Tabbed view
- `Mod + d` = Application menu
- `Mod+Shift+e` = Restart Sway

## NixOS

### Packages

```
environment.systemPackages = with pkgs; [
vim
wget
firefox-wayland
spotify
steam
todoist-electron
gimp
pinta
gedit
keepassxc
synology-drive-client
vscode
dolphin
libsForQt5.kdeconnect-kde
killall
networkmanager
git
kitty
powershell
networkmanagerapplet
gnome.gnome-keyring
blueman
gnome.gnome-bluetooth
bluez
bluez-tools
pkgs.libsForQt5.bismuth # KDE Tiling
upower # nodig voor power management (firefox)
];
```
