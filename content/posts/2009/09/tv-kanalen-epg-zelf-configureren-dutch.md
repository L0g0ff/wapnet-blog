---
_edit_last: "1"
author: thomasf
categories:
  - media-center
date: "2009-09-16T22:19:54+00:00"
dsq_thread_id: "5136178152"
guid: https://blog.wapnet.nl/?p=227
parent_post_id: null
post_id: "227"
title: TV kanalen + EPG zelf configureren (Dutch)
url: /2009/09/tv-kanalen-epg-zelf-configureren-dutch/

---
**TV kanalen + EPG zelf configureren**

In de oorspronkelijke opzet van de EPG functie in MCE2005 heeft men het doel gehad de kanalen setup en programmagids in Mediacenter op (voor de gebruiker) zeer eenvoudige manier in te kunnen stellen: Simpelweg je postcode kiezen, je signaalbron instellen, info binnenhalen en klaar is kees, tenminste... dat was de bedoeling...

**Probleemstelling**
Op vele fora lees je verschillende problemen die oorsprong vinden in het niet up-to-date zijn van de zenderinformatie die aan je postcode verbonden is. Dit (kan) resulteren in zeer irritante verschijnselen zoals het niet corresponderen van kanalen met de EPG, ontbrekende kanalen etc.

Ik heb hier zelf ook een aanzienlijke tijd mee lopen stoeien. Submitten van wijzigingen bij Microsoft / BDE levert vaak geen of late updates op. Kortom: de voordelen van het hele principe achter het autmatisch kanaalinformatie binnenhalen + EPG zijn zo langzamerhand een nadeel geworden.

**Oplossing**
Ik heb na het nodige gepuzzel een oplossing die het volgende tot gevolg heeft:

-  Alle TV kanalen van (in mijn geval) de kabel zijn in MCE beschikbaar
-  Alle TV kanalen hebben de juiste naam
-  Alle TV signalen (waar beschikbaar) hebben correcte EPG informatie
-  Hiervoor is geen bijzondere extra software nodig, zodat je gauw weer terug kan naar je oorspronkelijke situatie als je dat wenst.

Mijn oplossing is gebaseerd op analoge kabeltelevisie met een interne tuner, je kan delen hiervan natuurlijk ook bij gebruik van externe settopboxen toepassen.

