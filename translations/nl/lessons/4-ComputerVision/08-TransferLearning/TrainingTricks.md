# Deep Learning Training Tricks

Naarmate neurale netwerken dieper worden, wordt het proces van hun training steeds uitdagender. Een groot probleem is het zogenaamde [vanishing gradients](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) of [exploding gradients](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Deze post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) geeft een goede introductie tot deze problemen.

Om het trainen van diepe netwerken efficiënter te maken, zijn er een aantal technieken die kunnen worden toegepast.

## Waarden binnen een redelijke interval houden

Om numerieke berekeningen stabieler te maken, willen we ervoor zorgen dat alle waarden binnen ons neuraal netwerk binnen een redelijke schaal liggen, meestal [-1..1] of [0..1]. Dit is geen strikte eis, maar de aard van floating-point berekeningen is zodanig dat waarden van verschillende grootheden niet nauwkeurig samen kunnen worden gemanipuleerd. Bijvoorbeeld, als we 10<sup>-10</sup> en 10<sup>10</sup> optellen, krijgen we waarschijnlijk 10<sup>10</sup>, omdat de kleinere waarde wordt "omgezet" naar dezelfde orde als de grotere, waardoor de mantisse verloren gaat.

De meeste activatiefuncties hebben non-lineariteiten rond [-1..1], en daarom is het logisch om alle invoergegevens te schalen naar het interval [-1..1] of [0..1].

## Initiële gewichtsinitialisatie

Idealiter willen we dat de waarden binnen hetzelfde bereik blijven na het doorlopen van netwerklagen. Daarom is het belangrijk om gewichten zo te initialiseren dat de verdeling van waarden behouden blijft.

Een normale verdeling **N(0,1)** is geen goed idee, omdat als we *n* inputs hebben, de standaarddeviatie van de output *n* zou zijn, en waarden waarschijnlijk buiten het interval [0..1] zouden springen.

De volgende initialisaties worden vaak gebruikt:

 * Uniforme verdeling -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** garandeert dat voor inputs met een gemiddelde van nul en een standaarddeviatie van 1 hetzelfde gemiddelde/standaarddeviatie behouden blijft
 * **N(0,√2/(n_in+n_out))** -- de zogenaamde **Xavier-initialisatie** (`glorot`), dit helpt om de signalen binnen bereik te houden tijdens zowel forward als backward propagatie

## Batch Normalization

Zelfs met een goede gewichtsinitialisatie kunnen gewichten tijdens de training willekeurig groot of klein worden, waardoor signalen buiten het juiste bereik komen. We kunnen signalen terugbrengen door een van de **normalisatietechnieken** te gebruiken. Hoewel er verschillende technieken zijn (Weight Normalization, Layer Normalization), wordt Batch Normalization het vaakst gebruikt.

Het idee van **batch normalization** is om alle waarden binnen de minibatch in aanmerking te nemen en normalisatie uit te voeren (d.w.z. gemiddelde aftrekken en delen door standaarddeviatie) op basis van die waarden. Het wordt geïmplementeerd als een netwerklaag die deze normalisatie uitvoert na het toepassen van de gewichten, maar vóór de activatiefunctie. Hierdoor zien we waarschijnlijk een hogere uiteindelijke nauwkeurigheid en snellere training.

