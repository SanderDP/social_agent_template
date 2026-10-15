# Startprompt — Social Agent Template (+ Alcolympics)

Plak alles hieronder in een nieuwe Claude Code-sessie met als werkmap
`C:\Users\Sander\Documents\Projecten GitHub\social_agent_template`.

---

Je bent mijn architect en bouwer voor een **herbruikbaar AI-socialemediateam in Claude Code**.
Eerst bouwen we een **generiek sjabloon** (deze map), daarna zetten we het op voor mijn eerste
merk: **Alcolympics** (www.alcolympics.be). Later wil ik hetzelfde sjabloon voor andere zaken
gebruiken, dus alles wat merkspecifiek is moet in één map per merk zitten (`brands/<merk>/`).

## Wat ik wil (einddoel)
- Elke week maakt het team **3–5 kant-en-klare video's** (9:16) voor **Instagram (Reels) en
  TikTok**. Ideeën/inhoud mogen overlappen (bv. hetzelfde concept in twee varianten).
- **Ik post zelf.** Er wordt NIETS automatisch gepubliceerd — geen Metricool of andere
  publicatietool. Ik bekijk de video's op mijn gemak, kies er meestal 1–3, en post ze zelf.
- Per video krijg ik een **"postpakket"**: de video (MP4), een cover/thumbnail, de **caption**
  (NL, Vlaams), **hashtags**, eventueel sound-/tekstsuggesties, en een **voorstel voor dag + uur
  met de reden waarom** (doelgroep, actualiteit, wat eerder goed werkte). Apart voor IG en
  TikTok als dat verschilt.
- Ik krijg een **melding op mijn iPhone via de Claude-app** zodra de wekelijkse video's klaar
  zijn, met **waar ze staan** (map/bestandsnamen) en een korte samenvatting.
- Het team volgt **analytics** op (zie hieronder wat gratis en toegelaten is), leert wat werkt
  en wat niet, en **stuurt bij** (pivot) voor de volgende week.

## Het team (4 rollen — als subagents in `.claude/agents/` + bijhorende skills)
1. **Actualiteit-agent** — draait aan het begin van de week (of vóór een productierun).
   Onderzoekt wat er speelt in **België** voor de doelgroep: studentenevents en -weken, TD's,
   cantussen, feestdagen, lange weekends, festivals, grote matchen (voetbal/EK/WK), het weer
   (terrasweer!), trends/sounds op TikTok/Instagram, en nieuws rond alcohol of merken. Levert een
   kort **weekbriefje** met kansen én met **onderwerpen die we moeten vermijden** (gevoelig
   nieuws, tragedies, alcoholincidenten). Bronnen vermelden.
2. **Content-agent (creatief)** — bedenkt elke week iets **nieuws en creatiefs** op basis van het
   weekbriefje. Maakt per voorstel: concept/hook, script, storyboard, de **video** (Remotion,
   9:16, 1080×1920), **caption** (NL), hashtags, cover/thumbnail, en een voorstel voor datum/uur.
   Uitgerust met alle grafische tools die we installeren (Remotion + skills, Pexels voor
   rechtenvrij stockbeeld, Python voor zelfgemaakte muziek/geluidseffecten, image-tools).
3. **Reviewer-agent (kritisch)** — beoordeelt elk concept vóór ik het zie, met concrete,
   onderbouwde kritiek en een duidelijke **goed/aanpassen/afkeuren**. Controleert minstens:
   - **Merk**: klopt het met `brands/alcolympics/brand.md` (toon, kleuren, termen, feiten)?
   - **Alcohol & verantwoordelijkheid**: 18+, geen aanmoediging van overmatig drinken, Belgische
     alcoholcode (zie merkbijbel §9).
   - **Copyright & platformregels**: muziek (zakelijk account → enkel rechtenvrij, eigen audio of
     de Commercial Music Library van TikTok), stockbeeld-licenties, geen merklogo's of echte
     personen zonder toestemming, **TikTok Community Guidelines en regels rond alcohol/branded
     content**, en de Instagram/Meta-richtlijnen. Bij twijfel: afkeuren of aanpassen.
   - **"Ziet dit eruit als AI?"** (zie hieronder) — strengste punt.
   - **Kwaliteit**: hook in de eerste 1–2 s, leesbaarheid op gsm, safe zones (geen tekst in de
     bovenste ±250 px en onderste ±420 px), tempo, afwerking.
   Laat de content-agent bijwerken tot het concept slaagt (max. 2 rondes), pas dan naar mij.
