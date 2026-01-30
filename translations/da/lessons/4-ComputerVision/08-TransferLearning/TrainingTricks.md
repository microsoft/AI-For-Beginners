# Tricks til træning af dybe neurale netværk

Når neurale netværk bliver dybere, bliver træningsprocessen mere og mere udfordrende. Et stort problem er de såkaldte [forsvindende gradienter](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) eller [eksploderende gradienter](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Denne artikel](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) giver en god introduktion til disse problemer.

For at gøre træningen af dybe netværk mere effektiv, kan man anvende nogle teknikker.

## Holde værdier inden for et rimeligt interval

For at gøre numeriske beregninger mere stabile, skal vi sikre, at alle værdier i vores neurale netværk ligger inden for en rimelig skala, typisk [-1..1] eller [0..1]. Det er ikke et strengt krav, men på grund af flydende punkt-beregningers natur kan værdier med forskellige størrelsesordener ikke manipuleres præcist sammen. For eksempel, hvis vi lægger 10<sup>-10</sup> og 10<sup>10</sup> sammen, vil vi sandsynligvis få 10<sup>10</sup>, fordi den mindre værdi "konverteres" til samme størrelsesorden som den større, og mantissen går tabt.

De fleste aktiveringsfunktioner har ikke-lineariteter omkring [-1..1], og derfor giver det mening at skalere alle inputdata til intervallet [-1..1] eller [0..1].

## Initialisering af vægte

Ideelt set ønsker vi, at værdierne forbliver inden for samme interval, når de passerer gennem netværkslagene. Derfor er det vigtigt at initialisere vægtene på en måde, der bevarer værdiernes fordeling.

Normalfordelingen **N(0,1)** er ikke en god idé, fordi hvis vi har *n* input, vil standardafvigelsen af output være *n*, og værdierne vil sandsynligvis springe ud af intervallet [0..1].

Følgende initialiseringer bruges ofte:

- Uniform fordeling -- `uniform`
- **N(0,1/n)** -- `gaussian`
- **N(0,1/√n_in)** garanterer, at for input med middelværdi nul og standardafvigelse 1 vil samme middelværdi/standardafvigelse forblive
- **N(0,√2/(n_in+n_out))** -- den såkaldte **Xavier-initialisering** (`glorot`), som hjælper med at holde signalerne inden for intervallet under både fremad- og bagudpropagering

## Batch-normalisering

Selv med korrekt vægtinitialisering kan vægtene blive vilkårligt store eller små under træningen, hvilket kan føre til, at signalerne kommer uden for det korrekte interval. Vi kan bringe signalerne tilbage ved at bruge en af **normaliseringsteknikkerne**. Selvom der findes flere (vægt-normalisering, lag-normalisering), er den mest anvendte Batch-normalisering.

Ideen bag **batch-normalisering** er at tage højde for alle værdier i minibatchen og udføre normalisering (dvs. trække middelværdien fra og dividere med standardafvigelsen) baseret på disse værdier. Det implementeres som et netværkslag, der udfører denne normalisering efter vægtene er anvendt, men før aktiveringsfunktionen. Resultatet er ofte højere endelig nøjagtighed og hurtigere træning.