Hier is het [originele artikel](https://arxiv.org/pdf/1502.03167.pdf) over batch normalization, de [uitleg op Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), en [een goede introductie in een blogpost](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (en een [in het Russisch](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** is een interessante techniek die een bepaald percentage willekeurige neuronen verwijdert tijdens de training. Het wordt ook geïmplementeerd als een laag met één parameter (percentage neuronen dat moet worden verwijderd, meestal 10%-50%), en tijdens de training worden willekeurige elementen van de invoervector op nul gezet voordat ze naar de volgende laag worden doorgegeven.

Hoewel dit misschien een vreemd idee lijkt, kun je het effect van dropout zien bij het trainen van een MNIST-cijferclassifier in de [`Dropout.ipynb`](Dropout.ipynb) notebook. Het versnelt de training en stelt ons in staat om een hogere nauwkeurigheid te bereiken in minder trainingsepochen.

Dit effect kan op verschillende manieren worden verklaard:

 * Het kan worden beschouwd als een willekeurige schokfactor voor het model, die de optimalisatie uit een lokaal minimum haalt
 * Het kan worden beschouwd als *impliciete modelgemiddeling*, omdat we kunnen zeggen dat we tijdens dropout een iets ander model trainen

> *Sommige mensen zeggen dat wanneer een dronken persoon iets probeert te leren, hij dit de volgende ochtend beter zal onthouden in vergelijking met een nuchter persoon, omdat een brein met enkele slecht functionerende neuronen beter probeert te adapteren om de betekenis te begrijpen. We hebben zelf nooit getest of dit waar is.*

## Overfitting voorkomen

Een van de zeer belangrijke aspecten van deep learning is het vermogen om [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) te voorkomen. Hoewel het verleidelijk kan zijn om een zeer krachtig neuraal netwerkmodel te gebruiken, moeten we altijd het aantal modelparameters in balans brengen met het aantal trainingssamples.

> Zorg ervoor dat je het concept van [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) begrijpt dat we eerder hebben geïntroduceerd!

Er zijn verschillende manieren om overfitting te voorkomen:

 * Early stopping -- continu de fout op de validatieset monitoren en de training stoppen wanneer de validatiefout begint toe te nemen.
 * Expliciete gewichtsafname / regularisatie -- een extra straf toevoegen aan de verliesfunctie voor hoge absolute waarden van gewichten, wat voorkomt dat het model zeer onstabiele resultaten krijgt
 * Modelgemiddeling -- meerdere modellen trainen en vervolgens het resultaat middelen. Dit helpt om de variantie te minimaliseren.
 * Dropout (impliciete modelgemiddeling)

## Optimizers / Trainingsalgoritmen

Een ander belangrijk aspect van training is het kiezen van een goed trainingsalgoritme. Hoewel klassiek **gradient descent** een redelijke keuze is, kan het soms te traag zijn of andere problemen veroorzaken.

In deep learning gebruiken we **Stochastic Gradient Descent** (SGD), wat een gradient descent is toegepast op minibatches, willekeurig geselecteerd uit de trainingsset. Gewichten worden aangepast met behulp van deze formule:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Bij **momentum SGD** behouden we een deel van de gradient van eerdere stappen. Het is vergelijkbaar met wanneer we ergens heen bewegen met traagheid, en we een duw krijgen in een andere richting; onze traject verandert niet onmiddellijk, maar behoudt een deel van de oorspronkelijke beweging. Hier introduceren we een andere vector v om de *snelheid* te vertegenwoordigen:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Hier geeft parameter γ aan in hoeverre we traagheid in rekening brengen: γ=0 komt overeen met klassieke SGD; γ=1 is een pure bewegingsvergelijking.

### Adam, Adagrad, etc.

Omdat we in elke laag signalen vermenigvuldigen met een matrix W<sub>i</sub>, afhankelijk van ||W<sub>i</sub>||, kan de gradient ofwel afnemen en dicht bij 0 zijn, of onbeperkt stijgen. Dit is de kern van het Exploding/Vanishing Gradients-probleem.

Een van de oplossingen voor dit probleem is om alleen de richting van de gradient in de vergelijking te gebruiken en de absolute waarde te negeren, d.w.z.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), waarbij ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Dit algoritme wordt **Adagrad** genoemd. Andere algoritmen die hetzelfde idee gebruiken: **RMSProp**, **Adam**

> **Adam** wordt beschouwd als een zeer efficiënt algoritme voor veel toepassingen, dus als je niet zeker weet welke je moet gebruiken - gebruik Adam.

### Gradient clipping

Gradient clipping is een uitbreiding van het bovenstaande idee. Wanneer ||∇ℒ|| ≤ θ, nemen we de oorspronkelijke gradient in de gewichtsoptimalisatie, en wanneer ||∇ℒ|| > θ - delen we de gradient door zijn norm. Hier is θ een parameter; in de meeste gevallen kunnen we θ=1 of θ=10 nemen.

### Learning rate decay

Het succes van training hangt vaak af van de learning rate parameter η. Het is logisch om aan te nemen dat grotere waarden van η resulteren in snellere training, wat iets is dat we meestal willen aan het begin van de training, en dat kleinere waarden van η ons in staat stellen om het netwerk fijn af te stemmen. Daarom willen we in de meeste gevallen η verminderen tijdens het trainingsproces.

Dit kan worden gedaan door η te vermenigvuldigen met een bepaald getal (bijv. 0,98) na elke epoch van de training, of door een meer gecompliceerde **learning rate schedule** te gebruiken.

## Verschillende netwerkarchitecturen

Het kiezen van de juiste netwerkarchitectuur voor je probleem kan lastig zijn. Normaal gesproken zouden we een architectuur nemen die bewezen heeft te werken voor onze specifieke taak (of een vergelijkbare). Hier is een [goed overzicht](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) van neurale netwerkarchitecturen voor computer vision.

> Het is belangrijk om een architectuur te kiezen die krachtig genoeg is voor het aantal trainingssamples dat we hebben. Het kiezen van een te krachtig model kan resulteren in [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Een andere goede manier zou zijn om een architectuur te gebruiken die automatisch aanpast aan de vereiste complexiteit. Tot op zekere hoogte zijn **ResNet**-architectuur en **Inception** zelf-aanpassend. [Meer over computer vision-architecturen](../07-ConvNets/CNN_Architectures.md)

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.