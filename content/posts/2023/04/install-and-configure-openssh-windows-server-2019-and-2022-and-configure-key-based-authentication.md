---
_thumbnail_id: "2119"
author: thomasf
categories:
  - networking
  - windows
cover:
  alt: OpenSSH_logo
  image: /wp-content/uploads/2023/04/OpenSSH_logo.png
date: "2023-04-06T14:27:08+00:00"
guid: https://blog.wapnet.nl/?p=2115
parent_post_id: null
post_id: "2115"
title: Install and Configure OpenSSH Windows Server 2019 and 2022 and configure key-based authentication
url: /2023/04/install-and-configure-openssh-windows-server-2019-and-2022-and-configure-key-based-authentication/

---
OpenSSH is a free and open-source software that allows secure communication between computers over an unsecured network. It is widely used on Linux and Unix systems, but it is also available for Windows systems. In this article, we will show you how to install and configure OpenSSH on a Windows 2022 server.

## Step 1: Install OpenSSH

The first step is to install OpenSSH on your Windows server. To do this, follow these steps:

```
# Install the OpenSSH Server
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
# Start the sshd service
Start-Service sshd

# OPTIONAL but recommended:
Set-Service -Name sshd -StartupType 'Automatic'

# Confirm the Firewall rule is configured. It should be created automatically by setup. Run the following to verify
if (!(Get-NetFirewallRule -Name "OpenSSH-Server-In-TCP" -ErrorAction SilentlyContinue | Select-Object Name, Enabled)) {
    Write-Output "Firewall Rule 'OpenSSH-Server-In-TCP' does not exist, creating it..."
    New-NetFirewallRule -Name 'OpenSSH-Server-In-TCP' -DisplayName 'OpenSSH Server (sshd)' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22
} else {
    Write-Output "Firewall rule 'OpenSSH-Server-In-TCP' has been created and exists."
}
```

## Step 2: Configure OpenSSH

Once OpenSSH is installed on your server, you need to configure it to allow secure communication. Follow these steps to configure OpenSSH:

- Open notepad
- Open the configuration file `C:\ProgramData\ssh\sshd_config`
- **Remove** the "#" at the beginning of the line `#PubkeyAuthentication yes` to uncomment it: `PubkeyAuthentication yes`
- Locate the line that starts with `#PasswordAuthentication yes` and **remove** the "#" at the beginning of the line to uncomment it and change it to **NO**: `PasswordAuthentication no`
- **Add** the "#" at the beginning of the line `AuthorizedKeysFile PROGRAMDATA/ssh/administrators_authorized_keys` to **comment it out**: `#AuthorizedKeysFile PROGRAMDATA/ssh/administrators_authorized_keys`
- Save the changes and close the configuration file.
- Restart the service

```
# Restart the sshd service
Restart-Service sshd
```

## Step 3: Configure the Administrator for key-based authentication

After the configuration is complete, you need to configure the public key.

Optional: If you don't have a public/private keypair use this command to create the files on your client:

```
ssh-keygen -t rsa -b 4096
```

{{< figure src="/wp-content/uploads/2023/04/image-5.png" alt="" caption="" >}}

- Open the Explorer and go to `C:\Users\<Username>\`
- Create a folder `.ssh`
- Create a text file (without extension!) `authorized_keys`
- Open the file in notepad
- Paste your ssh-rsa public key in this `authorized_keys` file (this is the content of `id_rsa.pub`)

{{< figure src="/wp-content/uploads/2023/04/image-2.png" alt="" caption="" >}}

- Save the file
- Remove the inheritance so that only the user and system has full permission

{{< figure src="/wp-content/uploads/2023/04/image-4.png" alt="" caption="" >}}

## Step 4: Test OpenSSH

To test if OpenSSH is installed and configured correctly, follow these steps:

- Open a Command Prompt window.
- Type "ssh username@<server>" and press Enter.
- If the connection is successful, you should see a welcome message.

{{< figure src="/wp-content/uploads/2023/04/image-6.png" alt="" caption="" >}}

Congratulations! You have successfully installed and configured OpenSSH on your Windows 2022 server and configure it securely with key-based authentication.

## Optional: change CMD to Powershell

If you want to connect directly in PowerShell instead of the default command use this PowerShell command

```
New-ItemProperty -Path "HKLM:\SOFTWARE\OpenSSH" -Name DefaultShell -Value "C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe" -PropertyType String -Force
```

Happy connecting :)
