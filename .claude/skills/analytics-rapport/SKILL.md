---
name: analytics-rapport
description: Maak het wekelijkse analyticsrapport - wat werkt, wat niet, en concrete bijsturing voor de volgende week. Gebruikt door de manager.
---

# Analytics-rapport

Input: `brands/<merk>/analytics/*.json`, `weeks/*/gepost.md`, `brands/<merk>/log/formats.md`.
Output: `brands/<merk>/analytics/rapport-<jaar-week>.md` en `brands/<merk>/log/bijsturing.md`
(overschrijven: dat is de input voor maandag).

## Rapport (kort)
1. **Wat is er gepost** (video, platform, moment).
2. **Cijfers** per video, met de **mediaan van het account** als vergelijkingspunt
   (niet het gemiddelde: één uitschieter vertekent alles).
3. **Wat werkte / wat niet**, gekoppeld aan één variabele: format, hook, lengte, moment,
   caption. Label [V] als het cijfer het toont, [?] als het een vermoeden is.
4. **Kijktijd en skip-rate** zeggen het meest over de hook. Gebruik ze als ze er zijn.

## Testen (testladder)
- Test **één variabele tegelijk**, over ±4 weken (min. 4 video's per variant).
- Een variant wint pas bij ≥ +20 % op de mediaan. Anders blijft de huidige aanpak.
- Bewezen regels gaan naar `brands/<merk>/formule.md` met datum en cijfers.

## Bijsturing (`log/bijsturing.md`, max 10 regels)
- Wat we volgende week **meer** doen, **minder** doen, en welke **test** loopt.
- Advies over postmomenten op basis van de data (tot er genoeg data is: [S]).
