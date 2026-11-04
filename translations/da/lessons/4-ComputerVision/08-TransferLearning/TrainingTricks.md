# Deep Learning Træningstricks

Når neurale netværk bliver dybere, bliver processen med deres træning mere og mere udfordrende. Et stort problem er såkaldte [forsvindende gradienter](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) eller [eksploderende gradienter](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Dette indlæg](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) giver en god introduktion til disse problemer.

For at gøre træningen af dybe netværk mere effektiv, findes der nogle teknikker, der kan bruges.

## Holde værdier inden for rimeligt interval

For at gøre numeriske beregninger mere stabile, ønsker vi at sikre, at alle værdier i vores neurale netværk er inden for en rimelig skala, typisk [-1..1] eller [0..1]. Det er ikke et meget strengt krav, men karakteren af flydende kommatal-beregninger er sådan, at værdier af forskellig størrelsesorden ikke kan bearbejdes præcist sammen. For eksempel, hvis vi lægger 10<sup>-10</sup> og 10<sup>10</sup> sammen, får vi sandsynligvis 10<sup>10</sup>, fordi den mindre værdi vil blive "konverteret" til samme orden som den større, og dermed går mantissa tabt.

De fleste aktiveringsfunktioner har ikke-lineariteter omkring [-1..1], og det giver derfor mening at skalere alle inputdata til intervallet [-1..1] eller [0..1].

## Initial vægtinitialisering

Ideelt set ønsker vi, at værdierne er inden for samme område efter at være passeret gennem netværkets lag. Derfor er det vigtigt at initialisere vægte på en måde, der bevarer værdifordelingen.

Normalfordeling **N(0,1)** er ikke en god idé, fordi hvis vi har *n* inputs, vil output's standardafvigelse være *&radic;n*, og værdierne vil sandsynligvis springe uden for [0..1] intervallet.

Følgende initialiseringer bruges ofte:

 * Uniform fordeling -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** garanterer, at for input med nul middelværdi og standardafvigelse på 1, vil samme middelværdi/standardafvigelse forblive
 * **N(0,&radic;2/(n_in+n_out))** -- såkaldt **Xavier initialisering** (`glorot`), det hjælper med at holde signalerne inden for rækkevidde under både fremad- og bagudpropagering

## Batch Normalisering

Selv med korrekt vægtinitialisering kan vægte blive arbitrært store eller små under træningen, og de vil bringe signaler uden for det korrekte område. Vi kan bringe signalerne tilbage ved at bruge en af **normaliserings**-teknikkerne. Mens der findes flere (Vægtnormalisering, Lagnormalisering), er den mest anvendte Batch Normalisering.

Ideen med **batch normalisering** er at tage højde for alle værdier på tværs af minibatchen og udføre normalisering (dvs. trække middelværdien fra og dividere med standardafvigelsen) baseret på disse værdier. Det implementeres som et netværkslag, der udfører denne normalisering efter vægtene er anvendt, men før aktiveringsfunktionen. Som resultat ser vi typisk højere endelig nøjagtighed og hurtigere træning.

