# Triki za učenje globokega učenja

Ko postajajo nevronske mreže globlje, postaja proces njihovega učenja vse bolj zahteven. Glavni problem so tako imenovani [izginjajoči gradienti](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ali [eksplodirajoči gradienti](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Ta prispevek](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) dobro uvaja v te probleme.

Da bi bilo učenje globokih mrež učinkovitejše, lahko uporabimo nekaj tehnik.

## Ohranitev vrednosti v razumnih intervalih

Da bi bile numerične računanja bolj stabilna, želimo zagotoviti, da so vse vrednosti v naši nevronski mreži v razumni skali, običajno [-1..1] ali [0..1]. To ni zelo stroga zahteva, vendar je narava plavajočih točk takšna, da vrednosti različnih velikosti ni mogoče natančno skupaj obdelovati. Na primer, če dodamo 10<sup>-10</sup> in 10<sup>10</sup>, bomo najverjetneje dobili 10<sup>10</sup>, ker bi bila manjša vrednost "pretvorjena" v isti red kot večja, s čimer bi mantisa bila izgubljena.

Večina aktivacijskih funkcij ima nelinearnosti okoli [-1..1], zato je smiselno vse vhodne podatke preskalirati na interval [-1..1] ali [0..1].

## Začetna inicializacija uteži

Idealno bi bilo, da so vrednosti v istem razponu tudi po prehodu skozi plasti mreže. Pomembno je torej inicializirati uteži tako, da ohranimo porazdelitev vrednosti.

Normalna porazdelitev **N(0,1)** ni dobra izbira, ker če imamo *n* vhodov, bi bila standardna deviacija izhoda *&radic;n*, vrednosti pa bi verjetno skočile izven intervala [0..1].

Pogosto uporabljene inicializacije so:

 * Uniformna porazdelitev -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** zagotavlja, da za vhode z ničelnim povprečjem in standardno deviacijo 1 ostaneta povprečje in standardna deviacija enaki
 * **N(0,&radic;2/(n_in+n_out))** -- tako imenovana **Xavier inicializacija** (`glorot`), ki pomaga ohranjati signale v območju tako pri naprej kot nazaj propagaciji

## Normalizacija serije (Batch Normalization)

Tudi ob pravilni inicializaciji uteži se uteži lahko med učenjem poljubno povečajo ali zmanjšajo, kar bo signale pripeljalo izven ustreznega razpona. Signale lahko vrnemo nazaj z uporabo ene od tehnik **normalizacije**. Obstaja več tehnik (normalizacija uteži, plastna normalizacija), najpogosteje uporabljena pa je normalizacija serije.

Ideja **normalizacije serije** je, da se upoštevajo vse vrednosti čez minibatch in se izvede normalizacija (odštevanje povprečja in deljenje s standardno deviacijo) na podlagi teh vrednosti. Implementirana je kot plast v mreži, ki to normalizacijo izvaja po uporabi uteži, a pred aktivacijsko funkcijo. Zaradi tega je običajno višja končna natančnost in hitrejše učenje.

Tukaj je [originalni članek](https://arxiv.org/pdf/1502.03167.pdf) o normalizaciji serije, [razlaga na Wikipediji](https://en.wikipedia.org/wiki/Batch_normalization) in [dober uvodni blog objava](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (ter ena [v ruščini](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** je zanimiva tehnika, ki med učenjem odstrani določen odstotek naključnih nevronov. Implementirana je kot plast z enim parametrom (odstotek nevronov za odstranitev, običajno 10-50%), ki med učenjem nastavi naključne elemente vhodnega vektorja na nič, še preden ga posreduje naslednji plasti.

Čeprav se to morda sliši nenavadno, lahko učinek dropouta vidite v [`Dropout.ipynb`](Dropout.ipynb) beležnici, ki uči klasifikator številk MNIST. Pospeši učenje in omogoči višjo natančnost v manj epohah.

Ta učinek je mogoče razložiti na več načinov:

 * Lahko ga razumemo kot naključni šok modelu, ki ga spravi iz lokalnega minimuma
 * Lahko ga razumemo kot *implicitno povprečenje modela*, ker med dropoutom učimo rahlo drugačen model

> *Nekateri pravijo, da ko pijanec nekaj poskuša naučiti, si to bolje zapomni naslednje jutro kot trezen, saj možgani z nekaj nefunkcionalnimi nevroni poskušajo bolje prilagoditi in razumeti smisel. Mi tega nismo preizkusili.*

## Preprečevanje prekomernega prileganja

Eden zelo pomembnih vidikov globokega učenja je lahko preprečevanje [prekomernega prileganja](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Čeprav je morda mamljivo uporabiti zelo zmogljiv model nevronske mreže, moramo vedno uravnotežiti število parametrov modela s številom učnih vzorcev.

> Poskrbite, da razumete koncept [prekomernega prileganja](../../3-NeuralNetworks/05-Frameworks/Overfitting.md), ki smo ga že predstavili!

Obstaja več načinov za preprečevanje prekomernega prileganja:

 * Zgodnja zaustavitev -- neprestano spremljanje napake na validacijskem naboru in zaustavitev učenja, ko začne napaka rasti.
 * Izrecno razpadanje uteži / regularizacija -- dodajanje dodatne kazni funkciji izgube za visoke absolutne vrednosti uteži, kar preprečuje, da bi model postal zelo nestabilen
 * Povprečenje modela -- učenje več modelov in nato povprečenje rezultatov. To pomaga minimizirati varianco.
 * Dropout (implicitno povprečenje modela)

## Optimizatorji / algoritmi učenja

Drug pomemben vidik učenja je izbira dobrega algoritma učenja. Čeprav je klasični **gradientni spust** razumljiva izbira, je včasih prepočasen ali povzroči druge težave.

V globokem učenju uporabljamo **stohastični gradientni spust** (SGD), ki je gradientni spust uporabljen na minibatchih, naključno izbranih iz učnega nabora. Uteži se prilagajajo po formuli:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

Pri **momentum SGD** ohranjamo del gradienta iz prejšnjih korakov. Podobno kot ko se premikamo z inercijo, in dobimo udarec v drugo smer, se naša pot ne spremeni takoj, ampak obdrži del prvotnega gibanja. Tu uvedemo še en vektor v, ki predstavlja *hitrost*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Parameter &gamma; tu označuje, v kolikšni meri upoštevamo inercijo: &gamma;=0 ustreza klasičnemu SGD; &gamma;=1 je enačba čistega gibanja.

### Adam, Adagrad itd.

Ker v vsaki plasti signal pomnožimo z matriko W<sub>i</sub>, je od ||W<sub>i</sub>|| odvisno, ali se gradient zmanjšuje proti 0 ali pa neomejeno raste. To je jedro problema eksplodirajočih/izginjajočih gradientov.

Ena od rešitev problema je uporabiti samo smer gradienta v enačbi in ignorirati absolutno vrednost, tj.

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), kjer ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Ta algoritem se imenuje **Adagrad**. Drugi algoritmi, ki uporabljajo isto idejo: **RMSProp**, **Adam**

> **Adam** velja za zelo učinkovit algoritem za številne aplikacije, zato če niste prepričani, katerega uporabiti - uporabite Adam.

### Obrezovanje gradienta (Gradient clipping)

Gradient clipping je razširitev zgornje ideje. Ko je ||&nabla;&lagran;|| &le; &theta;, upoštevamo prvotni gradient pri optimizaciji uteži, ko pa je ||&nabla;&lagran;|| > &theta; - gradient delimo z njegovo normo. Tukaj je &theta; parameter, v večini primerov lahko vzamemo &theta;=1 ali &theta;=10.

### Zmanjšanje hitrosti učenja (Learning rate decay)

Uspeh učenja pogosto zavisi od parametra hitrosti učenja &eta;. Logično je predpostaviti, da večje vrednosti &eta; vodijo do hitrejšega učenja, kar običajno želimo na začetku učenja, medtem ko manjša vrednost &eta; omogoča natančnejšo nastavitev mreže. Zato želimo v večini primerov zniževati &eta; med učenjem.

To lahko naredimo tako, da po vsaki epohi pomnožimo &eta; z nekim številom (npr. 0.98) ali pa uporabimo bolj zapletno **nadzira hitrosti učenja**.

## Različne arhitekture mrež

Izbira prave arhitekture mreže za vaš problem je lahko zahtevna. Običajno vzamemo arhitekturo, ki se je izkazala za uspešno pri naši specifični nalogi (ali podobni). Tukaj je [dober pregled](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) arhitektur nevronskih mrež za računalniški vid.

> Pomembno je izbrati arhitekturo, ki bo dovolj zmogljiva za število učnih vzorcev, ki jih imamo. Izbira premočnega modela lahko privede do [prekomernega prileganja](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Druga dobra možnost je uporabiti arhitekturo, ki se samodejno prilagaja zahtevani kompleksnosti. V določeni meri se arhitekturi **ResNet** in **Inception** prilagajata sama. [Več o arhitekturah za računalniški vid](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->