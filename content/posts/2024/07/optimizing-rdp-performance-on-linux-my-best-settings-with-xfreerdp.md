---
author: thomasf
categories:
  - linux
  - windows
date: "2024-07-27T21:01:14+00:00"
guid: https://blog.wapnet.nl/?p=2183
parent_post_id: null
post_id: "2183"
title: 'Optimizing RDP Performance on Linux: My Best Settings with xfreerdp'
url: /2024/07/optimizing-rdp-performance-on-linux-my-best-settings-with-xfreerdp/

---
### XfreeRDP3

If you're like me and rely heavily on Remote Desktop Protocol (RDP) to connect to Windows servers from a Linux environment, you know how crucial performance can be. After experimenting with numerous settings, I've found a configuration that delivers the best performance using `xfreerdp`. Here’s a breakdown of the settings that worked wonders for me.

#### Why xfreerdp?

`xfreerdp` is an open-source RDP client that offers a plethora of customization options, making it a powerful tool for Linux users needing to connect to Windows servers. Its flexibility allows for fine-tuning, which is essential for optimizing performance.

#### My Go-To Command

Here is the `xfreerdp` command that gave me the best results:

```
xfreerdp3 /u:some_admin@some-domain.local /p:"P@ASSWRRRDDD" /v:10.10.10.10 /dynamic-resolution /compression /network:auto /gfx:AVC420:on +clipboard -themes
```

Let’s break down what each part of this command does:

- **/u:some\_admin@some-domain.local**: Specifies the username to use for the connection.
- **/p:"P@ASSWRRRDDD"**: Specifies the password. Ensure this is securely stored and managed.
- **/v:10.10.10.10**: The IP address of the Windows server.
- **/dynamic-resolution**: Adjusts the screen resolution dynamically to match the size of the `xfreerdp` window.
- **/compression**: Enables compression to reduce the amount of data transferred, improving performance over slower connections.
- **/network:auto**: Automatically adjusts settings based on network conditions for optimal performance.
- **/gfx:AVC420:on**: Uses the AVC420 codec for efficient video compression, providing a good balance between quality and performance.
- **+clipboard**: Enables clipboard sharing between the local and remote systems.
- **-themes**: Disables desktop themes on the remote server to reduce the amount of graphical processing required.

#### Additional Tips for Improved Performance

To enhance your Remote Desktop (RDP) experience from Linux, adjusting the performance settings on the Windows server can make a big difference. Here’s a quick guide:

1. **Open System Properties**:

- Right-click on "This PC" or "Computer" and select "Properties".
- Click on "Advanced system settings".

1. **Adjust Performance Options**:

- In the System Properties window, under the "Advanced" tab, click "Settings" in the Performance section.
- In the Performance Options window, select "Custom" and adjust the settings as shown in the screenshot below.

1. **Recommended Settings**:

- Uncheck unnecessary visual effects like animations, shadows, and Peek.
- Check only essential items for a smoother experience.

Refer to the screenshot for detailed settings adjustments.

By tweaking these settings, you can significantly improve the responsiveness of your RDP sessions.

{{< figure src="path-to-your-screenshot" alt="Performance Options" caption="Performance Options" >}}

{{< figure src="/wp-content/uploads/2024/07/image.png" alt="" caption="" >}}

#### Conclusion

Finding the right settings for `xfreerdp` can be a game-changer for your remote desktop experience on Linux. The command and tips I’ve shared should help you achieve a smoother and more responsive connection to your Windows servers. Don’t hesitate to tweak these settings further based on your specific network conditions and requirements.

Happy remoting!

* * *
