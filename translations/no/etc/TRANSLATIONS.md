# Bidra ved å oversette leksjoner

Vi ønsker oversettelser av leksjonene i dette pensumet velkommen!

## Retningslinjer

Det finnes mapper i hver leksjonsmappe og introduksjonsmappe som inneholder de oversatte markdown-filene.

> Merk, vennligst ikke oversett kode i kodeeksempelfilene; det eneste som skal oversettes er README, oppgaver og quizene. Takk!

Oversatte filer bør følge denne navnekonvensjonen:

**README._[language]_.md**

hvor _[language]_ er en to-bokstavs språkforkortelse som følger ISO 639-1-standarden (f.eks. `README.es.md` for spansk og `README.nl.md` for nederlandsk).

**assignment._[language]_.md**

På samme måte som README-filer, vennligst oversett oppgavene også.

**Quizer**

1. Legg til oversettelsen din i quiz-appen ved å legge til en fil her: https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations, med riktig navnekonvensjon (en.json, fr.json). **Vennligst ikke lokaliser ordene 'true' eller 'false'. Takk!**

2. Legg til språkforkortelsen din i nedtrekksmenyen i quiz-appens App.vue-fil.

3. Rediger quiz-appens [translations index.js-fil](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js) for å legge til språket ditt.

4. Til slutt, rediger ALLE quiz-lenkene i dine oversatte README.md-filer slik at de peker direkte til din oversatte quiz: https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1 blir https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id

**TAKK**

Vi setter virkelig pris på innsatsen din!

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.