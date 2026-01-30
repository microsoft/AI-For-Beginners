# Ethische en Verantwoorde AI

Je bent bijna klaar met deze cursus, en ik hoop dat je inmiddels duidelijk ziet dat AI gebaseerd is op een aantal formele wiskundige methoden die ons in staat stellen om relaties in data te vinden en modellen te trainen om bepaalde aspecten van menselijk gedrag na te bootsen. Op dit moment in de geschiedenis beschouwen we AI als een zeer krachtig hulpmiddel om patronen uit data te halen en deze patronen toe te passen om nieuwe problemen op te lossen.

## [Pre-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/5/)

In sciencefiction zien we echter vaak verhalen waarin AI een gevaar vormt voor de mensheid. Meestal draaien deze verhalen om een soort AI-opstand, waarbij AI besluit de confrontatie met mensen aan te gaan. Dit impliceert dat AI emoties heeft of beslissingen kan nemen die niet door de ontwikkelaars zijn voorzien.

De soort AI die we in deze cursus hebben behandeld, is niets meer dan grote matrixberekeningen. Het is een zeer krachtig hulpmiddel om ons te helpen onze problemen op te lossen, en zoals elk ander krachtig hulpmiddel - kan het zowel voor goede als slechte doeleinden worden gebruikt. Belangrijk is dat het *misbruikt* kan worden.

## Principes van Verantwoorde AI

Om dit onbedoelde of opzettelijke misbruik van AI te voorkomen, stelt Microsoft de belangrijke [Principes van Verantwoorde AI](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-77998-cacaste) vast. De volgende concepten liggen ten grondslag aan deze principes:

* **Eerlijkheid** heeft betrekking op het belangrijke probleem van *modelbiases*, die kunnen worden veroorzaakt door het gebruik van bevooroordeelde data voor training. Bijvoorbeeld, wanneer we proberen de kans te voorspellen dat iemand een baan als softwareontwikkelaar krijgt, zal het model waarschijnlijk een hogere voorkeur geven aan mannen - simpelweg omdat de trainingsdataset waarschijnlijk bevooroordeeld was richting een mannelijk publiek. We moeten trainingsdata zorgvuldig balanceren en het model onderzoeken om biases te vermijden en ervoor te zorgen dat het model meer relevante kenmerken in overweging neemt.
* **Betrouwbaarheid en Veiligheid**. Van nature kunnen AI-modellen fouten maken. Een neuraal netwerk geeft waarschijnlijkheden terug, en we moeten hiermee rekening houden bij het nemen van beslissingen. Elk model heeft een bepaalde precisie en recall, en we moeten dit begrijpen om schade te voorkomen die door verkeerde adviezen kan worden veroorzaakt.
* **Privacy en Beveiliging** hebben enkele AI-specifieke implicaties. Bijvoorbeeld, wanneer we data gebruiken om een model te trainen, wordt deze data op een bepaalde manier "geïntegreerd" in het model. Enerzijds verhoogt dit de beveiliging en privacy, anderzijds moeten we onthouden welke data is gebruikt voor de training van het model.
* **Inclusiviteit** betekent dat we AI niet bouwen om mensen te vervangen, maar om mensen te ondersteunen en ons werk creatiever te maken. Het is ook gerelateerd aan eerlijkheid, omdat de datasets die we verzamelen bij ondervertegenwoordigde gemeenschappen waarschijnlijk bevooroordeeld zijn, en we moeten ervoor zorgen dat deze gemeenschappen worden opgenomen en correct worden behandeld door AI.
* **Transparantie**. Dit houdt in dat we altijd duidelijk maken dat AI wordt gebruikt. Ook willen we, waar mogelijk, AI-systemen gebruiken die *interpreteerbaar* zijn.
* **Verantwoordelijkheid**. Wanneer AI-modellen beslissingen nemen, is het niet altijd duidelijk wie verantwoordelijk is voor die beslissingen. We moeten ervoor zorgen dat we begrijpen waar de verantwoordelijkheid voor AI-beslissingen ligt. In de meeste gevallen willen we mensen betrekken bij het nemen van belangrijke beslissingen, zodat echte mensen verantwoordelijk worden gehouden.

## Tools voor Verantwoorde AI

Microsoft heeft de [Responsible AI Toolbox](https://github.com/microsoft/responsible-ai-toolbox) ontwikkeld, die een reeks tools bevat:

* Interpretability Dashboard (InterpretML)
* Fairness Dashboard (FairLearn)
* Error Analysis Dashboard
* Responsible AI Dashboard dat omvat:

   - EconML - tool voor Causal Analysis, gericht op "wat-als"-vragen
   - DiCE - tool voor Counterfactual Analysis waarmee je kunt zien welke kenmerken moeten worden gewijzigd om de beslissing van het model te beïnvloeden

Voor meer informatie over AI-ethiek, bezoek [deze les](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/3-fairness?WT.mc_id=academic-77998-cacaste) in het Machine Learning Curriculum, inclusief opdrachten.

## Herziening & Zelfstudie

Volg dit [Learn Path](https://docs.microsoft.com/learn/modules/responsible-ai-principles/?WT.mc_id=academic-77998-cacaste) om meer te leren over verantwoorde AI.

## [Post-lecture quiz](https://white-water-09ec41f0f.azurestaticapps.net/quiz/6/)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.