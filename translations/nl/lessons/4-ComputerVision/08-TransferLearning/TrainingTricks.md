# Deep Learning Trainings trucs

Naarmate neurale netwerken dieper worden, wordt het trainingsproces steeds uitdagender. Een groot probleem is het zogenaamde [verdwijnen van gradiënten](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) of [exploderen van gradiënten](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Deze post](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) geeft een goede introductie in deze problemen.

Om het trainen van diepe netwerken efficiënter te maken, zijn er een paar technieken die gebruikt kunnen worden.

## Waarden binnen redelijke grenzen houden

Om numerieke berekeningen stabieler te maken, willen we ervoor zorgen dat alle waarden binnen ons neurale netwerk zich binnen een redelijke schaal bevinden, meestal [-1..1] of [0..1]. Dit is geen heel strenge eis, maar de aard van floating-point berekeningen is zodanig dat waarden van verschillende grootte niet nauwkeurig samen gemanipuleerd kunnen worden. Bijvoorbeeld, als we 10<sup>-10</sup> en 10<sup>10</sup> optellen, krijgen we waarschijnlijk 10<sup>10</sup>, omdat de kleinere waarde wordt "omgezet" naar dezelfde orde als de grotere, waardoor de mantisse verloren gaat.

De meeste activatiefuncties hebben niet-lineariteiten rond [-1..1], dus het is logisch om alle inputdata te schalen naar het interval [-1..1] of [0..1].

## Initiële Gewicht Initialisatie

Idealiter willen we dat de waarden na doorgeven door netwerklaag in hetzelfde bereik blijven. Daarom is het belangrijk om gewichten zo te initialiseren dat de verdeling van waarden behouden blijft.

Een normale verdeling **N(0,1)** is geen goed idee, want als we *n* inputs hebben, wordt de standaardafwijking van de output *&radic;n* en zullen waarden waarschijnlijk buiten het [0..1]-interval vallen.

De volgende initialisaties worden vaak gebruikt:

 * Uniforme verdeling -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** garandeert dat voor inputs met nulgemiddelde en standaardafwijking 1 hetzelfde gemiddelde/standaardafwijking behouden blijft
 * **N(0,&radic;2/(n_in+n_out))** -- zogenaamde **Xavier initialisatie** (`glorot`), helpt om signalen binnen bereik te houden tijdens zowel voorwaartse als achterwaartse propagatie

## Batch Normalisatie

Zelfs met goede gewichtinitialisatie kunnen gewichten arbitrair groot of klein worden tijdens training, waardoor signalen uit het juiste bereik raken. We kunnen signalen terugbrengen met een van de **normalisatietechnieken**. Er zijn er meerdere (Weight Normalization, Layer Normalization), maar de meest gebruikte is Batch Normalisatie.

Het idee van **batch normalisatie** is om alle waarden binnen een minibatch mee te nemen en normalisatie uit te voeren (dat wil zeggen, het gemiddelde aftrekken en delen door de standaardafwijking) gebaseerd op die waarden. Het is geïmplementeerd als een netwerklaag die deze normalisatie uitvoert na het toepassen van de gewichten, maar vóór de activatiefunctie. Dit zorgt meestal voor een hogere uiteindelijke nauwkeurigheid en snellere training.

