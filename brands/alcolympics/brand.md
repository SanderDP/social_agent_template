# Merkbijbel — Alcolympics

> Opgesteld door de Claude-sessie die de Alcolympics-webapp heeft gebouwd (okt. 2026).
> Dit is de bron van waarheid voor álle content. Bij twijfel: de broncode van de app
> (zie §11) is leidend, niet je eigen interpretatie.

---

## 1. In één zin

**Alcolympics is een gratis, speelse drink-app voor vriendengroepen: je logt wat je drinkt,
klimt in de ranking van je groep, speelt achievements vrij en daagt andere groepen uit in een
Boit War.** Slogan: **"Track je drankjes. Versla je vrienden."**

- Website/app: **https://www.alcolympics.be** (webapp/PWA: werkt in de browser en als app op
  het beginscherm; een native iOS-app is in voorbereiding).
- Eigenaar: **De-Pauw BV** (KBO BE0818.250.032). Alcolympics is een handelsnaam. Zaakvoerder/
  maker: Sander De Pauw (contact: sander@de-pauw.eu).
- **Schrijfwijze:** altijd **"Alcolympics"** (met y). De oude schrijfwijze "Alcolimpics" komt nog
  voor in technische namen (mapnaam, app-ID) — nooit in content gebruiken.
- Het logo leest "Alc / Olympics" (gestapeld).

## 2. Doelgroep

