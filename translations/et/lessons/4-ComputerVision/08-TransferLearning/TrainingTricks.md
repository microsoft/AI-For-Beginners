# Süvaõppe treenimise nipid

Kui närvivõrgud muutuvad sügavamaks, muutub nende treenimine üha keerulisemaks. Üks peamisi probleeme on nn [kaduvad gradiendid](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) või [plahvatavad gradiendid](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [See postitus](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) annab hea sissejuhatuse nendesse probleemidesse.

Sügavate võrkude treenimise tõhusamaks muutmiseks saab kasutada mitmeid tehnikaid.

## Väärtuste hoidmine mõistlikus vahemikus

Et arvutused oleksid numbriliselt stabiilsemad, tahame tagada, et kõik väärtused meie närvivõrgus jääksid mõistlikku vahemikku, tavaliselt [-1..1] või [0..1]. See ei ole väga range nõue, kuid ujukomaarvutuste olemus on selline, et erineva suurusjärguga väärtusi ei saa täpselt koos manipuleerida. Näiteks, kui liidame 10<sup>-10</sup> ja 10<sup>10</sup>, saame tõenäoliselt 10<sup>10</sup>, sest väiksem väärtus "muundatakse" suurema väärtuse suurusjärgule ja mantissa kaob.

Enamik aktivatsioonifunktsioone on mittelineaarsed vahemikus [-1..1], mistõttu on mõistlik skaleerida kogu sisendandmed vahemikku [-1..1] või [0..1].

## Algne kaalude initsialiseerimine

Ideaalis tahame, et väärtused jääksid samasse vahemikku pärast võrgukihtide läbimist. Seetõttu on oluline initsialiseerida kaalud nii, et väärtuste jaotus säiliks.

Normaaljaotus **N(0,1)** ei ole hea idee, sest kui meil on *n* sisendit, oleks väljundi standardhälve *n*, ja väärtused kipuksid hüppama välja vahemikust [0..1].

Sageli kasutatakse järgmisi initsialiseerimisi:

 * Ühtlane jaotus -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** tagab, et nullkeskmise ja standardhälbega 1 sisendite korral jääb sama keskmine/standardhälve
 * **N(0,&radic;2/(n_in+n_out))** -- nn **Xavier initsialiseerimine** (`glorot`), mis aitab hoida signaale vahemikus nii edasi- kui tagasipropageerimisel

## Partii normaliseerimine

Isegi korraliku kaalude initsialiseerimise korral võivad kaalud treenimise käigus muutuda suvaliselt suureks või väikseks, viies signaalid sobivast vahemikust välja. Signaale saab tagasi tuua, kasutades üht **normaliseerimise** tehnikatest. Kuigi neid on mitmeid (kaalude normaliseerimine, kihi normaliseerimine), kasutatakse kõige sagedamini partii normaliseerimist.

**Partii normaliseerimise** idee seisneb selles, et arvestatakse kõiki väärtusi minibatch'i ulatuses ja tehakse normaliseerimine (st lahutatakse keskmine ja jagatakse standardhälbega) nende väärtuste põhjal. See rakendatakse võrgukihina, mis teeb normaliseerimise pärast kaalude rakendamist, kuid enne aktivatsioonifunktsiooni. Selle tulemusena saavutatakse tõenäoliselt kõrgem lõplik täpsus ja kiirem treenimine.

Siin on [algne artikkel](https://arxiv.org/pdf/1502.03167.pdf) partii normaliseerimisest, [selgitus Wikipedias](https://en.wikipedia.org/wiki/Batch_normalization) ja [hea sissejuhatav blogipostitus](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (ja üks [vene keeles](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** on huvitav tehnika, mis eemaldab treenimise ajal teatud protsendi juhuslikke neuroneid. See rakendatakse kihina ühe parameetriga (protsent eemaldatavaid neuroneid, tavaliselt 10%-50%), ja treenimise ajal nullib see juhuslikud sisendvektori elemendid enne nende edastamist järgmisele kihile.

Kuigi see võib tunduda kummalise ideena, näete dropout'i mõju MNIST numbrituvastaja treenimisel [`Dropout.ipynb`](Dropout.ipynb) märkmikus. See kiirendab treenimist ja võimaldab saavutada kõrgemat täpsust vähemate treeningepohhidega.

Seda efekti saab selgitada mitmel viisil:

 * Seda võib pidada mudeli juhuslikuks šokifaktoriks, mis viib optimeerimise lokaalsest miinimumist välja
 * Seda võib pidada *kaudseks mudeli keskmistamiseks*, sest dropout'i ajal treenime veidi erinevat mudelit

> *Mõned inimesed ütlevad, et kui purjus inimene üritab midagi õppida, mäletab ta seda järgmisel hommikul paremini kui kaine inimene, sest ajus, kus mõned neuronid ei tööta korralikult, püüab paremini kohaneda ja mõtet haarata. Me pole ise kunagi testinud, kas see on tõsi või mitte.*

## Üleõppimise vältimine

Üks süvaõppe väga oluline aspekt on [üleõppimise](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) vältimine. Kuigi võib olla ahvatlev kasutada väga võimsat närvivõrgumudelit, peaksime alati tasakaalustama mudeli parameetrite arvu treeningnäidiste arvuga.

> Veenduge, et mõistate [üleõppimise](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) kontseptsiooni, mida oleme varem tutvustanud!

Üleõppimise vältimiseks on mitmeid viise:

 * Varajane peatamine -- jälgige pidevalt valideerimiskomplekti viga ja lõpetage treenimine, kui valideerimisviga hakkab suurenema.
 * Selgesõnaline kaalude lagunemine / regulaarimine -- lisage kaotuse funktsioonile täiendav karistus suurte kaalude absoluutväärtuste eest, mis hoiab ära mudeli väga ebastabiilsete tulemuste saamise
 * Mudeli keskmistamine -- treenige mitu mudelit ja keskmistage tulemus. See aitab vähendada variatsiooni.
 * Dropout (kaudne mudeli keskmistamine)

## Optimeerijad / treenimisalgoritmid

Teine oluline treenimise aspekt on hea treenimisalgoritmi valimine. Kuigi klassikaline **gradientide langus** on mõistlik valik, võib see mõnikord olla liiga aeglane või põhjustada muid probleeme.

Süvaõppes kasutame **stohhastilist gradientide langust** (SGD), mis on gradientide langus, mida rakendatakse treeningkomplektist juhuslikult valitud minibatch'idele. Kaalud kohandatakse järgmise valemi abil:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Moment

**Momentiga SGD** puhul säilitame osa eelmiste sammude gradientidest. See on sarnane olukorrale, kus liigume kuskile inertsiga ja saame löögi teises suunas – meie trajektoor ei muutu kohe, vaid säilitab osa algsest liikumisest. Siin tutvustame teist vektorit v, mis esindab *kiirust*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Siin parameeter &gamma; näitab, mil määral arvestame inertsiga: &gamma;=0 vastab klassikalisele SGD-le; &gamma;=1 on puhas liikumisvõrrand.

### Adam, Adagrad jne.

Kuna igas kihis korrutame signaale mingi maatriksiga W<sub>i</sub>, sõltuvalt ||W<sub>i</sub>||, võib gradient kas väheneda ja olla lähedal nullile või tõusta lõpmatuseni. See on plahvatavate/kaduvate gradientide probleemi olemus.

Üks lahendus sellele probleemile on kasutada võrrandis ainult gradiendi suunda ja ignoreerida absoluutväärtust, st

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), kus ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Seda algoritmi nimetatakse **Adagrad**. Teised algoritmid, mis kasutavad sama ideed: **RMSProp**, **Adam**

> **Adam** on paljude rakenduste jaoks väga tõhus algoritm, nii et kui te pole kindel, millist kasutada – kasutage Adamit.

### Gradientide kärpimine

Gradientide kärpimine on ülaltoodud idee laiendus. Kui ||&nabla;&lagran;|| &le; &theta;, arvestame kaalude optimeerimisel algset gradienti, ja kui ||&nabla;&lagran;|| > &theta; – jagame gradiendi selle normiga. Siin &theta; on parameeter, enamikul juhtudel võime võtta &theta;=1 või &theta;=10.

### Õppemäära vähendamine

Treeningu edukus sõltub sageli õppemäära parameetrist &eta;. On loogiline eeldada, et suuremad &eta; väärtused toovad kaasa kiirema treenimise, mida tavaliselt soovime treeningu alguses, ja siis väiksemad &eta; väärtused võimaldavad meil võrku peenhäälestada. Seega tahame enamikul juhtudel &eta; treeningu käigus vähendada.

Seda saab teha, korrutades &eta; mingi arvuga (nt 0.98) pärast iga treeningepohhi või kasutades keerukamat **õppemäära ajakava**.

## Erinevad võrguarhitektuurid

Õige võrguarhitektuuri valimine oma probleemi jaoks võib olla keeruline. Tavaliselt võtaksime arhitektuuri, mis on tõestanud, et töötab meie konkreetse ülesande (või sarnase) jaoks. Siin on [hea ülevaade](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) närvivõrkude arhitektuuridest arvutinägemise jaoks.

> On oluline valida arhitektuur, mis on piisavalt võimas treeningnäidiste arvu jaoks, mis meil on. Liiga võimsa mudeli valimine võib viia [üleõppimiseni](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Teine hea viis oleks kasutada arhitektuuri, mis kohandub automaatselt vajaliku keerukusega. Teatud määral on **ResNet** arhitektuur ja **Inception** isekohanduvad. [Rohkem arvutinägemise arhitektuuridest](../07-ConvNets/CNN_Architectures.md)

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.