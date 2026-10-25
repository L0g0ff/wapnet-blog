---
author: thomasf
categories:
  - linux
  - powershell
  - windows
date: "2022-04-05T07:33:51+00:00"
guid: https://blog.wapnet.nl/?p=2045
parent_post_id: null
post_id: "2045"
title: Powershell better tab autocomplete
url: /2022/04/powershell-better-tab-autocomplete/

---
With Powershell ISE you can use CTRL + SPACE for auto completion.

{{< figure src="/wp-content/uploads/2022/04/image.png" alt="" caption="" >}}

But when you work in a native Powershell window you don't have this option. And many often you cycle with tab completion trough the powershell and because you press the TAB button too soon you have to remove characters and cycle again trough all the commands.

Unit now ;-)

There is an easy fix you can implement so the Powershell have the same auto completion like bash.

- Type `notepad $profile` for Windows or `gedit $profile` for Linux
- Add the line `Set-PSReadlineKeyHandler -Key Tab -Function MenuComplete`

{{< figure src="/wp-content/uploads/2022/04/image-1.png" alt="" caption="" >}}

- Save the file and restart Powershell
- And now you have a much better working tab completion

{{< figure src="/wp-content/uploads/2022/04/image-5.png" alt="" caption="" >}}

{{< figure src="/wp-content/uploads/2022/04/image-4.png" alt="" caption="" >}}

Happy coding :)
