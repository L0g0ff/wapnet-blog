---
_edit_last: "1"
_wp_old_slug: ""
author: thomasf
categories:
  - windows
date: "2010-10-14T13:03:00+00:00"
dsq_thread_id: "5292394394"
guid: https://blog.wapnet.nl/?p=433
parent_post_id: null
post_id: "433"
title: Print Spooler Crash Troubleshooting Steps
url: /2010/10/print-spooler-crash-troubleshooting-steps/

---
(copy from: [http://blogs.technet.com/b/perfguru/archive/2008/08/06/print-spooler-crash-troubleshooting-steps.aspx](http://blogs.technet.com/b/perfguru/archive/2008/08/06/print-spooler-crash-troubleshooting-steps.aspx))

> # Overview of Print Spooler Component
>
>  **Print Processor**
>
> The print processor tells the spooler to alter a job according to the document data type. It works together with the printer driver to move the spooled print jobs from the hard disk drive to the printer.
>
> **Print Monitor**
>
> The print monitors are the name of any component that processes the print job after it has spooled and are responsible for directing the output to the print device. Print monitors can be divided into two classes:
>
> - **Language monitors**
> - **Port monitors**
>
> **Language monitors** are typically used only for bi-directional printers. A bi-directional printer
>
> Supports two-way communication to answer status, and configurations questions sent to it. A
>
> Bi-directional printer can also give unsolicited status information about the job being printed,
>
> and error conditions such as paper out.
>
> **Port monitors** consist of user-mode DLLs. They are responsible for providing a     communications    path between the user-mode print spooler and the kernel-mode port drivers that access I/O port hardware.
>
> Print Spooler crash happens most of the time due to third party print processor and print monitor. We can set printers to use default print processor and monitor by machine changes in the registry called as Print hive cleaning
>
> **Note that all of the changes described in this section will take effect when the Print Spooler service is restarted.**
>
> # Confirm the default Local Print Provider
>
> 1) Use Regedit to locate the Print key in the Registry:
>
> **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Print**
>
> 2) Click to highlight the Print key in Regedit and export the key as a .reg file for backup purposes (File > Export).
>
> 3) Locate the Local Port Registry key:
>
> **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Print\\Monitors\\Local Port**
>
> 4) Confirm that the Driver value in the Local Port Registry key is set to Localspl.dll. If it is not, double-click the Driver value to edit the Data String and set it to Localspl.dll.
>
> # Remove 3rd Party Port and Language Monitors
>
> 1) Note any 3rd-party Monitors that are listed in the **Monitors** Registry key for future reference:
>
> **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Print\\Monitors**
>
> The default Monitors are:
>
> ==========================
>
> AppleTalk Printing Devices
>
> **BJ Language Monitor** **Local Port**
>
> LPR Port
>
> **PJL Language Monitor** **Standard TCP/IP Port** **USB Monitor** **Windows NT Fax Monitor**
>
> ==========================
>
> **Note:** Not all of the above default Port Monitors will be present in all cases. You may also see the Microsoft Office Document Imaging Monitor which is installed by MS Office.
>
> The 2 types of monitors that may be listed here are **Port Monitors** and/or **Language Monitors**. As a general rule, Language Monitors will not have any printer ports defined in the Ports subkey and may be removed without causing a problem. Port Monitors such as **HP Standard TCP/IP**, however, may have active printers using this port type. If a 3rd-party Port Monitor is in use, with printers defined in the Ports subkey under the Port Monitor, you will need to convert the port(s) to a Standard TCP/IP Port ( **Standard Port Monitor**).
>
> 2) To convert the printer ports from the 3rd-party Port Monitor to Standard TCP/IP Port Monitor, perform the following steps:
>
> #### Convert 3rd Party Ports to Standard TCP/IP Ports
>
> 1) Open the **Printers and Faxes** folder.
>
> 2) Right-click the printer that was identified as using the 3rd-party Port Monitor and select **Properties**.
>
> 3) In the Properties for the printer, click the **Ports** tab.
>
> 4) On the Ports tab, click the **Add Port** button.
>
> 5) In the **Printer Ports** dialog, select **Standard TCP/IP** and click the **New Port** button to start the **Add Standard TCP/IP Printer Port Wizard**.
>
> 6) Click **Next** when the **Add Standard TCP/IP Printer Port Wizard** starts to specify the printer that will be using this new port.
>
> 7) Enter the **Printer Name or IP Address** for the printer that will be using this new port and click **Next**.
>
> **Note:** The wizard automatically fills in the port name for you in the **Port Name** box. You can either accept this name or type the name that you want to use, and then click **Next**. Standard Port Monitor then sends a query to the print device. Based on the SNMP values that are returned, the device details are determined and the appropriate device options are displayed. If the print device cannot be identified, you must supply additional information about it.
>
> 8) If the **Additional Port Information Required** page is displayed, perform one of the following tasks under **Device Type**:
>
> Click **Standard**, click the appropriate device in the list, and then click **Next**.
>
> -or-
>
> Click **Custom**, click **Settings**, specify the protocol settings ( **RAW** or **LPR**) and the **SNMP** status settings that you want to use, click **OK**, and then click **Next**.
>
> 10) If the wizard prompts you for the print server protocol, specify the protocol that you want to use, either **RAW** or **LPR**.
>
> 11) If the wizard prompts you to select a port, specify the port that you want to use in the **Device Port** box, and then click **Next**.
>
> 12) Click **Finish**, and then click **Close**. On the Ports tab in the Properties for the printer, you should see that the printer is now set to use the new Standard TCP/IP Port that you just created. The new Standard TCP/IP port is also displayed in the **Ports on this server** list on the **Ports** tab in the **Print Server Properties** ( **File > Server** Properties from within the **Printers** folder)
>
> 13) You can then delete the 3rd-party port from the **Ports** tab within the **Print Server Properties**.
>
> 14) Repeat these steps for all printers that are using a 3rd-party Port Monitor.
>
> After moving all printers to the Standard TCP/IP Port Monitor, we can delete the 3rd-party Port Monitor's Registry key under the **Monitors** key:
>
> **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Print\\Monitors**
>
> #### Remove All Other 3rd party Monitors
>
> For any other 3rd party Monitors that are identified under the **Monitors** key and are confirmed to **NOT** have any printer ports listed under the Ports subkey for the Monitor, we will need to perform the following 2 steps
>
> - Identify printers configured to use the 3rd party Monitor.
> - Delete the reference to the Monitor for that printer.
> - Delete the Registry key for the 3rd party Monitor.
>
> Note: The **Client Printer Port** is the Citrix Metaframe Monitor used for autocreated client printers in Terminal Server sessions. **Do not remove this Monitor unless it is confirmed to be related to the problem:**
>
> ==========================
>
> **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print\\Monitors\\Client Printer Port**
>
> Driver REG\_SZ cpmmon.dll
>
> ==========================
>
> See the following article before removing **Lexmark Monitors:** **155516** How to Remove the Lexmark MarkVision Monitor
>
> [http://support.microsoft.com/?id=155516](http://support.microsoft.com/?id=155516)
>
> 1) Note the name of the 3rd-party Monitor that is being removed. We will use this name to search the Print Registry key for references to this Monitor.
>
> Assume, for example, that the **HP Master Monitor** is installed:
>
> ==========================
>
> **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print\\Monitors\\HP Master Monitor**
>
> EOJTimeout REG\_DWORD 0xea60
>
> Driver REG\_SZ HPBMMON.DLL
>
> ==========================
>
> 2) In Regedit, click to highlight the Print key:
>
> **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Print**
>
> 3) Press **F3**, or click the **Edit** menu and select **Find**.
>
> 4) In the **Find What** field, type the name of the 3rd-party Monitor that is being removed, **HP Master Monitor** in this example, and click **Find Next**. Identify printers that are configured to use the Monitor that we are removing, for example:
>
> ==========================
>
> **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print\\Environments\\Windows NT x86\\Drivers\\Version-3\\HP Color LaserJet 2500 PCL 6**
>
> Configuration File REG\_SZ HPBF342E.DLL
>
> Data File REG\_SZ HPBF342I.PMD
>
> Driver REG\_SZ HPBF342G.DLL
>
> Help File REG\_SZ HPBF342E.HLP
>
> **Monitor REG\_SZ HP Master Monitor**
>
> ==========================
>
> 5) Double-click the **Monitor** value to delete the 3rd party Monitor data string. In this example, delete the "HP Master Monitor" value. The Monitor value will be left with a blank data string, as follows:
>
> ==========================
>
> **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print\\Environments\\Windows NT x86\\Drivers\\Version-3\\HP Color LaserJet 2500 PCL 6**
>
> Configuration File REG\_SZ HPBF342E.DLL
>
> Data File REG\_SZ HPBF342I.PMD
>
> Driver REG\_SZ HPBF342G.DLL
>
> Help File REG\_SZ HPBF342E.HLP
>
> **Monitor REG\_SZ**
>
> ==========================
>
> 6) Repeat the steps above for all 3rd-party Monitors.
>
> 7) Stop and restart the Print Spooler service for the changes take effect.
>
> **Net stop spooler** **Net start spooler** **Note:** In most cases, removing the 3rd party Monitors will not affect normal printing. If new problems are seen after removing the 3rd party Monitors, we can restore the backed up Print Registry key to restore the original configuration..
>
> You can then perform the steps above again in smaller steps, stopping and starting the Print Spooler service more frequently, to determine if a specific component is required. If so, skip the removal of this component and continue removing the other 3rd-party items.
>
> **Note:** If the problem is easily reproducible, you may also individually remove the 3rd-party Monitors to try to narrow the problem down to a particular Monitor. This procedure will take more time and may require restarting the Print Spooler service multiple times.
>
> # Remove 3rd-party Print Providers
>
> Remove 3rd party Print Providers by deleting the 3rd-party providers in the following Registry key:
>
> **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Print\\Providers**
>
> The default **Print Providers** are:
>
> Internet Print Provider
>
> Lanman Print Services
>
> The **Client Printer** Provider is the Citrix Metaframe provider used for autocreated client printers in Terminal Server sessions. Do not remove this Provider unless it is confirmed to be related to the problem:
>
> ==========================
>
> **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print\\Providers\\Client Printer**
>
> Name REG\_SZ C:\\Program Files\\Citrix\\system32\\cdmprov.dll
>
> DisplayName REG\_SZ Client Printer
>
> ==========================
>
> 2) Stop and restart the Print Spooler service for the changes take effect.
>
> Net stop spooler
>
> Net start spooler
>
> # Remove 3rd Party Print Processors
>
> Perform the following steps to confirm that all printers are configured to use the **WinprintPrint Processor.**
>
> - Identify printers that are configured to use a 3rd party Print Processor.
> - Change the 3rd party Print Processor to Winprint.
> - Delete the Registry key for the 3rd party Print Processor.
>
> 1) Note the name of the installed Print Processors under the following Registry key:
>
> **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print\\Environments\\Windows NT x86\\Print Processors**
>
> The default Print Processor is **Winprint**:
>
> ==========================
>
> **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print\\Environments\\Windows NT x86\\Print Processors\\winprint**
>
> Driver REG\_SZ localspl.dll
>
> ==========================
>
> Assume, for example, that the **HPPRN05** is installed:
>
> ==========================
>
> **HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print\\Environments\\Windows NT x86\\Print Processors\\HPPRN05**
>
> Driver REG\_SZ HPPRN05.DLL
>
> ==========================
>
> 2) In Regedit, click to highlight the Print key:
>
> **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Print**
>
> 3) Press **F3**, or click the **Edit** menu and select **Find**.
>
> 4) In the **Find What** field, type **Print Processor** and click **Find Next**. Identify the Print Processor being used for each printer:
>
> ==========================
>
> HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print\\Printers\\Client1
>
> ChangeID REG\_DWORD 0x1b9fa8c9
>
> Status REG\_DWORD 0x180
>
> Name REG\_SZ Client\\XPWS
>
> Share Name REG\_SZ
>
> **Print Processor REG\_SZ HPPRN05**
>
> ==========================
>
> 5) Double-click the **Print Processor** value to change the 3rd party processor data string to **Winprint**:
>
> ==========================
>
> HKEY\_LOCAL\_MACHINE\\System\\CurrentControlSet\\Control\\Print\\Printers\\Client1
>
> ChangeID REG\_DWORD 0x1b9fa8c9
>
> Status REG\_DWORD 0x180
>
> Name REG\_SZ Client\\XPWS
>
> Share Name REG\_SZ
>
> **Print Processor REG\_SZ WinPrint**
>
> ==========================
>
> 6) Repeat the steps above for all 3rd-party Print Processors.
>
> 7) Stop and restart the Print Spooler service for the changes to take effect.
>
> **Net stop spooler** **Net start spooler** **Note:** In most cases, changing the print processor to Winprint will not affect normal printing. If new problems are seen after changing the print processor,  we can restore the backed up **Print** Registry key and restart the Print Spooler service to restore the original configuration.
>
> You can then perform the steps above again in smaller steps, stopping and starting the Print Spooler service more frequently, to determine if a specific component is required. If so, skip the removal of this component and continue removing the other 3rd party items.
>
> Additional steps to be done
>
> 1) Check the Spool folder to see if there are any old files in the folder. When printing is working properly, the files in the Spool folder are deleted as the jobs are printed. The default Spool folder is:
>
> **systemroot\\System32\\Spool\\Printers**
>
> The Spool folder location can be confirmed by checking the **DefaultSpoolDirectory** Registry value in the following Registry key:
>
> **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Print\\Printers**
>
> Move any old files that are in the Spool folder to see if the problem still occurs. Corrupt files in the Spool folder can cause Print Spooler service problems. You may need to stop the Print Spooler service to move the files from the Spool folder.
>
> 2) The Print Spooler service is, by default, dependent only upon the **Remote Procedure Call (RPC)** service, **RPCSS**. To confirm the Spooler dependencies, check the **DependOnService** value in the following Registry key:
>
> **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Spooler**
>
> Confirm that the dependent services are started. If there are any other dependent services listed, in addition to **RPCSS**, edit the DependOnService Registry value to remove all dependencies except **RPCSS**.
>
> 3) Configure the installed antivirus application to exclude scanning the **Spool** folder. There can be contention between the antivirus application and the Print Spooler service that may cause intermittent printing problems.
>
> If still issue persists we need to collect ADPlus crash dump of print spooler service. ADPlus is a tool that will allow us to get a memory dump from a process that is giving you problems.
>
> To get this tool, please install the “Debugging Tools for Windows" from [http://www.microsoft.com/whdc/devtools/debugging/installx86.mspx](http://www.microsoft.com/whdc/devtools/debugging/installx86.mspx)
>
> Once these tools are installed, do the following:
>
> 1\. Create a directory called c:\\adplus
>
> 2\. Open a command prompt and change to the directory where you installed the debugging tools.  By default, this is c:\\Program Files\\Debugging Tools for Windows
>
> 3\. Type the following: " **cscript adplus.vbs -hang -pn <mmc.exe> -o c:\\adplus**”
>
> 4\. Do not interfere with the windows that is opened, just let it run minimized.
> 5\. You will not be able to log off the system while you are monitoring.
> 6\. When the crash occurs, please zip and send me the contents of the c:\\adplus directory.
>
> For more information please see refer to this Knowledge Base article: 286350 HOWTO: Use Autodump+ to Troubleshoot "Hangs" and "Crashes"[http://support.microsoft.com/?id=286350](http://support.microsoft.com/?id=286350%20)
>
> After collecting the dump please contact Microsoft for the analysis.
