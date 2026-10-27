---
title: "From PRTG to Open Source Monitoring: Why I Picked Zabbix"
date: 2026-10-22T12:00:00+02:00
url: /2026/10/from-prtg-to-open-source-monitoring-why-i-picked-zabbix/
author: Thomas Faddegon
categories:
  - monitoring
  - docker
  - linux
tags:
  - howto
  - linux
cover:
  image: cover.jpg
  alt: A smiling sysadmin carries a box of old analog gauges across a bridge toward a bright monitoring dashboard with green charts, server racks and a small cloud cluster
---
**The Goal**

PRTG has been my bread and butter for years. I do PRTG consultancy, hosting and training, so this post is not a "PRTG is bad" rant. It isn't. It's a very good product, and for a lot of customers it's still the right choice.

But I wanted to know what open source can do in 2026. I mean really free: no licence per sensor, no "community edition" with the good stuff behind a paywall. So I wrote down what PRTG does for me today and went shopping.

**What PRTG Does for Me**

- A probe in the customer network that connects *out* to my self-hosted core server.
- All management happens centrally on that server.
- Auto-discovery is switched on.
- It's easy for end users. Some customers build their own dashboards.
- Lots of preconfigured sensors.
- I pull data out of the PRTG API and build my own reports.
- Customers can add their own devices and sensors.
- Alerting just works and is easy to set up.

That last bit, plus the DIY part for customers, is where PRTG really shines. Keep that in mind.

**The Contenders**

I already had a hunch that Zabbix could do everything technically. My worry was the customer DIY part, because Zabbix isn't exactly known for being user friendly. So I had a broad comparison done against the official docs of each project. The short version:

- **Zabbix**: an *active* proxy connects out to the server, buffers data during an outage, and does discovery locally. That's the closest thing to a PRTG remote probe. Huge template library, strong API, mature alerting. AGPLv3, free for commercial use.
- **Checkmk Community** (formerly Raw): great service discovery and the slickest UI of the bunch. But in distributed mode the central site connects *to* the remote sites, and a remote site is a full Checkmk install, not a lightweight probe. Checkmk itself says monitoring other organisations needs the commercial multi-tenancy edition.
- **NetXMS**: the underdog. An agent can tunnel out and act as a proxy for a whole customer network, with active and passive discovery and fine-grained object ACLs. Smaller ecosystem and fewer ready-made templates.
- **OpenNMS Horizon**: excellent remote Minions, but heavy and very NOC-oriented. Better when you manage everything yourself.
- **Icinga 2**: solid satellites that can connect outward, but no PRTG-style network scan out of the box, and many moving parts.
- **LibreNMS**: great SNMP discovery, but its own docs say distributed polling is *not* meant for remote polling. Every poller needs the central database, Redis and RRDCached.
- **Centreon Open Source**: free pollers, but integrated auto-discovery is a licensed module. That takes away a big part of the PRTG convenience.
- **Pandora FMS Community**: the old community branch has ended, so it's off the list.
- **Prometheus + Grafana**: technically capable, but you end up building your own monitoring platform. Scheduled PDF reporting in Grafana is Enterprise.
- **Netdata**: nice for hosts, but the current UI and Cloud are not open source.

**The Catch: Multi-Tenancy**

None of them gives you hard customer isolation in one shared, free instance. In Zabbix you build it out of user groups, host groups and roles. That works fine for read-only customers. But if a customer gets admin rights to add their own hosts, it gets fragile. In Zabbix 7.4 a user can even see and pick *any* proxy; the fix is planned for 8.0.

Then the obvious thing hit me: if the software costs nothing, why share it at all? **My advice: a separate Zabbix server per tenant.** Their own database, frontend, users, dashboards and proxy. That gives you the most flexibility: customers can get far more rights without any risk to other customers, and you can upgrade, tune or move each one on its own schedule. Reporting just talks to more than one API. The price is a few more updates, and that can be automated.

**Feeling It for Myself**

Docs don't tell you how a product *feels*. So I spun up Checkmk Community and NetXMS in Docker next to a small SNMP test device and onboarded it myself.

Honest verdict: Checkmk looks a lot slicker. But it has a learning curve too. Once both have a learning curve, Zabbix's active proxies, templates, API and alerting weigh more. So for me Zabbix is the best one-to-one PRTG replacement.

**The Pilot: Zabbix in Docker**

For the pilot I took a hosting cluster at OVH that runs on Nutanix. One new Ubuntu 24.04 VM with 2 vCPU, 8 GB RAM and 64 GB disk, which matches the official Zabbix sizing guide for a small install. On it, the stack Zabbix recommends for containers: separate server, web and database containers. Nothing more. No Java gateway or SNMP trap receiver until I actually need them.

```yaml
services:
  postgres:
    image: postgres:16-alpine
    env_file: .env
    volumes:
      - pgdata:/var/lib/postgresql/data
    restart: unless-stopped

  zabbix-server:
    image: zabbix/zabbix-server-pgsql:ubuntu-7.4-latest
    env_file: .env
    depends_on: [postgres]
    restart: unless-stopped

  zabbix-web:
    image: zabbix/zabbix-web-nginx-pgsql:ubuntu-7.4-latest
    env_file: .env
    ports:
      - "8080:8080"
    depends_on: [zabbix-server]
    restart: unless-stopped

volumes:
  pgdata:
```