- **18–30 jaar**, Vlaanderen/België, Nederlandstalig. Studenten (kotstudenten, studentenclubs,
  doop/cantus, TD's), jonge werkenden, vriendengroepen, jeugdhuizen, sportclubs na de match.
- Gebruik: op café, op fuiven, op festivals, op kot, tijdens het weekend, op de Gentse Feesten,
  carnaval, Oktoberfest-avonden, studentenweken (bv. 24-urenloop), EK/WK-avonden.
- **Strikt 18+.** Nooit content die minderjarigen aanspreekt of minderjarigen toont.

## 3. Toon & persoonlijkheid

- **Speels, cheeky, sociaal, zelfspot.** Het is een spel met vrienden, géén bedrijf, geen
  "lifestyle-merk", geen wellness-app.
- Vlaams, informeel, **"je"** (nooit "u"). Licht Vlaamse uitdrukkingen mogen ("boitten",
  "zatlap", "een pintje pakken", "op café", "kot", "TD", "cantus", "den Duvel").
- Humor zit in **herkenbaarheid** (die ene vriend die altijd "nog eentje" zegt, de groepschat
  op zondagochtend, de kater op maandag), niet in het verheerlijken van dronkenschap.
- Kort en punchy. Liever één goede grap dan drie halve.

### Eigen begrippen (altijd exact zo gebruiken)
| Term | Betekenis |
|---|---|
| **Sippen** | Een drankje loggen in de app (knop "Drankje sippen"). Werkwoord: "sippen", "gesipt". |
| **Stella-equivalent** | Elk drankje wordt omgerekend naar het aantal flesjes Stella Artois 25 cl (5,2%) met evenveel pure alcohol. Eerlijk vergelijken: een Duvel ≈ 2,2 Stella, een glas wijn ≈ 1,4, een shot ≈ 0,9. |
| **Rank Points (RP)** | Punten per drankje (10 RP per Stella-equivalent) + bonus voor achievements. |
| **Boit Ranked** | De live ranglijst van je vriendengroep. Een groep join je enkel met een groepscode. |
| **Boit Wars** | Groep tegen groep, **7 dagen lang**, elke sip van je groep telt. Eigen logo. |
| **Challenges** | Drankspelletjes/uitdagingen alleen of met de groep (zie §6). |
| **Achievements & badges** | Vrij te spelen titels; je kan favoriete badges uitlichten op je profiel. |
| **Ranks** | 22 levels, 8 tiers (zie §5). |

## 4. Functies (wat de app écht doet — nooit iets verzinnen)

1. **Sippen in 2 tikken** — drankje kiezen (database met Belgische bieren, wijnen, sterke drank,
   cocktails), hoeveelheid, tijdstip. Na het loggen: een "Gesipt! 🍻"-feestje met "+X RP",
   bubbels en een rankbalk die vooruit schuift.
2. **Home** — stats (vandaag, week, all-time, Stella-equivalent), recente activiteit, weekgrafiek.
3. **Boit Ranked** — groepen maken/joinen met code, live ranglijst (week/maand/all-time), een
   doorschuivende "nieuwsband" met de laatste gebeurtenissen in de groep (wie wat dronk, benders,
   nieuwe leden, badges, inhaalacties).
4. **Boit Wars** — een groep daagt een andere groep uit; 7 dagen; scoreverloop; winnaar.
   Tegenstanders zien enkel groepstotalen (privacy).
5. **Ranks** — glanzende rank-chips naast je naam (brons → zilver → … → holografische
   Godlike Zuiper).
6. **Achievements & speciale badges** — o.a. Cara Warrior, Witte Wijn Demon, Kater Koning(in),
   Shotjes Sergeant, Halve Liter Held, Cocktail Connaisseur, Weekend Warrior, Jenever Jager,
   Terraske Specialist, After-Work Alco, Rosé Ridder, Studentikoze Stamgast, Nachtuil, Vroege
   Vogel, Groepsdier, Century Club Lid, Power Hour Volbracht, Quarters Kampioen, … Speciale
   zeldzame badges: Kwistenbiebel, Beustel Hesser, HessenBeustel Weustel.
7. **Challenges / drankspelletjes** — Voetbal Shots, Per Total, Century Club, Power Hour,
   Edward Fortyhands, Quarters, Never Have I Ever, Triple-Dubble.
8. **Vrienden** — vriendschapsverzoeken (pas vrienden na aanvaarding).
9. **Pushmeldingen** — o.a. als iemand je inhaalt, benders, Boit War-updates, herinneringen.
10. **Shop** — merch (zie §7). Betalen via Mollie (Bancontact/Belfius/KBC…), verzending via bpost
    of afhalen.
11. **Privacy** — drankdata enkel zichtbaar voor wederzijdse vrienden en groepsgenoten; gehost
    in de EU; geen reclame; geen verkoop van data. 2FA voor beheer.

Wat de app **niet** heeft: geen bezorging van drank, geen alcoholverkoop, geen betaalde
abonnementen, geen ads. Beweer nooit cijfers (aantal gebruikers, reviews) die niet aangeleverd
zijn door Sander.

## 5. Rangladder (exact)

8 tiers, elk met divisie III → II → I (behalve de top):
1. **Pussy Drinker** (start) · 2. **Baby Boitter** · 3. **Saaf Sipper** · 4. **Kalme Neugelaar** ·
5. **Baas Boitter** · 6. **Advanced Alcolieker** · 7. **Tanker Unit** · 8. **Godlike Zuiper** (geen divisies).

Tierkleuren van de chips: brons, zilver, roze-magenta, cyaan, blauw, paars, rood-oranje,
holografisch (doorschuivende regenboog) voor Godlike Zuiper.

## 6. Merkidentiteit (visueel)

- **Kleuren**
  - Achtergrond: `#fffaf7` (warm wit), kaarten `#ffffff`
  - Tekst: `#16161d`, secundair `#6b6b78`
  - Merkverloop (uit het logo): `#c8105a` → `#e5383b` → `#ff9a00` (magenta → rood → oranje)
  - Eén vaste accentkleur: `#c8105a`
- **Lettertypes:** IBM Plex Sans (700) voor titels, Noto Sans (400/600/700) voor tekst
  (beide via Google Fonts / `@remotion/google-fonts`).
- **Stijl in de app:** luchtig en fris; zachte zwevende kleurvlekken (magenta/oranje) op warm wit,
  opstijgende bierbelletjes, glanzende knoppen met merkverloop, ronde vormen, kaarten die
  binnenschuiven, verende (spring) animaties, trillingen bij tikken.
- **Logo's** (in de app-repo, `public/`):
  - `logo-icon.png` — gestapeld "Alc/Olympics"-logo met verloop (hoofdlogo)
  - `logo.png` — horizontaal woordmerk "Alcolympics" (klein gebruik, kopbalk)
  - `boit-wars-logo.png` en `boit-wars-logo-white.png` — Boit Wars-logo
  - `boit-ranked-logo.png` — Boit Ranked-logo
  - `icons/` — app-iconen

## 7. Shop (merch, echte producten)

Productfoto's: `Alcolimpics/public/shop/` (mockups én losse designs `*-design.png`).

| Product | Prijs |
|---|---|
| Alcolympics T-shirt | €18,99 |
| BachtBak T-shirt / Sweater / Polo | €18,99 / €35,99 / €22,99 |
| BoeBoe Certified T-shirt / Sweater | €18,99 / €35,99 |
| Captain Cooked T-shirt / Sweater | €18,99 / €35,99 |
| Kwisten Biebel T-shirt / Sweater | €18,99 / €35,99 |
| Neugelmeister T-shirt / Sweater | €18,99 / €35,99 |
| Beustel Hesser Polo / Longsleeve | €22,99 / €20,99 |
| Pope Promillius Polo | €22,99 |

Verdienmodel: de app is gratis; merch financiert de verdere ontwikkeling ("Met merch uit de shop
help je ons op weg naar de App Store"). Groepsshirts voor een Boit War = sterk verhaal.
Prijzen kunnen wijzigen: controleer in de app/shop vóór je een prijs in een post zet.

## 8. Bestaande content & bouwstenen (hergebruiken!)

- **Remotion-project:** `C:\Users\Sander\Documents\Projecten GitHub\remotion`
  (Remotion 4.0.534, React 19, TS). Bevat al:
  - `src/alcolympics/` — 15 s promo (60 fps): intro, slogan, sip-demo, rangladder, outro, met
    zelf gesynthetiseerde muziek/geluidseffecten (`scripts/make-audio.mjs`).
  - `src/reel/` — 40 s reel met 9 scènes (wat, sippen, Boit Ranked, ranks, Boit Wars,
    challenges, shop-slider, CTA), props instelbaar in Studio.
  - `src/social/` en `src/fight/` — kortere social-video's (sip, wars, "Titelgevecht").
  - `public/` — logo's, shopfoto's, audio.
  - Globale Remotion-skills voor Claude: `~/.claude/skills/remotion-*`.
- **Landingspagina-copy:** `Alcolimpics/src/lib/i18n/sections/landing.ts` (NL+EN, FAQ).

## 9. Regels & grenzen (VERPLICHT — de reviewer controleert hierop)

### 9.1 Alcohol & verantwoord drinken
- Elke post vermeldt (in beeld of caption) **"18+"** en waar passend **"Drink met mate."**
- **Nooit** overmatig/snel drinken aanmoedigen of verheerlijken (geen "zuip zo veel mogelijk",
  geen bingedrinken als doel, geen braken/blackouts als grap, geen drinken + rijden, geen
  drinken + zwemmen/werk/school).
- **Nooit** alcohol koppelen aan sportprestaties, seksueel succes, sociaal succes of "volwassen
  worden" (Belgische alcoholcode / Convenant, JEP).
- Geen minderjarigen, geen personen die jonger dan 25 ogen als "hoofdrolspeler" in drinkscènes,
  geen schooluniformen, geen kinderlijke stijl (cartoonfiguren die kinderen aanspreken).
- Humor mag over de **groep, de competitie en herkenbare situaties**, niet over dronkenschap zelf.
- Bij gevoelig nieuws rond alcohol (ongevallen, overlijden, doopschandalen): **niet** op inspelen.
- Hulp: De DrugLijn — druglijn.be · 078 15 10 20 (mag in bio/caption bij serieuzere posts).

### 9.2 Platformregels
- TikTok en Instagram beperken content die alcoholgebruik promoot; vooral bij jongeren. Houd het
  speels en sociaal, toon geen roekeloos drinken, gebruik geen "drink-challenge"-dynamiek die
  gevaarlijk is. Branded content / betaalde samenwerking altijd labelen.
- Accounts zijn **zakelijke accounts** → op TikTok enkel muziek uit de **Commercial Music Library**
  of eigen/zelfgemaakte audio. Op Instagram idem: geen populaire copyrighted nummers.

### 9.3 Merken, copyright & personen
- Biermerken (Stella, Duvel, Jupiler, Cara…) mogen in tekst als drankje genoemd worden zoals in
  de app (Stella-equivalent), maar **geen logo's, flessen-close-ups als reclame, of suggestie
  van samenwerking**. Geen andere merken/logo's in beeld zonder toestemming.
- Geen herkenbare echte personen zonder toestemming; geen beelden van andermans socials.
- Stockbeeld enkel van rechtenvrije bronnen (Pexels/Pixabay met hun licentie; check of mensen
  herkenbaar en commercieel bruikbaar zijn), en liever eigen app-beelden/animatie.
- Muziek/geluid: zelf maken (Python-synthese zoals in het Remotion-project) of uit de officiële
  commerciële bibliotheek van het platform.

### 9.4 Privacy
- Nooit echte gebruikersdata, gebruikersnamen of drankgeschiedenis van echte gebruikers tonen.
  Demo-data met verzonnen namen (bv. "Den Zatte Zesde", "De Pintjesbrigade", Lotte, Jonas, Arne,
  Robbe, Fien) is oké.

## 10. Content-pijlers (ideeënrichting, geen keurslijf)

1. **Herkenbaar** — situaties uit het uitgaansleven/kotleven met een Alcolympics-twist.
2. **App in actie** — sippen, ranking die verschuift, rank-up, Boit War-spanning (echte UI).
3. **Boit Wars** — groep vs groep, "titelgevecht", uitdagen.
4. **Actualiteit** — studentenevents, feestdagen, weekend, matchen, festivals (zie §2), met een
   knipoog — en altijd binnen §9.
5. **Shop** — merch met humor (de namen lenen zich ervoor: Captain Cooked, Pope Promillius…).
6. **Community/challenges** — drankspelletjes, polls, "tag je groep".

CTA's: "Speel gratis op alcolympics.be", "Daag je groep uit", "Link in bio".
Hashtag-richting (spaarzaam, max 3–5): #alcolympics #studentenleven #kotleven #vriendengroep #belgie.

## 11. Bronnen voor de agents (lees bij twijfel)

- App-broncode: `C:\Users\Sander\Documents\Projecten GitHub\Alcolimpics`
  - `src/app/page.tsx` (landingspagina), `src/lib/i18n/sections/landing.ts` (marketingcopy)
  - `src/app/globals.css` (kleuren, animaties), `src/lib/services/rank.ts` (ranks)
  - `prisma/seed.ts` (drankjes, achievements, challenges, shopproducten)
  - `src/app/privacy/`, `src/app/terms/` (privacy & voorwaarden), `docs/legal/` (risicoanalyse)
- Remotion: `C:\Users\Sander\Documents\Projecten GitHub\remotion`
- Live site: https://www.alcolympics.be (landingspagina is publiek; de app achter login)

## 12. Nog aan te vullen door Sander
- Instagram-handle en TikTok-handle van Alcolympics.
- Gewenste postmomenten (vermoedelijk wo/do avond + vr/za), en of er een vast "format" per week
  moet zijn.
- Mag Sander zelf in beeld? Zijn er vrienden die (met toestemming) mogen meespelen in content?
