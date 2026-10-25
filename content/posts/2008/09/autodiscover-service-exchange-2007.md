---
_edit_last: "1"
author: thomasf
categories:
  - exchange
date: "2008-09-26T20:03:53+00:00"
guid: https://blog.wapnet.nl/?p=51
parent_post_id: null
post_id: "51"
tags:
  - autodiscover
  - exchange-2007
title: Autodiscover Service Exchange 2007
url: /2008/09/autodiscover-service-exchange-2007/

---
For Autodiscover, you actually have two options.

1\. Repeat the above process, with a new dedicated web site for autodiscover.
The command for a new Autodiscover virtual directory is

> New-AutodiscoverVirtualDirectory -Websitename Autodiscover -BasicAuthentication:$true -WindowsAuthentication:$true

That web site can then get its own SSL certificate.
This could be useful if you use two different domains, one for email and one for external facing web services. Autodiscover uses the same domain as your email.
However if you have multiple domains for email, you will need to use the redirect method.
2\. Add to the external web site and configure a redirect.

To add the Autodiscover virtual directory to the External web site created in above:

> New-AutodiscoverVirtualDirectory -Websitename External -BasicAuthentication:$true -WindowsAuthentication:$true

The redirection configuration is very important to ensure that it works correctly. The redirection method requires port 80 (http) traffic to come in. For internal traffic that is fine, but for external traffic you may want to look at a way of configuring the redirection using a public web site.

At the time of writing, this is Microsoft's article on redirection. It is covered under the section Hosted Environments and the Autodiscover Service, but would also be useful if you have more than one domain, or you use a different domain for email than you do for external facing web services.
