<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5d1cbc67a9690adb5b33adf297794087",
  "translation_date": "2025-08-25T22:18:28+00:00",
  "source_file": "lessons/1-Intro/README.md",
  "language_code": "sk"
}
-->
> Obrázok od [Dmitry Soshnikov](http://soshnikov.com)

S postupom času sa výpočtové zdroje stali lacnejšími a dostupnosť dát sa zvýšila, čo umožnilo prístupom založeným na neurónových sieťach dosahovať vynikajúce výsledky v porovnaní s ľuďmi v mnohých oblastiach, ako je počítačové videnie alebo rozpoznávanie reči. V poslednom desaťročí sa pojem Umelá inteligencia často používa ako synonymum pre neurónové siete, pretože väčšina úspechov AI, o ktorých počujeme, je založená práve na nich.

Môžeme pozorovať, ako sa prístupy menili, napríklad pri vytváraní počítačového programu na hranie šachu:

* Skoré šachové programy boli založené na vyhľadávaní – program sa explicitne snažil odhadnúť možné ťahy súpera na niekoľko nasledujúcich ťahov a vybral optimálny ťah na základe najlepšej pozície, ktorú bolo možné dosiahnuť v niekoľkých ťahoch. To viedlo k vývoju tzv. [alpha-beta prerezávacieho](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) vyhľadávacieho algoritmu.
* Vyhľadávacie stratégie fungujú dobre na konci hry, kde je vyhľadávací priestor obmedzený malým počtom možných ťahov. Na začiatku hry je však vyhľadávací priestor obrovský a algoritmus sa dá zlepšiť učením z existujúcich zápasov medzi ľudskými hráčmi. Následné experimenty využívali tzv. [prístup založený na prípadoch](https://en.wikipedia.org/wiki/Case-based_reasoning), kde program hľadal prípady v databáze znalostí, ktoré sú veľmi podobné aktuálnej pozícii v hre.
* Moderné programy, ktoré porážajú ľudských hráčov, sú založené na neurónových sieťach a [posilňovacom učení](https://en.wikipedia.org/wiki/Reinforcement_learning), kde sa programy učia hrať výlučne tým, že dlhodobo hrajú proti sebe a učia sa zo svojich vlastných chýb – podobne ako ľudia, keď sa učia hrať šach. Počítačový program však môže odohrať oveľa viac hier za oveľa kratší čas, a tak sa môže učiť oveľa rýchlejšie.

✅ Urobte si malý prieskum o iných hrách, ktoré boli hrané AI.

Podobne môžeme vidieť, ako sa menil prístup k vytváraniu „hovoriacich programov“ (ktoré by mohli prejsť Turingovým testom):

* Skoré programy tohto druhu, ako napríklad [Eliza](https://en.wikipedia.org/wiki/ELIZA), boli založené na veľmi jednoduchých gramatických pravidlách a preformulovaní vstupnej vety na otázku.
* Moderní asistenti, ako Cortana, Siri alebo Google Assistant, sú všetko hybridné systémy, ktoré používajú neurónové siete na prevod reči na text a rozpoznanie nášho zámeru, a potom využívajú nejaké logické uvažovanie alebo explicitné algoritmy na vykonanie požadovaných akcií.
* V budúcnosti môžeme očakávať úplný model založený na neurónových sieťach, ktorý bude schopný samostatne spracovať dialóg. Nedávne GPT a [Turing-NLG](https://turing.microsoft.com/) rodiny neurónových sietí ukazujú v tomto smere veľký úspech.

> Obrázok od Dmitry Soshnikov, [fotografia](https://unsplash.com/photos/r8LmVbUKgns) od [Marina Abrosimova](https://unsplash.com/@abrosimova_marina_foto), Unsplash

## Nedávny výskum v oblasti AI

Obrovský nárast výskumu neurónových sietí začal okolo roku 2010, keď sa začali sprístupňovať veľké verejné dátové súbory. Obrovská zbierka obrázkov nazvaná [ImageNet](https://en.wikipedia.org/wiki/ImageNet), ktorá obsahuje približne 14 miliónov anotovaných obrázkov, dala vzniknúť [ImageNet Large Scale Visual Recognition Challenge](https://image-net.org/challenges/LSVRC/).

![Presnosť ILSVRC](../../../../lessons/1-Intro/images/ilsvrc.gif)

> Obrázok od [Dmitry Soshnikov](http://soshnikov.com)

V roku 2012 boli [Konvolučné neurónové siete](../4-ComputerVision/07-ConvNets/README.md) prvýkrát použité na klasifikáciu obrázkov, čo viedlo k výraznému poklesu chybovosti klasifikácie (z takmer 30 % na 16,4 %). V roku 2015 architektúra ResNet od Microsoft Research [dosiahla presnosť na úrovni človeka](https://doi.org/10.1109/ICCV.2015.123).

Odvtedy neurónové siete preukázali veľmi úspešné správanie v mnohých úlohách:

---

Rok | Dosiahnutá úroveň človeka
-----|--------
2015 | [Klasifikácia obrázkov](https://doi.org/10.1109/ICCV.2015.123)
2016 | [Rozpoznávanie konverzačnej reči](https://arxiv.org/abs/1610.05256)
2018 | [Automatický preklad](https://arxiv.org/abs/1803.05567) (z čínštiny do angličtiny)
2020 | [Popisovanie obrázkov](https://arxiv.org/abs/2009.13682)

V posledných rokoch sme boli svedkami obrovských úspechov veľkých jazykových modelov, ako sú BERT a GPT-3. Toto sa stalo najmä vďaka tomu, že je dostupné veľké množstvo všeobecných textových dát, ktoré umožňujú trénovať modely na zachytenie štruktúry a významu textov, predtrénovať ich na všeobecných textových zbierkach a následne špecializovať tieto modely na konkrétnejšie úlohy. Viac sa o [Spracovaní prirodzeného jazyka](../5-NLP/README.md) dozvieme neskôr v tomto kurze.

## 🚀 Výzva

Preskúmajte internet a určte, kde je podľa vás AI najefektívnejšie využívaná. Je to v aplikácii na mapovanie, v službe na prevod reči na text alebo vo videohre? Preskúmajte, ako bol systém vytvorený.

## [Kvíz po prednáške](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/201)

## Prehľad & Samoštúdium

Preskúmajte históriu AI a ML prečítaním [tejto lekcie](https://github.com/microsoft/ML-For-Beginners/tree/main/1-Introduction/2-history-of-ML). Vyberte si prvok zo sketchnote na začiatku tejto lekcie alebo tejto a preskúmajte ho podrobnejšie, aby ste pochopili kultúrny kontext, ktorý ovplyvnil jeho vývoj.

**Úloha**: [Game Jam](assignment.md)

**Upozornenie**:  
Tento dokument bol preložený pomocou služby na automatický preklad [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.