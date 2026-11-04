# Deep Learning Treningsknep

Når nevrale nettverk blir dypere, blir prosessen med å trene dem mer og mer utfordrende. Et stort problem er såkalte [forsvinnende gradienter](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) eller [eksploderende gradienter](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Dette innlegget](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) gir en god introduksjon til disse problemene.

For å gjøre treningen av dype nettverk mer effektiv, finnes det noen teknikker man kan bruke.

## Holde verdier innenfor et rimelig intervall

For å gjøre numeriske beregninger mer stabile, ønsker vi å sikre at alle verdier i nevrale nettverket ligger innenfor en rimelig skala, vanligvis [-1..1] eller [0..1]. Det er ikke et veldig strengt krav, men flyttallsberegninger har en natur som gjør at verdier med ulik størrelsesorden ikke kan manipuleres nøyaktig sammen. For eksempel, hvis vi legger til 10<sup>-10</sup> og 10<sup>10</sup>, får vi sannsynligvis 10<sup>10</sup>, fordi den mindre verdien "konverteres" til samme orden som den større, og dermed går mantissen tapt.

De fleste aktiveringsfunksjoner har ikke-linearitet rundt [-1..1], så det gir mening å skalere all inngangsdata til [-1..1] eller [0..1].

## Initial vekt-initialisering

Ideelt sett ønsker vi at verdiene skal være i samme område etter å ha passert gjennom nettverkslagene. Derfor er det viktig å initialisere vektene på en måte som bevarer fordelingen av verdier.

Normalfordeling **N(0,1)** er ikke et godt valg, fordi hvis vi har *n* innganger, vil standardavviket til output være *&radic;n*, og verdiene vil sannsynligvis hoppe utenfor [0..1] intervallet.

Følgende initialiseringer brukes ofte:

 * Uniform fordeling -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** garanterer at for input med null gjennomsnitt og standardavvik på 1 forblir samme gjennomsnitt/standardavvik
 * **N(0,&radic;2/(n_in+n_out))** -- såkalt **Xavier-initialisering** (`glorot`), som hjelper å holde signalene innenfor rekkevidde under både fremover- og bakoverpropagasjon

## Batch Normalisering

Selv med riktig vektinitialisering kan vektene bli arbitrært store eller små under trening, og de vil dra signalene ut av riktig område. Vi kan bringe signalene tilbake ved å bruke en av **normaliseringsteknikkene**. Mens det finnes flere (Vektnormalisering, Lagnormalisering), er den mest brukte Batch Normalisering.

Ideen bak **batch normalisering** er å ta hensyn til alle verdier over minibatchen, og utføre normalisering (dvs. trekke fra gjennomsnitt og dividere på standardavvik) basert på disse verdiene. Den implementeres som et nettverkslag som gjør denne normaliseringen etter vektene er brukt, men før aktiveringsfunksjonen. Resultatet er ofte høyere endelig nøyaktighet og raskere trening.

