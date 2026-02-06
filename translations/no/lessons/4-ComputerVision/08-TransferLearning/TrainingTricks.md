# Triks for Trening av Dype Nevrale Nettverk

Etter hvert som nevrale nettverk blir dypere, blir treningsprosessen stadig mer utfordrende. Et stort problem er de såkalte [forsvinnende gradientene](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) eller [eksploderende gradientene](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Denne artikkelen](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) gir en god introduksjon til disse problemene.

For å gjøre treningen av dype nettverk mer effektiv, finnes det noen teknikker som kan brukes.

## Holde verdier innenfor et rimelig intervall

For å gjøre numeriske beregninger mer stabile, ønsker vi å sikre at alle verdier i det nevrale nettverket er innenfor en rimelig skala, typisk [-1..1] eller [0..1]. Dette er ikke et veldig strengt krav, men naturen til flyttallsberegninger er slik at verdier med forskjellige størrelsesordener ikke kan manipuleres nøyaktig sammen. For eksempel, hvis vi legger sammen 10<sup>-10</sup> og 10<sup>10</sup>, vil vi sannsynligvis få 10<sup>10</sup>, fordi den mindre verdien blir "konvertert" til samme størrelsesorden som den større, og dermed vil mantissa gå tapt.

De fleste aktiveringsfunksjoner har ikke-lineariteter rundt [-1..1], og derfor gir det mening å skalere alle inngangsdata til [-1..1] eller [0..1]-intervallet.

## Initialisering av vekter

Ideelt sett ønsker vi at verdiene skal være i samme område etter å ha passert gjennom nettverkslagene. Derfor er det viktig å initialisere vektene på en måte som bevarer fordelingen av verdier.

Normalfordeling **N(0,1)** er ikke en god idé, fordi hvis vi har *n* innganger, vil standardavviket til utgangen være *n*, og verdiene vil sannsynligvis hoppe ut av [0..1]-intervallet.

Følgende initialiseringer brukes ofte:

 * Uniform fordeling -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garanterer at for innganger med null gjennomsnitt og standardavvik på 1, vil det samme gjennomsnittet/standardavviket forbli
 * **N(0,√2/(n_in+n_out))** -- den såkalte **Xavier-initialiseringen** (`glorot`), som hjelper med å holde signalene innenfor området under både fremover- og bakoverpropagering

## Batch-normalisering

Selv med riktig initialisering av vekter, kan vektene bli vilkårlig store eller små under treningen, og de vil føre signalene ut av riktig område. Vi kan bringe signalene tilbake ved å bruke en av **normaliseringsteknikkene**. Selv om det finnes flere av dem (vektnormalisering, lag-normalisering), er den mest brukte Batch-normalisering.

Ideen med **batch-normalisering** er å ta hensyn til alle verdier i minibatchen og utføre normalisering (dvs. trekke fra gjennomsnittet og dele på standardavviket) basert på disse verdiene. Det implementeres som et nettverkslag som utfører denne normaliseringen etter at vektene er brukt, men før aktiveringsfunksjonen. Resultatet er ofte høyere slutt-nøyaktighet og raskere trening.