**De procedure in stappen**
Om eerlijk te zijn is de procedure tijdrovend, je bent al gauw een uurtje zoet. Het resultaat is er echter wel naar ![smile](http://www.degroeneknop.nl/forum/Smileys/dgk/smile.gif). Om de televisiekanalen + EPG zelf te configureren moeten de volgende stappen doorlopen worden:

-  Aanpassen van de MCE frequentietabel (MCETuningOverrides.xml)
-  Uitvoeren van een handmatige frequentiescan
-  Kanalen handmatig aan EPG toewijzen
-  Niet herkende kanaalnamen manueel toevoegen
-  Kanaalvolgorde naar wens indelen

Navolgend een beschrijving hiervan:

**Aanpassen van de frequentietabel**
De kanaaltabel waar Microsoft gebruik van maakt komt vaak niet overeen met de opgegeven kanaalnummers van de provider van het kabelsignaal. Dit is extra lastig wanneer deze provider gebruik maakt van + en – kanalen (waar dus finetuning nodig is). Je kan natuurlijk gewoon in MCE een scan maken, maar mijn ervaring is dat dit erg lang duurt, veel kanalen dubbel gevonden worden terwijl andere kanalen niet gevonden worden.

Doe daarom het volgende:

-  Zoek (op internet) het actuele zenderoverzicht van de CAI. Hier vind je ook de frequentie van de zenders. Het is handig hier een printout van te maken
-  Nummer op het uitgeprintte papier nu alle beschikbare kanalen in de gewenste volgorde
-  Edit de volgende file in je MCE: c:\\windows\\ehome\\MCETuningOverrides.xml met bijvoorbeeld notepad.
-  Maak voor de zekerheid vooraf even een backup van de oorspronkelijke file.
-  Je ziet nu de door Microsoft gekozen kanaalindeling. Deze gaan we wijzigen in de door jou gewenste kanaalvolgorde, zoals op je papier:
-  Bij mij is bijvoorbeeld Nederland 1 tevens kanaal nummer 1. Volgens mijn kabelmaatschappij is deze zender te vinden op 189.250 MHz.
-  In MCETuningOverrides.xml wijzig je het volgende:

<Index Channel="1"><AnalogLocator Id="TV1" CarrierFrequency="189250000" /></Index>

-  Deze handeling voer je voorts uit in Index channel 2 voor jouw kanaal 2. Dit gaat door tot je alle kanalen hebt ingevuld..
-  Alle kanalen die je niet nodig hebt wis je voorts uit MCETuningOverrides.xml.
-  Voorts pas je bovenin deze zelfde file de volgende regel aan:

<AnalogTVTuningSpace Id="31" UniqueName="Netherlands Cable" MinChannel="1" MaxChannel="34" DefaultFormat="PAL\_B" InputType="Cable">

Het nummer bij “MaxChannel” dient hierbij overeen te komen met het aantal index kanalen dat je hebt ingevoerd.

-  Dit zijn alle handelingen die je moet doen om de frequentietabel overeen te laten komen met jouw kabelsignaal.

Een groot voordeel: je hebt nooit meer met finetuning te maken, de frequenties zijn hier exact...

**Uitvoeren van een handmatige frequentiescan**
Nu gaan we Mediacenter een scan laten uitvoeren op alle beschikbare kanalen, als volgt:

-  Start mediacenter
-  Kies Instellingen > TV > Gids en doorloop de procedure. Vul ook je postcode in !
-  Nadat de gegevens zijn gedownload selecteer je: “Analoge kabeltelevisie nog niet in kaart gebracht”
-  Nu gaat MCE een scan maken waarbij keurig de frequenties gescand worden die je in MCETuningOverrides.xml zijn vastgelegd.

Dit betekent dat de kanalen snel gevonden worden zonder dubbelingen. Als het goed is heeft MCE na de scan evenveel kanalen gevonden als jij in de xml file hebt vastgelegd. Is dit niet het geval, doe dan de scan gerust opnieuw. Ik heb het zelf 2x meegemaakt dat toch stomweg een zender geskipt werd, en voorts bij een tweede scan wel goed gevonden...

De reden om bovenstaande procedure te volgen is de volgende: wanneer je in een eerdere situatie de EPG op de “normale” manier hebt gevonden worden slechts de gedownloadde kanalen opgeslagen in mediacenter. Als straks kanalen aan de gids toegekend gaan worden kan het voorkomen dat sommige gewenste kanalen niet in de EPG keuzelijst voorkomen. Door de handmatige scan te maken download MCE simpelweg _alle_ beschikbare EPG kanalen die via Internet beschikbaar zijn (momenteel 47 stuks dd. 28-8-2006). Sla bovenstaande stappen dus niet over.

**Kanalen handmatig aan de EPG toewijzen**
Dit deel spreekt redelijk voor zich, het is namelijk (alweer) standaard MCE functionaliteit.

Bij het scannen van de kanalen haalt MCE de zendernaam in beginsel uit de VITS lijnen (teletekst). Dit levert echter niet niet altijd de kloppende zendernaam op die EPG gebruikt. Nickelodeon en Talpa delen bijvoorbeeld een kanaal waardoor de gevonden naam per dagdeel verschillend is. De exact klopende zendernamen krijgen automatisch EPG informatie toegewezen zodat je er feitelijk niets aan hoeft te doen. Aan de afwijkende zendernamen moet je echter zelf EPG toekennen. Om te zorgen dat zoveel mogelijk kanalen nu van EPG gegevens voorzien zijn doe je het volgende:

-  Ga naar Instellingen > Tv > Gids > Gegevens aan een kanaal toevoegen
-  Selecteer het eerste kanaal en druk op de OK of enter toets.
-  Als op de eerste regel staat:”geen gegevens voor dit kanaal weergeven” scrol je naar beneden, net zolang tot je de bijbehorende EPG kanaalnaam gevonden hebt.
-  Indien op de eerste regel gewoon de kloppende zendernaam staat hoef je voor dat betreffende kanaal niets te doen omdat hij al door de EPG herkend is.
-  Deze handeling voer je voor alle zenders uit.
-  Vergeet niet om aan het einde “opslaan” te kiezen, anders kan je opnieuw beginnen...

**Niet herkende kanalen manueel een naam geven**
Soms worden kanalen helemaal niet herkend, en krijgen ze de naam “onbekend” of iets gelijkwaardigs mee. Dit geldt bijvoorbeeld vaak voor lokale TV zenders, infokanalen, tekstkranten etc. Als dit je niets uitmaakt hoef je niets te doen. Wanneer je aan deze zenders echter toch een kloppende naam wil geven, doe dan het volgende:

-  Ga naar: Instellingen > Gids > Ontbrekende kanalen toevoegen > Kanaal toevoegen
-  Geef een onbenoemd kanaal nu de gewenste naam en kies volgende
-  Vul nu bij kanaalnummer het nummer in dat je ingevuld hebt op je _uitgeprintte frequentielijst!_
-  Herhaal deze procedure voor alle niet benoemde kanalen
-  Kies als je klaar bent “gereed”, anders kan je opnieuw beginnen
-  Ga nu naar instellingen > TV > Gids > Kanalen bewerken
-  Haal nu het vinkje weg voor alle _onbenoemde_ kanalen zodat ze uit je werkelijke zenderoverzicht verdwijnen.

Op deze wijze hebben alle niet automatisch herkende kanalen keurig een gewenste naam.

**Kanaalvolgorde naar wens indelen**
We zijn bijna klaar. Als alles hierboven goed gegaan is heb je nu het hele pakket aan zenders in je MCE geprogrammeerd en is waar mogelijk de juiste EPG informatie toegevoegd. Het kan nu zijn dat enkele zenders niet op gewenste volgorde staan, ondanks het feit dat je ze wel op de gewenste volgorde hebt geprogrammeerd in MCETuningOverrides.xml. Dit komt doordat MCE een frequentiescan uitvoert, en geen kanaalscan. Het spreekt voor zich hoe je de kanaalvolgorde moet wijzigen.

Just in case: Instellingen > TV > Gids > Kanaalvolgorde wijzigen

**Tenslotte**
Inderdaad, het is veel werk als je het helemaal perfect wil maken. In mijn geval was het _de_ oplossing voor alles en is het relatief eenvoudig aan te passen indien je kabel leverancier mocht besluiten e.e.a. om te gooien of een kanaaltje toe te voegen. Je hoeft in ieder geval niet langer te wachten op een eventuele update van BDE (de instantie die verantwoordelijk is voor de updates van de gids).

Delen van de bovenstaande beschrijving zijn niet nieuw, maar gebaseerd op informatie die op diverse fora te vinden was. Alhoewel je met bovenstaande beschrijving nauwelijks iets kan verknoeien is het gebruik ervan op eigen risico. Vragen en tips zijn van harte welkom ([info@pa1okz.com](mailto:info@pa1okz.com))

Veel succes !

Source: http://www.degroeneknop.nl/forum/index.php?PHPSESSID=54c270f695e599a2f822884d0b1638cc&/topic,2619.0.html
