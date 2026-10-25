---
_thumbnail_id: "1866"
author: thomasf
categories:
  - azure
  - linux
  - powershell
cover:
  alt: Shell
  image: /wp-content/uploads/2020/10/Shell.png
date: "2021-02-06T21:55:12+00:00"
guid: https://blog.wapnet.nl/?p=1873
parent_post_id: null
post_id: "1873"
title: Create Azure Linux VM with worpress pre-installed
url: /2021/02/create-azure-linux-vm-with-worpress-pre-installed/

---
This is my first completed automated Linux Azure VM deployment. I like to share it with you.

There are 3 parts

1. Create a keygen for ssh
1. Powershell script
1. Bash script

First start powershell and create a keypair **with** passphase


```powershell
ssh-keygen -m PEM -t rsa -b 4096
```


Then place the bash script somewhere on your local computer


```bash
#! /bin/bash
apt-get update
apt-get install -y wordpress php libapache2-mod-php mysql-server php-mysql

echo "Alias /blog /usr/share/wordpress" >>/etc/apache2/sites-available/wordpress.conf
echo "" >>/etc/apache2/sites-available/wordpress.conf
echo " Options FollowSymLinks" >>/etc/apache2/sites-available/wordpress.conf
echo " AllowOverride Limit Options FileInfo" >>/etc/apache2/sites-available/wordpress.conf
echo " DirectoryIndex index.php" >>/etc/apache2/sites-available/wordpress.conf
echo " Order allow,deny" >>/etc/apache2/sites-available/wordpress.conf
echo " Allow from all" >>/etc/apache2/sites-available/wordpress.conf
echo "" >>/etc/apache2/sites-available/wordpress.conf
echo "" >>/etc/apache2/sites-available/wordpress.conf
echo " Options FollowSymLinks" >>/etc/apache2/sites-available/wordpress.conf
echo " Order allow,deny" >>/etc/apache2/sites-available/wordpress.conf
echo " Allow from all" >>/etc/apache2/sites-available/wordpress.conf
echo "" >>/etc/apache2/sites-available/wordpress.conf

a2ensite wordpress
a2enmod rewrite
reload apache2
service apache2 reload
systemctl restart apache2

mysql -e "CREATE DATABASE wordpress;"
mysql -e "CREATE USER wordpress@localhost IDENTIFIED BY 'Secret@Pass1';"
mysql -e "GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP,ALTER ON wordpress.* TO wordpress@localhost;"
mysql -e "FLUSH PRIVILEGES;"

echo ">/etc/wordpress/config-localhost.php
echo "define('DB_NAME', 'wordpress');">>/etc/wordpress/config-localhost.php
echo "define('DB_USER', 'wordpress');">>/etc/wordpress/config-localhost.php
echo "define('DB_PASSWORD', 'Secret@Pass1');">>/etc/wordpress/config-localhost.php
echo "define('DB_HOST', 'localhost');">>/etc/wordpress/config-localhost.php
echo "define('DB_COLLATE', 'utf8_general_ci');">>/etc/wordpress/config-localhost.php
echo "define('WP_CONTENT_DIR', '/usr/share/wordpress/wp-content');">>/etc/wordpress/config-localhost.php
echo "?>">>/etc/wordpress/config-localhost.php

service mysql start

publicip=$(dig +short myip.opendns.com @resolver1.opendns.com) && mv /etc/wordpress/config-localhost.php /etc/wordpress/config-$publicip.php
```


Then put the code in the Powershell ISE, change some variables and kickoff the script.

The things you may need to change:

- script.sh location


```powershell
New-AzResourceGroup -Name lxautodeploy -Location westeurope

# Create a subnet configuration
$subnetConfig = New-AzVirtualNetworkSubnetConfig `
 -Name "mySubnet" `
 -AddressPrefix 192.168.1.0/24

# Create a virtual network
$vnet = New-AzVirtualNetwork `
 -ResourceGroupName "lxautodeploy" `
 -Location "westeurope" `
 -Name "myVNET" `
 -AddressPrefix 192.168.0.0/16 `
 -Subnet $subnetConfig

# Create a public IP address and specify a DNS name
$pip = New-AzPublicIpAddress `
 -ResourceGroupName "lxautodeploy" `
 -Location "westeurope" `
 -AllocationMethod Static `
 -IdleTimeoutInMinutes 4 `
 -Name "mypublicdns$(Get-Random)"

# Create an inbound network security group rule for port 22
$nsgRuleSSH = New-AzNetworkSecurityRuleConfig `
 -Name "myNetworkSecurityGroupRuleSSH" `
 -Protocol "Tcp" `
 -Direction "Inbound" `
 -Priority 1000 `
 -SourceAddressPrefix * `
 -SourcePortRange * `
 -DestinationAddressPrefix * `
 -DestinationPortRange 22 `
 -Access "Allow"

# Create an inbound network security group rule for port 80
$nsgRuleWeb = New-AzNetworkSecurityRuleConfig `
 -Name "myNetworkSecurityGroupRuleWWW" `
 -Protocol "Tcp" `
 -Direction "Inbound" `
 -Priority 1001 `
 -SourceAddressPrefix * `
 -SourcePortRange * `
 -DestinationAddressPrefix * `
 -DestinationPortRange 80 `
 -Access "Allow"

# Create a network security group
$nsg = New-AzNetworkSecurityGroup `
 -ResourceGroupName "lxautodeploy" `
 -Location "westeurope" `
 -Name "myNetworkSecurityGroup" `
 -SecurityRules $nsgRuleSSH,$nsgRuleWeb

# Create a virtual network card and associate with public IP address and NSG
$nic = New-AzNetworkInterface `
 -Name "myNic" `
 -ResourceGroupName "lxautodeploy" `
 -Location "westeurope" `
 -SubnetId $vnet.Subnets[0].Id `
 -PublicIpAddressId $pip.Id `
 -NetworkSecurityGroupId $nsg.Id

# Define a credential object
$securePassword = ConvertTo-SecureString ' ' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential ("azureuser", $securePassword)

# Create a virtual machine configuration
$vmConfig = New-AzVMConfig `
 -VMName "myLXVM" `
 -VMSize "Standard_D2s_v3" | `
Set-AzVMOperatingSystem `
 -Linux `
 -ComputerName "myLXVM" `
 -Credential $cred `
 -DisablePasswordAuthentication | `
Set-AzVMSourceImage `
 -PublisherName "Canonical" `
 -Offer "UbuntuServer" `
 -Skus "18.04-LTS" `
 -Version "latest" | `
Add-AzVMNetworkInterface `
 -Id $nic.Id

# Configure the SSH key
$sshPublicKey = cat ~/.ssh/id_rsa.pub
Add-AzVMSshPublicKey `
 -VM $vmconfig `
 -KeyData $sshPublicKey `
 -Path "/home/azureuser/.ssh/authorized_keys"

New-AzVM `
 -ResourceGroupName "lxautodeploy" `
 -Location westeurope -VM $vmConfig

Get-AzPublicIpAddress -ResourceGroupName "lxautodeploy" | Select "IpAddress"

Invoke-AzVMRunCommand -ResourceGroupName "lxautodeploy" -Name 'myLXVM' -CommandId 'RunShellScript' -ScriptPath "script.sh" -Verbose
```


Now you can go to http://<publicip> **/blog** to access the new blog

You can access the server with ssh azureuser@<publicip>

{{< figure src="/wp-content/uploads/2021/02/image.png" alt="" caption="" >}}

Have fun with it!
