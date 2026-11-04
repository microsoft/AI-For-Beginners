# Süvaõppe treeningnipid

Kuna närvivõrgud muutuvad järjest sügavamaks, muutub ka nende treenimine järjest keerukamaks. Üks peamine probleem on niinimetatud [haja gradientide](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) või [plahvatavate gradientide](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.) probleem. [See postitus](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) annab nende probleemide kohta hea ülevaate.

Selleks, et sügavate närvivõrkude treenimine oleks efektiivsem, saab kasutada mitmeid tehnikaid.

## Väärtuste hoidmine mõistlikus vahemikus

Mittearvutuslike operatsioonide stabiilsuse tagamiseks tahame olla kindlad, et kõik närvivõrgu väärtused jäävad mõistlikku skaala, tavaliselt [-1..1] või [0..1] vahemikku. See pole väga range nõue, kuid ujukoma-arvutuste olemus on selline, et erineva suurusjärgu väärtusi ei saa täpselt koos manipuleerida. Näiteks, kui liidame 10<sup>-10</sup> ja 10<sup>10</sup>, saame tõenäoliselt 10<sup>10</sup>, sest väiksem väärtus "konverteeritakse" sama suurusjärku kui suurem, ning mantiss võib kaduda.

Enamik aktivatsioonifunktsioone on mittenilineaarsed [-1..1] vahemikus, seega on mõistlik skaleerida kogu sisendandmestik [-1..1] või [0..1] vahemikku.

## Algne kaalude initsialiseerimine

Ideaalsel juhul soovime, et väärtused jääksid pärast läbimist võrgukihist samasse vahemikku. Seetõttu on oluline kaalud initsialiseerida nii, et säiliks väärtuste jaotus.

Normaaljaotus **N(0,1)** pole hea valik, sest kui meil on *n* sisendit, on väljundi standardhälve *&radic;n*, ning väärtused võivad tõusta väljapoole [0..1] vahemikku.

Sageli kasutatakse järgmisi initsialiseerimisi:

 * Ühtlane jaotus -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** tagab, et nullkeskmise ja standardhälbega 1 sisendi puhul jääb keskmine ja standardhälve samaks
 * **N(0,&radic;2/(n_in+n_out))** -- nii-öelda **Xavier initsialiseerimine** (`glorot`), mis aitab hoida signaale vahemikus nii edasi- kui tagasipropagatsiooni ajal

## Partiise normaliseerimine

Isegi korraliku kaalude initsialiseerimise puhul võivad kaalud treeningu käigus muutuda suvaliselt suurteks või väikesteks, tuues signaalid väljapoole õiget vahemikku. Saame signaale tagasi viia, kasutades ühte **normaliseerimise** tehnikatest. Kuigi neid on mitu (Weight normalization, Layer Normalization), on kõige enam kasutatav Partiise normaliseerimine.

**Partiise normaliseerimise** idee on võtta kogu minipartiisi väärtused arvesse ja teha normaliseerimine (st lahutada keskmine ja jagada standardhälbega) nende väärtuste põhjal. See on implementeeritud võrgukihina, mis teeb normaliseerimise pärast kaalude rakendamist, kuid enne aktivatsioonifunktsiooni. Tulemuseks on tavaliselt kõrgem lõplik täpsus ja kiirem treenimine.

