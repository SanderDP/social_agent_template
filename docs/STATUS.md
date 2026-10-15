# Status — waar we gebleven zijn (15 okt. 2026)

## Klaar
- **Fase 0:** vragen beantwoord → `docs/fase0-beslissingen.md`. Instagram @alcolympics.be is zakelijk.
- **Fase 1:** onderzoek + voorstel → `docs/fase1-voorstel.md`. Gekozen: **optie A** (alles in de
  cloud op maandag), op voorwaarde dat de haalbaarheidstests slagen.
- **Fase 2 gestart:** basisstructuur, private repo `SanderDP/social_agent_template`, Remotion-testvideo
  (`remotion/`). Lokaal renderen werkt (3 s video in ±45 s).

## Lopend
- Cloud-haalbaarheidstest (`docs/haalbaarheid-test.md`) gestart via `claude --cloud`:
  sessie https://claude.ai/code/session_01QNiUFAHJB8zsXznXosBgUZ
- **Resultaat nog onbekend:** de sessie heeft niets gepusht (geen branch `claude/haalbaarheid`,
  geen release). Volgende stap: de sessie openen, kijken of ze wacht of vastliep, en het
  resultaat laten pushen of hier plakken.

## Bekend
- Google Drive valt af als levering (MP4 via de connector = te veel usage). Getest wordt een
  GitHub-release als bijlage.
- Een cloud-sessie starten met de knop in de desktop-app lukte niet vanuit de eerste sessie;
  `claude --cloud "..."` in een terminal werkt wel.
- Pushmelding vanaf de pc werkt enkel met Remote Control aan.

## Daarna (Fase 2)
1. Op basis van het testresultaat: optie A of B definitief.
2. `remotion/` uitbouwen met bouwstenen uit het bestaande Remotion-project.
3. Anti-AI-stijlgids + `scripts/check_style.py`, platformregels, agents en skills.
4. Stappenplan Instagram-sleutel → eerste testopvraging.