Hier is het [originele artikel](https://arxiv.org/pdf/1502.03167.pdf) over batch normalisatie, de [uitleg op Wikipedia](https://en.wikipedia.org/wiki/Batch_normalization), en [een goede introductieblogpost](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (en een [in het Russisch](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** is een interessante techniek die tijdens training een bepaald percentage willekeurige neuronen verwijdert. Het is ook geïmplementeerd als een laag met één parameter (percentage neuronen om te verwijderen, meestal 10%-50%), en tijdens training worden willekeurige elementen van de inputvector op nul gezet, voordat deze naar de volgende laag gaan.

Hoewel dit misschien een vreemd idee lijkt, kunt u het effect van dropout zien op het trainen van een MNIST-cijferclassificator in de [`Dropout.ipynb`](Dropout.ipynb) notebook. Het versnelt de training en stelt ons in staat om hogere nauwkeurigheid in minder train-epochs te bereiken.

Dit effect kan op verschillende manieren worden verklaard:

 * Het kan worden beschouwd als een willekeurige schok voor het model, die optimalisatie uit een lokaal minimum haalt
 * Het kan worden beschouwd als *impliciete modelgemiddeling*, omdat we kunnen zeggen dat we tijdens dropout een iets ander model trainen

> *Sommige mensen zeggen dat wanneer een dronken persoon iets probeert te leren, hij dit de volgende ochtend beter zal herinneren dan een nuchter persoon, omdat een brein met enkele disfunctionerende neuronen beter probeert aan te passen om de betekenis te begrijpen. We hebben dit nooit zelf getest of het waar is of niet*

## Overfitting voorkomen

Een van de zeer belangrijke aspecten van deep learning is het kunnen voorkomen van [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Hoewel het verleidelijk kan zijn een zeer krachtig neuraal netwerkmodel te gebruiken, moeten we altijd het aantal modelparameters afwegen tegen het aantal trainingsvoorbeelden.

> Zorg ervoor dat je het concept van [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) dat we eerder hebben geïntroduceerd goed begrijpt!

Er zijn verschillende manieren om overfitting te voorkomen:

 * Vroegtijdig stoppen -- continu de fout op de validatieset monitoren en stoppen met trainen zodra de validatiefout begint te stijgen.
 * Expliciete gewichtsvermindering / Regularisatie -- een extra straf toevoegen aan de verliesfunctie voor hoge absolute waarden van gewichten, wat voorkomt dat het model zeer instabiele resultaten krijgt
 * Modelgemiddeling -- meerdere modellen trainen en dan het resultaat middelen. Dit helpt om de variantie te minimaliseren.
 * Dropout (Impliciete modelgemiddeling)

## Optimizers / Trainingsalgoritmes

Een ander belangrijk aspect van trainen is het kiezen van een goed trainingsalgoritme. Hoewel klassieke **gradient descent** een redelijke keuze is, kan dit soms te langzaam zijn, of andere problemen veroorzaken.

In deep learning gebruiken we **Stochastische Gradient Descent** (SGD), wat gradient descent is toegepast op minibatches die willekeurig uit de trainingsset worden geselecteerd. Gewichten worden aangepast met deze formule:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

In **momentum SGD** houden we een deel van de gradiënt van eerdere stappen vast. Dit is vergelijkbaar met wanneer we ergens heen bewegen met traagheid en een duw krijgen in een andere richting; onze traject verandert niet onmiddellijk maar houdt een deel van de oorspronkelijke beweging vast. Hier introduceren we een andere vector v om de *snelheid* te representeren:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Hier geeft parameter &gamma; aan in welke mate we traagheid meenemen: &gamma;=0 komt overeen met klassieke SGD; &gamma;=1 is een zuivere bewegingsvergelijking.

### Adam, Adagrad, enz.

Omdat we in elke laag signalen vermenigvuldigen met een matrix W<sub>i</sub>, afhankelijk van ||W<sub>i</sub>||, kan de gradiënt zowel afnemen en dichtbij nul komen, als onbeperkt stijgen. Dit is de kern van het probleem van Exploding/Vanishing Gradients.

Een van de oplossingen voor dit probleem is om alleen de richting van de gradiënt in de vergelijking te gebruiken, en de absolute waarde te negeren, dat wil zeggen:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), waarbij ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Dit algoritme heet **Adagrad**. Andere algoritmes die hetzelfde idee gebruiken zijn: **RMSProp**, **Adam**

> **Adam** wordt beschouwd als een zeer efficiënt algoritme voor veel toepassingen, dus als u niet zeker weet welke u moet gebruiken - gebruik Adam.

### Gradiënt knippen

Gradiënt knippen is een uitbreiding van het bovenstaande idee. Wanneer ||&nabla;&lagran;|| &le; &theta; beschouwen we de originele gradiënt in de gewichtsoptimalisatie, en wanneer ||&nabla;&lagran;|| > &theta; delen we de gradiënt door zijn norm. Hier is &theta; een parameter, in de meeste gevallen kunnen we &theta;=1 of &theta;=10 nemen.

### Afname van het leerpercentage

Succes van de training hangt vaak af van de leerparameter &eta;. Het is logisch aan te nemen dat grotere waarden van &eta; resulteren in snellere training, wat we meestal in het begin willen, en daarna kleinere waarden van &eta; ons in staat stellen het netwerk fijn af te stemmen. Daarom willen we in de meeste gevallen &eta; laten afnemen tijdens het trainingsproces.

Dit kan gedaan worden door &eta; te vermenigvuldigen met een getal (bijvoorbeeld 0.98) na elke epoch van de training, of door gebruik te maken van een complexere **learning rate schedule**.

## Verschillende Netwerkarchitecturen

Het kiezen van de juiste netwerkarchitectuur voor uw probleem kan lastig zijn. Gewoonlijk kiezen we een architectuur die bewezen heeft te werken voor onze specifieke taak (of een vergelijkbare). Hier is een [goed overzicht](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) van neurale netwerkarchitecturen voor computer vision.

> Het is belangrijk een architectuur te kiezen die krachtig genoeg is voor het aantal trainingsvoorbeelden dat we hebben. Een te krachtig model kan leiden tot [overfitting](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Een andere goede aanpak is een architectuur gebruiken die zich automatisch aanpast aan de vereiste complexiteit. Tot op zekere hoogte zijn de **ResNet** architectuur en **Inception** zelf-aanpassend. [Meer over computer vision architecturen](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->