4. **Manager-agent** — mijn aanspreekpunt. Bundelt de goedgekeurde video's per week in één map
   met een overzicht (`weeks/<jaar-week>/README.md` + per video een map met MP4, cover,
   `caption.txt`, `hashtags.txt`, `postvoorstel.md`), **stuurt mij de melding op mijn iPhone**
   met waar alles staat, verwerkt mijn feedback/aanpassingen (dan laat hij de content-agent
   bijwerken), noteert welke video's ik effectief gepost heb (ik zeg het hem, of hij leidt het
   af uit de analytics), en doet de **analytics**: wekelijks rapport, wat werkt/niet, en concrete
   bijsturing voor de volgende week (input voor de actualiteit- en content-agent). Houdt een
   logboek bij (`brands/<merk>/log/`).

## Belangrijkste eis: het mag NIET als AI-gegenereerd aanvoelen
Het hele team moet weten wat mensen vandaag als "AI-content" herkennen, en dat vermijden.
Maak hiervoor een **anti-AI-stijlgids** (`guides/anti-ai-style.md`) op basis van onderzoek,
die de content- en reviewer-agent verplicht gebruiken. Denk o.a. aan:
- Tekst: geen typische AI-zinnen ("Unlock…", "Dive into…", "game-changer", "Ready to…?",
  "Let's…!", overdreven enthousiasme), geen lange gedachtestreepjes, geen opsommingen van drie
  bijvoeglijke naamwoorden, geen emoji-regen, geen perfect gepolijste maar inhoudsloze zinnen.
  Schrijf zoals een Vlaamse twintiger echt praat/typt: kort, droog, soms onaf.
- Beeld: geen AI-gegenereerde mensen/gezichten/handen, geen glanzende "stock-AI-esthetiek",
  geen generieke AI-stemmen. Liever echte app-beelden (UI), eigen animatie, echte foto's/video's
  (eventueel aangeleverd door mij), lichte imperfectie.
- Ritme: niet elke video hetzelfde sjabloon; varieer formats (POV, "groepschat", meme-formats,
  ranking-reveal, mini-sketch-script dat ik zelf kan opnemen, enz.).
- Geef **eerlijke** content: geen verzonnen reviews, cijfers of testimonials.

## Wat we al onderzocht hebben (startpunt — verifieer zelf de actuele details)
- **Posten**: doe ik zelf (bewuste keuze). Geen publicatietools, geen posting-API's.
- **Analytics — gratis en toegelaten (eigen accounts):**
  - **Instagram**: de officiële *Instagram API with Instagram Login* geeft sinds 2025 ook
    **gebruikers- en media-insights** (bereik, views, likes, opgeslagen, gedeeld…) via de
    permissie `instagram_business_manage_insights`. Gratis; vereist een **zakelijk/creator-
    account** en een eigen **Meta-ontwikkelaarsapp** in *Development mode* met mijn account als
    tester/admin (geen App Review nodig zolang het enkel mijn eigen account is). Verifieer in de
    actuele Meta-documentatie.
  - **TikTok**: de officiële **Display API** (`/v2/video/list`, `/v2/video/query`, `user.info`)
    geeft basiscijfers van mijn **eigen publieke video's** (views, likes, reacties, shares —
    controleer welke velden v2 teruggeeft). Gratis, werkt in sandbox voor eigen accounts.
    **Diepere TikTok-cijfers** (kijktijd, % volledig bekeken, doelgroep, bereik per dag) zitten
    níet in die API → oplossing: ik exporteer of screenshot wekelijks mijn TikTok Studio-
    analytics in `brands/<merk>/analytics/inbox/`, en de manager-agent leest die in.
  - **Trends**: geen officiële gratis trend-API. Gebruik **websearch**, het publiek
    **TikTok Creative Center** (trending hashtags/sounds/creators; check of België selecteerbaar
    is) en nieuwsbronnen — **lezen zoals een mens**, géén massaal automatisch scrapen (strijdig
    met de voorwaarden van TikTok/Instagram). Geen betaalde scrapers.
  - **Niet doen**: inloggen met mijn wachtwoord in scripts, onofficiële API's of scrapers van
    Instagram/TikTok (accountrisico).
- **Planning**: **Claude Code Routines** (geplande cloud-agents, bv. maandag 07:00 cron
  `0 7 * * 1`; research preview, run-limieten per plan) of lokale geplande taken op mijn pc.
  Onderzoek of video renderen met Remotion in een cloud-routine lukt; zo niet, een hybride
  opzet (onderzoek + scripts in de cloud, renderen lokaal).
- **Melding naar iPhone**: onderzoek de beste manier binnen Claude Code / de Claude-app
  (bv. de pushmelding-functie van Claude Code, Remote Control, of de melding wanneer een
  routine klaar is) en test het effectief.
