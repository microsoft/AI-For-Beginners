# Etisk och Ansvarsfull AI

Du har nästan avslutat den här kursen, och jag hoppas att du nu tydligt ser att AI bygger på ett antal formella matematiska metoder som gör att vi kan hitta relationer i data och träna modeller för att återspegla vissa aspekter av mänskligt beteende. Vid denna tidpunkt i historien anser vi att AI är ett mycket kraftfullt verktyg för att extrahera mönster från data och tillämpa dessa mönster för att lösa nya problem.

## [För-lärosessionens quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Men i science fiction ser vi ofta berättelser där AI utgör en fara för mänskligheten. Vanligtvis handlar dessa berättelser om någon form av AI-revolt, när AI beslutar att konfrontera människor. Detta innebär att AI har någon form av känsla eller kan fatta beslut som dess utvecklare inte förutsåg.

Den typ av AI som vi har lärt oss om i den här kursen är inget mer än stor matrisaritmetik. Det är ett mycket kraftfullt verktyg för att hjälpa oss att lösa våra problem, och precis som med alla andra kraftfulla verktyg - kan det användas för både goda och dåliga syften. Viktigt att notera är att det kan *missbrukas*.

## Principer för Ansvarsfull AI

För att undvika detta oavsiktliga eller avsiktliga missbruk av AI, anger Microsoft de viktiga [Principerna för Ansvarsfull AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Följande koncept ligger till grund för dessa principer:

* **Rättvisa** är kopplat till det viktiga problemet med *modellpartiskhet*, som kan orsakas av att använda partisk data för träning. Till exempel, när vi försöker förutsäga sannolikheten att få ett jobb som mjukvaruutvecklare för en person, är det troligt att modellen ger högre preferens till män - bara för att träningsdatasetet sannolikt var partiskt mot en manlig publik. Vi måste noggrant balansera träningsdata och undersöka modellen för att undvika partiskhet och se till att modellen tar hänsyn till mer relevanta egenskaper.
* **Tillförlitlighet och Säkerhet**. Av sin natur kan AI-modeller göra misstag. Ett neuralt nätverk returnerar sannolikheter, och vi måste ta hänsyn till detta när vi fattar beslut. Varje modell har viss precision och återkallande, och vi behöver förstå detta för att förhindra skador som felaktiga råd kan orsaka.
* **Integritet och Säkerhet** har vissa AI-specifika implikationer. Till exempel, när vi använder viss data för att träna en modell, blir dessa data på något sätt "integrerade" i modellen. Å ena sidan ökar det säkerheten och integriteten, å andra sidan måste vi komma ihåg vilken data modellen tränades på.
* **Inkludering** betyder att vi inte bygger AI för att ersätta människor, utan snarare för att komplettera människor och göra vårt arbete mer kreativt. Det är också relaterat till rättvisa, eftersom när vi arbetar med underrepresenterade samhällen, är de flesta dataset vi samlar in sannolikt partiska, och vi måste se till att dessa samhällen inkluderas och hanteras korrekt av AI.
* **Transparens**. Detta inkluderar att se till att vi alltid är tydliga med att AI används. Dessutom, där det är möjligt, vill vi använda AI-system som är *tolkbara*.
* **Ansvar**. När AI-modeller kommer med beslut, är det inte alltid klart vem som är ansvarig för dessa beslut. Vi måste se till att vi förstår var ansvaret för AI-beslut ligger. I de flesta fall vill vi inkludera människor i beslutsprocessen för att säkerställa att faktiska personer hålls ansvariga.

## Verktyg för Ansvarsfull AI

Microsoft har utvecklat [Ansvarsfull AI-verktygslådan](https://github.com/microsoft/responsible-ai-toolbox) som innehåller en uppsättning verktyg:

* Tolkbarhetsdashboard (InterpretML)
* Rättvisedashboard (FairLearn)
* Felanalysdashboard
* Ansvarsfull AI-dashboard som inkluderar

   - EconML - verktyg för kausal analys, som fokuserar på vad-händer-om-frågor
   - DiCE - verktyg för motfaktisk analys som låter dig se vilka egenskaper som behöver ändras för att påverka modellens beslut

För mer information om AI-etik, vänligen besök [denna lektion](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) i läroplanen för maskininlärning som inkluderar uppgifter.

## Granskning & Självstudier

Ta denna [Lärväg](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) för att lära dig mer om ansvarsfull AI.

## [Efter-lärosessionens quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.