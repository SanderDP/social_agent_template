# Haalbaarheidstest cloud — resultaat ronde 2

Uitgevoerd op 2026-10-16 in een Claude Code-cloudsessie, vanaf `main` (commit `155b28f`).
Node v22.22.0, npm 10.9.4. TLS-verificatie is nergens uitgeschakeld.

| Test | Resultaat |
|---|---|
| 1 — Remotion renderen | **gelukt** |
| 2 — MP4 leveren via aparte branch | **gelukt** |

## Test 1 — Remotion renderen

Commando's: `cd remotion && npm ci && npm run render:test`

- **Gelukt:** ja (exitcode 0 voor beide commando's)
- **Duur:** `npm ci` 7 s, `npm run render:test` 18 s, samen ongeveer 25 s.
  In die 18 s zit ook het eenmalig downloaden van Chrome Headless Shell (98,9 MB van
  `remotion.media`), dat via de proxy zonder fouten verliep.
- **Bestandsgrootte** `remotion/out/haalbaarheid.mp4`: 69.723 bytes (69,7 kB)
- **Controle met ffprobe:** h264, 1080×1920 (9:16), 30 fps, 3,0 s (90 frames).
- **Beeld:** een frame op 2 s toont het Alcolympics-logo en de tekst "render-test ok" in het
  juiste lettertype. De lokale lettertypes uit `remotion/public/fonts/` werken dus.
- **Foutmelding:** geen. De fout uit ronde 1 (`ERR_CERT_AUTHORITY_INVALID` bij het laden van een
  Google Font) komt niet meer voor.
- Enige opmerking in de log (geen fout): Remotion meldt een verschil tussen het geheugen dat
  de cgroup rapporteert en `/proc/meminfo`, en rekent met de laagste waarde. Dat had geen
  invloed op de render.

## Test 2 — MP4 leveren via een aparte branch

- Branch `claude/levering-test` gemaakt vanaf `main`, MP4 gekopieerd naar
  `levering/haalbaarheid.mp4`.
- Forceren was **niet nodig**: `.gitignore` houdt `levering/` niet tegen (alleen `remotion/out/`
  en `*.mov`/`*.wav` worden genegeerd), dus een gewone `git add` volstond.
- Commit `a57a54d` is **gepusht**, zonder fouten.
- Via de GitHub-API gecontroleerd dat het bestand er staat, met dezelfde grootte (69.723 bytes).
- Link: https://github.com/SanderDP/social_agent_template/blob/claude/levering-test/levering/haalbaarheid.mp4

## Conclusie voor de maandagroutine

Beide knelpunten uit ronde 1 zijn opgelost. In een cloudsessie lukt renderen met lokale
lettertypes, en leveren via een aparte branch ook. Aandachtspunten:

- Bij elke nieuwe sessie wordt Chrome Headless Shell opnieuw gedownload (~99 MB, een paar
  seconden). Dat werkt, maar het hangt af van `remotion.media` en de proxy.
- MP4's in git stapelen zich op in de repo-geschiedenis. Voor 3 korte video's per week valt
  dat mee, maar het is beter om per levering een aparte branch te gebruiken (bv.
  `levering/JJJJ-WW`) en oude leverbranches op te ruimen.
- De MP4 staat niet op deze branch (`claude/haalbaarheid-2`), alleen op `claude/levering-test`.
