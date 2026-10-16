# Status — waar we gebleven zijn (16 okt. 2026)

## Klaar
- **Fase 0:** `docs/fase0-beslissingen.md`. Instagram @alcolympics.be is zakelijk.
- **Fase 1:** `docs/fase1-voorstel.md`.
- **Optie A bevestigd** (cloud-test ronde 2, branch `claude/haalbaarheid-2`): renderen in de
  cloud werkt met lokale lettertypes (±25 s voor de test), levering via een aparte branch werkt.
  Releases zijn verboden in cloud-sessies.
- **Team gebouwd:** `guides/` (anti-AI-stijlgids, platformregels, workflow),
  `scripts/check_style.py`, 4 agents in `.claude/agents/`, 8 skills in `.claude/skills/`,
  logbestanden in `brands/alcolympics/log/`, `.env` afgeschermd in `.claude/settings.json`.
- **Push:** "Push when Claude decides" staat aan (`/config`). Lokaal wordt niet gepusht zolang
  de eigenaar actief is aan de pc. Vanuit de cloud: nog niet bevestigd.

## Volgende stappen
1. **Remotion-bouwstenen** overnemen uit `../remotion` naar `remotion/src/blokken/`
   (sip-animatie, rank-chips, groepschat, logo-outro) + assets.
2. **Audio-script** (`scripts/audio/`) uit het bestaande Remotion-project.
3. **App-beeldenbibliotheek**: één keer schermopnames met demo-data (pc aan, donderdag).
4. **Instagram-sleutel**: stappenplan (Meta-app, token, network secret) + `scripts/ig_insights.py`
   + testopvraging.
5. **Pexels-sleutel** als network secret.
6. **Testweek met de hand** (Fase 3), daarna de routines (ma 07:07 productie, zo 19:07 analytics).
7. Opruimen: branches `claude/haalbaarheid*` en `claude/levering-test`.
