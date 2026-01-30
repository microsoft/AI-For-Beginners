# Bidra genom att översätta lektioner

Vi välkomnar översättningar av lektionerna i detta läroplan!

## Riktlinjer

Det finns mappar i varje lektionsmapp och introduktionsmapp som innehåller de översatta markdown-filerna.

> Observera, vänligen översätt inte någon kod i kodexempelfilerna; det enda som ska översättas är README, uppgifter och frågesporter. Tack!

Översatta filer bör följa denna namngivningskonvention:

**README._[language]_.md**

där _[language]_ är en tvåbokstavskod enligt ISO 639-1-standarden (t.ex. `README.es.md` för spanska och `README.nl.md` för nederländska).

**assignment._[language]_.md**

Precis som README-filer, vänligen översätt även uppgifterna.

**Frågesporter**

1. Lägg till din översättning till frågesport-appen genom att lägga till en fil här: https://github.com/microsoft/AI-For-Beginners/tree/main/etc/quiz-app/src/assets/translations, med korrekt namngivningskonvention (en.json, fr.json). **Vänligen lokalisera inte orden 'true' eller 'false'. Tack!**

2. Lägg till din språkkod i rullgardinsmenyn i frågesport-appens App.vue-fil.

3. Redigera frågesport-appens [translations index.js-fil](https://github.com/microsoft/AI-For-Beginners/blob/main/etc/quiz-app/src/assets/translations/index.js) för att lägga till ditt språk.

4. Slutligen, redigera ALLA frågesportlänkar i dina översatta README.md-filer så att de pekar direkt till din översatta frågesport: https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1 blir https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/1?loc=id

**TACK**

Vi uppskattar verkligen dina ansträngningar!

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.