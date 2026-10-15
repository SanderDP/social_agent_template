# Resultaat haalbaarheidstest cloud (Fase 2, stap 2)

Uitgevoerd op: 2026-10-15, in een cloud-sessie (Claude Code remote execution
environment) op branch `claude/haalbaarheid`.

Samenvatting: **optie A (volledig in de cloud) is op dit moment niet haalbaar.**
Alle drie de tests zijn mislukt, maar niet door een geblokkeerde host zoals
verondersteld in de testbeschrijving — de oorzaken liggen bij TLS-interceptie
door de agent-proxy (test 1) en een sessiebeleid dat GitHub-releases verbiedt
(test 3).

## Test 1 — Remotion renderen

**Gelukt: nee.**

Stappen:
1. De Linux-bibliotheken uit de opdracht (`libnss3`, `libdbus-1-3`, enz.) waren
   al aanwezig op het image; `apt-get install` installeerde niets nieuws.
2. `npm ci` in `remotion/` is gelukt (256 packages, 13 s, 0 vulnerabilities).
3. `npm run render:test` is gestart en heeft **niet** geblokkeerd op het
   downloaden van Chrome Headless Shell: de download van
   `https://remotion.media/chromium-headless-shell-linux-x64-157.0.8080.0.zip`
   (98,9 MB) is volledig gelukt. Dus **`remotion.media` is niet geblokkeerd**
   in deze sessie — dat weerlegt het voorbeeld uit de testbeschrijving.
4. Bundelen (esbuild) is gelukt tot 100%.
5. Het renderen zelf faalde bij het laden van een Google Font. Geen `403` en
   geen `host_not_allowed`, maar een TLS-certificaatfout:

   ```
   Browser failed to load https://fonts.gstatic.com/s/ibmplexsans/v23/zYXzKVElMYYaJe8bpLHnCwDKr932-G7dytD-Dmu1syxeKYY.woff2 (Fetch): net::ERR_CERT_AUTHORITY_INVALID

   An error occurred:
    TypeError  Failed to fetch
   at node_modules/remotion/dist/esm/no-react.mjs:1503
   at tryToLoad (node_modules/@remotion/google-fonts/dist/esm/IBMPlexSans.mjs:115)
   ```

**Oorzaak:** deze cloud-sessie routeert alle uitgaande HTTPS via een
agent-proxy die TLS zelf opnieuw termineert met een eigen CA
(`/root/.ccr/ca-bundle.crt`). Veel tools (curl, npm, git, …) zijn al
voorgeconfigureerd om die CA te vertrouwen, maar de los gedownloade **Chrome
Headless Shell** (via Puppeteer/Remotion) gebruikt zijn eigen NSS-certificate-
store en vertrouwt die CA niet. Daardoor ziet de browser elk HTTPS-verzoek
(hier: `fonts.gstatic.com`) als een ongeldig certificaat
(`ERR_CERT_AUTHORITY_INVALID`) en breekt de render af. Dit is dus geen
geblokkeerde host, maar een vertrouwensprobleem tussen de proxy-CA en de
headless browser. De proxy-status (`__agentproxy/status`) toonde
`"recentRelayFailures": []`, wat erop wijst dat het verzoek de proxy wél
passeerde en pas bij Chrome zelf strandde.
Volgens de proxy-richtlijnen mag TLS-verificatie nooit worden uitgeschakeld
(bv. via `--ignore-certificate-errors`), dus dat is niet geprobeerd.

**Resultaat `remotion/out/haalbaarheid.mp4`:** bestand bestaat niet (render
is nooit voltooid). Bestandsgrootte en duur van een succesvolle render zijn
dus niet gemeten; de mislukking trad op na ca. 23,5 s (inclusief bundelen en
chrome-download).

## Test 2 — pushmelding naar de iPhone

**Tool aanwezig: ja.** `PushNotification` was beschikbaar na laden via
`ToolSearch`.

Aanroep:
```
PushNotification(message="Cloud-test Alcolympics: render mislukt. Kwam deze melding aan?", status="proactive")
```

Exacte teruggave van de tool: `"Mobile push requested."`

De tool bevestigt alleen dat de push is *aangevraagd* (via Remote Control),
niet dat hij daadwerkelijk op het toestel is aangekomen. Of de melding echt
op de iPhone binnenkwam, kan alleen de gebruiker bevestigen.

## Test 3 — MP4 leveren zonder hem in git te zetten (GitHub release)

**Gelukt: nee.**

Omdat test 1 geen `remotion/out/haalbaarheid.mp4` opleverde, kon stap 2 (upload
van de mp4 naar `upload_url`) sowieso niet met het echte bestand getest
worden. Stap 1 (release aanmaken) is wel uitgevoerd, met de exacte opdracht
uit de testbeschrijving:

```
gh api repos/SanderDP/social_agent_template/releases -f tag_name=test-haalbaarheid -f name="Test haalbaarheid" -F prerelease=true
```

Bijkomstigheid: `gh auth status` meldt zelf een ongeldige `GH_TOKEN`
("Failed to log in to github.com using token (GH_TOKEN)"), maar de
daadwerkelijke API-aanroep loopt via een andere, sessie-specifieke
autenticatielaag en kwam wél bij GitHub aan. Die aanroep gaf:

```
HTTP 403
{"message":"Creating, editing, or deleting releases is not permitted for this session type.","documentation_url":"https://docs.anthropic.com/en/docs/claude-code/github-actions"}
```

**Oorzaak:** geen geblokkeerde host en geen netwerkfout — `api.github.com`
is bereikbaar (zie de `noProxy`-lijst van de agent-proxy, die GitHub-achtige
infrastructuur niet blokkeert) — maar een expliciet beleid van deze
sessie-omgeving dat het aanmaken/wijzigen/verwijderen van GitHub-releases
verbiedt voor "dit sessietype" (een cloud-sessie zoals deze). Dit is dus een
harde, door het platform opgelegde beperking, niet iets wat met andere
command-opties of met de GitHub MCP-server te omzeilen is: de MCP
GitHub-server biedt ook geen `create_release`/`upload_release_asset`-tool,
alleen lees-tools (`list_releases`, `get_latest_release`, `get_release_by_tag`).

Stap 2 (upload naar `uploads.github.com`) en stap 3 (downloadlink) zijn niet
bereikt, omdat stap 1 al faalde.

## Conclusie

| Test | Gelukt | Kernoorzaak |
|---|---|---|
| 1. Remotion render | Nee | TLS-vertrouwensfout van headless Chrome op de agent-proxy-CA bij `fonts.gstatic.com` (geen geblokkeerde host — `remotion.media` werkte wél) |
| 2. Pushmelding | Tool werkt, aflevering onbevestigd | Tool retourneert alleen "Mobile push requested." |
| 3. MP4 via GitHub release | Nee | Sessiebeleid verbiedt release-aanmaak (HTTP 403, "not permitted for this session type") voor dit sessietype |

Optie A (volledige wekelijkse productie in de cloud, zoals nu opgezet) stuit
op twee onafhankelijke blokkades die niet door deze sessie zelf op te lossen
zijn: (1) de headless-Chrome/Google-Fonts-render vereist dat Chrome de
proxy-CA vertrouwt (losse systeemconfiguratie, geen code-aanpassing), en (2)
MP4-levering via GitHub-releases is voor dit sessietype hard uitgeschakeld.
Een alternatieve leverroute voor de MP4 (bijv. zelf-gehoste storage, of een
sessietype met release-rechten) en een oplossing voor het CA-vertrouwen van
de headless browser zijn nodig voordat optie A haalbaar is.
