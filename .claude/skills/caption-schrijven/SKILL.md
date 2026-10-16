---
name: caption-schrijven
description: Schrijf caption en hashtags voor Reels en TikTok in de stem van het merk, zonder AI-tells. Gebruikt door de content-agent.
---

# Caption schrijven

Output in `weeks/<jaar-week>/video-0N/`: `caption.txt` (Instagram) en, als TikTok anders
moet, `caption-tiktok.txt`; `hashtags.txt`.

1. Lees de toon in `brands/<merk>/brand.md` en `guides/anti-ai-style.md` §1.
2. Schrijf **3 varianten** van max. 2 regels, kies de beste, gooi de rest weg.
   Test: zou een Vlaamse twintiger dit zo in de groepschat typen?
3. De caption herhaalt de grap niet. Ze voegt iets toe (een detail, een tag-oproep) of zegt
   bijna niks.
4. Verplicht: **18+** (en waar passend "drink met mate") als het niet al in beeld staat.
   CTA alleen als het natuurlijk is ("link in bio", "daag je groep uit").
5. Hashtags: 3–5, specifiek (merk + doelgroep + moment). Geen #fyp-spam of generieke tags.
6. TikTok-variant: vaak korter, iets meer "inside joke"; Instagram mag een tikje uitleg meer.
7. Draai `python scripts/check_style.py caption.txt`. Een FOUT betekent herschrijven.
