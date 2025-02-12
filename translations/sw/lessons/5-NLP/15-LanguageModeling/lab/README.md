# Träning av Skip-Gram Modell

Laborationsuppgift från [AI för Nybörjare Läroplan](https://github.com/microsoft/ai-for-beginners).

## Uppgift

I den här laborationen utmanar vi dig att träna en Word2Vec-modell med hjälp av Skip-Gram-tekniken. Träna ett nätverk med inbäddningar för att förutsäga närliggande ord i ett $N$-tokens-bred Skip-Gram-fönster. Du kan använda [koden från den här lektionen](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb) och göra några små ändringar.

## Datasetet

Du är välkommen att använda vilken bok som helst. Du kan hitta många gratis texter på [Project Gutenberg](https://www.gutenberg.org/), till exempel här är en direktlänk till [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt) av Lewis Carroll. Eller så kan du använda Shakespeares pjäser, som du kan få med följande kod:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Utforska!

Om du har tid och vill fördjupa dig i ämnet, försök att utforska flera saker:

* Hur påverkar storleken på inbäddningen resultaten?
* Hur påverkar olika textstilar resultatet?
* Ta flera mycket olika typer av ord och deras synonymer, erhåll deras vektorrepresentationer, tillämpa PCA för att reducera dimensionerna till 2 och plotta dem i 2D-utrymme. Ser du några mönster?

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår från användningen av denna översättning.