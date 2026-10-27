---
title: "KompassOS-DAWO: Building on the Dutch Government's NixOS Desktop"
date: 2026-10-08T12:00:00+02:00
url: /2026/10/kompassos-dawo-building-on-the-dutch-governments-nixos-desktop/
author: Thomas Faddegon
categories:
  - linux
tags:
  - linux
  - howto
cover:
  image: cover.jpg
  alt: Flat illustration of a dark-themed desktop monitor with a large compass and a snowflake-like hexagonal lattice in front of it, in white, gray and lime green
---
**The Goal**

The Dutch government is building its own Linux workplace. It's called [DAWO](https://dawo.overheid-a.nl/), short for *Digitaal Autonome Werkomgeving Overheid* (digitally autonomous government work environment). It's developed within the Ministry of the Interior (BZK), and the code lives in [DAWO-Core on Codeberg](https://codeberg.org/DAWO/DAWO-Core). It moved there from code.overheid.nl. Under the hood it's a NixOS flake.

I build [KompassOS](https://github.com/L0g0ff/KompassOS) as a hobby: a KDE distro on Fedora Atomic, based on Aurora. So of course I wanted to know: what if DAWO were the foundation and KompassOS sat on top? I don't know if this government project will take off. But if it does, it would be nice to be ready.

So this is an experiment. A proof of concept, not a migration.

**Step 0: Just Try DAWO**

I wanted to download an ISO. There isn't one. The [v0.1.3 release](https://codeberg.org/DAWO/DAWO-Core/releases/tag/v0.1.3) only ships source archives. You can build the installer yourself in a `nixos/nix` container:

```bash
git clone --branch v0.1.3 --depth 1 https://codeberg.org/DAWO/DAWO-Core.git src && cd src
nix --extra-experimental-features "nix-command flakes" \
  build .#nixosConfigurations.dawo-installer.config.system.build.isoImage
```

That works, but it boots to a text console. The repo calls it a *headless provisioning ISO*, based on NixOS' minimal installer. The Plasma or GNOME desktop only appears after you install a DAWO host profile onto the disk with `nixos-anywhere`. It's built for managed pilots, not for "boot it and click around". So I built a small live KDE ISO from DAWO's own Plasma profile to get a look at it.

One gotcha: rebuilding NixOS inside a 4 GB VM with KDE running got killed with `SIGKILL` during `glibc-locales`. That's the OOM killer. Give it 8 GB, or build serially:

```bash
sudo nixos-rebuild boot --flake /etc/nixos#<host> --max-jobs 1 --cores 1
```

**The Idea: DAWO as a Base Layer**

DAWO is designed to be consumed. The core provides the base, and a "consumer" flake adds its own hardware, branding, users and apps without forking the core. That fits KompassOS well. It's not really a port, though. BlueBuild recipes, DNF packages and system overlays all have to be expressed again in Nix. What you can carry over are the choices.

So *KompassOS-DAWO* is a flake with DAWO-Core as an input, plus:

- A test VM (4 vCPU, 8 GB RAM) and a pipeline: a push to `main` copies the config, runs `nixos-rebuild` and reboots.
- Apps from Aurora DX and KompassOS. Flatpak where possible (declaratively through nix-flatpak, like DAWO itself does), native Nix packages otherwise.
- DAWO's default `dawo` user password is well known, so I locked it and set my own one declaratively.

**The Catch: Software Doesn't Port One-to-One**

- **Citrix Workspace**: nixpkgs pinned a version Citrix no longer offers for download. I overrode the package to the version that *is* on their site, downloaded the tarball after accepting the EULA, and added it to the store with `nix-store --add-fixed sha256`.
- **Homebrew**: don't. Linuxbrew expects FHS paths that NixOS doesn't have. The brew equivalent is `nix profile`: `nix profile add nixpkgs#ripgrep`, as a normal user, without touching the system config.
- **Flatpaks installed by users**: DAWO sets `uninstallUnmanaged = true`, so anything a user installs system-wide is removed again on the next deploy. Users need their own Flathub remote and must install in user scope.

**The Theme: Aurora Dark on NixOS**

I took Aurora's dark Plasma setup (Breeze Dark, the look-and-feel package, splash and wallpaper) and swapped in the KompassOS wallpaper and logos, as a small Nix module. Three things didn't just work:

1. **The splash** only showed up from the second login. The theme gets applied after Plasma has already started.
2. **The start button** kept the KDE logo. `plasma-apply-lookandfeel` doesn't run the layout scripts unless you reset the whole panel layout. I didn't want that, so a targeted fix replaces only the launcher icon.
3. **The login screen** still showed DAWO's background. DAWO explicitly enables SDDM, even though Plasma Login Manager is the intended successor since Plasma 6.6. The fix: override SDDM's Breeze background with the same wallpaper.

**ujust on NixOS**

KompassOS, like Aurora, comes with `ujust`: `just` recipes for maintenance, with `ujust --choose` as a menu. On NixOS you can get that without rewriting the scripts:

```nix
# flake.nix
inputs.kompassos = { url = "github:L0g0ff/KompassOS"; flake = false; };

# configuration.nix
let
  ks = inputs.kompassos;
  portable = [ "kill_citrix" "setup_clamav" ];  # only recipes that make sense on NixOS
  justfile = pkgs.writeText "kompassos.just" (''
    default:
        @just --justfile {{justfile()}} --choose
  '' + lib.concatMapStrings (n: "import '${ks}/files/justfiles/${n}.just'\n") portable);
in {
  environment.systemPackages = with pkgs; [ just gum fzf
    (writeShellScriptBin "ujust" ''exec just --justfile ${justfile} --working-directory "$PWD" "$@"'') ];
  # the scripts hard-code /usr/lib/ujust/ujust.sh
  systemd.tmpfiles.rules = [ "L+ /usr/lib/ujust - - - - ${ks}/files/system/usr/lib/ujust" ];
}
```

Not everything belongs here. The `rpm-ostree`/bootc scripts and the Fedora ISO builders are out. Some are already covered by DAWO (`setup-zsh`), and others become a single Nix option (kernel parameters, allowed bridges). The brew-based AI tool installers now do `nix profile add nixpkgs#codex` (and the same for Claude Code, Gemini CLI and Copilot CLI). They install into the user's own profile, not the base image.

I tested this in a `nixos/nix` container, not yet on the DAWO VM itself. `ujust --list` showed the recipes, and the four AI tools installed and reported their versions. I didn't click through the interactive `--choose` menu myself.

**The ISO: Install Everything in One Go**

The last step was an ISO that installs a machine that looks roughly like my test VM. First I made the baseline healthy: `dawo-verify.service` failed because `sysctl` was missing from its path. Now the pipeline fails when a machine ends up `degraded` instead of `running`.

The installer is deliberately simple, and for now it's for VMs only:

```text
lsblk
sudo install-kompassos-dawo /dev/sdX
WIPE /dev/sdX        # typed confirmation; the disk gets wiped
sudo reboot
```

It installs offline from the ISO, so nothing gets downloaded during setup. The ISO is about 6.6 GB. A wipe script needs care, so I had it reviewed. It now refuses disks that are in use and stops if any safety check fails.

The first real install still failed twice:

- `lsblk` calls the column `DISK-SEQ`, not `DISKSEQ`. My mocked tests happily accepted the wrong name. 🙃
- `mount` ran right after `mkfs`, before the kernel had caught up, and tried to read the ext4 root as FAT. Fix: pass the filesystem type explicitly and wait for udev first.

After that it installed, rebooted and `systemctl is-system-running` said `running`. The boot screen now shows the install steps in English, and `/boot` is mounted with `umask=0077`.

**The Fine Print**

- This is a hobby PoC. The code lives in a private repo for now.
- Updates aren't solved yet. `dawo.autoUpdate` (DAWO uses `comin` for that) is disabled in my config. A machine installed from the ISO runs the commit the ISO was built from, and doesn't pull changes from `main` by itself yet.
- NixOS isn't immutable the way Silverblue is. `/nix/store` is read-only and every rebuild is a new generation you can roll back to. But `/etc`, `/var` and `/home` stay writable.

**Three Takeaways**

1. DAWO is a good base layer to build on. It's made to be consumed by your own flake, so you don't have to fork it.
2. Porting a distro to NixOS means rewriting it: you keep the choices, not the code. Most `ujust` scripts survived, though, thanks to one symlink and a whitelist.
3. Test a destructive installer on a real (virtual) disk. The mocks were green, and the real disk still found two bugs within minutes.

*Full disclosure: I built this together with my AI assistant, who also did most of the typing. I did the clicking and the rebooting.* 😉

Happy (Nix) hacking!
