# Predtrénované siete a transferové učenie

Trénovanie CNN môže zabrať veľa času a vyžaduje si veľké množstvo dát. Avšak veľká časť času sa venuje učeniu najlepších nízkoúrovňových filtrov, ktoré sieť môže použiť na extrahovanie vzorov z obrázkov. Prirodzene sa vynára otázka - môžeme použiť neurónovú sieť trénovanú na jednom datasete a prispôsobiť ju na klasifikáciu iných obrázkov bez potreby kompletného procesu trénovania?

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/15)

Tento prístup sa nazýva **transferové učenie**, pretože prenášame určitú znalosť z jedného modelu neurónovej siete na druhý. Pri transferovom učení zvyčajne začíname s predtrénovaným modelom, ktorý bol trénovaný na veľkom datasete obrázkov, ako je napríklad **ImageNet**. Tieto modely už dokážu dobre extrahovať rôzne črty z generických obrázkov, a v mnohých prípadoch stačí postaviť klasifikátor na vrchole týchto extrahovaných čŕt, aby sme dosiahli dobrý výsledok.

> ✅ Transferové učenie je termín, ktorý nájdete aj v iných akademických oblastiach, ako je vzdelávanie. Označuje proces prenášania znalostí z jednej oblasti do druhej.

## Predtrénované modely ako extraktory čŕt

Konvolučné siete, o ktorých sme hovorili v predchádzajúcej sekcii, obsahovali množstvo vrstiev, z ktorých každá mala za úlohu extrahovať určité črty z obrázku, od nízkoúrovňových kombinácií pixelov (ako horizontálna/vertikálna línia alebo ťah) až po vyššie úrovne kombinácií čŕt, ktoré zodpovedajú veciam ako oko alebo plameň. Ak trénujeme CNN na dostatočne veľkom datasete generických a rôznorodých obrázkov, sieť by sa mala naučiť extrahovať tieto spoločné črty.

Keras aj PyTorch obsahujú funkcie na jednoduché načítanie predtrénovaných váh neurónových sietí pre niektoré bežné architektúry, z ktorých väčšina bola trénovaná na obrázkoch z ImageNet. Najčastejšie používané sú popísané na stránke [Architektúry CNN](../07-ConvNets/CNN_Architectures.md) z predchádzajúcej lekcie. Konkrétne môžete zvážiť použitie jednej z nasledujúcich:

* **VGG-16/VGG-19**, ktoré sú relatívne jednoduché modely, ale stále poskytujú dobrú presnosť. Použitie VGG ako prvý pokus je často dobrá voľba na zistenie, ako transferové učenie funguje.
* **ResNet** je rodina modelov navrhnutých Microsoft Research v roku 2015. Majú viac vrstiev, a teda vyžadujú viac zdrojov.
* **MobileNet** je rodina modelov so zmenšenou veľkosťou, vhodná pre mobilné zariadenia. Použite ich, ak máte obmedzené zdroje a môžete obetovať trochu presnosti.

Tu sú ukážkové črty extrahované z obrázku mačky pomocou siete VGG-16:

![Črty extrahované VGG-16](../../../../../translated_images/sk/features.6291f9c7ba3a0b95.webp)

## Dataset Mačky vs. Psy

