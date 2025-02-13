# Återkommande Neurala Nätverk

## [För-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/116)

I tidigare avsnitt har vi använt rika semantiska representationer av text och en enkel linjär klassificerare ovanpå inbäddningarna. Vad denna arkitektur gör är att fånga den aggregerade betydelsen av ord i en mening, men den tar inte hänsyn till **ordningen** av orden, eftersom aggregationsoperationen ovanpå inbäddningarna tog bort denna information från den ursprungliga texten. Eftersom dessa modeller inte kan modellera ordning av ord, kan de inte lösa mer komplexa eller tvetydiga uppgifter som textgenerering eller frågesvar.

För att fånga betydelsen av textsekvenser behöver vi använda en annan neurala nätverksarkitektur, som kallas **återkommande neurala nätverk**, eller RNN. I RNN passerar vi vår mening genom nätverket ett symbol i taget, och nätverket producerar ett **tillstånd**, som vi sedan skickar tillbaka till nätverket med nästa symbol.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.sw.png)

> Bild av författaren

Givet inmatningssekvensen av token X<sub>0</sub>,...,X<sub>n</sub>, skapar RNN en sekvens av neurala nätverksblock och tränar denna sekvens end-to-end med hjälp av backpropagation. Varje nätverksblock tar ett par (X<sub>i</sub>,S<sub>i</sub>) som inmatning och producerar S<sub>i+1</sub> som resultat. Det slutliga tillståndet S<sub>n</sub> eller (utgång Y<sub>n</sub>) går in i en linjär klassificerare för att producera resultatet. Alla nätverksblock delar samma vikter och tränas end-to-end med en backpropagation-pass.

Eftersom tillståndsvektorer S<sub>0</sub>,...,S<sub>n</sub> passerar genom nätverket, kan det lära sig de sekventiella beroendena mellan orden. Till exempel, när ordet *not* dyker upp någonstans i sekvensen, kan det lära sig att neka vissa element inom tillståndsvektorn, vilket resulterar i negation.

> ✅ Eftersom vikterna för alla RNN-block på bilden ovan är delade, kan samma bild representeras som ett block (till höger) med en återkommande feedback-loop, som skickar utgångstillståndet från nätverket tillbaka till inmatningen.

## Anatomiska av en RNN Cell

Låt oss se hur en enkel RNN-cell är organiserad. Den tar emot det föregående tillståndet S<sub>i-1</sub> och den aktuella symbolen X<sub>i</sub> som inmatningar, och måste producera utgångstillståndet S<sub>i</sub> (och ibland är vi också intresserade av någon annan utgång Y<sub>i</sub>, som i fallet med generativa nätverk).

En enkel RNN-cell har två viktmatriser inuti: en som transformerar en inmatningssymbol (låt oss kalla den W), och en annan som transformerar ett inmatningstillstånd (H). I det här fallet beräknas nätverkets utgång som σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b), där σ är aktiveringsfunktionen och b är ytterligare bias.

<img alt="RNN Cell Anatom" src="images/rnn-anatomy.png" width="50%"/>

> Bild av författaren

I många fall passerar inmatningstokens genom inbäddningslagret innan de går in i RNN för att sänka dimensionaliteten. I det här fallet, om dimensionen av inmatningsvektorerna är *emb_size*, och tillståndsvektorn är *hid_size* - storleken på W är *emb_size*×*hid_size*, och storleken på H är *hid_size*×*hid_size*.

## Lång Korttidsminne (LSTM)

Ett av de största problemen med klassiska RNN:er är det så kallade **försvinnande gradienter** problemet. Eftersom RNN:er tränas end-to-end i en backpropagation-pass har det svårt att sprida fel till de första lagren av nätverket, och därmed kan nätverket inte lära sig relationer mellan avlägsna token. Ett av sätten att undvika detta problem är att införa **explisit tillståndshantering** genom att använda så kallade **portar**. Det finns två välkända arkitekturer av denna typ: **Long Short Term Memory** (LSTM) och **Gated Relay Unit** (GRU).

