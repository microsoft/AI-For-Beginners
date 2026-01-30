# Träna Skip-Gram-modell

Labuppgift från [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Uppgift

I den här labben utmanar vi dig att träna en Word2Vec-modell med Skip-Gram-teknik. Träna ett nätverk med inbäddning för att förutsäga närliggande ord i ett $N$-tokens-brett Skip-Gram-fönster. Du kan använda [koden från denna lektion](../CBoW-TF.ipynb) och göra små ändringar.

## Datasetet

Du är välkommen att använda vilken bok som helst. Du kan hitta många gratis texter på [Project Gutenberg](https://www.gutenberg.org/), till exempel finns här en direktlänk till [Alice's Adventures in Wonderland](https://www.gutenberg.org/files/11/11-0.txt)) av Lewis Carroll. Eller så kan du använda Shakespeares pjäser, som du kan hämta med följande kod:

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
* Ta flera väldigt olika typer av ord och deras synonymer, få deras vektorrepresentationer, applicera PCA för att reducera dimensionerna till 2, och plotta dem i ett 2D-utrymme. Ser du några mönster?

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör du vara medveten om att automatiska översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.