---
name: analytics-ophalen
description: Haal de cijfers van de eigen Instagram- (en later TikTok-) posts op via de officiële API's en de TikTok Studio-export in de inbox. Gebruikt door de manager.
---

# Analytics ophalen

Output: `brands/<merk>/analytics/<jaar-week>.json`

## Instagram
`python scripts/ig_insights.py --merk <merk> --week <jaar-week>`
(Instagram API with Instagram Login, eigen account. Script en sleutel volgen in Fase 2.)
Per Reel: views, reach, likes, comments, shares, saved, reposts, total_interactions,
ig_reels_avg_watch_time, reels_skip_rate. Accountcijfers blijven maar 90 dagen bewaard bij
Meta: altijd wekelijks opslaan.
Onder 100 volgers ontbreken sommige cijfers: noteer dat, verzin niets.

## TikTok (zodra het account er is)
- `python scripts/tiktok_display.py` (Display API: views, likes, comments, shares).
- Diepere cijfers (kijktijd, % volledig bekeken, publiek): lees de exports/screenshots in
  `brands/<merk>/analytics/inbox/` en verplaats ze daarna naar `inbox/verwerkt/`.

## Regels
- Enkel officiële API's en eigen exports. Geen scrapers, nooit inloggen met een wachtwoord.
- Sleutels komen uit de omgeving (network secret in de cloud, `.env` lokaal). Nooit printen.
- Mislukt een API-call (token vervallen): noteer het in het logboek en zet in de melding aan
  de eigenaar wat hij moet doen (zie `docs/` voor het token-stappenplan).
