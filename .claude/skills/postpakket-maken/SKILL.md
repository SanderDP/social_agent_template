---
name: postpakket-maken
description: Bundel goedgekeurde video's tot kant-en-klare postpakketten met postvoorstel, weekoverzicht en levering op een aparte branch. Gebruikt door de manager.
---

# Postpakket maken

## Per goedgekeurde video (`weeks/<jaar-week>/video-0N/`)
- `video.mp4`, `cover.png`, `caption.txt` (+ `caption-tiktok.txt`), `hashtags.txt`
- `postvoorstel.md`:
```
# video-0N — <titel>
**Wanneer**: <dag> <datum> om <uur> (Instagram) · <dag/uur> (TikTok, als anders)
**Waarom**: doelgroep-gewoonte, actualiteit uit het briefje, wat eerder werkte (cijfers uit
het laatste rapport, met label [V]/[S]/[?])
**Geluid bij het posten**: <concreet nummer uit de commerciële bibliotheek, of "eigen audio
laten staan">
**Tekst in de app toevoegen**: <eventuele tekstsuggestie of TTS>
**Let op**: <waarschuwing van de reviewer, als die er is>
```

## Weekoverzicht `weeks/<jaar-week>/README.md`
Tabel met per video: titel, format, één zin over het idee, voorgesteld moment, reviewoordeel,
downloadlink. Bovenaan: wat de eigenaar volgens jou als eerste zou moeten posten en waarom.

## Leveren
1. Commit alles behalve MP4/PNG naar `main`.
2. Maak branch `levering/<jaar-week>` vanaf `main`, voeg de MP4's en covers toe
   (`git add -f`), commit en push.
3. Downloadlinks: `https://github.com/<owner>/<repo>/blob/levering/<jaar-week>/weeks/<jaar-week>/video-0N/video.mp4`
4. Pushmelding (max 200 tekens), bv.:
   `3 video's voor week 43 klaar. Start met video-02 (do-avond). Alles: github.com/.../weeks/2026-43`
5. Regel in `brands/<merk>/log/logboek.md` en de formats in `brands/<merk>/log/formats.md`.
