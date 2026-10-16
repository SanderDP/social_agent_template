---
name: video-maken
description: Van concept tot gerenderde 9:16-video met Remotion - hook, script, storyboard, compositie, audio, render en cover. Gebruikt door de content-agent.
---

# Video maken

Per video een map `weeks/<jaar-week>/video-0N/`.

## 1. Concept (`concept.md`)
- **Format** (zie lijst in `guides/anti-ai-style.md` §4) en waarom het deze week past.
- **Hook** (0–1,5 s): wat zie en lees je in het eerste beeld?
- **Script** met tijdcodes, **storyboard** in 4–8 regels (beeld · tekst · geluid).
- Lengte 6–25 s.

## 2. Bouwen (Remotion, `remotion/`)
- Nieuwe compositie in `remotion/src/weeks/<jaar-week>/Video0N.tsx`, registreren in
  `remotion/src/Root.tsx` met id `W<jaar-week>V0N` (bv. `W2026_43V01`), 1080×1920, 30 fps.
- Hergebruik bouwstenen uit `remotion/src/blokken/` als die er zijn. Maak nieuwe bouwstenen
  generiek (props) en zet ze daar.
- **Lettertypes enkel via `remotion/src/fonts.ts`** (lokaal). Laad tijdens het renderen nooit
  iets van internet: download stockbeeld eerst naar `remotion/public/weeks/<jaar-week>/`.
- Stockbeeld: Pexels-API (`PEXELS_API_KEY`), licentie en link noteren in `bronnen.md`.
- App-beelden: `brands/<merk>/assets/ui/` (kopieer naar `remotion/public/`).
- Safe zones respecteren (zie `guides/platform-regels.md` §6). Merkkleuren en -termen uit
  `brand.md`.
- **18+** in beeld of in de caption.

## 3. Audio
Zelfgemaakt met Python (`scripts/audio/`) of geen audio en een geluidssuggestie uit de
commerciële bibliotheek voor bij het posten. Nooit een beschermd nummer in de MP4.

## 4. Renderen
```
cd remotion
npx remotion render src/index.ts <id> ../weeks/<jaar-week>/video-0N/video.mp4 --crf=20
npx remotion still src/index.ts <id> ../weeks/<jaar-week>/video-0N/cover.png --frame=<beste frame>
```
Controleer met 3 stills (begin, midden, eind) of tekst leesbaar is en in de safe zones staat.
MP4's en covers worden niet op `main` gecommit (zie `postpakket-maken`).
