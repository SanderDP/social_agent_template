# Haalbaarheidstest cloud (Fase 2, stap 2)

Opdracht voor een cloud-sessie. Doel: nagaan of de wekelijkse productie volledig in de cloud
kan draaien (optie A). Voer de drie tests uit, schrijf de resultaten weg en push ze.
Stop niet bij een mislukte test: noteer de fout en ga door met de volgende.

## Test 1 — Remotion renderen
1. Linux-bibliotheken voor Chrome Headless Shell (Ubuntu 24.04), indien nodig:
   `apt-get update && apt-get install -y libnss3 libdbus-1-3 libatk1.0-0 libatk-bridge2.0-0 libgbm1 libasound2t64 libxrandr2 libxkbcommon0 libxfixes3 libxcomposite1 libxdamage1 libpango-1.0-0 libcairo2 libcups2t64`
2. `cd remotion && npm ci && npm run render:test`
3. Noteer: gelukt ja/nee, duur, bestandsgrootte van `remotion/out/haalbaarheid.mp4`, en bij
   een fout de exacte melding. Vooral: welke host geblokkeerd werd (`403` /
   `host_not_allowed`), bv. `remotion.media`, `fonts.gstatic.com`, `fonts.googleapis.com`.

## Test 2 — pushmelding naar de iPhone
Gebruik de tool `PushNotification` (laad hem eerst via ToolSearch als hij uitgesteld is) met:
"Cloud-test Alcolympics: render [gelukt/mislukt]. Kwam deze melding aan?"
Noteer exact wat de tool teruggeeft. Bestaat de tool niet in deze sessie, noteer dat.

## Test 3 — MP4 leveren zonder hem in git te zetten
Probeer een GitHub-release met de MP4 als bijlage, via REST (geen GraphQL):
1. `gh api repos/{owner}/{repo}/releases -f tag_name=test-haalbaarheid -f name="Test haalbaarheid" -F prerelease=true`
2. Upload de MP4 naar de `upload_url` uit het antwoord (host `uploads.github.com`), bv. met
   `gh api --method POST -H "Content-Type: video/mp4" "<upload_url zonder {?name,label}>?name=haalbaarheid.mp4" --input remotion/out/haalbaarheid.mp4`
3. Noteer of het lukte en de downloadlink (`browser_download_url`).
Lukt het niet: noteer de fout.

## Resultaat
Schrijf alles naar `docs/haalbaarheid-resultaat.md` (per test: gelukt/mislukt, details,
foutmeldingen) en push naar de branch `claude/haalbaarheid`. Commit geen MP4.
