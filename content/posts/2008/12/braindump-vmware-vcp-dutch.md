---
_edit_last: "1"
author: thomasf
categories:
  - uncategorized
date: "2008-12-17T13:05:40+00:00"
dsq_thread_id: "5136177659"
guid: https://blog.wapnet.nl/?p=158
parent_post_id: null
post_id: "158"
title: Braindump VMWare  VCP (Dutch)
url: /2008/12/braindump-vmware-vcp-dutch/

---
VMWare kernel controleerd de volgende phisical hardware:
Memory (Not RAM), Physical processors, storage & networking controllers

Default iscsi port:
3260
Iana:
iscsi-target    3260/tcp   iSCSI port
iscsi-target    3260/udp   iSCSI port

Iscsi ondersteund geen clustering

Hoe ESX Serer de resources beheerd:
Elke VM heeft zijn eigen CPU, Memory, bandbreedte en storage. ESX gegaraneerd de vm's hun shares a.d.h.v:
\- Availeble resources
\- Reservation, limit of shares van de VM
\- Aantal active vm's op de ESX
\- Reservation, limit of shares van de resource pool
\- Overhead van het beheren van de virtualiatie

Als een VM te weinig resources in zijn resource pool heeft en de resources zijn ingesteld als expanceble dan zal
de VM proberen de resources te krijgen van de bovenliggende resource pool. Wanneer die ook te weinig resources heeft
zal de VM niet gestart kunenn worden

De minumum LUN capaciteit voor VMFS3 = 1200 mb

Storage zoning heeft de volgende uitwerkingen:
\- Beheerd & ISOleerd de paden binnen de storage fabric
\- Schroeft het aantal active LUN's terug. Je kunt met deze namelijk scheiden (isoleren)
\- Zorgt ervoor dat andere systemen buiten de SX servers niet bij de data kunnen.
\- Zorgt ervoor dat je de omgevingen kunt scheiden. Een testomgeving van een productie omgeving bijvoorbeeld
\- Kan je toegang tot een LUN verlenen of blokkeren.

ESX heeft de volgende systeemeisen:
\- Minstends 2 processoren van 1500Mhz van Intel Xeon of AMD Operon of AMD 64 x2 dual core processors
\- 1 Gig RAM
\- 1 of meerdere netwerk kaarten
\- Een SCSI disk, Glasvezel LUN, RAID LUN met ongepartioneerde ruimte

Na het koppelen van een SAN LUN naar een VM moeten de volgende gegevens worden opgegeven:
\- The Virual device mode (SCSI poort)
\- The Compatibility mode (Persistant or non persistant)

Je kan maximaal 512 poort groepen hebben op een single host

Wanneer je een slechte VM performance hebt als je twee cpu's hebt (bijv 3 & 4 die vast gepint staan met 100% reservation) zorg er dan voor
dat je 1 & 5 pakt zodat ze alle twee op een apparte fysieke CPU draaien.

Loadballancing binnen VMWare kan op verschillende manieren:
\- Route based on IP hash - Kies een upling aan de hand van een IP bron of doel pakke
\- Route based on **source** MAC hash - Kies een uplink aan de hand van de hash of van het source netwerkkaart
\- Route based on the originating virtual port ID - Kies een uplink gebasseerd op een virtuele port waar het  verkeer de virtuele switch ingaat

Wat is er vereist aan een cold migration van een VM
De VM moet uit staat (doh)

In een VI 3 omgeving maakt iSCSI gebruik van de volgende dynamisch discovery:
\- gebruikt send targets verzoeken (requests)
\- Dynamische discovery is de enige discovery optie voor de software initiators

Per ESX server kun je maximaal 64 iSCSI targets gebruiken

Per ESX server kun je maximaal 127 Vswitches gebruiken

Geldige iSCSI namen zijn:
\- IQN (iSCSI qualified name) iqn.<year-mo>.<reversed\_domain\_name>:unique\_name
\- EUI (Extended Unique Identifier) eui.<16 karaktername>  24 bits voor bedrijfsnaam, 40 bits voor een unieke ID zoals een serial nummer

In een DRS cluster zul je de volgende 3 stappen uit moeten voeren om een VM te maken:
\- Kies of jee een typische of cutom VM aan wilt maken
\- Selecteer de resource pool waar je de VM wilt draaien
\- Selecteer de datastore waar je de VM neer wilt planten

Virtual Center 2.5 ondersteund de volgende databases:
\- MS SQL 2005
\- MS SQL 2000 met SP4
\- Oracle 9iR2, 10gR1 en 10gR2

