# Triki za učenje globokega učenja

Ko postajajo nevronske mreže globlje, postaja proces njihovega učenja vse bolj zahteven. Ena glavnih težav so tako imenovani [izginjajoči gradienti](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) ali [eksplodirajoči gradienti](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Ta objava](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) ponuja dober uvod v te težave.

Da bi bilo učenje globokih mrež bolj učinkovito, lahko uporabimo nekaj tehnik.

## Ohranjanje vrednosti v razumnih intervalih

Da bi bile numerične izračune bolj stabilne, moramo zagotoviti, da so vse vrednosti znotraj naše nevronske mreže v razumnem obsegu, običajno [-1..1] ali [0..1]. To ni zelo stroga zahteva, vendar je narava izračunov s plavajočo vejico takšna, da vrednosti različnih velikosti ni mogoče natančno obdelovati skupaj. Na primer, če seštejemo 10<sup>-10</sup> in 10<sup>10</sup>, bomo verjetno dobili 10<sup>10</sup>, ker se bo manjša vrednost "pretvorila" v isti red kot večja, s čimer se bo mantisa izgubila.

Večina aktivacijskih funkcij ima nelinearnosti okoli [-1..1], zato je smiselno skalirati vse vhodne podatke na interval [-1..1] ali [0..1].

## Začetna inicializacija uteži

Idealno bi bilo, da so vrednosti v istem obsegu po prehodu skozi sloje mreže. Zato je pomembno inicializirati uteži na način, ki ohranja porazdelitev vrednosti.

Normalna porazdelitev **N(0,1)** ni dobra ideja, ker če imamo *n* vhodov, bo standardni odklon izhoda *n*, vrednosti pa bodo verjetno presegle interval [0..1].

Pogosto uporabljene inicializacije so:

- Enakomerna porazdelitev -- `uniform`
- **N(0,1/n)** -- `gaussian`
- **N(0,1/√n_in)** zagotavlja, da za vhode z ničelno srednjo vrednostjo in standardnim odklonom 1 ostaneta enaka srednja vrednost in standardni odklon
- **N(0,√2/(n_in+n_out))** -- tako imenovana **Xavier inicializacija** (`glorot`), ki pomaga ohranjati signale v obsegu med naprej in nazaj propagacijo

## Normalizacija po sklopih

Tudi ob pravilni inicializaciji uteži lahko te med učenjem postanejo poljubno velike ali majhne, kar bo signale spravilo iz ustreznega obsega. Signale lahko vrnemo nazaj z uporabo ene od tehnik **normalizacije**. Čeprav jih je več (normalizacija uteži, normalizacija slojev), se najpogosteje uporablja normalizacija po sklopih.

Ideja **normalizacije po sklopih** je upoštevati vse vrednosti znotraj minibatch-a in izvesti normalizacijo (tj. odšteti srednjo vrednost in deliti s standardnim odklonom) na podlagi teh vrednosti. Implementirana je kot sloj mreže, ki izvaja to normalizacijo po uporabi uteži, vendar pred aktivacijsko funkcijo. Rezultat je višja končna natančnost in hitrejše učenje.

