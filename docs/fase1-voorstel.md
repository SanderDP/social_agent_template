# Fase 1 — onderzoek & architectuurvoorstel (15 okt. 2026)

Legende: **[V]** geverifieerd in officiële documentatie · **[S]** uit secundaire bronnen of
aanname · **[T]** moet nog getest worden.

---

## 1. De drie open-source repo's

| Repo | Wat het is | Veiligheid | Bruikbaar? |
|---|---|---|---|
| **tomascavernelis/claude-code-agent-team** | 7 rollen als Markdown, publicatie-poort als hook, A/B-"testladder" op medianen. 38 bestanden, enkel Python-stdlib. | ✅ Schoon: geen netwerkcalls, geen verborgen code. De hook leest enkel lokale JSON. | **Beste basis voor ideeën.** |
| **ttalkkaklab/social-flow** | Enorme Koreaanse video-pijplijn (679 bestanden) als plugin met eigen MCP-server. | ⚠️ De server wordt geleverd als gecompileerde bundel van 6,4 MB, moeilijk te controleren. Vraagt tot 20 betaalde API-sleutels. | **Niet als basis.** Draait op AI-video/-stem/-muziek (Veo, Seedance, Suno, ElevenLabs): betalend en precies wat wij níet willen. |
| **stevenflanagan1/social-ai-team** | 10 skills voor kmo's (captions, contentkalender, rapport). Enkel Markdown. | ⚠️ Het installatiescript kopieert alles naar je *globale* `~/.claude/skills` en overschrijft wat er al staat. Niet uitvoeren. | **Beperkt.** Gericht op statische posts en betaalde tools (Blotato, Nano Banana, Firecrawl). |

**Wat we lenen**
- *agent-team:* rollen als versiebeheerde Markdown, met **minimale rechten per agent**. Elke
  bewering in briefing en rapport krijgt een label [V]/[S]/[?]. Ook de **testladder**: één
  variabele tegelijk testen en beoordelen op de **mediaan**, zodat één virale uitschieter niet
  telt. Voor 3 video's per week stretchen we dat naar een test van 4 weken.
- *social-flow:* een **automatische stijlcontrole**: een script dat verboden AI-zinnen
  machinaal afkeurt. Wij maken een Vlaams/Engelse versie (`scripts/check_style.py`) die de
  reviewer verplicht draait.
- *social-ai-team:* de opdeling in skills (merk-onboarding → contentmix → captions → rapport).

**Besluit:** we bouwen een eigen, lichtgewicht sjabloon. Geen code van derden en geen
MCP-servers van derden.

---

## 2. Analytics: wat kunnen we gratis ophalen?

### Instagram [V]
- Werkt met een **zakelijk of creator-account** via *Instagram API with Instagram Login*
  (`graph.instagram.com`), permissies `instagram_business_basic` +
  `instagram_business_manage_insights`. Voor je eigen account volstaat **Standard Access**:
  geen App Review nodig.
- Per Reel: `views`, `reach`, `likes`, `comments`, `shares`, `saved`, `reposts`,
  `total_interactions`, **`ig_reels_avg_watch_time`**, `ig_reels_video_view_total_time` en
  **`reels_skip_rate`**. Dat is rijker dan verwacht: gemiddelde kijktijd en skip-rate zijn
  precies wat we nodig hebben om hooks te beoordelen.
- ⚠️ **Sommige statistieken zijn niet beschikbaar onder 100 volgers.** De eerste weken kan er
  dus data ontbreken.
- ⚠️ Accountstatistieken blijven maar **90 dagen** bewaard. Het team slaat ze daarom elke week
  zelf op.
- Hoe je de sleutel aanmaakt en veilig plaatst, leg ik uit in Fase 2, op het moment dat we hem
  nodig hebben.

### TikTok [V/S] — later, zodra het account er is
- Display API: per video `view_count`, `like_count`, `comment_count`, `share_count`, `duration`
  en `create_time`. Scopes `user.info.basic` en `video.list`.
- Het toegangstoken is ±24 u geldig, het vernieuwingstoken ±1 jaar. Een script vernieuwt dat
  automatisch.
- Kijktijd en "% volledig bekeken" zitten er níet in. Die halen we uit jouw wekelijkse export
  van TikTok Studio.
- Opvallend: TikTok heeft een veld `is_aigc`, dat aangeeft of een video als AI-gegenereerd
  gelabeld is. Dat is nog een reden voor onze anti-AI-aanpak.
- [T] Werking in sandbox controleer ik pas als het account er is.

---

## 3. Planning en de melding op je iPhone

**Routines** [V]: beschikbaar op **Pro**. Ze draaien in de cloud, ook als je pc uit staat, en
werken vanuit een GitHub-repo. Elke run verbruikt je gewone Pro-usage. De cloud-machine is
Ubuntu met 4 vCPU, 16 GB RAM, Node en Python. Sleutels kunnen als **"network secret"**
bewaard worden: de agent gebruikt de sleutel dan zonder hem ooit te zien. Dat is ideaal voor
de Instagram-sleutel.

