---
author: thomasf
categories:
  - powershell
date: "2022-10-04T12:24:34+00:00"
guid: https://blog.wapnet.nl/?p=2079
parent_post_id: null
post_id: "2079"
title: Use PowerShell Invoke-WebRequest to login on a website
url: /2022/10/use-powershell-invoke-webrequest-to-login-on-a-website/

---
To automate some tasks with PowerShell on a website you sometimes need to log in. Today I tried some curl and postman tricks but it isn’t hard if you know what to script with PowerShell and bypass all other tools.

First, find a website to log in to, then check the page source and what the submit button does. In this example, it is “Inloggen” (dutch for login).

{{< figure src="/wp-content/uploads/2022/10/image-2.png" alt="" caption="" >}}

Then start the developer tools (F12), select the network tab, enter the credentials and login.

{{< figure src="/wp-content/uploads/2022/10/image.png" alt="" caption="" >}}

Now check the POST request in the developer tools.

{{< figure src="/wp-content/uploads/2022/10/image-1.png" alt="" caption="" >}}

The important things on this login form are:

- Gebruikersnaam (username)
- Wachtwoord (password)
- `__RequestVerificationToken`

Now we can write a simple script

```
$LoginUri = "https://example.website.nl/versie6-0-0/mijnscore/Login"
$BackendUri = "https://example.website.nl/mijnzwemscore/inhaalles.asp"
# ==========================================
$LoginResponse = Invoke-WebRequest -Uri $LoginUri -SessionVariable "Session"
$LoginBody = @{
    __RequestVerificationToken = $LoginResponse.InputFields[1].value
    Gebruikersnaam             = "EnterUsername"
    Wachtwoord                 = "EnterPassword"
    Submit                     = "Inloggen"
}
$LoginResponse = Invoke-WebRequest -Uri $LoginUri -WebSession $Session -Body $LoginBody -Method "POST"

Invoke-WebRequest -Uri $BackendUri -WebSession $Session
```

Explanation of the script:

1. Open the website and find out what the `__RequestVerificationToken` must be
1. Create a body with the credentials, the login form submit and the `__RequestVerificationToken`
1. Do the actual login and save the web session (cookies and stuff).
1. Now we can use the previous web session to check all the backend stuff

## **Edit: 10-5-2024**

In the comments I get 2 questions from Laerte Junior:

1. How do I get the `$LoginUri`
1. How do I get the `$BackendUri`

Let start with the first one. In this example I use Firefox and the zwemscore example

Press `F12` (Developers Options)

Now Login to the website and check the POST URL (right click copy)

{{< figure src="/wp-content/uploads/2024/05/image-7.png" alt="" caption="" >}}

and you get the `$LoginUri`

When you do an successful login you can see all the backend URI's. In my case was "Les Inhalen" the one I want to scrape the data from. So I click "Les Inhalen"

{{< figure src="/wp-content/uploads/2024/05/image-3.png" alt="" caption="" >}}

And I get the `$BackendUri`

{{< figure src="/wp-content/uploads/2024/05/image-8.png" alt="" caption="" >}}

Now run the first 3 lines from the script in PowerShell

```
$LoginUri = "https://thelocalgym.zwemscore.nl/versie6-0-0/mijnscore/Login"
$BackendUri = "https://thelocalgym.zwemscore.nl/mijnzwemscore/inhaalles.asp"
$LoginResponse = Invoke-WebRequest -Uri $LoginUri -SessionVariable "Session"
```

And check the `$LoginResponse.Inputfields`

{{< figure src="/wp-content/uploads/2024/05/image-5.png" alt="" caption="" >}}

In our case we need:

{{< figure src="/wp-content/uploads/2024/05/image-9.png" alt="" caption="" >}}

1. \_\_RequestVerificationToken
1. Gebruikersnaam (username)
1. Wachtwoord (Password)

Because we know the username and password the only dynamic thing is `__RequestVerificationToken`

So we can use 2 different ways to get the data.

The Dynamic way: `($LoginResponse.InputFields | Where-Object {$_.name -like "__RequestVerificationToken"}).value`

-OR-

The Array way (quick 'n dirty): `$LoginResponse.InputFields[6].value`

{{< figure src="/wp-content/uploads/2024/05/image-6.png" alt="" caption="" >}}

Quick 'n dirty

```
$LoginUri = "https://thelocalgym.zwemscore.nl/versie6-0-0/mijnscore/Login"
$BackendUri = "https://thelocalgym.zwemscore.nl/mijnzwemscore/inhaalles.asp"
# ==========================================
$LoginResponse = Invoke-WebRequest -Uri $LoginUri -SessionVariable "Session"
$LoginBody = @{
    __RequestVerificationToken = $LoginResponse.InputFields[6].value
    Gebruikersnaam             = "ExampleUser"
    Wachtwoord                 = "ExamplePass"
    Submit                     = "Inloggen"
}
$LoginResponse = Invoke-WebRequest -Uri $LoginUri -WebSession $Session -Body $LoginBody -Method "POST"

$response = Invoke-WebRequest -Uri $BackendUri -WebSession $Session

$response.RawContent
```

Dynamic way (better)

```
$LoginUri = "https://thelocalgym.zwemscore.nl/versie6-0-0/mijnscore/Login"
$BackendUri = "https://thelocalgym.zwemscore.nl/mijnzwemscore/inhaalles.asp"
# ==========================================
$LoginResponse = Invoke-WebRequest -Uri $LoginUri -SessionVariable "Session"
$RequestToken = ($LoginResponse.InputFields | Where-Object {$_.name -like "__RequestVerificationToken"}).value
$LoginBody = @{
    __RequestVerificationToken = $RequestToken
    Gebruikersnaam             = "ExampleUser"
    Wachtwoord                 = "ExamplePass"
    Submit                     = "Inloggen"
}
$LoginResponse = Invoke-WebRequest -Uri $LoginUri -WebSession $Session -Body $LoginBody -Method "POST"

$response = Invoke-WebRequest -Uri $BackendUri -WebSession $Session

$response.RawContent
```

Happy login :)