Siin on [originaaluuring](https://arxiv.org/pdf/1502.03167.pdf) partiise normaliseerimise kohta, [selgitus Wikipedias](https://en.wikipedia.org/wiki/Batch_normalization) ja [hea sissejuhatav blogipostitus](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (ning üks [vene keeles](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** on huvitav tehnika, mis eemaldab treeningu ajal juhusliku protsendi neuroneid. See on samuti implementeeritud kihina ühe parameetriga (protsent neuroneid, mida eemaldada - tavaliselt 10%-50%), ja treeningu ajal nullib juhuslikud sisendvektori elemendid enne järgmisesse kihi edastamist.

Kuigi see kõlab veidralt, võib näha dropouti mõju MNIST numbriklassifikaatori treenimisel [`Dropout.ipynb`](Dropout.ipynb) märkmikus. See kiirendab treeningut ja võimaldab saavutada kõrgemat täpsust vähemate treeningueepoopide jooksul.

Seda efekti saab seletada mitmel viisil:

 * Seda võib pidada juhuslikuks šokiteguriks mudelile, mis viib optimeerimise välja lokaalsest miinimumist
 * Seda võib käsitleda kui *implitsiitset mudelite keskmistamist*, sest dropouti ajal treenime natuke erinevat mudelit

> *Mõned ütlevad, et kui purjus inimene üritab midagi õppida, mäletab ta järgmisel hommikul seda paremini kui kainuses olev, sest ajul, millel on mõningaid kahjustunud neuroneid, on parem kohaneda tähenduse mõistmiseks. Me pole ise seda testinud, kas see on tõsi või mitte.*

## Ületreenimise vältimine

Üks süvaõppe väga oluline aspekt on [ületreenimise](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) vältimine. Kuigi võib olla ahvatlev kasutada väga võimsat närvivõrku, peaksime alati tasakaalustama mudeli parameetrite arvu treeningandmete hulgaga.

> Veenduge, et mõistate varem tutvustatud [ületreenimise](../../3-NeuralNetworks/05-Frameworks/Overfitting.md) kontseptsiooni!

Ületreenimist saab vältida mitmel viisil:

 * Varajane peatamine -- pidev veapõhine jälgimine valideerimiskogumil ja treeningu peatamine, kui valideerimisviga hakkab suurenema.
 * Eksplitseeritud kaalude kahanemine / reguliseerimine -- lisada lisakaristus kadu funktsioonile kõrgete kaalude absoluutväärtuste eest, mis hoiab mudeli stabiilsena.
 * Mudelite keskmistamine -- treenida mitut mudelit ja seejärel tulemusi keskmistada. See aitab vähendada dispersiooni.
 * Dropout (Implitsiitne mudelite keskmistamine)

## Optimeerijad / treeningualgoritmid

Teine oluline treeningu aspekt on valida hea treeningualgoritm. Kuigi klassikaline **gradientlangus** on mõistlik valik, võib see vahel olla liiga aeglane või põhjustada muid probleeme.

Süvaõppes kasutame **stokastilist gradientlangust** (SGD), mis on gradientlangus, rakendatud minipartiisidele, mis on juhuslikult valitud treeningkogumist. Kaale uuendatakse järgmiselt:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

**Momentumiga SGD** puhul säilitame osa eelmiste sammude gradientidest. See on nagu liikumine inertsi tõttu, kui saadame löögi teises suunas, pole trajektoor kohene muutus, vaid säilib osa algsest liikumisest. Siin tutvustame teist vektorit v, mis tähistab *kiirust*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Parameeter &gamma; näitab, kuivõrd arvestame inertsi: &gamma;=0 vastab klassikalisele SGD-le; &gamma;=1 on puhas liikumisvõrrand.

### Adam, Adagrad jms

Kuna igas kihis korrutame signaale mingi maatriksiga W<sub>i</sub>, siis sõltuvalt ||W<sub>i</sub>|| gradient kas kahaneb ja läheneb nullile või kasvab piiramatult. See on Haja/Plahvatavate Gradientide probleemi olemus.

Üks lahendusi sellele probleemile on kasutada võrrandis ainult gradienti suunda ja ignoreerida absoluutväärtust, st

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), kus ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Seda algoritmi nimetatakse **Adagrad**-iks. Samal ideel põhinevaid algoritme on ka **RMSProp**, **Adam**.

> **Adam** on paljudes rakendustes väga efektiivne algoritm, nii et kui sa pole kindel, kumba kasutada - kasuta Adamit.

### Gradientide kärpimine

Gradientide kärpimine on eeltoodud idee laiendus. Kui ||&nabla;&lagran;|| &le; &theta;, arvestame originaalset gradienti kaalude optimeerimisel, ning kui ||&nabla;&lagran;|| > &theta;, jagame gradienti selle normaaliga. Parameeter &theta; on definitsioonipõhine, enamasti sobib &theta;=1 või &theta;=10.

### Õppemäärade kahanemine

Treeningu edu sõltub tihti õppemäärast &eta;. Loogiline on eeldada, et suuremad &eta;-väärtused annavad kiirema treeningu, mida tavaliselt soovime alguses, ning seejärel võimaldab väiksem &eta; võrku peenhäälestada. Seega tahame enamasti &eta;-d treeningu käigus vähendada.

Seda saab teha, korrutades &eta; mingi arvuga (nt 0.98) iga treeningueepoo järel või kasutades keerulisemat **õppemäärade ajakava**.

## Erinevad võrgukihid

Õige võrgukihi valik probleemi jaoks võib olla keeruline. Tavaliselt valime arhitektuuri, mis on tõestanud oma töökindlust meie konkreetse ülesande (või sarnase) puhul. Siin on [hea ülevaade](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) arvutinägemise võrgukihidest.

> Oluline on valida piisavalt võimas arhitektuur treeningnäidete arvuga arvestades. Liiga võimas mudel võib viia ületreeninguni [ületreenimine](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Teine hea meetod on kasutada arhitektuuri, mis kohandub automaatselt vajaliku keerukusega. Mõõdukalt on ise-kohanduvad arhitektuurid **ResNet** ja **Inception**. [Rohkem arvutinägemise arhitektuuride kohta](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->