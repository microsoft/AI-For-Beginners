# Bearbetning av naturligt språk

![Sammanfattning av NLP-uppgifter i en doodle](../../../../translated_images/ai-nlp.b22dcb8ca4707ceaee8576db1c5f4089c8cac2f454e9e03ea554f07fda4556b8.sw.png)

I denna sektion kommer vi att fokusera på att använda neurala nätverk för att hantera uppgifter relaterade till **bearbetning av naturligt språk (NLP)**. Det finns många NLP-problem som vi vill att datorer ska kunna lösa:

* **Textklassificering** är ett typiskt klassificeringsproblem som rör textsekvenser. Exempel inkluderar att klassificera e-postmeddelanden som skräppost eller icke-skräppost, eller att kategorisera artiklar som sport, affärer, politik, etc. Dessutom, när vi utvecklar chattbotar, behöver vi ofta förstå vad en användare ville säga – i detta fall handlar det om **avsiktsklassificering**. Ofta behöver vi hantera många kategorier i avsiktsklassificering.
* **Sentimentanalys** är ett typiskt regressionsproblem, där vi behöver ge ett nummer (ett sentiment) som motsvarar hur positivt/negativt innebörden av en mening är. En mer avancerad version av sentimentanalys är **aspektbaserad sentimentanalys** (ABSA), där vi ger sentiment inte till hela meningen, utan till olika delar av den (aspekter), t.ex. *På denna restaurang gillade jag maten, men atmosfären var fruktansvärd*.
* **Named Entity Recognition** (NER) hänvisar till problemet med att extrahera vissa enheter från text. Till exempel kan vi behöva förstå att i frasen *Jag behöver flyga till Paris imorgon* hänvisar ordet *imorgon* till DATUM, och *Paris* är en PLATS.  
* **Nyckelordsextraktion** liknar NER, men vi behöver automatiskt extrahera ord som är viktiga för meningen i meningen, utan förutbildning för specifika enhetstyper.
* **Textklustring** kan vara användbart när vi vill gruppera liknande meningar, till exempel liknande förfrågningar i teknisk supportkonversationer.
* **Frågebesvarande** hänvisar till en models förmåga att svara på en specifik fråga. Modellen får en textpassage och en fråga som indata, och den behöver ange en plats i texten där svaret på frågan finns (eller, ibland, generera svaret).
* **Textgenerering** är en models förmåga att generera ny text. Det kan ses som en klassificeringsuppgift som förutsäger nästa bokstav/ord baserat på en viss *textprompt*. Avancerade textgenereringsmodeller, som GPT-3, kan lösa andra NLP-uppgifter som klassificering med en teknik som kallas [prompt programming](https://towardsdatascience.com/software-3-0-how-prompting-will-change-the-rules-of-the-game-a982fbfe1e0) eller [prompt engineering](https://medium.com/swlh/openai-gpt-3-and-prompt-engineering-dcdc2c5fcd29).
* **Textsammanfattning** är en teknik när vi vill att en dator ska "läsa" lång text och sammanfatta den i några meningar.
* **Maskinöversättning** kan ses som en kombination av textförståelse på ett språk och textgenerering på ett annat.

Fram till nyligen löstes de flesta NLP-uppgifter med traditionella metoder som grammatik. Till exempel, inom maskinöversättning användes parser för att omvandla den ursprungliga meningen till ett syntaxträd, sedan extraherades högre nivåer av semantiska strukturer för att representera meningen av meningen, och baserat på denna mening och grammatiken i målspråket genererades resultatet. Numera löses många NLP-uppgifter mer effektivt med hjälp av neurala nätverk.

> Många klassiska NLP-metoder är implementerade i [Natural Language Processing Toolkit (NLTK)](https://www.nltk.org) Python-biblioteket. Det finns en fantastisk [NLTK Book](https://www.nltk.org/book/) tillgänglig online som täcker hur olika NLP-uppgifter kan lösas med NLTK.

I vår kurs kommer vi mestadels att fokusera på att använda neurala nätverk för NLP, och vi kommer att använda NLTK där det behövs.

Vi har redan lärt oss om att använda neurala nätverk för att hantera tabulär data och bilder. Den största skillnaden mellan dessa typer av data och text är att text är en sekvens av variabel längd, medan indata storleken i fallet med bilder är känd i förväg. Medan konvolutionella nätverk kan extrahera mönster från indata, är mönster i text mer komplexa. T.ex. kan vi ha negation som är åtskild från subjektet och vara godtycklig för många ord (t.ex. *Jag gillar inte apelsiner*, vs. *Jag gillar inte de stora färgglada välsmakande apelsinerna*), och det bör fortfarande tolkas som ett mönster. Så för att hantera språk behöver vi introducera nya typer av neurala nätverk, såsom *återkommande nätverk* och *transformatorer*.

## Installera Bibliotek

Om du använder en lokal Python-installation för att köra denna kurs, kan du behöva installera alla nödvändiga bibliotek för NLP med följande kommandon:

**För PyTorch**
```bash
pip install -r requirements-torch.txt
```
**För TensorFlow**
```bash
pip install -r requirements-tf.txt
```

> Du kan prova NLP med TensorFlow på [Microsoft Learn](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/?WT.mc_id=academic-77998-cacaste)

## GPU Varning

I denna sektion, i några av exemplen kommer vi att träna ganska stora modeller.
* **Använd en GPU-aktiverad dator**: Det är rekommenderat att köra dina anteckningsböcker på en GPU-aktiverad dator för att minska väntetiderna när du arbetar med stora modeller.
* **GPU-minnesbegränsningar**: Att köra på en GPU kan leda till situationer där du får slut på GPU-minne, särskilt när du tränar stora modeller.
* **GPU-minnesanvändning**: Mängden GPU-minne som används under träning beror på olika faktorer, inklusive minibatch-storleken.
* **Minimera minibatch-storleken**: Om du stöter på GPU-minnesproblem, överväg att minska minibatch-storleken i din kod som en potentiell lösning.
* **TensorFlow GPU-minnesfrisläppande**: Äldre versioner av TensorFlow kanske inte släpper GPU-minne korrekt när flera modeller tränas inom en Python-kernel. För att effektivt hantera GPU-minnesanvändning kan du konfigurera TensorFlow att allokera GPU-minne endast efter behov.
* **Kodinkludering**: För att ställa in TensorFlow att växa GPU-minnesallokeringen endast när det behövs, inkludera följande kod i dina anteckningsböcker:

```python
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices)>0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True) 
```

Om du är intresserad av att lära dig om NLP från ett klassiskt ML-perspektiv, besök [denna samling av lektioner](https://github.com/microsoft/ML-For-Beginners/tree/main/6-NLP)

## I denna Sektion
I denna sektion kommer vi att lära oss om:

* [Representera text som tensorer](13-TextRep/README.md)
* [Ordembeddings](14-Emdeddings/README.md)
* [Språkmodellering](15-LanguageModeling/README.md)
* [Återkommande neurala nätverk](16-RNN/README.md)
* [Generativa nätverk](17-GenerativeNetworks/README.md)
* [Transformatorer](18-Transformers/README.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller felaktiga tolkningar som uppstår på grund av användningen av denna översättning.