Booten van een SAN heeft de volgende voordelen:
\- Goedkopere servers
\- Makkelijker om de servers te vervangen
\- Minder verspeelde ruimte (lokale ruimte ben je anders altijd kwijt)
\- Makkelijker om de servers te backuppen
\- Betere beheersbaarheid

Het upgraden van een ESX server 2.x met VMFS2 naar VMFS3 en vervolgens het benaderen van de 2.x server heeft
de volgende consequentie:
\- Alle VM's op de ESX2 kunnen gewoon aangezet worden (rare vraag...)

Wanneer er in je DRS cluster achter een resource pool staat "Grafted from XYZ" betekend dit het volgende:
Als je het rechtstreeks vertaald wordt het zoiets als: samengevoegd uit host naam....

Voorbeeld:
Je hebt een host met Resource pool...
deze voeg je toe aan een drs cluster...
Je hebt dan de keuze om de host toe te voegen zonder de oude resource pools.. alle vm's en komen dus onder he cluster te staan..

wanneer je de keuze graft new pool (heet geloof ik zo) dan wordt er in het DRS cluster een resource pool gemaakt met de oude resource pool instellingen van de host.....

Welke netwerk services worden geleverd door de VMkernel?

\- Iscsi
\- NFS
\- VMotion

Rollen die **niet** standaard zijn in een VC omgeving:
\- Local only
\- Virtual center
\- Privledges

Shares specificeert de "relative priority" of de importance (belangrijkheid) van een VM

Wat is er nodig voor NIC teaming:
\- De virtuele switch moet meer dan 1 uplink bevatten

Kun je ESX van een shared lun laten opstarten
\- Nee dit gaat niet. Shared lun's zijn bedoeld voor meerdere ESX servers. Voor het booten van een LUN moet deze dedicated zijn

Maximums:
Maximaal 6 apparaten waarvan je de videokaart altijd kwijt bent. Je kunt dus maximaal 5 PCI apparten aansluiten.

De netwerk adaperts "panel" laat de volgende gegevens zien:
\- Appaaraatnaam        (VMNic1, Vmnic2)
\- Speed            (100/1000Mbit)
\- Configured        (Auto/Full)
\- vSwitch
\- Networks        (Netwerk namen)

[![](/wp-content/uploads/2008/12/network-adapters-panel-vmware-sensored.jpg)](/wp-content/uploads/2008/12/network-adapters-panel-vmware-sensored.jpg)

