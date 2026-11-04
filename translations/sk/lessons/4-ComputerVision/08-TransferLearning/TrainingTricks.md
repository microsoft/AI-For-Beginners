# Triky pre trénovanie hlbokých učenia

Ako sa neurónové siete stávajú hlbšími, proces ich trénovania sa stáva čoraz náročnejším. Jedným z hlavných problémov sú tzv. [miznúce gradienty](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) alebo [explodujúce gradienty](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Tento príspevok](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) dobre predstavuje tieto problémy.

Na efektívnejšie trénovanie hlbokých sietí existuje niekoľko techník, ktoré je možné použiť.

## Udržiavanie hodnôt v rozumnom intervale

Aby sme zabezpečili stabilitu číselných výpočtov, chceme, aby všetky hodnoty v našej neurónovej sieti boli v rozumnom rozsahu, zvyčajne [-1..1] alebo [0..1]. Nie je to veľmi prísna požiadavka, no povaha výpočtov v plávajúcej desatinnej čiarke je taká, že hodnoty rôznych veľkostných rádov sa nedajú presne spracovať spoločne. Napríklad, ak sčítame 10<sup>-10</sup> a 10<sup>10</sup>, pravdepodobne dostaneme 10<sup>10</sup>, pretože menšia hodnota sa "pretvorí" na rovnaký rád ako väčšia, a tým sa mantisa stratí.

Väčšina aktivačných funkcií má nelineárnosti okolo [-1..1], preto je zmysluplné škálovať všetky vstupné dáta do intervalu [-1..1] alebo [0..1].

## Počiatočné inicializovanie váh

Ideálne chceme, aby hodnoty zostali v rovnakom rozsahu po prechode jednotlivými vrstvami siete. Preto je dôležité inicializovať váhy tak, aby sa zachovalo rozloženie hodnôt.

Normálne rozdelenie **N(0,1)** nie je dobrý nápad, pretože ak máme *n* vstupov, štandardná odchýlka výstupu bude *&radic;n*, a hodnoty môžu vyskočiť mimo intervalu [0..1].

Používajú sa nasledujúce inicializácie:

 * Rovnomerné rozdelenie -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/&radic;n_in)** zaručuje, že pre vstupy so strednou hodnotou nula a štandardnou odchýlkou 1 zostane rovnaká stredná hodnota/štandardná odchýlka
 * **N(0,&radic;2/(n_in+n_out))** -- tzv. **Xavierova inicializácia** (`glorot`), pomáha udržať signály v rozsahu počas dopredného aj spätneho šírenia

## Batch normalizácia

Aj pri správnom inicializovaní váh sa môžu váhy počas trénovania stať ľubovoľne veľkými alebo malými a priniesť signály mimo správneho rozsahu. Signály môžeme vrátiť naspäť použitím jednej z **normalizačných** techník. Hoci ich existuje viacero (normalizácia váh, vrstiev), najčastejšie používanou je Batch normalizácia.

Myšlienka **batch normalizácie** je zohľadniť všetky hodnoty v minibatchi a vykonať normalizáciu (t. j. odčítať priemer a vydeliť štandardnou odchýlkou) na základe týchto hodnôt. Implementuje sa ako vrstva siete, ktorá túto normalizáciu vykoná po aplikovaní váh, ale pred aktivačnou funkciou. Výsledkom je vyššia konečná presnosť a rýchlejšie trénovanie.

