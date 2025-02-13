# Mekanismer för uppmärksamhet och Transformatorer

## [För-lärare quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/118)

Ett av de mest betydelsefulla problemen inom NLP-området är **maskinöversättning**, en grundläggande uppgift som ligger till grund för verktyg som Google Translate. I denna sektion kommer vi att fokusera på maskinöversättning, eller mer generellt, på vilken *sekvens-till-sekvens* uppgift som helst (vilket också kallas **meningstransduktion**).

Med RNN:er implementeras sekvens-till-sekvens av två återkommande nätverk, där ett nätverk, **kodaren**, komprimerar en ingångssekvens till ett dolt tillstånd, medan ett annat nätverk, **avkodaren**, utvecklar detta dolda tillstånd till ett översatt resultat. Det finns ett par problem med denna metod:

* Det slutliga tillståndet för kodarnätverket har svårt att komma ihåg början av en mening, vilket leder till dålig kvalitet på modellen för långa meningar.
* Alla ord i en sekvens har samma inverkan på resultatet. I verkligheten har dock specifika ord i ingångssekvensen ofta mer inverkan på sekventiella utdata än andra.

**Uppmärksamhetsmekanismer** ger ett sätt att vikta den kontextuella påverkan av varje ingångsvektor på varje utdataförutsägelse av RNN. Sättet det implementeras på är genom att skapa genvägar mellan mellanliggande tillstånd av ingångs-RNN och utgångs-RNN. På detta sätt, när vi genererar utdata symbol y<sub>t</sub>, kommer vi att ta hänsyn till alla ingångs dolda tillstånd h<sub>i</sub>, med olika viktkoefficienter α<sub>t,i</sub>.

![Bild som visar en kodare/avkodare-modell med ett additivt uppmärksamhetslager](../../../../../translated_images/encoder-decoder-attention.7a726296894fb567aa2898c94b17b3289087f6705c11907df8301df9e5eeb3de.sw.png)

> Kodare-avkodare-modell med additiv uppmärksamhetsmekanism i [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf), citerad från [denna bloggpost](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)

Uppmärksamhetsmatrisen {α<sub>i,j</sub>} skulle representera graden av att vissa ingångsord spelar en roll i generationen av ett givet ord i utgångssekvensen. Nedan är ett exempel på en sådan matris:

![Bild som visar en exempeljustering som hittats av RNNsearch-50, tagen från Bahdanau - arviz.org](../../../../../translated_images/bahdanau-fig3.09ba2d37f202a6af11de6c82d2d197830ba5f4528d9ea430eb65fd3a75065973.sw.png)

