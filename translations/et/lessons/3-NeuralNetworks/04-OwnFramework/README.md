# Sissejuhatus tehisnärvivõrkudesse. Mitmekihiline perceptron

Eelmises osas õppisite tundma kõige lihtsamat tehisnärvivõrgu mudelit – ühekihilist perceptronit, mis on lineaarne kahe klassi klassifitseerimise mudel.

Selles osas laiendame seda mudelit paindlikumaks raamistikuks, mis võimaldab:

* teha **mitme klassi klassifikatsiooni** lisaks kahe klassi klassifikatsioonile
* lahendada **regressiooniprobleeme** lisaks klassifikatsioonile
* eristada klasse, mis ei ole lineaarselt eristatavad

Samuti arendame välja oma modulaarse raamistiku Pythonis, mis võimaldab meil luua erinevaid tehisnärvivõrgu arhitektuure.

## [Eelloengu viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/7)

## Masinõppe formaliseerimine

Alustame masinõppe probleemi formaliseerimisest. Oletame, et meil on treeningandmestik **X** koos siltidega **Y**, ja peame looma mudeli *f*, mis teeb kõige täpsemaid ennustusi. Ennustuste kvaliteeti mõõdetakse **kaofunktsiooni** &lagran; abil. Sageli kasutatakse järgmisi kaofunktsioone:

* Regressiooniprobleemi puhul, kui peame ennustama arvu, saame kasutada **absoluutset viga** &sum;<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| või **ruutviga** &sum;<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Klassifikatsiooni puhul kasutame **0-1 kaotust** (mis sisuliselt on sama mis mudeli **täpsus**) või **logistilist kaotust**.

Ühekihilise perceptroni puhul oli funktsioon *f* defineeritud kui lineaarne funktsioon *f(x)=wx+b* (kus *w* on kaalude maatriks, *x* on sisendite tunnuste vektor ja *b* on nihkevektor). Erinevate tehisnärvivõrgu arhitektuuride puhul võib see funktsioon olla keerukama kujuga.

> Klassifikatsiooni puhul on sageli soovitav saada võrgu väljundina klasside tõenäosused. Arvude teisendamiseks tõenäosusteks (nt väljundi normaliseerimiseks) kasutame sageli **softmax** funktsiooni &sigma;, ja funktsioon *f* muutub *f(x)=&sigma;(wx+b)*

Ülaltoodud *f* definitsioonis nimetatakse *w* ja *b* **parameetriteks** &theta;=⟨*w,b*⟩. Arvestades andmestikku ⟨**X**,**Y**⟩, saame arvutada kogu andmestiku vea parameetrite &theta; funktsioonina.

> ✅ **Tehisnärvivõrgu treenimise eesmärk on minimeerida viga, muutes parameetreid &theta;**

## Gradientlanguse optimeerimine

On olemas tuntud funktsiooni optimeerimise meetod, mida nimetatakse **gradientlanguseks**. Idee seisneb selles, et saame arvutada kaofunktsiooni tuletise (mitmemõõtmelisel juhul nimetatakse seda **gradientiks**) parameetrite suhtes ja muuta parameetreid nii, et viga väheneks. Seda saab formaliseerida järgmiselt:

* Algväärtusta parameetrid juhuslike väärtustega w<sup>(0)</sup>, b<sup>(0)</sup>
* Korda järgmist sammu mitu korda:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-&eta;&part;&lagran;/&part;w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-&eta;&part;&lagran;/&part;b

Treeningu ajal peaksid optimeerimissammud olema arvutatud kogu andmestikku arvestades (pidage meeles, et kaotus arvutatakse kõigi treeningnäidete summa põhjal). Kuid reaalses elus võtame andmestikust väikeseid osi, mida nimetatakse **minipartiideks**, ja arvutame gradientid andmealamkogumi põhjal. Kuna alamkogum valitakse iga kord juhuslikult, nimetatakse sellist meetodit **stohhastiliseks gradientlanguseks** (SGD).

## Mitmekihilised perceptronid ja tagasilevik

Ühekihiline võrk, nagu me eespool nägime, suudab klassifitseerida lineaarselt eristatavaid klasse. Rikkama mudeli loomiseks saame kombineerida mitu võrgu kihti. Matemaatiliselt tähendaks see, et funktsioon *f* oleks keerukama kujuga ja arvutataks mitmes etapis:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>&alpha;(z<sub>1</sub>)+b<sub>2</sub>
* f = &sigma;(z<sub>2</sub>)

Siin &alpha; on **mittelineaarne aktivatsioonifunktsioon**, &sigma; on softmax funktsioon ja parameetrid &theta;=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradientlanguse algoritm jääb samaks, kuid gradientide arvutamine muutub keerulisemaks. Arvestades ahel-diferentseerimise reeglit, saame tuletised arvutada järgmiselt:

* &part;&lagran;/&part;w<sub>2</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;w<sub>2</sub>)
* &part;&lagran;/&part;w<sub>1</sub> = (&part;&lagran;/&part;&sigma;)(&part;&sigma;/&part;z<sub>2</sub>)(&part;z<sub>2</sub>/&part;&alpha;)(&part;&alpha;/&part;z<sub>1</sub>)(&part;z<sub>1</sub>/&part;w<sub>1</sub>)

> ✅ Ahel-diferentseerimise reeglit kasutatakse kaofunktsiooni tuletiste arvutamiseks parameetrite suhtes.

Pange tähele, et kõigi nende avaldiste vasakpoolne osa on sama, ja seega saame tuletised tõhusalt arvutada, alustades kaofunktsioonist ja liikudes "tagasi" läbi arvutusgraafi. Seetõttu nimetatakse mitmekihilise perceptroni treenimise meetodit **tagasilevikuks** ehk 'backprop'.

<img alt="arvutusgraaf" src="../../../../../translated_images/et/ComputeGraphGrad.4626252c0de03507.webp"/>

> Image by [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Katame tagasileviku palju detailsemalt meie näidisnotebookis.  

## Kokkuvõte

Selles õppetunnis ehitasime oma tehisnärvivõrgu raamistiku ja kasutasime seda lihtsa kahemõõtmelise klassifikatsiooniprobleemi lahendamiseks.

## 🚀 Väljakutse

Kaasaolevas notebookis rakendate oma raamistiku mitmekihiliste perceptronite loomiseks ja treenimiseks. Näete üksikasjalikult, kuidas kaasaegsed tehisnärvivõrgud töötavad.

Jätkake [OwnFramework](OwnFramework.ipynb) notebookiga ja töötage see läbi.

## [Järelloengu viktoriin](https://ff-quizzes.netlify.app/en/ai/quiz/8)

## Ülevaade ja iseseisev õppimine

Tagasilevik on tehisintellekti ja masinõppe valdkonnas levinud algoritm, mida tasub [täpsemalt uurida](https://wikipedia.org/wiki/Backpropagation).

## [Ülesanne](lab/README.md)

Selles praktikumis palutakse teil kasutada selles õppetunnis loodud raamistikku MNIST käsitsi kirjutatud numbrite klassifikatsiooni lahendamiseks.

* [Juhised](lab/README.md)
* [Notebook](lab/MyFW_MNIST.ipynb)

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palun arvestage, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algkeeles tuleks lugeda autoriteetseks allikaks. Olulise teabe puhul on soovitatav kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.