Her er [originalartikkelen](https://arxiv.org/pdf/1502.03167.pdf) om batch normalisering, [forklaringen på Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), og [et godt introduksjonsblogginnlegg](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (og en [på russisk](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** er en interessant teknikk som fjerner en viss prosentandel tilfeldige nevroner under trening. Det er også implementert som et lag med én parameter (prosentandel nevroner som fjernes, typisk 10%-50%), og under trening settes tilfeldige elementer i inngangsvektoren til null før de sendes til neste lag.

Selv om dette kan høres ut som en merkelig idé, kan du se effekten av dropout på trening av MNIST sifferklassifiserer i [`Dropout.ipynb`](Dropout.ipynb) notebook. Det øker treningshastigheten og lar oss oppnå høyere nøyaktighet på færre trenings-epoker.

Denne effekten kan forklares på flere måter:

 * Det kan betraktes som en tilfeldig sjokkfaktor for modellen, som tar optimering ut av et lokalt minimum
 * Det kan betraktes som *implisitt modellgjennomsnittlig*, fordi man kan si at under dropout trener man en litt annen modell

> *Noen sier at når en beruset person prøver å lære noe, vil han huske det bedre neste morgen sammenlignet med en edru person, fordi hjernen med noen dysfunksjonelle nevroner prøver bedre å tilpasse seg for å forstå meningen. Vi har aldri testet om dette er sant eller ikke*

## Forebygge overtilpasning

En av de svært viktige aspektene ved dyp læring er å kunne forhindre [overtilegnelse](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Selv om det kan være fristende å bruke meget kraftige nevrale nettverksmodeller, bør vi alltid balansere antallet modellparametere med antall treningsprøver.

> Sørg for at du forstår konseptet [overtilegnelse](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) vi introduserte tidligere!

Det finnes flere måter å forhindre overtilpasning på:

 * Tidlig stopp -- kontinuerlig overvåke feil på valideringssett og stoppe trening når valideringsfeilen begynner å øke.
 * Eksplisitt vektnedregulering / regulering -- legge til en ekstra straff på tapsfunksjonen for høye absolutte verdier av vekter, som hindrer modellen i å få veldig ustabile resultater
 * Modellgjennomsnittlig -- trene flere modeller og så gjennomsnittsresultatet. Dette hjelper med å minske variasjonen.
 * Dropout (implisitt modellgjennomsnittlig)

## Optimalisatorer / Treningsalgoritmer

En annen viktig aspekt ved trening er å velge en god treningsalgoritme. Mens klassisk **grad descent** er et rimelig valg, kan det noen ganger være for tregt eller føre til andre problemer.

I dyp læring bruker vi **Stokastisk Gradient Descent** (SGD), som er gradientnedstigning anvendt på minibatcher, tilfeldig valgt fra treningssettet. Vektene justeres ved å bruke denne formelen:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

I **momentum SGD** beholder vi en del av gradienten fra forrige steg. Det er likt som når vi beveger oss med treghet og får et slag i en annen retning; banen vår endres ikke umiddelbart, men beholder noe av den opprinnelige bevegelsen. Her introduserer vi en annen vektor v som representerer *hastigheten*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Her indikerer parameteren &gamma; i hvilken grad vi tar treghet med i betraktningen: &gamma;=0 tilsvarer klassisk SGD; &gamma;=1 er ren bevegelseslikning.

### Adam, Adagrad, osv.

Siden i hvert lag multipliserer vi signaler med en matrise W<sub>i</sub>, avhengig av ||W<sub>i</sub>||, kan gradienten enten minke og nærme seg 0, eller vokse uendelig. Dette er kjernen i problemet med eksploderende/forvinnende gradienter.

En av løsningene på dette problemet er å bruke bare retningen til gradienten i formelen, og ignorere den absolutte verdien, altså

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), der ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Denne algoritmen kalles **Adagrad**. Andre algoritmer som bruker samme idé: **RMSProp**, **Adam**

> **Adam** anses som en svært effektiv algoritme for mange applikasjoner, så hvis du er usikker på hvilken du skal bruke – bruk Adam.

### Gradient-klipping

Gradient-klipping er en utvidelse av idéen ovenfor. Når ||&nabla;&lagran;|| &le; &theta;, bruker vi den originale gradienten i vektsoptimaliseringen, og når ||&nabla;&lagran;|| > &theta; – deler vi gradienten på normen. Her er &theta; en parameter, og i de fleste tilfeller kan vi velge &theta;=1 eller &theta;=10.

### Læringsratereduksjon

Treningssuksess avhenger ofte av læringsraten &eta;. Det er logisk å anta at større verdier av &eta; gir raskere trening, noe som vanligvis ønskes i starten av treningen, og deretter gir mindre verdi av &eta; oss mulighet til å finjustere nettverket. Dermed ønsker vi i de fleste tilfeller å redusere &eta; i løpet av treningen.

Dette kan gjøres ved å multiplisere &eta; med et tall (f.eks. 0,98) etter hver trenings-epoke, eller ved å bruke en mer komplisert **læringsrateplan**.

## Ulike nettverksarkitekturer

Å velge riktig nettverksarkitektur for problemet ditt kan være vanskelig. Vanligvis velger vi en arkitektur som har vist seg å fungere for vår spesifikke oppgave (eller en lignende). Her er en [god oversikt](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) over nevrale nettverksarkitekturer for datamaskinsyn.

> Det er viktig å velge en arkitektur som er kraftig nok for antall treningsprøver vi har. Å velge en for kraftig modell kan føre til [overtilegnelse](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

En annen god måte er å bruke en arkitektur som automatisk tilpasser seg den nødvendige kompleksiteten. Til en viss grad er **ResNet**-arkitekturen og **Inception** selvjusterende. [Mer om datamaskinsyn-arkitekturer](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->