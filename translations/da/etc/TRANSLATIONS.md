# Bidrag ved at oversætte lektioner

Vi byder velkommen til oversættelser af lektionerne i dette pensum!

## Retningslinjer

Der er mapper i hver lektionmappe og introduktionsmappe, som indeholder de oversatte markdown-filer.

> Bemærk, venligst undlad at oversætte nogen kode i kodeeksempelfilerne; det eneste, der skal oversættes, er README, opgaver og quizzer. Tak!

Oversatte filer skal følge denne navngivningskonvention:

**README._[language]_.md**

hvor _[language]_ er en to-bogstavs sprogforkortelse, der følger ISO 639-1-standarden (f.eks. `README.es.md` for spansk og `README.nl.md` for hollandsk).

**assignment._[language]_.md**

Ligesom README-filerne, bedes du også oversætte opgaverne.

**Quizzer**

1. Tilføj din oversættelse til quiz-appen ved at tilføje en fil her: https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations, med korrekt navngivningskonvention (en.json, fr.json). **Venligst undlad at lokalisere ordene 'true' eller 'false'. Tak!**

2. Tilføj din sprogkode til dropdown-menuen i quiz-appens App.vue-fil.

3. Rediger quiz-appens [translations index.js-fil](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js) for at tilføje dit sprog.

4. Til sidst, rediger ALLE quiz-links i dine oversatte README.md-filer, så de peger direkte på din oversatte quiz: https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1 bliver https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id

**TAK**

Vi værdsætter virkelig din indsats!

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at opnå nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.