Pin the major version (7.4 here) instead of `latest`, so a `docker compose pull` never surprises you with a major upgrade.

The rest of the basics:

- Change the default `Admin` password *before* anything goes public.
- A daily PostgreSQL and config backup with 14 days retention.
- A firewall that only lets the HAProxy VM reach the web port, and SSH only via the jump host.
- A reboot test: containers, firewall and backup timer all have to come back on their own.

**Behind HAProxy**

The cluster already had an HAProxy VM doing TLS offload, with a wildcard certificate for the subdomain the other tools live under. So no new proxy and no new certificate. Just one more backend that routes the Zabbix hostname to port 8080 on the new VM. Validate before you reload, and check that an existing route still works afterwards:

```bash
sudo cp /etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg.bak
sudo haproxy -c -f /etc/haproxy/haproxy.cfg && sudo systemctl reload haproxy
```

**Filling It Up**

Then the fun part: get as much of the cluster into Zabbix as access allows.

- **Linux VMs and Docker**: Zabbix agent 2 on every Linux VM I could reach with sudo, via one small script. Add the `zabbix` user to the `docker` group and the Docker template discovers the containers.
- **HAProxy**: a stats page bound to `127.0.0.1:8404` only, for the "HAProxy by Zabbix agent" template. On top of that, certificate expiry checks that alert when a certificate has less than 14 days left.
- **Websites**: HTTP checks with a `Host` header to HAProxy's internal address, because the public IP doesn't loop back from inside.
- **Nutanix VMs**: a Prism Central v3 API discovery rule that creates a host per VM with ping, power state, vCPU and RAM. A VM that's switched off raises an alert, and new VMs show up on their own.
- **Nutanix cluster**: the official **Nutanix Prism Element by HTTP** template. It discovers the cluster and every node and creates hosts for them, with storage, IOPS, latency and Nutanix's own alerts.

The agent config is a small drop-in, so the main config file stays untouched:

```ini
# /etc/zabbix/zabbix_agent2.d/server.conf
Server=<zabbix-vm-ip>,<docker-bridge-subnet>
Hostname=<host-name>
```

Comment out `Server`, `ServerActive` and `Hostname` in the main `zabbix_agent2.conf`, because duplicate keys stop agent 2 from starting.

**The Nutanix Gotcha**

The official template talks to **Prism Element**, not Prism Central. The account I had was a Prism Central account, and Prism Element simply returned a 401. The fix: create a read-only local user on Prism Element. You can do that through Prism Central's proxy, which passes the call to the cluster:

```bash
curl -k -u <pc-admin> -X POST \
  "https://<prism-central>:9440/PrismGateway/services/rest/v1/users?proxyClusterUuid=<cluster-uuid>" \
  -H 'Content-Type: application/json' \
  -d '{"profile":{"username":"zabbix","firstName":"Zabbix","lastName":"Monitoring","emailId":"monitoring@example.com","password":"<generated>","locale":"en-US"},"enabled":true}'
```

That user gets `ROLE_CLUSTER_VIEWER` by default, which is all the template needs. On the Prism Element host in Zabbix, set `{$NUTANIX.PRISM.ELEMENT.IP}` and `{$NUTANIX.USER}`, put the password in a *secret* macro `{$NUTANIX.PASSWORD}`, and set `{$HTTP.TLS.VERIFY}` to `none` for the self-signed certificate. The official template doesn't cover VMs, so I kept my own Prism Central discovery for those.

**It Paid Off Right Away**

Within minutes Zabbix flagged real issues nobody had noticed yet: a VM that Nutanix reported as running but didn't answer ping, two HAProxy backends failing their health checks, and a site returning a 503. That's exactly what you want from a pilot.

**The Fine Print**

- The agents run passive only for now, because the server's trapper port isn't published from the Docker stack.
- Windows servers are on ping only for the moment. Agent 2 is the way to go. If you're not allowed to install an agent, Zabbix can also run PowerShell over OpenSSH with *SSH agent* items, but then every metric is command output you parse yourself.
- A firewall without SNMP enabled stays on ping too. Once SNMP is on, there's a template waiting.
- Some template quirks, such as NIC speed `-1` on virtual NICs, are template noise. Don't chase them.
- Customer self-service still has to be proven with a real pilot customer. That's the next step.

**Three Takeaways**

1. Write down what your current tool actually does for you *before* you compare. "Outbound probe" and "customers add their own sensors" ruled out half the list for me.
2. When the software is free, run a separate server per tenant. It turns the hardest problem (multi-tenancy) into a bit of extra patching and gives you the most flexibility.
3. Read the template docs. The Nutanix template needs a Prism Element account, not Prism Central. One read-only user fixed it.

PRTG still does the "easy for end users" part better out of the box. I'll keep supporting it for customers who value that. But for my own hosting, Zabbix is a serious and very free contender.

*Full disclosure: I did the research and the pilot together with my AI assistant. It read a lot of documentation so I didn't have to.* 😉

Happy monitoring!