Her er [det oprindelige papir](https://arxiv.org/pdf/1502.03167.pdf) om batch normalisering, [forklaringen på Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), og [et godt introduktionsblogindlæg](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (og et [på russisk](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** er en interessant teknik, der fjerner en vis procentdel af tilfældige neuroner under træning. Det implementeres også som et lag med en parameter (procentdel af neuroner, der fjernes, typisk 10%-50%), og under træningen nulstiller det tilfældige elementer i inputvektoren, før det sendes videre til næste lag.

Selvom det kan lyde som en mærkelig idé, kan du se effekten af dropout på træningen af en MNIST-cifermarker i [`Dropout.ipynb`](Dropout.ipynb) notebook. Det accelererer træningen og tillader os at opnå højere nøjagtighed på færre træningsepoker.

Denne effekt kan forklares på flere måder:

 * Det kan betragtes som en tilfældig chokfaktor for modellen, der fjerner optimering fra lokale minima
 * Det kan betragtes som *implicit modelgennemsnit*, fordi vi kan sige, at under dropout træner vi en lidt anderledes model

> *Nogle siger, at når en beruset person prøver at lære noget, vil han huske det bedre næste morgen sammenlignet med en ædru person, fordi en hjerne med nogle fejl i neuronerne prøver at tilpasse sig bedre for at begribe meningen. Vi har aldrig testet os selv for om det er sandt eller ej*

## Forebygge overfitting

En af de meget vigtige aspekter ved deep learning er at kunne forhindre [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Selvom det kan være fristende at bruge en meget kraftfuld neural netværksmodel, bør vi altid afbalancere antallet af modelparametre med antallet af træningseksempler.

> Sørg for at du forstår konceptet med [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md), som vi tidligere har introduceret!

Der findes flere måder at forhindre overfitting på:

 * Early stopping -- kontinuerligt overvåge fejl på valideringssættet og stoppe træningen, når valideringsfejlen begynder at stige.
 * Eksplicit vægtreduktion / regularisering -- tilføje en ekstra straf til tabfunktionen for høje absolutte vægtværdier, hvilket forhindrer modellen i at få meget ustabile resultater
 * Modelgennemsnit -- træne flere modeller og derefter gennemsnitliggøre resultatet. Dette hjælper med at minimere variansen.
 * Dropout (Implicit modelgennemsnit)

## Optimeringsalgoritmer / Træningsalgoritmer

En anden vigtig aspekt af træningen er at vælge en god træningsalgoritme. Mens klassisk **gradient descent** er et rimeligt valg, kan det nogle gange være for langsomt eller forårsage andre problemer.

I deep learning bruger vi **Stokastisk Gradient Descent** (SGD), som er gradient descent anvendt på minibatches, tilfældigt udvalgt fra træningssættet. Vægtene justeres ved hjælp af denne formel:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

I **momentum SGD** holder vi en del af gradienten fra tidligere trin. Det er som når vi bevæger os et sted hen med inerti, og vi får et slag i en anden retning, vores bane ændres ikke med det samme, men beholder en del af den oprindelige bevægelse. Her introducerer vi en anden vektor v for at repræsentere *hastigheden*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Her angiver parameteren &gamma; i hvor høj grad vi tager inerti i betragtning: &gamma;=0 svarer til klassisk SGD; &gamma;=1 er en ren bevægelsesligning.

### Adam, Adagrad, osv.

Da vi i hvert lag multiplicerer signaler med en matrix W<sub>i</sub>, afhængigt af ||W<sub>i</sub>||, kan gradienten enten formindskes og nærme sig 0, eller stige uendeligt. Det er essensen af problemet med Eksploderende/Forsvindende gradienter.

En af løsningerne på dette problem er kun at bruge retningen af gradienten i ligningen og ignorere den absolutte værdi, dvs.

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), hvor ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Denne algoritme kaldes **Adagrad**. Andre algoritmer, som bruger samme idé, er: **RMSProp**, **Adam**

> **Adam** anses for at være en meget effektiv algoritme til mange anvendelser, så hvis du er usikker på, hvilken du skal bruge - brug Adam.

### Gradientklipning

Gradientklipning er en udvidelse af idéen ovenfor. Når ||&nabla;&lagran;|| &le; &theta;, bruges den oprindelige gradient i vægtoptimeringen, og når ||&nabla;&lagran;|| > &theta; - deler vi gradienten med dens norm. Her er &theta; en parameter, i de fleste tilfælde kan vi sætte &theta;=1 eller &theta;=10.

### Læringsrate aftagning

Træningssucces afhænger ofte af læringsrateparameteren &eta;. Det er logisk at antage, at større værdier af &eta; resulterer i hurtigere træning, hvilket typisk ønskes i starten af træningen, og derefter tillader en mindre værdi af &eta; os at finindstille netværket. Derfor ønsker vi i de fleste tilfælde at mindske &eta; i løbet af træningen.

Dette kan gøres ved at multiplicere &eta; med et tal (f.eks. 0,98) efter hver træningsepoke, eller ved at bruge en mere kompliceret **læringsrateplan**.

## Forskellige netværksarkitekturer

At vælge den rette netværksarkitektur til dit problem kan være tricky. Normalt vil vi vælge en arkitektur, som har vist sig at virke til vores specifikke opgave (eller en lignende). Her er et [godt overblik](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) over neurale netværksarkitekturer til computer vision.

> Det er vigtigt at vælge en arkitektur, der er kraftfuld nok i forhold til antallet af træningseksempler vi har. At vælge en for kraftfuld model kan resultere i [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

En anden god måde er at bruge en arkitektur, der automatisk tilpasser sig den nødvendige kompleksitet. Til en vis grad er **ResNet**-arkitekturen og **Inception** selvjusterende. [Mere om arkitekturer til computer vision](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->