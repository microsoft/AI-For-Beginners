# Etisk og Ansvarlig AI

Du er næsten færdig med dette kursus, og jeg håber, at du nu tydeligt kan se, at AI er baseret på en række formelle matematiske metoder, der gør det muligt for os at finde sammenhænge i data og træne modeller til at efterligne nogle aspekter af menneskelig adfærd. På dette tidspunkt i historien betragter vi AI som et meget kraftfuldt værktøj til at udtrække mønstre fra data og anvende disse mønstre til at løse nye problemer.

## [Quiz før forelæsning](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

Men i science fiction ser vi ofte historier, hvor AI udgør en fare for menneskeheden. Disse historier handler som regel om en form for AI-oprør, hvor AI beslutter sig for at konfrontere mennesker. Dette antyder, at AI har en form for følelser eller kan træffe beslutninger, som udviklerne ikke havde forudset.

Den type AI, vi har lært om i dette kursus, er intet andet end stor matrixaritmetik. Det er et meget kraftfuldt værktøj til at hjælpe os med at løse vores problemer, og som ethvert andet kraftfuldt værktøj - kan det bruges til både gode og dårlige formål. Vigtigt er det, at det kan *misbruges*.

## Principper for Ansvarlig AI

For at undgå denne utilsigtede eller bevidste misbrug af AI har Microsoft fastlagt de vigtige [Principper for Ansvarlig AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste). Følgende begreber understøtter disse principper:

* **Retfærdighed** er relateret til det vigtige problem med *modelbias*, som kan opstå ved brug af biased data til træning. For eksempel, når vi forsøger at forudsige sandsynligheden for, at en person får et job som softwareudvikler, vil modellen sandsynligvis give højere præference til mænd - blot fordi træningsdatasættet sandsynligvis var biased mod en mandlig målgruppe. Vi skal nøje balancere træningsdata og undersøge modellen for at undgå bias og sikre, at modellen tager højde for mere relevante egenskaber.
* **Pålidelighed og Sikkerhed**. Af natur kan AI-modeller begå fejl. Et neuralt netværk returnerer sandsynligheder, og vi skal tage det i betragtning, når vi træffer beslutninger. Hver model har en vis præcision og recall, og vi skal forstå dette for at forhindre skade, som forkerte råd kan forårsage.
* **Privatliv og Sikkerhed** har nogle AI-specifikke implikationer. For eksempel, når vi bruger nogle data til at træne en model, bliver disse data på en eller anden måde "integreret" i modellen. På den ene side øger det sikkerheden og privatlivet, men på den anden side skal vi huske, hvilke data modellen blev trænet på.
* **Inklusion** betyder, at vi ikke bygger AI for at erstatte mennesker, men snarere for at supplere mennesker og gøre vores arbejde mere kreativt. Det er også relateret til retfærdighed, fordi når vi arbejder med underrepræsenterede samfund, er de fleste af de datasæt, vi indsamler, sandsynligvis biased, og vi skal sikre, at disse samfund inkluderes og håndteres korrekt af AI.
* **Gennemsigtighed**. Dette indebærer, at vi altid skal være tydelige omkring, at AI bliver brugt. Derudover ønsker vi, hvor det er muligt, at bruge AI-systemer, der er *fortolkelige*.
* **Ansvarlighed**. Når AI-modeller træffer nogle beslutninger, er det ikke altid klart, hvem der er ansvarlig for disse beslutninger. Vi skal sikre, at vi forstår, hvor ansvaret for AI-beslutninger ligger. I de fleste tilfælde vil vi inkludere mennesker i beslutningsprocessen, så faktiske personer holdes ansvarlige.

## Værktøjer til Ansvarlig AI

Microsoft har udviklet [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox), som indeholder en række værktøjer:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard, der inkluderer

   - EconML - værktøj til Kausal Analyse, som fokuserer på "hvad-nu-hvis"-spørgsmål
   - DiCE - værktøj til Kontrafaktisk Analyse, der giver dig mulighed for at se, hvilke egenskaber der skal ændres for at påvirke modellens beslutning

For mere information om AI-etik, besøg venligst [denne lektion](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) i Machine Learning Curriculum, som inkluderer opgaver.

## Gennemgang & Selvstudie

Tag denne [Learn Path](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) for at lære mere om ansvarlig AI.

## [Quiz efter forelæsning](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på at sikre nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.