Her er [den originale artikkelen](https://arxiv.org/pdf/1502.03167.pdf) om batch-normalisering, [forklaringen på Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), og [en god introduksjonsartikkel](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (og en [på russisk](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** er en interessant teknikk som fjerner en viss prosentandel av tilfeldige nevroner under trening. Det implementeres også som et lag med én parameter (prosentandelen av nevroner som skal fjernes, vanligvis 10%-50%), og under trening nullstiller det tilfeldige elementer i inngangsvektoren før den sendes til neste lag.

Selv om dette kan høres ut som en merkelig idé, kan du se effekten av dropout på trening av MNIST-sifferklassifikatoren i notatboken [`Dropout.ipynb`](Dropout.ipynb). Det akselererer treningen og lar oss oppnå høyere nøyaktighet på færre trenings-epoker.

Denne effekten kan forklares på flere måter:

 * Det kan betraktes som en tilfeldig sjokkfaktor for modellen, som tar optimaliseringen ut av lokale minima
 * Det kan betraktes som *implisitt modellgjennomsnitt*, fordi vi kan si at under dropout trener vi en litt annerledes modell

> *Noen sier at når en beruset person prøver å lære noe, vil han huske det bedre neste morgen sammenlignet med en edru person, fordi en hjerne med noen dysfunksjonelle nevroner prøver å tilpasse seg bedre for å forstå meningen. Vi har aldri testet dette selv om det er sant eller ikke.*

## Forebygge overtilpasning

En av de viktigste aspektene ved dyp læring er å kunne forhindre [overtilpasning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Selv om det kan være fristende å bruke en veldig kraftig nevralt nettverksmodell, bør vi alltid balansere antall modellparametere med antall treningsprøver.

> Sørg for at du forstår konseptet med [overtilpasning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) som vi har introdusert tidligere!

Det finnes flere måter å forhindre overtilpasning på:

 * Tidlig stopp -- kontinuerlig overvåke feilen på valideringssettet og stoppe treningen når valideringsfeilen begynner å øke.
 * Eksplisitt vektforfall / Regularisering -- legge til en ekstra straff i tapsfunksjonen for høye absolutte verdier av vekter, som forhindrer modellen fra å gi svært ustabile resultater
 * Modellgjennomsnitt -- trene flere modeller og deretter gjennomsnittlig resultatet. Dette hjelper med å minimere variansen.
 * Dropout (implisitt modellgjennomsnitt)

## Optimaliseringsmetoder / Treningsalgoritmer

Et annet viktig aspekt ved trening er å velge en god treningsalgoritme. Selv om klassisk **gradient descent** er et rimelig valg, kan det noen ganger være for tregt eller føre til andre problemer.

I dyp læring bruker vi **Stokastisk Gradient Descent** (SGD), som er gradient descent anvendt på minibatcher, tilfeldig valgt fra treningssettet. Vektene justeres ved hjelp av denne formelen:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

I **momentum SGD** beholder vi en del av gradienten fra tidligere steg. Det ligner på når vi beveger oss et sted med treghet, og vi får et dytt i en annen retning; vår bane endres ikke umiddelbart, men beholder en del av den opprinnelige bevegelsen. Her introduserer vi en annen vektor v for å representere *hastigheten*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Her indikerer parameteren γ i hvilken grad vi tar hensyn til treghet: γ=0 tilsvarer klassisk SGD; γ=1 er en ren bevegelsesligning.

### Adam, Adagrad, etc.

Siden vi i hvert lag multipliserer signaler med en matrise W<sub>i</sub>, avhengig av ||W<sub>i</sub>||, kan gradienten enten bli svært liten og nærme seg 0, eller stige uendelig. Dette er essensen av problemet med eksploderende/forsvinnende gradienter.

En løsning på dette problemet er å bruke kun retningen til gradienten i ligningen og ignorere den absolutte verdien, dvs.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), hvor ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Denne algoritmen kalles **Adagrad**. Andre algoritmer som bruker samme idé: **RMSProp**, **Adam**

> **Adam** regnes som en svært effektiv algoritme for mange applikasjoner, så hvis du er usikker på hvilken du skal bruke - bruk Adam.

### Gradientklipping

Gradientklipping er en utvidelse av ideen ovenfor. Når ||∇ℒ|| ≤ θ, vurderer vi den opprinnelige gradienten i vektoptimaliseringen, og når ||∇ℒ|| > θ - deler vi gradienten med dens norm. Her er θ en parameter; i de fleste tilfeller kan vi ta θ=1 eller θ=10.

### Læringsrate-forfall

Treningsresultatet avhenger ofte av læringsrateparameteren η. Det er logisk å anta at større verdier av η resulterer i raskere trening, noe som er noe vi vanligvis ønsker i begynnelsen av treningen, og deretter tillater mindre verdier av η oss å finjustere nettverket. Derfor ønsker vi i de fleste tilfeller å redusere η i løpet av treningen.

Dette kan gjøres ved å multiplisere η med et tall (f.eks. 0,98) etter hver epoke av treningen, eller ved å bruke en mer komplisert **læringsrate-plan**.

## Ulike nettverksarkitekturer

Å velge riktig nettverksarkitektur for problemet ditt kan være vanskelig. Normalt vil vi velge en arkitektur som har vist seg å fungere for vår spesifikke oppgave (eller en lignende). Her er en [god oversikt](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) over nevrale nettverksarkitekturer for datamaskinsyn.

> Det er viktig å velge en arkitektur som er kraftig nok for antall treningsprøver vi har. Å velge en for kraftig modell kan føre til [overtilpasning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

En annen god tilnærming er å bruke en arkitektur som automatisk tilpasser seg den nødvendige kompleksiteten. Til en viss grad er **ResNet**-arkitekturen og **Inception** selvjusterende. [Mer om arkitekturer for datamaskinsyn](../07-ConvNets/CNN_Architectures.md).

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.