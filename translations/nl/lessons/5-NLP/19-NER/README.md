<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bd10f434e444bce61b7f97eeb1ff6a55",
  "translation_date": "2025-08-28T20:04:12+00:00",
  "source_file": "lessons/5-NLP/19-NER/README.md",
  "language_code": "nl"
}
-->
# Herkenning van benoemde entiteiten

Tot nu toe hebben we ons voornamelijk gericht op één NLP-taak: classificatie. Er zijn echter ook andere NLP-taken die met neurale netwerken kunnen worden uitgevoerd. Een van die taken is **[Herkenning van benoemde entiteiten](https://wikipedia.org/wiki/Named-entity_recognition)** (NER), waarbij specifieke entiteiten in tekst worden herkend, zoals plaatsen, persoonsnamen, datums, chemische formules, enzovoort.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/119)

## Voorbeeld van het gebruik van NER

Stel dat je een chatbot voor natuurlijke taal wilt ontwikkelen, vergelijkbaar met Amazon Alexa of Google Assistant. Intelligente chatbots werken door te *begrijpen* wat de gebruiker wil, door tekstclassificatie toe te passen op de invoerzinnen. Het resultaat van deze classificatie is de zogenaamde **intent**, die bepaalt wat de chatbot moet doen.

<img alt="Bot NER" src="images/bot-ner.png" width="50%"/>

> Afbeelding door de auteur

Een gebruiker kan echter enkele parameters als onderdeel van de zin opgeven. Bijvoorbeeld, bij het vragen naar het weer kan ze een locatie of datum specificeren. Een bot moet deze entiteiten kunnen begrijpen en de parameters dienovereenkomstig invullen voordat de actie wordt uitgevoerd. Dit is precies waar NER van pas komt.

> ✅ Een ander voorbeeld is [het analyseren van wetenschappelijke medische artikelen](https://soshnikov.com/science/analyzing-medical-papers-with-azure-and-text-analytics-for-health/). Een van de belangrijkste dingen waar we naar moeten zoeken, zijn specifieke medische termen, zoals ziektes en medische stoffen. Terwijl een klein aantal ziektes waarschijnlijk kan worden geëxtraheerd met substring-zoekopdrachten, vereisen complexere entiteiten, zoals chemische verbindingen en medicijnnamen, een meer geavanceerde aanpak.

## NER als tokenclassificatie

NER-modellen zijn in wezen **tokenclassificatiemodellen**, omdat we voor elk van de invoertokens moeten bepalen of het tot een entiteit behoort of niet, en zo ja, tot welke entiteitsklasse.

Bekijk de volgende titel van een artikel:

**Tricuspidalisklep regurgitatie** en **lithiumcarbonaat** **toxiciteit** bij een pasgeboren baby.

De entiteiten hier zijn:

* Tricuspidalisklep regurgitatie is een ziekte (`DIS`)
* Lithiumcarbonaat is een chemische stof (`CHEM`)
* Toxiciteit is ook een ziekte (`DIS`)

Let op dat één entiteit meerdere tokens kan beslaan. En, zoals in dit geval, moeten we onderscheid maken tussen twee opeenvolgende entiteiten. Daarom is het gebruikelijk om twee klassen te gebruiken voor elke entiteit: één die het eerste token van de entiteit specificeert (vaak wordt het voorvoegsel `B-` gebruikt, voor **begin**), en een andere voor de voortzetting van een entiteit (`I-`, voor **inner token**). We gebruiken ook `O` als klasse om alle **andere** tokens te vertegenwoordigen. Deze token-tagging wordt [BIO-tagging](https://en.wikipedia.org/wiki/Inside%E2%80%93outside%E2%80%93beginning_(tagging)) (of IOB) genoemd. Wanneer getagd, ziet onze titel er als volgt uit:

Token | Tag
------|-----
Tricuspidalisklep | B-DIS
regurgitatie | I-DIS
en | O
lithium | B-CHEM
carbonaat | I-CHEM
toxiciteit | B-DIS
bij | O
een | O
pasgeboren | O
baby | O
. | O

Omdat we een één-op-één-correspondentie tussen tokens en klassen moeten opbouwen, kunnen we een uiterst **veel-op-veel** neuraal netwerkmodel trainen vanuit dit beeld:

![Afbeelding die veelvoorkomende patronen van recurrente neurale netwerken toont.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.nl.jpg)

> *Afbeelding uit [deze blogpost](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) door [Andrej Karpathy](http://karpathy.github.io/). NER-tokenclassificatiemodellen komen overeen met de uiterst rechtse netwerkarchitectuur op deze afbeelding.*

## Trainen van NER-modellen

Omdat een NER-model in wezen een tokenclassificatiemodel is, kunnen we RNN's gebruiken waarmee we al bekend zijn voor deze taak. In dit geval zal elk blok van het recurrente netwerk het token-ID retourneren. Het volgende voorbeeldnotebook laat zien hoe je een LSTM kunt trainen voor tokenclassificatie.

## ✍️ Voorbeeldnotebooks: NER

Ga verder met leren in het volgende notebook:

* [NER met TensorFlow](NER-TF.ipynb)

## Conclusie

Een NER-model is een **tokenclassificatiemodel**, wat betekent dat het kan worden gebruikt om tokenclassificatie uit te voeren. Dit is een zeer veelvoorkomende taak in NLP, die helpt bij het herkennen van specifieke entiteiten in tekst, waaronder plaatsen, namen, datums en meer.

## 🚀 Uitdaging

Voltooi de opdracht via de onderstaande link om een model voor herkenning van medische entiteiten te trainen en probeer het vervolgens op een andere dataset.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/219)

## Review & Zelfstudie

Lees de blog [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) en volg de sectie Verdere Lezing in dat artikel om je kennis te verdiepen.

## [Opdracht](lab/README.md)

In de opdracht voor deze les moet je een model voor herkenning van medische entiteiten trainen. Je kunt beginnen met het trainen van een LSTM-model zoals beschreven in deze les, en doorgaan met het gebruik van het BERT-transformermodel. Lees [de instructies](lab/README.md) om alle details te krijgen.

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.