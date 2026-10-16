---
name: review-checklist
description: Vaste checklist waarmee de reviewer elke video beoordeelt en GOED / AANPASSEN / AFKEUREN geeft.
---

# Review-checklist

Schrijf per video in `weeks/<jaar-week>/review.md`:

```
## video-0N — <titel> — GOED | AANPASSEN | AFKEUREN (ronde 1|2)
| Criterium | Oordeel | Opmerking (concreet, met tijdcode/positie) |
|---|---|---|
| Ziet dit eruit als AI? | ✅/⚠️/❌ | |
| Merk (toon, termen, feiten, kleuren) | | |
| Alcohol & verantwoordelijkheid (18+, geen aanmoediging) | | |
| Copyright & platformregels | | |
| Hook in 1–2 s | | |
| Leesbaarheid gsm + safe zones | | |
| Tempo & afwerking | | |
| Caption (check_style.py: OK/FOUT) | | |
| Variatie t.o.v. vorige weken | | |
**Te doen**: genummerde lijst met exacte aanpassingen.
```

## Oordeel
- **AFKEUREN**: schending van alcoholregels, minderjarigen, copyright of platformregels die
  niet met één duidelijke aanpassing op te lossen is; of het ziet er onmiskenbaar uit als AI.
- **AANPASSEN**: elk ❌ of ⚠️ dat op te lossen is; elke FOUT van `check_style.py`.
- **GOED**: alles ✅, hoogstens kleine ⚠️ die je expliciet aanvaardt en motiveert.

## Werkwijze
1. Bekijk eerst het eerste beeld zonder context. Wat denk je in 1 seconde?
2. Dan de stills (begin, midden, eind) en het script.
3. Controleer feiten tegen `brand.md` (functienamen, ranks, prijzen). Eén fout feit = AANPASSEN.
4. Na ronde 2 nog niet GOED: AFKEUREN of meesturen met een duidelijke waarschuwing bovenaan
   het postpakket. De eigenaar beslist.