**Pushmelding** [V + getest]:
- De officiële pushmelding naar je iPhone werkt enkel als **Remote Control** actief is op een
  lokale sessie. Ik heb het net getest vanuit deze sessie: *"Mobile push not sent (Remote
  Control inactive)"*.
- Of een **cloud-routine** een push kan sturen, staat niet in de documentatie. [T] Dat test ik
  als eerste stap in Fase 2.
- **Terugvaloptie:** de routine mailt je een kort overzicht via de Gmail-koppeling die je al
  hebt. Dat geeft een gewone Mail-melding op je iPhone. Daarnaast verschijnt elke run ook in de
  Claude-app onder **Code**.

---

## 4. Kan Remotion renderen in de cloud?

**Waarschijnlijk wel** [S], maar het is nog niet getest [T]:
- Rekenkracht: 4 vCPU en 16 GB is ruim genoeg voor 3 korte 9:16-video's. Langere commando's
  mogen tot ±30 min op de achtergrond lopen.
- Remotion downloadt een eigen Chrome Headless Shell van `remotion.media` of
  `storage.googleapis.com`. Dat laatste domein staat standaard toe. `remotion.media` en
  `fonts.gstatic.com` (Google Fonts) voegen we toe aan de toegelaten domeinen, samen met
  `api.pexels.com` en `graph.instagram.com`.
- Je Remotion-project heeft **geen GitHub-remote**. De cloud kan het dus niet zien. Voorstel:
  een `remotion/`-werkmap in het nieuwe sjabloon, met enkel de bouwstenen en assets die we
  nodig hebben. `public/` is nu 49 MB, maar niet alles is nodig.
- **App-beelden:** de app kan niet in de cloud draaien. Daarom nemen we op een donderdag
  (pc aan) **één keer een bibliotheek** schermopnames op met demo-data
  (`brands/alcolympics/assets/ui/`). De cloud hergebruikt die en we vullen ze af en toe aan.

**Hoe krijg je de MP4 op je iPhone om te posten?** Video's horen niet in git: de repo zou
elk jaar ±3 GB groeien. Voorstel: de repo bevat enkel tekst (scripts, captions, rapporten).
De MP4's en covers gaan naar een map in je **Google Drive** via de bestaande Drive-koppeling.
Op je iPhone open je de Drive-app en kies je "Opslaan in Foto's". [T] Ook dat test ik eerst.

---

## 5. TikTok: twee waarschuwingen

1. **Account overnemen** [V]: TikTok's voorwaarden (EEA) zeggen dat je toegang **"niet aan
   iemand anders gegeven kan worden"** (§4.4). Je mag ook geen account van een ander gebruiken
   zonder toestemming (§4.5). Over verkopen staat er niets expliciet, maar overdragen is een
   grijze zone met risico op een ban. Doe je het toch, betaal er dan liefst niet voor. Zet
   meteen e-mail, gsm-nummer, wachtwoord en 2FA op jouw naam, en kijk eerst in de analytics
   of die 1000 volgers Vlaamse 18–30-jarigen zijn. Anders heb je er weinig aan, of erger: het
   algoritme leert dan het verkeerde publiek. *(Dit is geen juridisch advies.)*
2. **Alcohol** [S]: volgens TikTok mogen enkel **geverifieerde zakelijke accounts** organische
   content over gereguleerde producten zoals alcohol plaatsen. Video's die *overmatig drinken*
   tonen, worden niet aanbevolen in de For You-feed. Op Instagram wordt alcoholcontent voor
   tieners verborgen, en dat is voor ons geen probleem.
   → **Strategie voor beide platformen:** toon de *app, de competitie en herkenbare
   situaties*, niet het drinken zelf. Dat beschermt het bereik en past bij de merkbijbel §9.

**Over "virale clips van anderen gebruiken"** (je vraag uit Fase 0): ook zonder betaalde ads
is dat **copyright-inbreuk**. Het auteursrecht geldt los van advertenties, en een zakelijk
account telt als commercieel gebruik. Platformen halen zulke video's neer en geven strikes.
Wat wél mag: de **ingebouwde Remix** (Instagram) of **Stitch/Duet** (TikTok) bij het posten,
als de maker dat toelaat. Daarbuiten blijft het rechtenvrij stockbeeld, eigen animatie en
app-beelden.

---

## 6. Architectuurvoorstel