- **Bestaande open-source sjablonen** om eerst te bekijken (veiligheid + kwaliteit beoordelen,
  dan de beste als basis nemen of ideeën lenen):
  - github.com/tomascavernelis/claude-code-agent-team (rollen als Markdown, QA- en menselijke goedkeuringshaak)
  - github.com/ttalkkaklab/social-flow (volledige video-pijplijn, goedgekeurd publiceren)
  - github.com/stevenflanagan1/social-ai-team (social skills voor kmo's)
- **Video**: Remotion is al geïnstalleerd in `C:\Users\Sander\Documents\Projecten GitHub\remotion`
  met bestaande Alcolympics-video's en bouwstenen (zie merkbijbel §8), plus globale
  Remotion-skills in `~/.claude/skills/remotion-*`. Hergebruik dat (of maak een
  `remotion/`-werkmap binnen het sjabloon die ernaar verwijst).

## Alles over Alcolympics
- Lees eerst **`brands/alcolympics.md`** (in deze map) — de volledige merkbijbel, opgesteld door
  de sessie die de app gebouwd heeft. Verplaats/herwerk die naar `brands/alcolympics/brand.md`
  in de sjabloonstructuur.
- Diepere bron: de app-broncode in `C:\Users\Sander\Documents\Projecten GitHub\Alcolimpics`
  (paden staan in de merkbijbel §11) en de live site https://www.alcolympics.be.
- Logo's en shopfoto's: `Alcolimpics/public/` en `remotion/public/`.

## Aanpak (fases) — werk stap voor stap, toon mij resultaten
**Fase 0 — vragen & voorbereiden.** Stel mij eerst alle vragen die je nog hebt (o.a. de
open punten in merkbijbel §12, of ik zelf video's kan opnemen, budget). Geef me een checklist
van wat ik moet aanmaken/koppelen (Instagram zakelijk/creator-account, TikTok zakelijk account,
Meta-ontwikkelaarsapp voor Instagram-insights, TikTok-ontwikkelaarsapp voor de Display API,
Pexels-API-sleutel). **Plak of vraag nooit sleutels in de chat**: ik zet ze zelf in een `.env`
die in `.gitignore` staat.
Geef mij voor de analytics een **duidelijk, klikbaar stappenplan** (genummerd, met exacte
menu's/knoppen en welke waarden ik waar moet invullen) om:
1. de **Meta/Instagram-ontwikkelaarsapp** correct aan te maken en te koppelen aan mijn
   Instagram zakelijk/creator-account (Instagram API with Instagram Login, permissies
   `instagram_business_basic` + `instagram_business_manage_insights`, mijn account als
   tester, langlevend toegangstoken aanmaken en vernieuwen);
2. de **TikTok-ontwikkelaarsapp** voor de Display API aan te maken (sandbox, mijn account als
   testgebruiker, scopes `user.info.basic`/`user.info.stats`/`video.list`, toegangstoken);
3. te **testen** dat het team effectief cijfers kan ophalen (één testopvraging per platform),
   en wat ik moet doen als een token vervalt.
Verifieer elke stap in de actuele officiële documentatie vóór je hem geeft (de menu's van
Meta en TikTok veranderen geregeld), en help me live verder als ik vastloop.

**Fase 1 — onderzoek & keuze.** Licht de 3 repo's door, verifieer de analytics-toegang
(Instagram-insights en TikTok Display API voor eigen accounts), onderzoek de iPhone-melding en
of Remotion in een cloud-routine rendert. Stel een architectuur voor met voor- en nadelen.
Wacht op mijn akkoord.

**Fase 2 — het generieke sjabloon.** Mapstructuur (voorstel):
```
social_agent_template/
  .claude/agents/        actualiteit.md, content.md, reviewer.md, manager.md
  .claude/skills/        weekbriefing, video-maken, caption-schrijven, review-checklist,
                         copyright-check, postpakket-maken, analytics-ophalen, analytics-rapport
  guides/                anti-ai-style.md, platform-regels.md (TikTok/IG + alcohol + copyright),
                         workflow.md
  brands/<merk>/         brand.md, assets/, voorbeelden/, log/, analytics/
  weeks/<jaar-week>/     briefing.md, review.md, README.md (overzicht), video-01/…05/
                         (MP4, cover, caption.txt, hashtags.txt, postvoorstel.md), gepost.md
  scripts/               audio (Python), render, analytics (IG-insights + TikTok Display API)
  README.md              hoe gebruiken + hoe een nieuw merk toevoegen
```
Niets wordt ooit automatisch gepost: het eindproduct is een kant-en-klaar postpakket per video.
Plus de geplande runs (maandag: actualiteit → content → review → postpakketten + melding;
vrijdag of zondag: analyticsrapport).

**Fase 3 — Alcolympics.** Merkmap invullen, één volledige testweek met de hand doorlopen
(ik keur goed), dan automatiseren. Na 4 weken samen de analytics evalueren.

Werk in het Nederlands met mij. Video-tekst en captions: Nederlands (Vlaams). Begin nu met
**Fase 0**: lees de merkbijbel, en stel mij je vragen.
