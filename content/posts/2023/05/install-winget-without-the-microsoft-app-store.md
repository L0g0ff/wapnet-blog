---
_thumbnail_id: "2133"
author: thomasf
categories:
  - windows
cover:
  alt: new-software-old-computer
  image: /wp-content/uploads/2023/05/new-software-old-computer-e1684954329709.jpg
date: "2023-05-24T18:50:56+00:00"
guid: https://blog.wapnet.nl/?p=2130
parent_post_id: null
post_id: "2130"
title: Install winget without the Microsoft App Store
url: /2023/05/install-winget-without-the-microsoft-app-store/

---
If you are unable to access the Windows Store app and wish to install winget, you can easily do so by following these steps:

- First download the latest version of winget: [https://aka.ms/getwinget](https://aka.ms/getwinget)
- Then use this Powershell command to install winget

```
Add-AppxPackage -Path Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
```

Probably you will get this error:

_Windows cannot install package Microsoft.DesktopAppInstaller\_1.19.10173.0\_x64\_\_8wekyb3d8bbwe because this package depends on a framework that could not be found. Provide the framework "Microsoft.UI.Xaml.2.7" published by "CN=Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US", with neutral or x64 processor architecture and minimum version 7.2109.13004.0, along with this package to install. The frameworks with name "Microsoft.UI.Xaml.2.7" currently installed are: {}_

The reason is that you miss the dependency _**Microsoft.UI.Xaml.2.7**_

Now you have to go to the nuget website and download the nuget package: [https://www.nuget.org/packages/Microsoft.UI.Xaml/2.7.3](https://www.nuget.org/packages/Microsoft.UI.Xaml/2.7.3)

{{< figure src="/wp-content/uploads/2023/05/image.png" alt="" caption="" >}}

Then you have to rename the file extension of the downloaded file to .zip

Open the zip file and go to tools > AppX > X64 > Release and extract the Microsoft.UI.Xaml.2.7.appx file

{{< figure src="/wp-content/uploads/2023/05/image-1.png" alt="" caption="" >}}

Install the extracted appx file

```
Add-AppxPackage -Path .\Microsoft.UI.Xaml.2.7.appx
```

You may also get this error when you try to install winget

_Windows cannot install package Microsoft.DesktopAppInstaller\_1.19.10173.0\_x64\_\_8wekyb3d8bbwe because this package depen  
ds on a framework that could not be found. Provide the framework "Microsoft.VCLibs.140.00.UWPDesktop" published by "CN=  
Microsoft Corporation, O=Microsoft Corporation, L=Redmond, S=Washington, C=US", with neutral or x64 processor architect  
ure and minimum version 14.0.30704.0, along with this package to install. The frameworks with name "Microsoft.VCLibs.14  
0.00.UWPDesktop" currently installed_

You can download _Microsoft.VCLibs.140.00.UWPDesktop_ here: [https://aka.ms/Microsoft.VCLibs.x64.14.00.Desktop.appx](https://aka.ms/Microsoft.VCLibs.x64.14.00.Desktop.appx)

Install Microsoft.VCLibs.x64.14.00.Desktop with this command:

```
Add-AppxPackage -Path .\Microsoft.VCLibs.x64.14.00.Desktop.appx
```

And now you should install the winget application without errors:

```
Add-AppxPackage -Path .\Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle
```

Happy installing :)