### Optie A — alles in de cloud op maandag ⭐ (aanbevolen, als de tests lukken)
```
Ma 07:07  Cloud-routine "weekproductie" (één sessie, zuinig)
          1. actualiteit-agent  → weeks/2026-43/briefing.md  (trends, kansen, te vermijden, bronnen)
          2. content-agent      → 3 concepten + Remotion-code + captions + postvoorstel
          3. reviewer-agent     → aparte subagent met frisse blik (+ check_style.py),
                                  max. 2 rondes bijwerken
          4. render in de cloud → MP4 + cover → Google Drive /Alcolympics/2026-43/
          5. manager            → README.md-overzicht, commit naar GitHub, melding naar jou
Zo  19:07 Cloud-routine "analytics" → Instagram-cijfers ophalen, weekrapport,
          bijsturing voor maandag (+ TikTok-export uit de inbox, later)
```
- ✅ Pc mag uit; maandag klaar; trends zijn vers.
- ❌ Hangt af van 3 tests (renderen, melding, Drive-upload). Alles verbruikt cloud-usage.

### Optie B — hybride (terugvaloptie)
Elke donderdag 09:30 een **lokale geplande taak** op je pc: concepten maken en renderen. Op
maandag 07:07 een **korte cloud-routine** die de actualiteit nog eens checkt, een video afkeurt
of aanpast als er iets gevoeligs speelt, en je de melding stuurt.
- ✅ Renderen gebeurt zeker lokaal, zoals nu al werkt.
- ❌ Trends zijn tot een week oud als je post. Dat is jammer voor trendgedreven content.

### Optie C — alles lokaal op donderdag
- ✅ Eenvoudigst, geen cloudrisico's.
- ❌ Levering op donderdag in plaats van maandag. Ook de trends zijn dan oud.

### Usage op Pro
- **Eén cloud-sessie per week** voor de productie, plus een kleine analytics-run. Geen apart
  draaiende agents per stap.
- De rollen staan in `.claude/agents/` met het goedkoopste geschikte model:
  - **actualiteit:** Sonnet
  - **reviewer:** Sonnet, in een eigen subagent zodat hij met een frisse blik kijkt
  - **content:** het hoofdmodel
- Korte instructies; merkbijbel en gidsen worden enkel gelezen waar nodig.
- Na de eerste testweek meten we het verbruik op claude.ai/settings/usage en snoeien we bij.

### Mapstructuur (zoals de startprompt, met kleine aanpassingen)
```
social_agent_template/
  .claude/agents/   actualiteit.md · content.md · reviewer.md · manager.md
  .claude/skills/   weekbriefing · video-maken · caption-schrijven · review-checklist ·
                    copyright-check · postpakket-maken · analytics-ophalen · analytics-rapport
  .claude/settings.json   hooks: blokkeer elk publicatie-commando en het lezen of tonen van .env
  guides/           anti-ai-style.md · platform-regels.md · workflow.md
  brands/alcolympics/  brand.md · assets/ui/ · log/ · analytics/ (inbox/, rapporten) · formule.json
  weeks/2026-43/    briefing.md · review.md · README.md · video-01..03/
                    (caption.txt · hashtags.txt · postvoorstel.md · drive-link) · gepost.md
  remotion/         eigen Remotion-werkmap (bouwstenen uit je bestaande project)
  scripts/          check_style.py · audio (Python) · render · ig_insights.py · tiktok_display.py
  .env.example      namen van de sleutels, zonder waarden (.env staat in .gitignore)
  README.md         gebruik + nieuw merk toevoegen
```

### Eerste stappen in Fase 2 (in deze volgorde)
1. Private GitHub-repo aanmaken en de mapstructuur opzetten.
2. **Drie haalbaarheidstests** in een cloud-sessie: een testvideo renderen, een pushmelding
   versturen en een bestand uploaden naar Drive. De uitkomst beslist tussen A en B.
3. `remotion/`-werkmap opzetten en de nodige bouwstenen overnemen.
4. Anti-AI-stijlgids + `check_style.py`, platformregels, agents en skills schrijven.
5. Stappenplan voor de Instagram-sleutel (op dat moment geverifieerd) → eerste testopvraging.

---

## Bronnen
- Instagram Insights: https://developers.facebook.com/docs/instagram-platform/insights
- Instagram Media Insights: https://developers.facebook.com/docs/instagram-platform/reference/instagram-media/insights
- TikTok video object: https://developers.tiktok.com/doc/tiktok-api-v2-video-object
- TikTok Display API: https://developers.tiktok.com/doc/display-api-get-started
- TikTok business verification: https://ads.tiktok.com/help/article/about-business-registration
- TikTok Terms of Service (EEA): https://www.tiktok.com/legal/page/eea/terms-of-service/en
- Claude Code routines: https://code.claude.com/docs/en/routines
- Claude Code cloud-omgevingen: https://code.claude.com/docs/en/cloud-environments
- Claude Code mobiel / Remote Control: https://code.claude.com/docs/en/mobile · https://code.claude.com/docs/en/remote-control
- Alcohol & FYF (secundair): https://www.brewbound.com/news/tiktok-opens-ad-platform-to-beverage-alcohol-brands-in-the-us
- Instagram & tieners (secundair): https://www.androidheadlines.com/2025/10/instagram-further-restricts-teen-accounts-with-new-pg-13-changes.html
