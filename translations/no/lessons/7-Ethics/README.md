# Etisk og Ansvarlig AI

Du er nesten ferdig med dette kurset, og jeg håper at du nå tydelig ser at AI er basert på en rekke formelle matematiske metoder som lar oss finne sammenhenger i data og trene modeller til å etterligne noen aspekter av menneskelig atferd. På dette tidspunktet i historien anser vi AI som et svært kraftig verktøy for å trekke ut mønstre fra data og bruke disse mønstrene til å løse nye problemer.

## [Quiz før forelesning](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

I science fiction ser vi imidlertid ofte historier der AI utgjør en fare for menneskeheten. Vanligvis er disse historiene sentrert rundt en slags AI-opprør, der AI bestemmer seg for å konfrontere mennesker. Dette antyder at AI har en form for følelser eller kan ta beslutninger som utviklerne ikke hadde forutsett.

Den typen AI vi har lært om i dette kurset er ikke annet enn stor matriseberegning. Det er et svært kraftig verktøy for å hjelpe oss med å løse våre problemer, og som alle andre kraftige verktøy – det kan brukes til gode og dårlige formål. Viktigst av alt, det kan *misbrukes*.

## Prinsipper for Ansvarlig AI

For å unngå utilsiktet eller bevisst misbruk av AI, har Microsoft fastsatt viktige [Prinsipper for Ansvarlig AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Følgende konsepter ligger til grunn for disse prinsippene:

* **Rettferdighet** er knyttet til det viktige problemet med *modellskjevheter*, som kan oppstå ved bruk av skjev data til trening. For eksempel, når vi prøver å forutsi sannsynligheten for at en person får en jobb som programvareutvikler, vil modellen sannsynligvis gi høyere preferanse til menn – bare fordi treningsdatasettet sannsynligvis var skjevt mot en mannlig målgruppe. Vi må nøye balansere treningsdata og undersøke modellen for å unngå skjevheter, og sørge for at modellen tar hensyn til mer relevante egenskaper.
* **Pålitelighet og Sikkerhet**. Av natur kan AI-modeller gjøre feil. Et nevralt nettverk returnerer sannsynligheter, og vi må ta dette i betraktning når vi tar beslutninger. Hver modell har en viss presisjon og tilbakekalling, og vi må forstå dette for å forhindre skade som feil råd kan forårsake.
* **Personvern og Sikkerhet** har noen AI-spesifikke implikasjoner. For eksempel, når vi bruker noen data til å trene en modell, blir disse dataene på en eller annen måte "integrert" i modellen. På den ene siden øker det sikkerhet og personvern, på den andre siden må vi huske hvilke data modellen ble trent på.
* **Inkludering** betyr at vi ikke bygger AI for å erstatte mennesker, men heller for å styrke mennesker og gjøre arbeidet vårt mer kreativt. Det er også knyttet til rettferdighet, fordi når vi arbeider med underrepresenterte samfunn, er de fleste datasett vi samler sannsynligvis skjeve, og vi må sørge for at disse samfunnene er inkludert og håndtert korrekt av AI.
* **Åpenhet**. Dette inkluderer å sørge for at vi alltid er tydelige på at AI brukes. Også, der det er mulig, ønsker vi å bruke AI-systemer som er *tolkbare*.
* **Ansvarlighet**. Når AI-modeller kommer med noen beslutninger, er det ikke alltid klart hvem som er ansvarlig for disse beslutningene. Vi må sørge for at vi forstår hvor ansvaret for AI-beslutninger ligger. I de fleste tilfeller vil vi inkludere mennesker i beslutningsprosessen, slik at faktiske personer holdes ansvarlige.

## Verktøy for Ansvarlig AI

Microsoft har utviklet [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) som inneholder et sett med verktøy:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard som inkluderer

   - EconML – et verktøy for årsaksanalyse, som fokuserer på "hva hvis"-spørsmål
   - DiCE – et verktøy for kontrafaktisk analyse som lar deg se hvilke egenskaper som må endres for å påvirke modellens beslutning

For mer informasjon om AI-etikk, vennligst besøk [denne leksjonen](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) i Maskinlæringspensumet som inkluderer oppgaver.

## Gjennomgang og Selvstudium

Ta denne [Læringsstien](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) for å lære mer om ansvarlig AI.

## [Quiz etter forelesning](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.