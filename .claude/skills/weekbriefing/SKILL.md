---
name: weekbriefing
description: Maak het weekbriefje voor een merk - kansen, trends en te vermijden onderwerpen voor de komende 7 dagen, met bronnen. Gebruikt door de actualiteit-agent.
---

# Weekbriefing

Output: `weeks/<jaar-week>/briefing.md` (ISO-week, bv. `2026-43`).

## Zoek (gericht, ±10–15 zoekopdrachten, niet meer)
1. **Kalender**: feestdagen, lange weekends, schoolvakanties, examenperiodes, studentenweken,
   cantussen/TD's van grote kringen, festivals en stadsfeesten in de regio van het merk.
2. **Sport**: grote matchen (Rode Duivels, EK/WK, Champions League, Belgische topmatchen).
3. **Weer**: weekvoorspelling (terrasweer, regenweek, eerste vrieskou).
4. **Trends**: wat speelt op Reels/TikTok bij 18–30 (formats, memes, geluiden). Bronnen:
   websearch, het publieke TikTok Creative Center, nieuwsberichten over trends. Lezen, niet
   scrapen.
5. **Nieuws**: alcohol, uitgaansleven, studenten, en het merk zelf.

## Schrijf (max ±1 A4)
```
# Weekbriefje <jaar-week> — <merk>
## Top 3 kansen
- [V] <kans> — waarom relevant, wanneer (datum/dag), bron
## Trends en formats die nu werken
- [S] <trend/format> — hoe we het merkeigen kunnen inzetten, bron
## Kalender deze week
- ma … zo: wat valt waar
## Te vermijden
- <onderwerp> — waarom, bron
## Advies voor de content-agent
2–3 zinnen: waar zit de beste kans deze week, en welke toon past.
```
Elke bewering een label [V]/[S]/[?] en een link. Geen bron = [?].
