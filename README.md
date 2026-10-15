# Social Agent Template

Herbruikbaar AI-socialemediateam in Claude Code. Elke week maakt het team kant-en-klare
9:16-video's met een postpakket (caption, hashtags, cover, postvoorstel). **Er wordt nooit
automatisch gepost**: de eigenaar post zelf.

Eerste merk: **Alcolympics** (`brands/alcolympics/`).

> Status: Fase 2 in opbouw. Zie `docs/fase1-voorstel.md` voor de architectuur.

## Mappen
```
.claude/agents/   de 4 rollen (actualiteit, content, reviewer, manager)
.claude/skills/   herbruikbare werkwijzen
guides/           anti-AI-stijlgids, platformregels, workflow
brands/<merk>/    alles wat merkspecifiek is (brand.md, assets, log, analytics)
weeks/<jaar-week>/  output per week
remotion/         videobouwstenen (Remotion 4)
scripts/          render, audio, analytics, stijlcontrole
docs/             beslissingen en onderzoek
```

## Sleutels
Kopieer `.env.example` naar `.env` en vul die zelf in. Sleutels horen nooit in git of in de chat.
