# Etisk och Ansvarsfull AI

Du har nästan avslutat den här kursen, och jag hoppas att du nu tydligt ser att AI bygger på ett antal formella matematiska metoder som gör det möjligt för oss att hitta samband i data och träna modeller för att efterlikna vissa aspekter av mänskligt beteende. Vid denna tidpunkt i historien betraktar vi AI som ett mycket kraftfullt verktyg för att extrahera mönster från data och tillämpa dessa mönster för att lösa nya problem.

## [Pre-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

I science fiction ser vi dock ofta berättelser där AI utgör en fara för mänskligheten. Vanligtvis kretsar dessa berättelser kring någon form av AI-uppror, där AI beslutar sig för att konfrontera människor. Detta antyder att AI har någon form av känslor eller kan fatta beslut som dess utvecklare inte förutsett.

Den typ av AI som vi har lärt oss om i den här kursen är inget annat än stor matrisaritmetik. Det är ett mycket kraftfullt verktyg för att hjälpa oss att lösa våra problem, och precis som alla andra kraftfulla verktyg - kan det användas för goda och dåliga ändamål. Viktigt är att det kan *missbrukas*.

## Principer för Ansvarsfull AI

För att undvika detta oavsiktliga eller avsiktliga missbruk av AI, anger Microsoft de viktiga [Principerna för Ansvarsfull AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Följande koncept ligger till grund för dessa principer:

* **Rättvisa** är kopplat till det viktiga problemet med *modellbias*, som kan orsakas av att använda partisk data för träning. Till exempel, när vi försöker förutsäga sannolikheten för att en person ska få ett jobb som mjukvaruutvecklare, är modellen sannolikt att ge högre preferens till män - bara för att träningsdatan sannolikt var partisk mot en manlig målgrupp. Vi måste noggrant balansera träningsdatan och undersöka modellen för att undvika bias och se till att modellen tar hänsyn till mer relevanta egenskaper.
* **Tillförlitlighet och Säkerhet**. AI-modeller kan av sin natur göra misstag. Ett neuralt nätverk returnerar sannolikheter, och vi måste ta hänsyn till det när vi fattar beslut. Varje modell har viss precision och recall, och vi måste förstå detta för att förhindra skada som felaktiga råd kan orsaka.
* **Integritet och Säkerhet** har vissa AI-specifika implikationer. Till exempel, när vi använder viss data för att träna en modell, blir denna data på något sätt "integrerad" i modellen. Å ena sidan ökar det säkerheten och integriteten, å andra sidan måste vi komma ihåg vilken data modellen tränades på.
* **Inkludering** innebär att vi inte bygger AI för att ersätta människor, utan snarare för att förstärka människor och göra vårt arbete mer kreativt. Det är också kopplat till rättvisa, eftersom när vi arbetar med underrepresenterade grupper är de flesta dataset vi samlar in sannolikt partiska, och vi måste se till att dessa grupper inkluderas och hanteras korrekt av AI.
* **Transparens**. Detta inkluderar att säkerställa att vi alltid är tydliga med att AI används. Dessutom, där det är möjligt, vill vi använda AI-system som är *tolkbara*.
* **Ansvarsskyldighet**. När AI-modeller kommer fram till vissa beslut är det inte alltid klart vem som är ansvarig för dessa beslut. Vi måste se till att vi förstår var ansvaret för AI-beslut ligger. I de flesta fall vill vi inkludera människor i processen att fatta viktiga beslut, så att faktiska personer hålls ansvariga.

## Verktyg för Ansvarsfull AI

Microsoft har utvecklat [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) som innehåller en uppsättning verktyg:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard som inkluderar:

   - EconML - verktyg för kausal analys, som fokuserar på "vad händer om"-frågor
   - DiCE - verktyg för kontrafaktisk analys som låter dig se vilka egenskaper som behöver ändras för att påverka modellens beslut

För mer information om AI-etik, besök [denna lektion](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) i Machine Learning Curriculum som inkluderar uppgifter.

## Granskning & Självstudier

Ta denna [Learn Path](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) för att lära dig mer om ansvarsfull AI.

## [Post-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på sitt originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.