Een geldige reden om CPU Affinity (pinnen van CPU's) te gebruiken is omdat deze gegevens niet meegenomen worden door VMotion

Wanneer de "reservation type" is FIXED, zal VMWare altijd controleren of de resource pool zelf genoeg ongereserveerde resources heeft.
Is dit het geval dan zal de actie uitgevoerd worden. Is dit niet het geval zal je in de GUI een melding krijgen dat er te weinig
resources zijn.

Echter wanneer de reservation type "expandeble" is zal VMWare controleren of er genoeg ruimte is in de pool. Is er genoeg ruimte
dan zal de VM gestart kunnen worden. Is er te weinig dan zal de VM gaan kijken of er genoeg ruimte is in de bovenliggende
resource pool. Is daar genoeg ruimte dan zal de VM gestart worden. Is dat te weinig ruimte dan zal VMware de actie afbreken en
hier een melding van geven.

"Admision control" is het daadwerkelijke controleren van het starten van de VM op resources

Wanneer een CPU een minuut of 10 staat te stampen op 1,5Ghz en je wilt deze tijd verkorten dan kun je de CPU Limit verhogen, de CPU
affinity resetten naar default (= gelijk aan geen affinity = alle cpu's gebruiken) of de CPU resevation opschroeven

Het maximale VMFS3 volumes wat een ESX server aan kan is 256 en de max grootte is 2TB. Verder is het max aantal lun's
ook 256 stuks. Het aantal Maximale SCSI controllers ligt op 16. En het maximaal aantal LUN paden ligt op 32.

In een fully automatic DRS cluster kun je zorgen dat 2 machines altijd bij elkaar staan, nooit bij elkaar staan of nooit verhuist
worden naar een andere ESX server binnen het cluster. Volgens de examenvragen moet je de Affinity wizard starten. Ik vind het
niet echt een wizard maar je bepaald het met regels in een simpel kolommetje. Als je met de rechtermuis op je cluster klikt > edit settings > DRS. Dan heb
je daar "rules" en "Virtual Machine Options". Binnen de VM options kun je aangeven hoe snel je DRS wilt inzetten of dat je
dit helemaal niet wilt gebruiken op een "per host basis". Binnen de rules kun je opgeven of 2 VM's altijd samen of juist gescheiden
moeten worden.

Wanneer je binnen je DRS cluster in de advanced option report\_section=8 opgeeft dan wordt VMotion binnen het hele cluster uitgezet.

De waardes van traffic shaping op een Vswitch zijn:
\- Burst size
\- Avarage bandwith
\- peak bandwith

om een alarm te mogen aanmaken moet je lid zijn van een administrator groep. Dit mag een Resource pool admin, een virtual ma-
chine admin of een datacenter admin zijn.

Wanneer er wordt gewerkt met shares let dan op ht volgende.
vma    =    2000 shares
vmb    =    4000 shares

totaal is dus 6000 shares. wanner er wordt gevraagd hoeveel procent van de resources vma mag gebruiken is dat dus 33%

virtual server center gebruikt de poorten 27000 en 27010 om te kunnen communiceren met de license server.

je kunt niet 2 hosts verplaatsen tussen 2 verschillende datacenters. Ook niet wanneer deze door de zelfde virtual center beheerd worden.
Het zelfde geldt voor dubbele namen. Deze mogen wel voorkomen in 2 verschillende datacenters maar niet in het zelfde.

VMFS gebruikt short-lived SCSI reservation tijdens het wijzigen van de metadata op het file system.

Rechten groepen ESX:
\- Administrators
\- Read only
\- No access

Rechten groepen Virtual Center:

\- No access
\- Read only
\- Administrator
\- Virtual machine administrator
\- Virtual machine power user
\- Virtual machine user
\- Datacenter Administrator
\- Resource pool administrator

Rollen zijn dus verdeeld in default esx, Vm, Resource en Datacenter admins.
Dan heb je op VM niveau de power user, de user

Full access, admin readonly groupen zijn rommel. Daar heb je de readonly groep voor...

De core en basic management servers zijn:
\- Task scheduler                    Wanneer voer VC taak X uit. Bijvoorbeeld vmotion
\- VM Provisioning                    Het bevoorraaden van de VM (Harware, memory etc)
\- Host & VM Configuration                Het configureren van de ESX en VM's
\- Resources & Virtual machine inventory management    DRS is een mooi voorbeeld
\- Statics & Logging                    Logging met grafieken etc
\- Alarm & Events management                triggeren van de alarms en lgging onderin

\-\-\-\-\- k\*tstuk ------ (Meer info VMWare resource management guid pdf)
Mem.SamplePeriod houdt in hoevaak een server gemonitord wordt op memory activiteiten/gebruik. De standaard waarde is 60sec.
Mem.BalancePeriod houdt in hoe vaak de memory opnieuw ingedeeld wordt. Het opnieuw indelen wordt ook meteen ingeschakeld wanneer er grote
wijzigingen in het vrije geheugen plaatsvinden. Default 15 sec

\\* Mem.SamplePeriod
\\* Specifies the periodic time interval, measured in seconds of the virtual machine's execution time, over which memory activity is monitored to estimate working set sizes.
\\* 60

\\* Mem.BalancePeriod
\\* Specifies the periodic time interval, in seconds, for automatic memory reallocations. Reallocations are also triggered by significant changes in the amount of free memory.
\\* 15

Mem.CtlMaxpercent is het maximaal aantal procent wat de ballooning driver aan memory kan verwerken. 65% is default waarde
Mem.ShareScanVM geeft een rating hoe groot de kans is of een VM zijn memory moet delen met andere VM's. Standaard waarde = 50
Mem.ShareScanTotal specificeerd het system-wide rate welk  geheugen er gescand moet worden voor transparante page shareing mogelijkheden
De waarde (rate) is het aantal pages wat er per seconden gescant moet worden. Standaard waarde is 200 pages per sec.

'Memory tax' (Mem.IdleTax) helpt voorkomen dat virtual machines te veel geheugen opslurpen (hoarding) door Idle memory terug te geven aan de ESX
host. Het verschil tussen memory idle tax en de ballooning driver is dat de balloning driver op de guest os draait en gebruikt maakt van de
page file van het OS. Memory Tax doet dit op VM Niveau en heeft ook geen driver nodig. Standaard waarde van Idle.tax = 75

Mem.Balanceperiod:
Specificeerd de periode in seconden voor automatische opnieuw indeling (reallocations)
Reallocations worden ook gebuikt voor wijzigingen in het vrije geheugen
Standaard waarde = om de 15 seconden
\-\-\-\-\- k\*tstuk ------

3 elementen van Layer 2 Security binnen de ESX omgeving zijn:
\- Promiscouus mode    (accept/reject)    Wanneer deze op accept staat worden alle pakketen op de vSwitch binnenkomen ook op deze mac gemikt (ideaal voor sniffing)
\- Mac address changes (accept/reject)    Wanneer deze op reject staat zal VMWare geen andere MAC's toestaan dan die in de VMX config file gedefinieerd staan
\- Forget Transmits    (accept/reject)    Alle uitgaande MAC adres pakketten anders dan het daadwerkelijke mac adres worden gedropt.

Een SAN LUN moet op Virtual Compatibility mode staan om snapshots te kunnen maken.

Wanneer een ESX server geen gedeelde storage heeft zal deze een VMFS paritie en een VMKCORE partitie aan moeten maken.
De VMFS volume wordt vervolgens gemount onder /vmfs/volumes. De vmkcore wordt niet gemount. Dit lijkt een beetje op een linux swap file
alleen staat hier de kernel ook geparkeerd...

De VMCore paritie wordt ook gebruikt voor het dumpen van de logging & de store core dumps (purple screen of death)

Wat zijn redenen om van je SAN te booten ipv via local storage:
\- Geen onderhoud op locale storage
\- Makkelijke clonen van service consoles
\- Diskless hardware configuratie zoals sommige blade systemen

De twee methodes op iSCSI te benaderen zijn:
Active/Active
Active/Pasive

Wanneer 1 VM crasht zal de dump altijd worden opgeslagen tussen de overige files VM files. Het zou ook raar zijn dit ergens anders op te slaan
want je zoekt je een ongeluk anders.

Wanneer 2 VM's in aan dezelfde vSwitch gekoppeld zijn heeft de data uitwisseling: Route Locally. Route internally is FOUT.

De minimale versie waar de Virtual Center op draait is Windows 2000 SP4 Met update rollup 1

Een virtual machine kan in 2 manieren draaien. In de direct execution mode en in de Virtualisation mode. Het verschil tussen beide is dan de
direct execution mode rechtstreeks op de CPU draait.

Een reden geen processor affinity te gebruiken is omdat het genegeerd wordt door VMotion

Virtual Machine Storage:
\- Gaat tot 4 hostadapters per VM
\- Gaat tot 15 targets per bus adapter
\- Gaat tot 60 targets per VM, 256 targets tegelijk in alle VM's per ESX server

De eisen van een VMWare consolidated backup zijn (proxy):
\- De server moet een fysieke server zijn
\- Het OS moet windows zijn

Met VMWare betaal je per fysieke CPU. Hoe meer cores dus hoe beter :) Voor VMotion moet je ook betalen. Ook per fysieke CPU.

Wanneer HA en DRS op de server actief zijn en een server crasht dan wordt het DRS algorithme op HA toegepast.

De volgende ESX management processen en services draaien in de server console:
\- hostd        Stuur de actie in het service console aan met de VI client
\- VMauthd    Authoriseerd alle remote users die met de VI client aanmelden. Koppelingen met andere authorisatie meganismen zijn ook
toegestaan. LDAP en PAM bijvoorbeeld
\- net-snmpd    Hiermee kun je met elke SNMP tool de ESX server beheren.

een vwitch heeft de volgende policies:
\- Layer 2 security policy
\- Traffic shaping
\- Loadballancing en Failover Policy

De volgende types worden gebruikt voor SCSI bus sharing
\- Geen        Virtual Disks kunnen niet geshared worden met andere virtual disks
\- Virtual    Virtual disks kunnen geshared worden met andere VM's op dezelfde server
\- Physical    Virtual disks kunnen geshared worden door VM's op alle servers

De volgende policies zijn van toepassing op Nic Teaming > Load ballancing:
\- Route based on the originating virtual port ID
\- Route based on IP hash
\- Route based on source MAC hash
\- Use explicit failobver order

Wat zijn de 3 verschillende physieke implemantatie alternatieven op SCSI devices gepresenteerd als een scsi targt:
\- Virtual Machine .vmdk bestand opgeslagen op een VMFS volume
\- Lokaal SCSI apparaat rechtstreeks op de VM
\- Apparaat mapping via een SAN LUN

De volgende besturings systemen zijn voldoende voor een VC Licentie server:
\- Windows 2003
\- XP met SP2
\- Windows 2000 met SP4

Als een Virtuele Virtual Center server crash bijvoorbeeld door een power outage dan zal deze  met HA automatisch
gestart worden door een andere host.

Je hebt 2 netwerk types of netwerk serices in ESX nodig (meestal voor de scheiding tussen iscsi)
\- Verbind het VM netwerk rechtstreeks met het fysieke netwerk
\- Verbind de VMKernel services rechstreeks met het fysieke netwerk

VMotion kan uitgevoerd worden op SAN, NAS & iSCSI

De geadviseerde policy voor Active/Passive is Must Recently Used (MRU)