> Figur från [Bahdanau et al., 2015](https://arxiv.org/pdf/1409.0473.pdf) (Fig.3)

Uppmärksamhetsmekanismer är ansvariga för mycket av den nuvarande eller nära nuvarande toppmoderna inom NLP. Att lägga till uppmärksamhet ökar dock kraftigt antalet modellparametrar vilket ledde till skalningsproblem med RNN:er. En viktig begränsning av att skala RNN:er är att den återkommande naturen av modellerna gör det utmanande att batcha och parallellisera träning. I en RNN måste varje element i en sekvens bearbetas i sekventiell ordning, vilket innebär att det inte kan parallelliseras enkelt.

![Kodare Avkodare med Uppmärksamhet](../../../../../lessons/5-NLP/18-Transformers/images/EncDecAttention.gif)

> Figur från [Google's Blog](https://research.googleblog.com/2016/09/a-neural-network-for-machine.html)

Antagandet av uppmärksamhetsmekanismer kombinerat med denna begränsning ledde till skapandet av de nuvarande toppmoderna transformatormodellerna som vi känner och använder idag, såsom BERT till Open-GPT3.

## Transformatormodeller

En av de huvudsakliga idéerna bakom transformatorer är att undvika den sekventiella naturen av RNN:er och att skapa en modell som är parallelliserbar under träning. Detta uppnås genom att implementera två idéer:

* positionskodning
* använda självuppmärksamhetsmekanism för att fånga mönster istället för RNN:er (eller CNN:er) (det är därför artikeln som introducerar transformatorer kallas *[Attention is all you need](https://arxiv.org/abs/1706.03762)*)

### Positionskodning/Embedding

Idén med positionskodning är följande. 
1. När man använder RNN:er representeras den relativa positionen av token av antalet steg, och behöver därför inte uttryckligen representeras. 
2. Men när vi växlar till uppmärksamhet, behöver vi veta de relativa positionerna för token inom en sekvens. 
3. För att få positionskodning, kompletterar vi vår sekvens av token med en sekvens av tokenpositioner i sekvensen (dvs. en sekvens av siffror 0,1, ...).
4. Vi blandar sedan tokenpositionen med en tokeninbäddningsvektor. För att omvandla positionen (heltal) till en vektor kan vi använda olika tillvägagångssätt:

* Träningsbar inbäddning, liknande tokeninbäddning. Detta är den metod vi överväger här. Vi tillämpar inbäddningslager ovanpå både token och deras positioner, vilket resulterar i inbäddningsvektorer av samma dimensioner, som vi sedan lägger ihop.
* Fast positionskodningsfunktion, som föreslagits i den ursprungliga artikeln.

<img src="images/pos-embedding.png" width="50%"/>

> Bild av författaren

Resultatet vi får med positionsinbäddning inbäddas både den ursprungliga token och dess position inom en sekvens.

### Multi-Head Själv-Uppmärksamhet

Nästa steg är att fånga vissa mönster inom vår sekvens. För att göra detta använder transformatorer en **självuppmärksamhets**mekanism, som i grunden är uppmärksamhet tillämpad på samma sekvens som ingång och utgång. Tillämpning av självuppmärksamhet gör att vi kan ta hänsyn till **kontext** inom meningen och se vilka ord som är relaterade. Till exempel gör det att vi kan se vilka ord som hänvisas till av referenser, såsom *det*, och även ta kontexten i beaktande:

![](../../../../../translated_images/CoreferenceResolution.861924d6d384a7d68d8d0039d06a71a151f18a796b8b1330239d3590bd4947eb.sw.png)

> Bild från [Google Blog](https://research.googleblog.com/2017/08/transformer-novel-neural-network.html)

I transformatorer använder vi **Multi-Head Attention** för att ge nätverket kraften att fånga flera olika typer av beroenden, t.ex. långsiktiga vs. kortsiktiga ordförhållanden, medreferens vs. något annat, osv.

[TensorFlow Notebook](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb) innehåller mer information om implementeringen av transformatorlager.

### Kodare-Avkodare Uppmärksamhet

I transformatorer används uppmärksamhet på två ställen:

* För att fånga mönster inom ingångstexten med hjälp av självuppmärksamhet
* För att utföra sekvensöversättning - det är uppmärksamhetslagret mellan kodaren och avkodaren.

Kodare-avkodare uppmärksamhet är mycket lik den uppmärksamhetsmekanism som används i RNN:er, som beskrivits i början av denna sektion. Detta animerade diagram förklarar rollen av kodare-avkodare uppmärksamhet.

![Animerad GIF som visar hur utvärderingarna utförs i transformatormodeller.](../../../../../lessons/5-NLP/18-Transformers/images/transformer-animated-explanation.gif)

Eftersom varje ingångsposition mappas oberoende till varje utgångsposition kan transformatorer parallellisera bättre än RNN:er, vilket möjliggör mycket större och mer uttrycksfulla språkmodeller. Varje uppmärksamhetshuvud kan användas för att lära sig olika relationer mellan ord som förbättrar efterföljande NLP-uppgifter.

## BERT

**BERT** (Bidirectional Encoder Representations from Transformers) är ett mycket stort flerlagers transformatornätverk med 12 lager för *BERT-base*, och 24 för *BERT-large*. Modellen förtränas först på en stor korpus av textdata (WikiPedia + böcker) med hjälp av osupervised träning (förutsäga maskerade ord i en mening). Under förträningen absorberar modellen betydande nivåer av språkförståelse som sedan kan utnyttjas med andra dataset genom finjustering. Denna process kallas **överföringsinlärning**.

![Bild från http://jalammar.github.io/illustrated-bert/](../../../../../translated_images/jalammarBERT-language-modeling-masked-lm.34f113ea5fec4362e39ee4381aab7cad06b5465a0b5f053a0f2aa05fbe14e746.sw.png)

> Bild [källa](http://jalammar.github.io/illustrated-bert/)

## ✍️ Övningar: Transformatorer

Fortsätt din inlärning i följande anteckningsböcker:

* [Transformatorer i PyTorch](../../../../../lessons/5-NLP/18-Transformers/TransformersPyTorch.ipynb)
* [Transformatorer i TensorFlow](../../../../../lessons/5-NLP/18-Transformers/TransformersTF.ipynb)

## Slutsats

I denna lektion lärde du dig om transformatorer och uppmärksamhetsmekanismer, alla viktiga verktyg i NLP-verktygslådan. Det finns många varianter av transformatorarkitekturer inklusive BERT, DistilBERT, BigBird, OpenGPT3 och mer som kan finjusteras. [HuggingFace-paketet](https://github.com/huggingface/) tillhandahåller ett förråd för träning av många av dessa arkitekturer med både PyTorch och TensorFlow.

## 🚀 Utmaning

## [Efter-lärare quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/218)

## Granskning & Självstudie

* [Bloggpost](https://mchromiak.github.io/articles/2017/Sep/12/Transformer-Attention-is-all-you-need/), som förklarar den klassiska [Attention is all you need](https://arxiv.org/abs/1706.03762) artikeln om transformatorer.
* [En serie bloggposter](https://towardsdatascience.com/transformers-explained-visually-part-1-overview-of-functionality-95a6dd460452) om transformatorer, som förklarar arkitekturen i detalj.

## [Uppgift](assignment.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller inkonsekvenser. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.