Her er den [originale artikel](https://arxiv.org/pdf/1502.03167.pdf) om batch-normalisering, en [forklaring på Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), og en [god introducerende blogpost](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (og en [på russisk](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** er en interessant teknik, der fjerner en vis procentdel af tilfældige neuroner under træningen. Det implementeres også som et lag med én parameter (procentdelen af neuroner, der skal fjernes, typisk 10%-50%), og under træningen nulstiller det tilfældige elementer i inputvektoren, før den sendes videre til næste lag.

Selvom dette måske lyder som en mærkelig idé, kan du se effekten af dropout på træning af en MNIST-cifferklassifikator i notebooken [`Dropout.ipynb`](Dropout.ipynb). Det fremskynder træningen og giver mulighed for at opnå højere nøjagtighed på færre træningsepochs.

Denne effekt kan forklares på flere måder:

- Det kan betragtes som en tilfældig "chokfaktor" for modellen, som hjælper med at undgå lokale minima
- Det kan ses som en *implicit gennemsnitlig model*, fordi vi under dropout træner en lidt anderledes model

> *Nogle siger, at når en beruset person forsøger at lære noget, vil han huske det bedre næste morgen sammenlignet med en ædru person, fordi en hjerne med nogle dysfunktionelle neuroner forsøger bedre at tilpasse sig for at forstå meningen. Vi har aldrig selv testet, om dette er sandt eller ej.*

## Forebyggelse af overtilpasning

En meget vigtig del af dyb læring er at kunne forhindre [overtilpasning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Selvom det kan være fristende at bruge en meget kraftfuld neuralt netværksmodel, bør vi altid balancere antallet af modelparametre med antallet af træningsprøver.

> Sørg for, at du forstår konceptet [overtilpasning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md), som vi tidligere har introduceret!

Der er flere måder at forhindre overtilpasning på:

- Tidlig stop -- overvåg løbende fejl på valideringssættet og stop træningen, når valideringsfejlen begynder at stige.
- Eksplicit vægtforfald / Regularisering -- tilføjelse af en ekstra straf til tabfunktionen for høje absolutte værdier af vægte, hvilket forhindrer modellen i at give meget ustabile resultater
- Modelgennemsnit -- træning af flere modeller og derefter gennemsnit af resultaterne. Dette hjælper med at minimere variansen.
- Dropout (Implicit Modelgennemsnit)

## Optimeringsalgoritmer / Træningsalgoritmer

En anden vigtig del af træningen er at vælge en god træningsalgoritme. Selvom klassisk **gradient descent** er et rimeligt valg, kan det nogle gange være for langsomt eller føre til andre problemer.

I dyb læring bruger vi **Stokastisk Gradient Descent** (SGD), som er gradient descent anvendt på minibatches, der er tilfældigt udvalgt fra træningssættet. Vægtene justeres ved hjælp af denne formel:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

I **momentum SGD** gemmer vi en del af gradienten fra tidligere trin. Det svarer til, når vi bevæger os et sted med inerti, og vi modtager et skub i en anden retning; vores bane ændrer sig ikke straks, men bevarer en del af den oprindelige bevægelse. Her introducerer vi en anden vektor v til at repræsentere *hastigheden*:

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

Her angiver parameteren γ, i hvilken grad vi tager inerti i betragtning: γ=0 svarer til klassisk SGD; γ=1 er en ren bevægelsesligning.

### Adam, Adagrad osv.

Da vi i hvert lag multiplicerer signaler med en matrix W<sub>i</sub>, afhængigt af ||W<sub>i</sub>||, kan gradienten enten blive meget lille og nærme sig 0 eller stige uendeligt. Dette er essensen af problemet med eksploderende/forsvindende gradienter.

En løsning på dette problem er kun at bruge gradientens retning i ligningen og ignorere den absolutte værdi, dvs.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), hvor ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Denne algoritme kaldes **Adagrad**. Andre algoritmer, der bruger samme idé: **RMSProp**, **Adam**

> **Adam** anses for at være en meget effektiv algoritme til mange anvendelser, så hvis du er i tvivl om, hvilken du skal bruge - brug Adam.

### Gradientklipning

Gradientklipning er en udvidelse af ideen ovenfor. Når ||∇ℒ|| ≤ θ, bruger vi den oprindelige gradient i vægtoptimeringen, og når ||∇ℒ|| > θ - dividerer vi gradienten med dens norm. Her er θ en parameter; i de fleste tilfælde kan vi tage θ=1 eller θ=10.

### Læringsratenedsættelse

Træningssucces afhænger ofte af læringsrateparameteren η. Det er logisk at antage, at større værdier af η resulterer i hurtigere træning, hvilket er noget, vi typisk ønsker i begyndelsen af træningen, og derefter tillader mindre værdier af η os at finjustere netværket. Derfor ønsker vi i de fleste tilfælde at reducere η under træningsprocessen.

Dette kan gøres ved at multiplicere η med et tal (f.eks. 0,98) efter hver træningsepoch eller ved at bruge en mere kompliceret **læringsrateplan**.

## Forskellige netværksarkitekturer

At vælge den rigtige netværksarkitektur til dit problem kan være vanskeligt. Normalt vil vi vælge en arkitektur, der har vist sig at fungere for vores specifikke opgave (eller en lignende). Her er en [god oversigt](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) over neurale netværksarkitekturer til computer vision.

> Det er vigtigt at vælge en arkitektur, der er kraftfuld nok til antallet af træningsprøver, vi har. At vælge en for kraftfuld model kan føre til [overtilpasning](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

En anden god tilgang er at bruge en arkitektur, der automatisk tilpasser sig den nødvendige kompleksitet. Til en vis grad er **ResNet**-arkitekturen og **Inception** selvjusterende. [Mere om computer vision-arkitekturer](../07-ConvNets/CNN_Architectures.md)

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.