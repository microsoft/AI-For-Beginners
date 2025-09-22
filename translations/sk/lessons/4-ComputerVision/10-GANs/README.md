<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-25T22:39:12+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "sk"
}
-->
# Generatívne adversariálne siete

V predchádzajúcej časti sme sa naučili o **generatívnych modeloch**: modeloch, ktoré dokážu generovať nové obrázky podobné tým v tréningovej množine. VAE bol dobrým príkladom generatívneho modelu.

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/19)

Ak sa však pokúsime generovať niečo naozaj zmysluplné, napríklad maľbu v rozumnej kvalite, pomocou VAE, zistíme, že tréning sa nekonverguje dobre. Pre tento prípad použitia by sme sa mali naučiť o inej architektúre špecificky zameranej na generatívne modely - **Generatívne adversariálne siete**, alebo GANy.

Hlavná myšlienka GANov spočíva v tom, že máme dve neurónové siete, ktoré sa budú trénovať proti sebe:

<img src="images/gan_architecture.png" width="70%"/>

> Obrázok od [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Malý slovník:
> * **Generátor** je sieť, ktorá prijíma náhodný vektor a ako výsledok produkuje obrázok.
> * **Diskriminátor** je sieť, ktorá prijíma obrázok a mala by určiť, či ide o skutočný obrázok (z tréningovej množiny), alebo či bol vygenerovaný generátorom. V podstate ide o klasifikátor obrázkov.

### Diskriminátor

Architektúra diskriminátora sa nelíši od bežnej siete na klasifikáciu obrázkov. V najjednoduchšom prípade môže ísť o plne prepojený klasifikátor, ale pravdepodobne to bude [konvolučná sieť](../07-ConvNets/README.md).

> ✅ GAN založený na konvolučných sieťach sa nazýva [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Diskriminátor CNN pozostáva z nasledujúcich vrstiev: niekoľko konvolúcií + poolingov (s klesajúcou priestorovou veľkosťou) a jednej alebo viacerých plne prepojených vrstiev na získanie "vektorov vlastností", a nakoniec binárneho klasifikátora.

> ✅ 'Pooling' v tomto kontexte je technika, ktorá zmenšuje veľkosť obrázka. "Poolingové vrstvy znižujú rozmery dát kombinovaním výstupov klastrov neurónov v jednej vrstve do jedného neurónu v nasledujúcej vrstve." - [zdroj](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generátor

Generátor je o niečo zložitejší. Môžete si ho predstaviť ako obrátený diskriminátor. Začína sa latentným vektorom (namiesto vektora vlastností), ktorý má plne prepojenú vrstvu na jeho konverziu do požadovanej veľkosti/tvaru, nasledovanú dekonvolúciami + zväčšovaním. Toto je podobné *dekodéru* v [autoenkóderi](../09-Autoencoders/README.md).

> ✅ Pretože konvolučná vrstva je implementovaná ako lineárny filter prechádzajúci obrázkom, dekonvolúcia je v podstate podobná konvolúcii a môže byť implementovaná pomocou rovnakej logiky vrstvy.

<img src="images/gan_arch_detail.png" width="70%"/>

> Obrázok od [Dmitry Soshnikov](http://soshnikov.com)

### Tréning GANov

GANy sa nazývajú **adversariálne**, pretože medzi generátorom a diskriminátorom prebieha neustála súťaž. Počas tejto súťaže sa obidva modely zlepšujú, čím sa sieť učí vytvárať stále lepšie obrázky.

Tréning prebieha v dvoch fázach:

* **Tréning diskriminátora**. Táto úloha je pomerne jednoduchá: vygenerujeme dávku obrázkov pomocou generátora, označíme ich ako 0, čo znamená falošný obrázok, a vezmeme dávku obrázkov z tréningovej množiny (s označením 1, skutočný obrázok). Získame nejakú *stratu diskriminátora* a vykonáme spätné šírenie.
* **Tréning generátora**. Toto je o niečo zložitejšie, pretože nepoznáme očakávaný výstup generátora priamo. Vezmeme celú GAN sieť pozostávajúcu z generátora nasledovaného diskriminátorom, nakŕmime ju náhodnými vektormi a očakávame, že výsledok bude 1 (zodpovedajúci skutočným obrázkom). Potom zmrazíme parametre diskriminátora (nechceme, aby sa v tomto kroku trénoval) a vykonáme spätné šírenie.

Počas tohto procesu straty generátora a diskriminátora významne neklesajú. V ideálnom prípade by mali oscilovať, čo zodpovedá zlepšovaniu výkonu oboch sietí.

## ✍️ Cvičenia: GANy

* [GAN Notebook v TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [GAN Notebook v PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Problémy s tréningom GANov

GANy sú známe tým, že sú obzvlášť náročné na tréning. Tu je niekoľko problémov:

* **Kolaps módu**. Tento termín znamená, že generátor sa naučí vytvárať jeden úspešný obrázok, ktorý oklame diskriminátor, a nie rôzne obrázky.
* **Citlivosť na hyperparametre**. Často sa stáva, že GAN nekonverguje vôbec, a potom náhle zníženie rýchlosti učenia vedie ku konvergencii.
* Udržiavanie **rovnováhy** medzi generátorom a diskriminátorom. V mnohých prípadoch môže strata diskriminátora klesnúť na nulu pomerne rýchlo, čo spôsobí, že generátor už nebude schopný ďalej trénovať. Na prekonanie tohto problému môžeme skúsiť nastaviť rôzne rýchlosti učenia pre generátor a diskriminátor, alebo preskočiť tréning diskriminátora, ak je strata už príliš nízka.
* Tréning pre **vysoké rozlíšenie**. Tento problém, podobne ako pri autoenkóderoch, vzniká, pretože rekonštrukcia príliš mnohých vrstiev konvolučnej siete vedie k artefaktom. Tento problém sa zvyčajne rieši tzv. **progresívnym rastom**, keď sa najprv niekoľko vrstiev trénuje na obrázkoch s nízkym rozlíšením, a potom sa vrstvy "odomknú" alebo pridajú. Ďalším riešením by bolo pridanie extra spojení medzi vrstvami a tréning viacerých rozlíšení naraz - podrobnosti nájdete v tomto [Multi-Scale Gradient GANs článku](https://arxiv.org/abs/1903.06048).

## Prenos štýlu

GANy sú skvelým spôsobom, ako generovať umelecké obrázky. Ďalšou zaujímavou technikou je tzv. **prenos štýlu**, ktorý vezme jeden **obsahový obrázok** a prekreslí ho v inom štýle, aplikujúc filtre zo **štýlového obrázka**.

Ako to funguje:
* Začneme s náhodným šumovým obrázkom (alebo s obsahovým obrázkom, ale pre pochopenie je jednoduchšie začať s náhodným šumom).
* Naším cieľom bude vytvoriť taký obrázok, ktorý bude blízky obsahovému obrázku aj štýlovému obrázku. To sa určí pomocou dvoch funkcií straty:
   - **Strata obsahu** sa vypočíta na základe vlastností extrahovaných CNN na niektorých vrstvách z aktuálneho obrázka a obsahového obrázka.
   - **Strata štýlu** sa vypočíta medzi aktuálnym obrázkom a štýlovým obrázkom šikovným spôsobom pomocou Gramových matíc (viac podrobností v [príkladovom notebooku](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)).
* Na vyhladenie obrázka a odstránenie šumu zavádzame aj **stratu variácie**, ktorá počíta priemernú vzdialenosť medzi susednými pixelmi.
* Hlavná optimalizačná slučka upravuje aktuálny obrázok pomocou gradientného zostupu (alebo iného optimalizačného algoritmu) na minimalizáciu celkovej straty, ktorá je váženým súčtom všetkých troch strát.

## ✍️ Príklad: [Prenos štýlu](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/20)

## Zhrnutie

V tejto lekcii ste sa naučili o GANoch a ako ich trénovať. Tiež ste sa dozvedeli o špeciálnych výzvach, ktorým tento typ neurónových sietí čelí, a o niektorých stratégiách, ako ich prekonať.

## 🚀 Výzva

Prejdite si [notebook o prenose štýlu](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) s použitím vlastných obrázkov.

## Prehľad a samoštúdium

Pre referenciu si prečítajte viac o GANoch v týchto zdrojoch:

* Marco Pasini, [10 lekcií, ktoré som sa naučil pri tréningu GANov za jeden rok](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), *de facto* architektúra GANov na zváženie
* [Vytváranie generatívneho umenia pomocou GANov na Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Zadanie

Znovu si prejdite jeden z dvoch notebookov spojených s touto lekciou a pretrénujte GAN na vlastných obrázkoch. Čo dokážete vytvoriť?

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.