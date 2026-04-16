# Triky pri tréningu hlbokého učenia

Ako sa neurónové siete stávajú hlbšími, proces ich tréningu sa stáva čoraz náročnejším. Jedným z hlavných problémov sú takzvané [miznúce gradienty](https://en.wikipedia.org/wiki/Vanishing_gradient_problem) alebo [explodujúce gradienty](https://deepai.org/machine-learning-glossary-and-terms/exploding-gradient-problem#:~:text=Exploding%20gradients%20are%20a%20problem,updates%20are%20small%20and%20controlled.). [Tento článok](https://towardsdatascience.com/the-vanishing-exploding-gradient-problem-in-deep-neural-networks-191358470c11) poskytuje dobrý úvod do týchto problémov.

Na zefektívnenie tréningu hlbokých sietí existuje niekoľko techník, ktoré môžeme použiť.

## Udržiavanie hodnôt v rozumnom intervale

Aby boli numerické výpočty stabilnejšie, chceme zabezpečiť, že všetky hodnoty v našej neurónovej sieti budú v rozumnom rozsahu, typicky [-1..1] alebo [0..1]. Nie je to veľmi prísna požiadavka, ale povaha výpočtov s pohyblivou desatinnou čiarkou je taká, že hodnoty rôznych veľkostí sa nedajú presne manipulovať spolu. Napríklad, ak sčítame 10<sup>-10</sup> a 10<sup>10</sup>, pravdepodobne dostaneme 10<sup>10</sup>, pretože menšia hodnota bude „konvertovaná“ na rovnaký rád ako väčšia, a tým sa stratí mantisa.

Väčšina aktivačných funkcií má nelinearity okolo [-1..1], a preto má zmysel škálovať všetky vstupné dáta do intervalu [-1..1] alebo [0..1].

## Inicializácia počiatočných váh

Ideálne chceme, aby hodnoty zostali v rovnakom rozsahu po prechode cez vrstvy siete. Preto je dôležité inicializovať váhy tak, aby sa zachovala distribúcia hodnôt.

Normálne rozdelenie **N(0,1)** nie je dobrý nápad, pretože ak máme *n* vstupov, štandardná odchýlka výstupu bude *n*, a hodnoty pravdepodobne vyskočia z intervalu [0..1].

Nasledujúce inicializácie sa často používajú:

 * Rovnomerné rozdelenie -- `uniform`
 * **N(0,1/n)** -- `gaussian`
 * **N(0,1/√n_in)** zaručuje, že pre vstupy s nulovým priemerom a štandardnou odchýlkou 1 zostane rovnaký priemer/štandardná odchýlka
 * **N(0,√2/(n_in+n_out))** -- takzvaná **Xavierova inicializácia** (`glorot`), pomáha udržiavať signály v rozsahu počas predného aj spätného šírenia

## Batch Normalization

Aj pri správnej inicializácii váh sa môžu váhy počas tréningu stať ľubovoľne veľkými alebo malými, čo spôsobí, že signály vyjdú z správneho rozsahu. Signály môžeme vrátiť späť pomocou jednej z techník **normalizácie**. Aj keď existuje niekoľko z nich (normalizácia váh, normalizácia vrstiev), najčastejšie používaná je Batch Normalization.

Myšlienka **batch normalizácie** je zohľadniť všetky hodnoty v rámci minibatchu a vykonať normalizáciu (t.j. odpočítať priemer a vydeliť štandardnou odchýlkou) na základe týchto hodnôt. Implementuje sa ako vrstva siete, ktorá vykonáva túto normalizáciu po aplikovaní váh, ale pred aktivačnou funkciou. Výsledkom je pravdepodobne vyššia konečná presnosť a rýchlejší tréning.

Tu je [pôvodný článok](https://arxiv.org/pdf/1502.03167.pdf) o batch normalizácii, [vysvetlenie na Wikipédii](https://en.wikipedia.org/wiki/Batch_normalization), a [dobrý úvodný blogový príspevok](https://towardsdatascience.com/batch-normalization-in-3-levels-of-understanding-14c2da90a338) (a jeden [v ruštine](https://habrahabr.ru/post/309302/)).

## Dropout

**Dropout** je zaujímavá technika, ktorá počas tréningu odstraňuje určitý percentuálny podiel náhodných neurónov. Implementuje sa tiež ako vrstva s jedným parametrom (percento neurónov na odstránenie, typicky 10%-50%), a počas tréningu nuluje náhodné prvky vstupného vektora pred ich odoslaním do ďalšej vrstvy.

Aj keď to môže znieť ako zvláštny nápad, môžete vidieť efekt dropout na tréningu klasifikátora číslic MNIST v notebooku [`Dropout.ipynb`](../../../../../lessons/4-ComputerVision/08-TransferLearning/Dropout.ipynb). Urýchľuje tréning a umožňuje dosiahnuť vyššiu presnosť v menšom počte tréningových epoch.

Tento efekt možno vysvetliť niekoľkými spôsobmi:

 * Môže byť považovaný za náhodný šokový faktor pre model, ktorý ho vyvedie z lokálneho minima
 * Môže byť považovaný za *implicitné priemerovanie modelu*, pretože môžeme povedať, že počas dropout trénujeme mierne odlišný model

> *Niektorí ľudia hovoria, že keď sa opitý človek snaží niečo naučiť, zapamätá si to lepšie nasledujúce ráno v porovnaní s triezvym človekom, pretože mozog s niektorými nefunkčnými neurónmi sa snaží lepšie prispôsobiť, aby pochopil význam. Nikdy sme sami netestovali, či je to pravda alebo nie.*

## Prevencia overfittingu

Jedným z veľmi dôležitých aspektov hlbokého učenia je schopnosť predchádzať [overfittingu](../../3-NeuralNetworks/05-Frameworks/Overfitting.md). Aj keď môže byť lákavé použiť veľmi výkonný model neurónovej siete, vždy by sme mali vyvážiť počet parametrov modelu s počtom tréningových vzoriek.

> Uistite sa, že rozumiete konceptu [overfittingu](../../3-NeuralNetworks/05-Frameworks/Overfitting.md), ktorý sme predstavili skôr!

Existuje niekoľko spôsobov, ako predchádzať overfittingu:

 * Skoré zastavenie -- neustále monitorovanie chyby na validačnej množine a zastavenie tréningu, keď sa validačná chyba začne zvyšovať.
 * Explicitný úbytok váh / Regularizácia -- pridanie dodatočného trestu do funkcie straty za vysoké absolútne hodnoty váh, čo zabraňuje modelu dosahovať veľmi nestabilné výsledky
 * Priemerovanie modelu -- tréning niekoľkých modelov a následné priemerovanie výsledkov. To pomáha minimalizovať varianciu.
 * Dropout (Implicitné priemerovanie modelu)

## Optimalizátory / Tréningové algoritmy

Ďalším dôležitým aspektom tréningu je výber dobrého tréningového algoritmu. Aj keď je klasický **gradient descent** rozumnou voľbou, môže byť niekedy príliš pomalý alebo spôsobiť iné problémy.

V hlbokom učení používame **Stochastic Gradient Descent** (SGD), čo je gradient descent aplikovaný na minibatch, náhodne vybraný z tréningovej množiny. Váhy sa upravujú pomocou tejto rovnice:

w<sup>t+1</sup> = w<sup>t</sup> - η∇ℒ

### Momentum

V **momentum SGD** uchovávame časť gradientu z predchádzajúcich krokov. Je to podobné ako keď sa pohybujeme niekam s hybnosťou, a dostaneme úder iným smerom, naša trajektória sa nezmení okamžite, ale zachová si časť pôvodného pohybu. Tu zavádzame ďalší vektor v na reprezentáciu *rýchlosti*:

* v<sup>t+1</sup> = γ v<sup>t</sup> - η∇ℒ
* w<sup>t+1</sup> = w<sup>t</sup>+v<sup>t+1</sup>

Tu parameter γ označuje rozsah, do akého berieme hybnosť do úvahy: γ=0 zodpovedá klasickému SGD; γ=1 je čistá pohybová rovnica.

### Adam, Adagrad, atď.

Keď v každej vrstve násobíme signály nejakou maticou W<sub>i</sub>, v závislosti od ||W<sub>i</sub>|| môže gradient buď miznúť a byť blízko 0, alebo rásť neobmedzene. Toto je podstata problému Explodujúcich/Miznúcich Gradientov.

Jedným z riešení tohto problému je použiť v rovnici iba smer gradientu a ignorovať absolútnu hodnotu, t.j.

w<sup>t+1</sup> = w<sup>t</sup> - η(∇ℒ/||∇ℒ||), kde ||∇ℒ|| = √∑(∇ℒ)<sup>2</sup>

Tento algoritmus sa nazýva **Adagrad**. Ďalšie algoritmy, ktoré používajú rovnakú myšlienku: **RMSProp**, **Adam**

> **Adam** je považovaný za veľmi efektívny algoritmus pre mnohé aplikácie, takže ak si nie ste istí, ktorý použiť - použite Adam.

### Gradient clipping

Gradient clipping je rozšírenie vyššie uvedenej myšlienky. Keď ||∇ℒ|| ≤ θ, berieme do úvahy pôvodný gradient pri optimalizácii váh, a keď ||∇ℒ|| > θ - delíme gradient jeho normou. Tu θ je parameter, vo väčšine prípadov môžeme zvoliť θ=1 alebo θ=10.

### Learning rate decay

Úspech tréningu často závisí od parametra learning rate η. Je logické predpokladať, že väčšie hodnoty η vedú k rýchlejšiemu tréningu, čo je niečo, čo typicky chceme na začiatku tréningu, a potom menšie hodnoty η umožňujú jemné doladenie siete. Preto vo väčšine prípadov chceme znižovať η počas tréningu.

To sa dá dosiahnuť násobením η nejakým číslom (napr. 0.98) po každej epoche tréningu, alebo použitím zložitejšieho **rozvrhu learning rate**.

## Rôzne architektúry sietí

Výber správnej architektúry siete pre váš problém môže byť zložitý. Normálne by sme si vybrali architektúru, ktorá sa osvedčila pre našu konkrétnu úlohu (alebo podobnú). Tu je [dobrý prehľad](https://www.topbots.com/a-brief-history-of-neural-network-architectures/) architektúr neurónových sietí pre počítačové videnie.

> Je dôležité vybrať architektúru, ktorá bude dostatočne výkonná pre počet tréningových vzoriek, ktoré máme. Výber príliš výkonného modelu môže viesť k [overfittingu](../../3-NeuralNetworks/05-Frameworks/Overfitting.md).

Ďalším dobrým spôsobom by bolo použiť architektúru, ktorá sa automaticky prispôsobí požadovanej zložitosti. Do určitej miery sú architektúry **ResNet** a **Inception** samo-prispôsobivé. [Viac o architektúrach pre počítačové videnie](../07-ConvNets/CNN_Architectures.md).

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.