V tomto príklade použijeme dataset [Mačky a Psy](https://www.microsoft.com/download/details.aspx?id=54765&WT.mc_id=academic-77998-cacaste), ktorý je veľmi blízky reálnemu scenáru klasifikácie obrázkov.

## ✍️ Cvičenie: Transferové učenie

Pozrime sa na transferové učenie v praxi v príslušných notebookoch:

* [Transferové učenie - PyTorch](TransferLearningPyTorch.ipynb)
* [Transferové učenie - TensorFlow](TransferLearningTF.ipynb)

## Vizualizácia ideálnej mačky

Predtrénovaná neurónová sieť obsahuje rôzne vzory vo svojej *pamäti*, vrátane predstáv o **ideálnej mačke** (ako aj ideálnom psovi, ideálnej zebre, atď.). Bolo by zaujímavé nejako **vizualizovať tento obrázok**. Avšak nie je to jednoduché, pretože vzory sú rozptýlené po celých váhach siete a tiež organizované v hierarchickej štruktúre.

Jeden prístup, ktorý môžeme použiť, je začať s náhodným obrázkom a potom sa pokúsiť použiť techniku **optimalizácie pomocou gradientného zostupu**, aby sme upravili tento obrázok tak, že sieť začne myslieť, že je to mačka.

![Optimalizačný cyklus obrázku](../../../../../translated_images/sk/ideal-cat-loop.999fbb8ff306e044.webp)

Ak to však urobíme, dostaneme niečo veľmi podobné náhodnému šumu. Je to preto, že *existuje mnoho spôsobov, ako presvedčiť sieť, že vstupný obrázok je mačka*, vrátane niektorých, ktoré vizuálne nedávajú zmysel. Hoci tieto obrázky obsahujú veľa vzorov typických pre mačku, nič ich neobmedzuje, aby boli vizuálne zreteľné.

Na zlepšenie výsledku môžeme do funkcie straty pridať ďalší člen, ktorý sa nazýva **variácia straty**. Je to metrika, ktorá ukazuje, ako podobné sú susedné pixely obrázku. Minimalizácia variácie straty robí obrázok hladším a zbavuje sa šumu - čím odhaľuje vizuálne príťažlivejšie vzory. Tu je príklad takýchto "ideálnych" obrázkov, ktoré sú klasifikované ako mačka a zebra s vysokou pravdepodobnosťou:

![Ideálna mačka](../../../../../translated_images/sk/ideal-cat.203dd4597643d6b0.webp) | ![Ideálna zebra](../../../../../translated_images/sk/ideal-zebra.7f70e8b54ee15a7a.webp)
-----|-----
 *Ideálna mačka* | *Ideálna zebra*

Podobný prístup môže byť použitý na vykonanie tzv. **adversariálnych útokov** na neurónovú sieť. Predpokladajme, že chceme oklamať neurónovú sieť a urobiť z psa mačku. Ak vezmeme obrázok psa, ktorý je sieťou rozpoznaný ako pes, môžeme ho trochu upraviť pomocou optimalizácie gradientného zostupu, až kým sieť nezačne klasifikovať obrázok ako mačku:

![Obrázok psa](../../../../../translated_images/sk/original-dog.8f68a67d2fe0911f.webp) | ![Obrázok psa klasifikovaný ako mačka](../../../../../translated_images/sk/adversarial-dog.d9fc7773b0142b89.webp)
-----|-----
*Pôvodný obrázok psa* | *Obrázok psa klasifikovaný ako mačka*

Pozrite si kód na reprodukciu vyššie uvedených výsledkov v nasledujúcom notebooku:

* [Ideálna a adversariálna mačka - TensorFlow](AdversarialCat_TF.ipynb)

## Záver

Pomocou transferového učenia môžete rýchlo zostaviť klasifikátor pre úlohu klasifikácie vlastných objektov a dosiahnuť vysokú presnosť. Vidíte, že zložitejšie úlohy, ktoré teraz riešime, vyžadujú vyšší výpočtový výkon a nemôžu byť ľahko vyriešené na CPU. V ďalšej jednotke sa pokúsime použiť ľahšiu implementáciu na trénovanie rovnakého modelu s nižšími výpočtovými zdrojmi, čo vedie len k mierne nižšej presnosti.

## 🚀 Výzva

V sprievodných notebookoch sú poznámky na konci o tom, ako transferové učenie najlepšie funguje s podobnými trénovacími dátami (napríklad nový typ zvieraťa). Urobte experimenty s úplne novými typmi obrázkov, aby ste zistili, ako dobre alebo zle vaše modely transferového učenia fungujú.

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Prehľad a samostatné štúdium

Prečítajte si [TrainingTricks.md](TrainingTricks.md), aby ste si prehĺbili znalosti o ďalších spôsoboch trénovania modelov.

## [Úloha](lab/README.md)

V tomto laboratóriu použijeme reálny dataset [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) domácich miláčikov s 35 plemenami mačiek a psov a vytvoríme klasifikátor pomocou transferového učenia.

---

