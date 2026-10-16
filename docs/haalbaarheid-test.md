# Haalbaarheidstest cloud — ronde 2

Ronde 1 staat in `docs/haalbaarheid-resultaat.md` op de branch `claude/haalbaarheid`:
de render faalde omdat headless Chrome tijdens het renderen een Google Font van internet
haalde en de proxy-CA niet vertrouwt (`ERR_CERT_AUTHORITY_INVALID`), en GitHub-releases
zijn verboden voor cloud-sessies.

Aanpassingen sindsdien: lettertypes staan lokaal in `remotion/public/fonts/` en worden via
`@remotion/fonts` geladen. Tijdens het renderen wordt dus niets meer van internet gehaald.
Levering gebeurt niet meer via releases maar via een aparte branch.

Voer de twee tests uit. Stop niet bij een mislukte test: noteer de exacte fout. Schakel nooit
TLS-verificatie uit.

## Test 1 — Remotion renderen (opnieuw)
1. `cd remotion && npm ci && npm run render:test`
2. Noteer: gelukt ja/nee, totale duur, bestandsgrootte van `remotion/out/haalbaarheid.mp4`,
   en bij een fout de exacte melding.

## Test 2 — MP4 leveren via een aparte branch
1. Maak vanaf `main` een nieuwe branch `claude/levering-test`.
2. Kopieer de MP4 naar `levering/haalbaarheid.mp4` (forceer toevoegen als `.gitignore` hem
   tegenhoudt), commit en push die branch.
3. Noteer of het pushen lukte en de link
   `https://github.com/SanderDP/social_agent_template/blob/claude/levering-test/levering/haalbaarheid.mp4`.

## Resultaat
Schrijf alles naar `docs/haalbaarheid-resultaat-2.md` en push naar de branch
`claude/haalbaarheid-2`. Zet de MP4 enkel op `claude/levering-test`, niet op
`claude/haalbaarheid-2`. Stuur op het einde een pushmelding (tool `PushNotification`) met
"Cloud-test 2 klaar: render [gelukt/mislukt], levering [gelukt/mislukt]".
