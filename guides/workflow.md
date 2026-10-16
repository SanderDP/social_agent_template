# Workflow

## Wekelijkse productie (maandag 07:07, cloud-routine)
Eén sessie, rollen na elkaar, zuinig met usage.

1. **Manager** leest `brands/<merk>/log/bijsturing.md` (laatste analytics-advies) en
   `brands/<merk>/log/formats.md`, maakt `weeks/<jaar-week>/`.
2. **Actualiteit-agent** → `weeks/<jaar-week>/briefing.md` (skill `weekbriefing`).
3. **Content-agent** → 3 concepten in `weeks/<jaar-week>/video-01..03/` (skills `video-maken`,
   `caption-schrijven`), rendert met Remotion.
4. **Reviewer-agent** (subagent, frisse blik) → `weeks/<jaar-week>/review.md` met per video
   GOED / AANPASSEN / AFKEUREN (skills `review-checklist`, `copyright-check`).
   AANPASSEN → content-agent past aan → opnieuw review. **Max. 2 rondes**, daarna valt de
   video af of gaat hij mee met een duidelijke waarschuwing.
5. **Manager** → postpakketten (skill `postpakket-maken`), `weeks/<jaar-week>/README.md`,
   commit tekst naar `main`, MP4's + covers naar de branch `levering/<jaar-week>`,
   en een melding (PushNotification) met de link.

## Analytics (zondag 19:07, cloud-routine)
Manager: skill `analytics-ophalen` → `brands/<merk>/analytics/<jaar-week>.json`, dan skill
`analytics-rapport` → `brands/<merk>/analytics/rapport-<jaar-week>.md` en
`brands/<merk>/log/bijsturing.md` (input voor maandag).

## Feedback van de eigenaar
De eigenaar zegt in een sessie wat hij gepost heeft en wat hij ervan vindt. De manager:
- vult `weeks/<jaar-week>/gepost.md` aan (welke video, platform, datum, uur);
- noteert feedback in `brands/<merk>/log/feedback.md`;
- laat bij een aanpassingsvraag de content-agent bijwerken en opnieuw leveren.

## Leveren
- Tekst (briefing, scripts, captions, rapporten) → `main`.
- MP4's en covers → branch `levering/<jaar-week>`. Oude leverbranches worden na 4 weken
  verwijderd (de manager stelt dat voor; de eigenaar keurt goed).

## Labels voor beweringen (briefing en rapporten)
**[V]** geverifieerd met bron · **[S]** aanname of secundaire bron · **[?]** hypothese.