![Bild som visar ett exempel på en lång korttidsminnescell](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Bildkälla TBD

LSTM-nätverket är organiserat på ett sätt som liknar RNN, men det finns två tillstånd som passerar från lager till lager: det aktuella tillståndet C och den dolda vektorn H. Vid varje enhet sammanfogas den dolda vektorn H<sub>i</sub> med inmatningen X<sub>i</sub>, och de kontrollerar vad som händer med tillståndet C via **portar**. Varje port är ett neuralt nätverk med sigmoidaktivering (utgång i intervallet [0,1]), vilket kan ses som en bitmask när den multipliceras med tillståndsvektorn. Det finns följande portar (från vänster till höger på bilden ovan):

* **Glömskeporten** tar en dold vektor och avgör vilka komponenter av vektorn C vi behöver glömma, och vilka som ska passera.
* **Inmatningsporten** tar viss information från inmatnings- och dolda vektorer och sätter in den i tillståndet.
* **Utgångsporten** transformerar tillståndet via ett linjärt lager med *tanh*-aktivering, och väljer sedan några av sina komponenter med hjälp av en dold vektor H<sub>i</sub> för att producera ett nytt tillstånd C<sub>i+1</sub>.

Komponenter av tillståndet C kan ses som vissa flaggor som kan slås på och av. Till exempel, när vi stöter på ett namn *Alice* i sekvensen, kan vi vilja anta att det hänvisar till en kvinnlig karaktär, och höja flaggan i tillståndet att vi har ett kvinnligt substantiv i meningen. När vi vidare stöter på fraserna *and Tom*, kommer vi att höja flaggan att vi har ett plural substantiv. Genom att manipulera tillståndet kan vi på så sätt hålla reda på de grammatiska egenskaperna hos meningsdelar.

> ✅ En utmärkt resurs för att förstå internals av LSTM är denna fantastiska artikel [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) av Christopher Olah.

## Bidirektionella och Flerlager RNN:er

Vi har diskuterat återkommande nätverk som fungerar i en riktning, från början av en sekvens till slutet. Det verkar naturligt, eftersom det liknar hur vi läser och lyssnar på tal. Men eftersom vi i många praktiska fall har slumpmässig åtkomst till inmatningssekvensen, kan det vara meningsfullt att köra återkommande beräkningar i båda riktningarna. Sådana nätverk kallas **bidirektionella** RNN:er. När vi hanterar ett bidirektionellt nätverk, behöver vi två dolda tillståndsvektorer, en för varje riktning.

Ett återkommande nätverk, antingen en-riktat eller bidirektionellt, fångar vissa mönster inom en sekvens och kan lagra dem i en tillståndsvektor eller skicka dem till utgången. Precis som med konvolutionella nätverk kan vi bygga ett annat återkommande lager ovanpå det första för att fånga högre nivåmönster och bygga från lågnivåmönster som extraherats av det första lagret. Detta leder oss till begreppet **flerlager RNN**, som består av två eller fler återkommande nätverk, där utgången från det föregående lagret skickas till nästa lager som inmatning.

![Bild som visar en flerlagers lång-korttidsminnes-RNN](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.sw.jpg)

*Bild från [detta underbara inlägg](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3) av Fernando López*

## ✍️ Övningar: Inbäddningar

Fortsätt din inlärning i följande anteckningsböcker:

* [RNNs med PyTorch](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNNs med TensorFlow](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Slutsats

I denna enhet har vi sett att RNN:er kan användas för sekvensklassificering, men i själva verket kan de hantera många fler uppgifter, såsom textgenerering, maskinöversättning och mer. Vi kommer att överväga dessa uppgifter i nästa enhet.

## 🚀 Utmaning

Läs igenom viss litteratur om LSTM och överväg deras tillämpningar:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/216)

## Granskning & Självstudie

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) av Christopher Olah.

## [Uppgift: Anteckningsböcker](assignment.md)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi tar inget ansvar för eventuella missförstånd eller feltolkningar som uppstår från användningen av denna översättning.