Tukaj je [izvirni članek](https://arxiv.org/pdf/1502.03167.pdf) o normalizaciji po sklopih, [razlaga na Wikipediji](https://en.wikipedia.org/wiki/Batch_normalization) in [dober uvodni blog](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (ter eden [v ruščini](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** je zanimiva tehnika, ki med učenjem odstrani določen odstotek naključnih nevronov. Implementirana je kot sloj z enim parametrom (odstotek nevronov za odstranitev, običajno 10%-50%), med učenjem pa ničla naključne elemente vhodnega vektorja, preden jih posreduje naslednjemu sloju.

Čeprav se to morda sliši kot nenavadna ideja, lahko učinek dropout-a na učenje klasifikatorja MNIST številk vidite v zvezku [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Pospeši učenje in omogoča doseganje višje natančnosti v manj učnih epohah.

Ta učinek lahko razložimo na več načinov:

- Lahko ga obravnavamo kot naključni šok modelu, ki optimizacijo premakne iz lokalnega minimuma
- Lahko ga obravnavamo kot *implicitno povprečenje modela*, saj lahko rečemo, da med dropout-om učimo nekoliko drugačen model

> *Nekateri pravijo, da si pijan človek bolje zapomni nekaj naslednje jutro v primerjavi s treznim človekom, ker možgani z nekaj okvarjenimi nevroni bolje prilagodijo, da zajamejo pomen. Nikoli nismo sami testirali, ali je to res ali ne.*

## Preprečevanje prenaučenja

Eden najpomembnejših vidikov globokega učenja je sposobnost preprečevanja [prenaučenja](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Čeprav je morda mamljivo uporabiti zelo zmogljiv model nevronske mreže, moramo vedno uravnotežiti število parametrov modela s številom učnih vzorcev.

> Poskrbite, da razumete koncept [prenaučenja](../../3-NeuralNetworks/05-Frameworks/Overfitting.md), ki smo ga predstavili prej!

Obstaja več načinov za preprečevanje prenaučenja:

- Zgodnje ustavljanje -- neprekinjeno spremljanje napake na validacijskem sklopu in ustavitev učenja, ko se napaka na validacijskem sklopu začne povečevati.
- Eksplicitno razpadanje uteži / regularizacija -- dodajanje dodatne kazni funkciji izgube za visoke absolutne vrednosti uteži, kar preprečuje modelu doseganje zelo nestabilnih rezultatov
- Povprečenje modela -- učenje več modelov in nato povprečenje rezultatov. To pomaga zmanjšati varianco.
- Dropout (Implicitno povprečenje modela)

## Optimizatorji / algoritmi učenja

Drug pomemben vidik učenja je izbira dobrega algoritma učenja. Čeprav je klasični **gradientni spust** razumna izbira, je lahko včasih prepočasen ali povzroči druge težave.

V globokem učenju uporabljamo **stohastični gradientni spust** (SGD), ki je gradientni spust, uporabljen na minibatch-ih, naključno izbranih iz učnega sklopa. Uteži se prilagodijo po tej formuli:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

Pri **momentum SGD** ohranjamo del gradienta iz prejšnjih korakov. To je podobno, kot če se premikamo nekam z inercijo, in prejmemo udarec v drugo smer; naša pot se ne spremeni takoj, ampak ohranja del prvotnega gibanja. Tukaj uvedemo še en vektor v, ki predstavlja *hitrost*:

- v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
- w<sup>t+1</sup> = w<sup>t</sup> + v<sup>t+1</sup>

Parameter γ tukaj označuje, v kolikšni meri upoštevamo inercijo: γ=0 ustreza klasičnemu SGD; γ=1 je čista enačba gibanja.

### Adam, Adagrad itd.

Ker v vsakem sloju množimo signale z matriko W<sub>i</sub>, odvisno od ||W<sub>i</sub>||, lahko gradient bodisi izginja in je blizu 0, bodisi narašča neomejeno. To je bistvo problema eksplodirajočih/izginjajočih gradientov.

Ena od rešitev tega problema je uporaba samo smeri gradienta v enačbi in ignoriranje absolutne vrednosti, tj.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), kjer ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Ta algoritem se imenuje **Adagrad**. Drugi algoritmi, ki uporabljajo isto idejo: **RMSProp**, **Adam**

> **Adam** velja za zelo učinkovit algoritem za številne aplikacije, zato če niste prepričani, katerega uporabiti - uporabite Adam.

### Omejevanje gradienta

Omejevanje gradienta je razširitev zgornje ideje. Ko je ||∇ℒ|| ≤ θ, upoštevamo prvotni gradient pri optimizaciji uteži, in ko je ||∇ℒ|| > θ - gradient delimo z njegovo normo. Tukaj je θ parameter, v večini primerov lahko vzamemo θ=1 ali θ=10.

### Zmanjševanje hitrosti učenja

Uspeh učenja pogosto zavisi od parametra hitrosti učenja η. Logično je domnevati, da večje vrednosti η vodijo do hitrejšega učenja, kar je nekaj, kar običajno želimo na začetku učenja, nato pa manjše vrednosti η omogočajo fino nastavitev mreže. Zato v večini primerov želimo zmanjšati η med procesom učenja.

To lahko storimo tako, da η pomnožimo z nekim številom (npr. 0,98) po vsaki epohi učenja ali z uporabo bolj zapletenega **načrta hitrosti učenja**.

## Različne arhitekture mrež

Izbira prave arhitekture mreže za vaš problem je lahko zahtevna. Običajno bi izbrali arhitekturo, ki se je izkazala za učinkovito za našo specifično nalogo (ali podobno). Tukaj je [dober pregled](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) arhitektur nevronskih mrež za računalniški vid.

> Pomembno je izbrati arhitekturo, ki bo dovolj zmogljiva glede na število učnih vzorcev, ki jih imamo. Izbira preveč zmogljivega modela lahko vodi do [prenaučenja](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Druga dobra možnost je uporaba arhitekture, ki se bo samodejno prilagodila zahtevani kompleksnosti. Do neke mere sta arhitekturi **ResNet** in **Inception** samoprilagodljivi. [Več o arhitekturah za računalniški vid](../07-ConvNets/CNN_Architectures.md).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve AI za prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.