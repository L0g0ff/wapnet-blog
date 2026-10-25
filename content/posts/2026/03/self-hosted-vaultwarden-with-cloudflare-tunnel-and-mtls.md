---
author: thomasf
categories:
  - linux
  - networking
  - security
date: "2026-03-22T00:25:33+00:00"
guid: https://blog.wapnet.nl/?p=2272
parent_post_id: null
post_id: "2272"
title: Self-hosted Vaultwarden with Cloudflare Tunnel and mTLS
url: /2026/03/self-hosted-vaultwarden-with-cloudflare-tunnel-and-mtls/

cover:
  image: /images/covers/self-hosted-vaultwarden-with-cloudflare-tunnel-and-mtls.jpg
  alt: Home vault server connected through a secure tunnel to the cloud with two certificates shaking hands
---
I was using tailscale + vaultwarden before but I don't want to use a VPN connection to access my passwords. But I do want a client certificate for extra security.

So I write this to guide to exposing Vaultwarden securely via Cloudflare Tunnel, protected by mutual TLS (mTLS) client certificates. No open ports required.

_Please note: it looks like iOS bitwarden app don't have the option to import a mtls certificate_.

## Why this setup?

- No open ports on your router
- Cloudflare terminates TLS — no certificate management on your end
- mTLS ensures only devices with a valid client certificate can reach Vaultwarden
- The Bitwarden Android app supports client certificates natively since v2025.2.0

## Prerequisites

- A Synology NAS with Container Manager
- A domain managed by Cloudflare (e.g. `example.com`)
- Vaultwarden already running in Docker

* * *

## 1\. Vaultwarden configuration

Make sure your Vaultwarden container has these environment variables set:

```
DOMAIN=https://vault.example.com
SIGNUPS_ALLOWED=false
EXPERIMENTAL_CLIENT_FEATURE_FLAGS=mutual-tls

```

The `mutual-tls` feature flag tells the Bitwarden Android app to show the client certificate option in settings.

Verify it's active:

```
curl https://vault.example.com/api/config | grep mutual

```

You should see `"mutual-tls":true` in the response.

* * *

## 2\. Cloudflare Tunnel setup

### Create the tunnel

1. Go to [Cloudflare Zero Trust](https://one.dash.cloudflare.com) → Networks → Tunnels
1. Click **Create tunnel** → choose **Cloudflared**
1. Give it a name and copy the tunnel token

### Run cloudflared on Synology

Create `/volume1/docker/compose/cloudflared/docker-compose.yml`:

```
services:
  cloudflared:
    image: cloudflare/cloudflared:latest
    container_name: cloudflared
    restart: unless-stopped
    network_mode: host
    command: tunnel --no-autoupdate run --token YOUR_TUNNEL_TOKEN

```

```
cd /volume1/docker/compose/cloudflared
docker compose up -d

```

`network_mode: host` allows cloudflared to reach Vaultwarden via `localhost:5151`.

{{< figure src="/wp-content/uploads/2026/03/image-3.png" alt="" caption="" >}}

### Configure the public hostname

In the Cloudflare dashboard, under your tunnel → **Public Hostnames**:

FieldValueSubdomain`vault`Domain`example.com`Type`HTTP`URL`localhost:5151`

* * *

## 3\. mTLS client certificate

### Enable mTLS for your hostname

1. Cloudflare dashboard → your domain → **SSL/TLS → Client Certificates**
1. Under **Hosts**, add `vault.example.com`
1. Click **Create Certificate** → set validity (10 years recommended)
1. Download the certificate and private key

### Generate a .p12 file

```
openssl pkcs12 -export \
  -out vault-client.p12 \
  -inkey client.key \
  -in client.crt

```

Set a password when prompted — you'll need it when importing on your devices.

### Create the WAF rule

1. Cloudflare dashboard → your domain → **Security → Security rules → Custom rules**

{{< figure src="/wp-content/uploads/2026/03/image.png" alt="" caption="" >}}

1. Click **Create rule**
1. Click **Edit expression** and paste:

```
(not cf.tls_client_auth.cert_verified and http.host eq "vault.example.com")

```

1. Action: **Block**
1. Click **Deploy**

This blocks all requests without a valid client certificate before they reach Vaultwarden.

{{< figure src="/wp-content/uploads/2026/03/image-1.png" alt="" caption="" >}}

* * *

When you try to access the URL you get a nice big red cross :)

{{< figure src="/wp-content/uploads/2026/03/image-4.png" alt="" caption="" >}}

### Change the cache setting

I'll get a lot of 403 issues because of the caching. You can disable/bypass the cache in cloudflare:

{{< figure src="/wp-content/uploads/2026/03/image-8.png" alt="" caption="" >}}

## 4\. Install the certificate

### Firefox (Linux/Windows)

1. Open `about:preferences#privacy`
1. Scroll to **Certificates** → **View Certificates**
1. Tab **Your Certificates** → **Import**
1. Select `vault-client.p12` and enter your password

Firefox will automatically present the certificate when connecting to `vault.example.com`.

and then... :)

{{< figure src="/wp-content/uploads/2026/03/image-6.png" alt="" caption="" >}}

### Select Automatically

If you use Firefox best is to change the security.default\_personal\_cert setting in the about:config to **Select Automatically**

{{< figure src="/wp-content/uploads/2026/03/image-7.png" alt="" caption="" >}}

### Bitwarden Android app

1. Transfer `vault-client.p12` to your phone
1. Open the Bitwarden app → tap the server URL field → **Custom**
1. Set **Web vault server URL** to `https://vault.example.com`
1. Scroll to **CLIENT CERTIFICATE (MTLS)**
1. Tap **Import certificate** → select `vault-client.p12` → enter password
1. Tap **Save**

{{< figure src="/wp-content/uploads/2026/03/image-2.png" alt="" caption="" >}}

* * *

## 5\. Verify

Open `https://vault.example.com` in Firefox — you should be prompted to select your certificate. After confirming, the Vaultwarden login page loads.

Without a certificate, or with an invalid one, Cloudflare returns HTTP 403 before the request ever reaches your server.

* * *

## Notes

- Generate a separate `.p12` per device so you can revoke individual certificates if needed
- The Cloudflare free plan supports mTLS with up to 5 custom rules
- Vaultwarden data is end-to-end encrypted by the Bitwarden client — Cloudflare only sees encrypted vault traffic
- Keep your Vaultwarden container updated; use Watchtower or a scheduled pull for automatic updates
