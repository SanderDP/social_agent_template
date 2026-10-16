# Anti-AI-stijlgids

Verplicht voor de content- en reviewer-agent. Doel: niemand mag bij het scrollen denken
"dit is AI". Dit is het strengste criterium van de review. `scripts/check_style.py` vangt de
tekstfouten machinaal op; de rest is oordeel.

Geldt voor elk merk. Merkspecifieke toon staat in `brands/<merk>/brand.md`.

---

## 1. Tekst (in beeld, caption, hashtags)

### Verboden woorden en zinnen (machinaal gecontroleerd)
- Engelse AI-clichés: *unlock, dive into, delve, game-changer, elevate, unleash, seamless,
  level up, ready to…?, let's…!, look no further, whether you're… or…, in today's fast-paced
  world, take it to the next level, the ultimate, revolutionize, embark, journey, vibrant.*
- Nederlandse varianten: *ontdek de wereld van, duik in, til je … naar een hoger niveau, klaar
  om…?, laten we…!, de ultieme, naadloos, ontgrendel, ben jij er klaar voor, het is tijd om,
  in een wereld waar, niet alleen … maar ook, of je nu … of …, boordevol, unieke ervaring.*
- Lege superlatieven: *ongelooflijk, episch, legendarisch* (tenzij als ironie van een
  personage), *must-have, next level, iconisch*.

### Verboden vormen
- **Lange gedachtestreepjes (—)** in captions en tekst in beeld. Gebruik een punt, komma of niks.
- **Drieslagen**: geen opsommingen van drie bijvoeglijke naamwoorden of drie parallelle zinnen
  ("Snel. Simpel. Sociaal.").
- **Emoji-regen**: maximaal 2 emoji per caption, nooit aan het begin van elke regel, geen
  🚀✨🔥💯-combinaties.
- **Vraag-als-opener** ("Ben jij ook iemand die…?") en **retorische afsluiter** ("Wat denk
  jij?"). Een echte vraag aan de groep mag ("wie van jullie is dit").
- **Perfect gepolijste maar lege zinnen**: als een zin over elk merk zou kunnen gaan, schrappen.
- **Uitroeptekens**: maximaal één per caption.
- **Hashtagblokken**: maximaal 5, onderaan, klein, niets generieks als #fun #life #vibes.

### Wél
- Schrijf zoals een Vlaamse twintiger typt in een groepschat: **kort, droog, soms onaf**,
  kleine letters mogen, een tikfout-gevoel mag (geen echte spelfouten in merktermen).
- **Eén idee per video**, één grap. Liever te kort dan uitgelegd.
- **Specifiek > algemeen**: "zaterdag 3u, Overpoort, Jonas zegt nog eentje" verslaat
  "die momenten met vrienden".
- Captions van **1–2 regels** zijn normaal. Lange captions alleen als de video erom vraagt.
- De **grap staat in de video**, de caption voegt iets toe of zegt bijna niks.

---

## 2. Beeld

### Nooit
- AI-gegenereerde mensen, gezichten, handen of dieren.
- Glanzende "AI-stock"-esthetiek: perfecte symmetrie, plastic huid, paarsblauwe gloed,
  overdreven bokeh, onmogelijke reflecties.
- Generieke stockclips die meteen als stock herkenbaar zijn (lachend groepje proost in slow
  motion naar de camera).
- Elke video dezelfde intro, dezelfde overgang, dezelfde titelanimatie.

### Wel
- **Echte app-beelden** (schermopnames met demo-data uit `brands/<merk>/assets/ui/`).
- **Eigen animatie** die als UI of meme aanvoelt, niet als reclamespot.
- Rechtenvrij beeld (Pexels/Pixabay) dat **gewoon** oogt: licht onscherp, scheve kadrering,
  telefoonbeeld > cinematisch.
- **Lichte imperfectie**: een harde cut, tekst die niet perfect gecentreerd staat, een
  native-ogend lettertype zoals de platformen zelf gebruiken.
- Formats die mensen zelf maken: schermopname, groepschat, notities-app, meme-tekst boven beeld.

---

## 3. Geluid
- **Geen generieke AI-vertelstem** (de vlakke "explainer"-stem).
- **Wel toegelaten**: herkenbare meme-TTS ("bro thought I was new"-stijl). Dat is memecultuur,
  geen AI-content. Spaarzaam, en bij voorkeur de ingebouwde TTS van het platform bij het
  posten (de eigenaar zet die dan zelf).
- Muziek: zelfgemaakt (Python) of uit de commerciële bibliotheek van het platform. Het
  postvoorstel noemt dan een concreet geluid om bij het posten te kiezen.

---

## 4. Ritme en variatie
- **Nooit twee weken na elkaar hetzelfde format als hoofdvideo.**
- Wissel af tussen: POV, groepschat, meme-format (beeld + bovenschrift), ranking-reveal,
  "how it feels to…"-trend, schermopname met reactie, fake-notificatie, mini-sketch-script,
  poll/vraag aan de groep, before/after.
- Varieer lengte (6–25 s), tempo, kleurgebruik en openingsbeeld.
- `brands/<merk>/log/formats.md` houdt bij welk format wanneer gebruikt is.

---

## 5. Eerlijkheid
- Geen verzonnen reviews, cijfers, gebruikersaantallen of testimonials.
- Geen nep-screenshots van "echte" gebruikers. Demo-data is herkenbaar fictief.
- Trends volgen mag, doen alsof iets viraal is niet.

---

## 6. De snelle test (reviewer)
Lees de caption hardop en bekijk de video zonder geluid. Beantwoord eerlijk:
1. Zou een Vlaamse 22-jarige dit zo typen? Zo niet: herschrijven.
2. Zie je binnen 1 seconde iets dat op AI of stock lijkt? Zo ja: afkeuren of beeld vervangen.
3. Lijkt deze video op die van vorige week? Zo ja: ander format.
4. Kan je de grap in één zin uitleggen zonder "en dan"? Zo niet: te ingewikkeld.
