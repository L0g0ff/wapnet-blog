---
_thumbnail_id: "2042"
author: thomasf
categories:
  - azure
  - monitoring
cover:
  alt: windows-powershell-ise-icon
  image: /wp-content/uploads/2022/04/windows-powershell-ise-icon.png
date: "2025-01-05T17:02:05+00:00"
guid: https://blog.wapnet.nl/?p=2223
parent_post_id: null
post_id: "2223"
title: PRTG Monitor Azure Backups
url: /2025/01/prtg-monitor-azure-backups/

---
I adapted an existing solution from [2azure.nl](https://www.2azure.nl/2019/06/25/use-prtg-to-monitor-azure-backup-status/) for monitoring Azure Backup status through PRTG in our environment.

I did some refactoring and I like to share the code with you.

Run the script in PRTG with these parameters:

```
-Password "XXXXX" -applicationid "XXXXX" -TenantId "XXXXX" -VaultName "XXXXX" -ResourceGroupName "XXXXX"
```

The complete script is available in the code block below."

```
param(
    [Parameter(Mandatory = $true)]
    [string]$Password,
    [Parameter(Mandatory = $true)]
    [string]$ApplicationId,
    [Parameter(Mandatory = $true)]
    [string]$TenantId,
    [Parameter(Mandatory = $true)]
    [string]$VaultName,
    [Parameter(Mandatory = $true)]
    [string]$ResourceGroupName
)

# Run Once: Install required modules
# Install-Module -Name Az.Accounts
# Install-Module -Name Az.RecoveryServices

Import-Module Az.Accounts
Import-Module Az.RecoveryServices

# Login
$securePassword = ConvertTo-SecureString $Password -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential($ApplicationId, $securePassword)
Connect-AzAccount -Credential $credential -ServicePrincipal -TenantId $TenantId | Out-Null

# Access specific vault
$vault = Get-AzRecoveryServicesVault -Name $VaultName -ResourceGroupName $ResourceGroupName
if ($vault) {
    # Set vault context
    $vault | Set-AzRecoveryServicesVaultContext

    # Check backups last 24 hours, only Backup operations
    $jobs = Get-AzRecoveryServicesBackupJob -From (Get-Date).AddDays(-1).ToUniversalTime() |
            Where-Object { $_.Operation -eq "Backup" } |
            Select-Object Status, WorkloadName

    $completed = ($jobs | Where-Object {$_.Status -eq 'Completed'}).Count
    $failed = ($jobs | Where-Object {$_.Status -eq 'Failed'}).Count
    $running = ($jobs | Where-Object {$_.Status -eq 'InProgress'}).Count

    # Get unique workload names
    $workloadNames = ($jobs | Select-Object -ExpandProperty WorkloadName -Unique) -join ', '

    # Output for PRTG
    if ($failed -eq 0 -and $completed -gt 0) {
        $result = "<prtg>
            <result>
                <channel>Completed jobs</channel>
                <value>$completed</value>
                <LimitMode>1</LimitMode>
                <LimitMinError>1</LimitMinError>
                <LimitErrorMsg>No completed backups found!</LimitErrorMsg>
            </result>
            <result>
                <channel>Failed jobs</channel>
                <value>$failed</value>
                <LimitMode>1</LimitMode>
                <LimitMaxError>0</LimitMaxError>
                <LimitErrorMsg>Failed backup jobs detected!</LimitErrorMsg>
            </result>
            <result>
                <channel>Running jobs</channel>
                <value>$running</value>
                <LimitMode>1</LimitMode>
                <LimitMaxWarning>1</LimitMaxWarning>
                <LimitMaxError>2</LimitMaxError>
                <LimitWarningMsg>Multiple backup jobs running</LimitWarningMsg>
                <LimitErrorMsg>Too many backup jobs running!</LimitErrorMsg>
            </result>
            <text>Backup successful in vault: $($vault.Name) for workloads: $workloadNames</text>
        </prtg>"
    } else {
        $result = "<prtg>
            <error>1</error>
            <text>Backup failed in vault: $($vault.Name), failed jobs: $failed, workloads: $workloadNames</text>
        </prtg>"
    }
} else {
    $result = "<prtg>
        <error>1</error>
        <text>Could not find vault $VaultName in resource group $ResourceGroupName</text>
    </prtg>"
}

Write-Host $result
```