Tu je [pôvodný článok](https://arxiv.org/pdf/1502.03167.pdf) o batch normalizácii, [vysvetlenie na Wikipédii](https://en.wikipedia.org/wiki/Batch_normalization) a [dobrý úvodný blogový príspevok](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (a jeden [v ruštine](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** je zaujímavá technika, ktorá počas trénovania vynecháva určitú percentuálnu časť náhodných neurónov. Tiež sa implementuje ako vrstva s jedným parametrom (percento neurónov na vynechanie, zvyčajne 10%-50%) a počas trénovania nuluje náhodné prvky vstupného vektora pred jeho odoslaním do ďalšej vrstvy.

Hoci to môže znieť zvláštne, efekt dropout na trénovanie klasifikátora číslic MNIST môžete vidieť v poznámkovom bloku [`Dropout.ipynb`](Dropout.ipynb). Urýchľuje trénovanie a umožňuje dosiahnuť vyššiu presnosť v menšom počte epoch.

Tento efekt je možné vysvetliť niekoľkými spôsobmi:

 * Môže to byť považované za náhodný šokovací faktor pre model, ktorý vytrhne optimalizáciu zo zaseknutia v lokálnom minime
 * Môže to byť považované za *implicitné priemerovanie modelu*, pretože počas dropout trénujeme mierne odlišný model

> *Niektorí ľudia hovoria, že keď sa opitý človek snaží niečo naučiť, jeho mozog si to lepšie zapamätá nasledujúce ráno, v porovnaní s triezvym, pretože mozog s niektorými nefunkčnými neurónmi sa snaží lepšie prispôsobiť, aby pochopil význam. Sami sme nikdy netestovali, či je to pravda.*

## Prevencia pretrénovania

Jedným z veľmi dôležitých aspektov hlbokého učenia je schopnosť predchádzať [pretrénovaniu](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Aj keď môže byť lákavé použiť veľmi výkonný model neurónovej siete, vždy by sme mali vyvážiť počet parametrov modelu s počtom trénovacích vzoriek.

> Uistite sa, že rozumiete konceptu [pretrénovania](../../3-NeuralNetworks/05-Frameworks/Overfitting.md), ktorý sme predstavili skôr!

Existuje niekoľko spôsobov, ako predchádzať pretrénovaniu:

 * Predčasné ukončenie -- neustále monitorovať chybu na validačnej množine a zastaviť trénovanie, keď sa chyba na validácii začne zvyšovať.
 * Explicitný rozpad váh / regulácia -- pridať ďalšiu penalizáciu do stratovej funkcie za vysoké absolútne hodnoty váh, čo zabráni modelu prinášať veľmi nestabilné výsledky
 * Priemerovanie modelov -- trénovať niekoľko modelov a potom priemerovať výsledok. Pomáha to minimalizovať varianciu.
 * Dropout (Implicitné priemerovanie modelu)

## Optimalizátory / trénovacie algoritmy

Ďalším dôležitým aspektom trénovania je výber dobrého trénovacieho algoritmu. Kým klasický **gradientný zostup** je rozumnou voľbou, môže byť niekedy príliš pomalý alebo spôsobiť iné problémy.

V hlbokom učení používame **Stochastický gradientný zostup** (SGD), čo je gradientný zostup aplikovaný na minibatch-e, náhodne vybranom z trénovacej množiny. Váhy sa upravujú pomocou nasledujúceho vzorca:

w<sup>t+1</sup> = w<sup>t</sup> - &eta;&nabla;&lagran;

### Momentum

V **momentum SGD** si uchovávame časť gradientu z predchádzajúcich krokov. Je to podobné, ako keď sa pohybujeme s zotrvačnosťou a dostaneme úder v inom smere, naša trajektória sa nezmení okamžite, ale zachováva si časť pôvodného pohybu. Tu zavádzame ďalší vektor v na reprezentáciu *rýchlosti*:

* v<sup>t+1</sup> = &gamma; v<sup>t</sup> - &eta;&nabla;&lagran;
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Tu parameter &gamma; udáva mieru, do akej zohľadňujeme zotrvačnosť: &gamma;=0 zodpovedá klasickému SGD; &gamma;=1 je čistá rovnica pohybu.

### Adam, Adagrad a pod.

Keďže v každej vrstve násobíme signály nejakou maticou W<sub>i</sub>, v závislosti od ||W<sub>i</sub>|| môže gradient buď klesať a byť blízko nule, alebo rásť do nekonečna. To je podstata problému Explodujúcich/Miznúcich gradientov.

Jedným z riešení tohto problému je v rovnici používať iba smer gradientu a ignorovať jeho absolútnu hodnotu, t. j.

w<sup>t+1</sup> = w<sup>t</sup> - &eta;(&nabla;&lagran;/||&nabla;&lagran;||), kde ||&nabla;&lagran;|| = &radic;&sum;(&nabla;&lagran;)<sup>2</sup>

Tento algoritmus sa nazýva **Adagrad**. Ďalšie algoritmy používajúce rovnaký prístup sú: **RMSProp**, **Adam**

> **Adam** je považovaný za veľmi efektívny algoritmus v mnohých aplikáciách, takže ak si nie ste istí, ktorý použiť - použite Adam.

### Orezávanie gradientov

Orezávanie gradientov je rozšírením vyššie uvedenej myšlienky. Keď ||&nabla;&lagran;|| &le; &theta;, berieme pôvodný gradient pri optimalizácii váh, a keď ||&nabla;&lagran;|| > &theta; - gradient vydelíme jeho normou. Tu je &theta; parameter, v väčšine prípadov môžeme použiť &theta;=1 alebo &theta;=10.

### Zmenšovanie rýchlosti učenia

Úspech trénovania často závisí od parametra rýchlosti učenia &eta;. Je logické predpokladať, že väčšie hodnoty &eta; vedú k rýchlejšiemu trénovaniu, čo zvyčajne chceme na začiatku trénovania, a potom menšia hodnota &eta; nám umožní sieť jemne doladiť. Preto v väčšine prípadov chceme počas trénovania znižovať hodnotu &eta;.

To môžeme urobiť vynásobením &eta; nejakým číslom (napr. 0.98) po každej epoche trénovania, alebo použitím komplikovanejšieho **plánu zmenšovania rýchlosti učenia**.

## Rôzne architektúry sietí

Výber správnej architektúry siete pre váš problém môže byť zložitý. Zvyčajne si vyberieme architektúru, ktorá sa osvedčila pre našu konkrétnu úlohu (alebo podobnú). Tu je [dobrý prehľad](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) architektúr neurónových sietí pre počítačové videnie.

> Je dôležité vybrať architektúru, ktorá bude dosť výkonná pre počet trénovacích vzoriek, ktoré máme. Výber príliš výkonného modelu môže viesť k [pretrénovaniu](../../3-NeuralNetworks/05-Frameworks/Overfitting.md)

Ďalším dobrým spôsobom je použiť architektúru, ktorá sa automaticky prispôsobí požadovanej zložitosti. Do istej miery sú **ResNet** a **Inception** architektúry samozosvedčujúce. [Viac o architektúrach pre počítačové videnie](../07-ConvNets/CNN_Architectures.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->