---
author: thomasf
categories:
  - linux
date: "2008-02-04T22:37:15+00:00"
guid: https://blog.wapnet.nl/?p=14
parent_post_id: null
post_id: "14"
tags:
  - accu
  - battery
  - intel
  - levensduur
  - livetime
  - network
  - nic
  - ubuntu
  - wireless
title: Ubuntu
url: /2008/02/ubuntu/

---
Hi everyone,
this is a simple Howto for owners of laptops with Intel 2200 or 3945 wifi cards. Using these commands will use laptop-mode automatically at bootup to improve your battery life. Additionnaly, there are two scripts to be added to laptop-mode so that it manages the power saving modes on the intel wifi cards. This howto assumes you already have a working wireless setup, there are other threads on getting you wifi working, please keep this thread about power management.

**To use laptop-mode by default**:

Code:

```
sudo gedit /etc/default/acpi-support
```

Scroll down change laptop-mode to true:

Code:

```
ENABLE_LAPTOP_MODE=true
```

For some reason, laptop-mode is only started when the AC is unplugged. This might seem fine unless you bootup the laptop on the battery, in which case laptop-mode never gets started. Thus, to enable laptop-mode at boot (taken from a lost thread):

Code:

```
sudo update-rc.d laptop-mode multiuser
```

Now that laptop-mode is started automatically, we can make sure it manages the power saving on the intel wireless cards (ipw3945 & iwp2200) this way.

To use the power management, you will need to install the wireless tools:

Code:

```
sudo apt-get install linux-restricted-modules-generic wireless-tools
```

 **For both intel 3945 (ipw3945 driver) and 2200 (ipw2200 driver) cards**:

First, create the helper function file (taken from largecat's post on page 2 of this thread):

Code:

```
sudo gedit /etc/acpi/intelWifiPwr.sh
```

copy & paste this code in the editor, save and exit.

Code:

```
#!/bin/bash
# Power saving setting for the Intel 3945 and 2200 wireless adaptor
#
# This script relies upon the name of the driver.

I3945_DRIVERNAME=ipw3945
I2200_DRIVERNAME=ipw2200

IWPRIV=/sbin/iwpriv
IWCONFIG=/sbin/iwconfig

SET_I3945_AC_PARMS="set_power 6"
SET_I3945_BAT_PARMS="set_power 7"

SET_I2200_AC_PARMS="power off"
SET_I2200_BAT_PARMS="power on"

#
# Find all the wireless devices using the supplied driver names.
# Place the interface names on the list WIFI_IFNAMES.
#
function findWifiIfsByDriver {
    local DEVICE;
    local LINK_TARGET;
    WIFI_IFNAMES=""

    for DEVICE in /sys/class/net/*; do
	if [ -d $DEVICE/wireless ]; then
# See if the driver for $DEVICE matches the supplied one by checking the link to
# the driver.
	    if [ -h $DEVICE/device/driver ]; then
		LINK_TARGET=`readlink $DEVICE/device/driver | sed 's/.*\///'`

		if [ $LINK_TARGET == $1 ]; then

# add the interface name to the list
		    WIFI_IFNAMES=$WIFI_IFNAMES" "`echo -n $DEVICE | sed 's/.*\///'`
		fi
	    fi
	fi
    done
}

#
# Set all the adaptors using the supplied driver into the supplied
# power saving mode
#
# $1 - driver name
# $2 - power command
# $3 - power command arguments
#
function setWifiPwrSave {
    local DEVICE;
    findWifiIfsByDriver $1;

    for DEVICE in $WIFI_IFNAMES; do
#	echo "Would execute $2 $DEVICE $3"
	$2 $DEVICE $3
    done
}

function intel3945_BatPwrSave {
    setWifiPwrSave "$I3945_DRIVERNAME" "$IWPRIV" "$SET_I3945_BAT_PARMS"
}

function intel3945_AcPwrSave {
    setWifiPwrSave "$I3945_DRIVERNAME" "$IWPRIV" "$SET_I3945_AC_PARMS"
}

function intel2200_BatPwrSave {
    setWifiPwrSave "$I2200_DRIVERNAME" "$IWCONFIG" "$SET_I2200_BAT_PARMS"
}

function intel2200_AcPwrSave {
    setWifiPwrSave "$I2200_DRIVERNAME" "$IWCONFIG" "$SET_I2200_AC_PARMS"
}
```

Then we will create 2 scripts. The first will run when the laptop is unplugged, the later when it runs on AC.

On battery:

Code:

```
sudo gedit /etc/laptop-mode/batt-start/20-wireless-battery.sh
```

Then copy and paste this code into the editor, save and exit:

Code:

```
#!/bin/bash

# source the helper script
. /etc/acpi/intelWifiPwr.sh

# set Battery power saving
intel3945_BatPwrSave
intel2200_BatPwrSave
```

Make it executable:

Code:

```
sudo chmod +x /etc/laptop-mode/batt-start/20-wireless-battery.sh
```

On AC:

Code:

```
sudo gedit /etc/laptop-mode/batt-stop/20-wireless-ac.sh
```

Then copy and paste this code into the editor, save and exit:

Code:

```
#!/bin/bash

# source the helper script
. /etc/acpi/intelWifiPwr.sh

# set Battery power saving
intel3945_AcPwrSave
intel2200_AcPwrSave
```

Make it executable:

Code:

```
sudo chmod +x /etc/laptop-mode/batt-stop/20-wireless-ac.sh
```

That's it, you can give it a try by plugging and unplugging the AC and running iwconfig to verify that the Power management: on/off changes (this can take up to 15 seconds to change)

Bron: http://ubuntuforums.org/showthread.php?t=419772
