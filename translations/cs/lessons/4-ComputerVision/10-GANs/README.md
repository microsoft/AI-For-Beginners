<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-25T22:38:46+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "cs"
}
-->
# Generativní adversariální sítě

V předchozí části jsme se naučili o **generativních modelech**: modelech, které dokážou generovat nové obrázky podobné těm v trénovacím datasetu. VAE byl dobrým příkladem generativního modelu.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/110)

Nicméně, pokud se pokusíme generovat něco opravdu smysluplného, například malbu v rozumném rozlišení, pomocí VAE, zjistíme, že trénování neprobíhá dobře. Pro tento případ bychom se měli naučit o jiné architektuře, která je specificky zaměřená na generativní modely - **Generativní adversariální sítě**, neboli GANs.

Hlavní myšlenkou GAN je mít dvě neuronové sítě, které se budou trénovat proti sobě:

<img src="images/gan_architecture.png" width="70%"/>

> Obrázek od [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Malý slovníček:
> * **Generátor** je síť, která vezme nějaký náhodný vektor a jako výsledek vytvoří obrázek.
> * **Diskriminátor** je síť, která vezme obrázek a měla by určit, zda se jedná o skutečný obrázek (z trénovacího datasetu), nebo zda byl vytvořen generátorem. V podstatě jde o klasifikátor obrázků.

### Diskriminátor

Architektura diskriminátoru se neliší od běžné klasifikační sítě pro obrázky. V nejjednodušším případě může být plně propojeným klasifikátorem, ale pravděpodobněji půjde o [konvoluční síť](../07-ConvNets/README.md).

> ✅ GAN založený na konvolučních sítích se nazývá [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)

Diskriminátor CNN se skládá z následujících vrstev: několik konvolucí+poolingů (s klesající prostorovou velikostí) a jedné nebo více plně propojených vrstev pro získání "vektorů vlastností", konečný binární klasifikátor.

> ✅ 'Pooling' v tomto kontextu je technika, která zmenšuje velikost obrázku. "Poolingové vrstvy snižují rozměry dat kombinováním výstupů neuronových clusterů na jedné vrstvě do jednoho neuronu na další vrstvě." - [zdroj](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generátor

Generátor je o něco složitější. Můžete si ho představit jako obrácený diskriminátor. Začíná latentním vektorem (namísto vektoru vlastností), má plně propojenou vrstvu, která ho převede na požadovanou velikost/tvar, následovanou dekonvolucemi+zvětšováním. To je podobné *dekodéru* části [autoenkodéru](../09-Autoencoders/README.md).

> ✅ Protože konvoluční vrstva je implementována jako lineární filtr procházející obrázkem, dekonvoluce je v podstatě podobná konvoluci a může být implementována pomocí stejné logiky vrstvy.

<img src="images/gan_arch_detail.png" width="70%"/>

> Obrázek od [Dmitry Soshnikov](http://soshnikov.com)

### Trénování GAN

GANs se nazývají **adversariální**, protože mezi generátorem a diskriminátorem probíhá neustálá soutěž. Během této soutěže se oba generátor i diskriminátor zlepšují, takže síť se učí vytvářet stále lepší obrázky.

Trénování probíhá ve dvou fázích:

* **Trénování diskriminátoru**. Tento úkol je poměrně přímočarý: generujeme dávku obrázků pomocí generátoru, označíme je 0, což znamená falešný obrázek, a vezmeme dávku obrázků z vstupního datasetu (s označením 1, skutečný obrázek). Získáme nějakou *ztrátu diskriminátoru* a provedeme zpětné šíření.
* **Trénování generátoru**. To je o něco složitější, protože neznáme očekávaný výstup generátoru přímo. Vezmeme celou GAN síť skládající se z generátoru následovaného diskriminátorem, nakrmíme ji nějakými náhodnými vektory a očekáváme výsledek 1 (odpovídající skutečným obrázkům). Poté zmrazíme parametry diskriminátoru (nechceme, aby se v tomto kroku trénoval) a provedeme zpětné šíření.

Během tohoto procesu ztráty generátoru i diskriminátoru neklesají výrazně. V ideální situaci by měly oscilovat, což odpovídá zlepšování výkonu obou sítí.

## ✍️ Cvičení: GANs

* [GAN Notebook v TensorFlow/Keras](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [GAN Notebook v PyTorch](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Problémy s trénováním GAN

GANs jsou známé tím, že jsou obzvláště obtížné na trénování. Zde je několik problémů:

* **Kolaps módu**. Tento termín znamená, že generátor se naučí vytvářet jeden úspěšný obrázek, který oklame diskriminátor, a ne různé obrázky.
* **Citlivost na hyperparametry**. Často můžete vidět, že GAN vůbec nekonverguje, a pak náhle snížení rychlosti učení vede ke konvergenci.
* Udržení **rovnováhy** mezi generátorem a diskriminátorem. V mnoha případech může ztráta diskriminátoru relativně rychle klesnout na nulu, což vede k tomu, že generátor už nemůže dále trénovat. Abychom tomu předešli, můžeme zkusit nastavit různé rychlosti učení pro generátor a diskriminátor nebo přeskočit trénování diskriminátoru, pokud je ztráta již příliš nízká.
* Trénování na **vysoké rozlišení**. Tento problém odráží stejný problém jako u autoenkodérů, který je vyvolán tím, že rekonstrukce příliš mnoha vrstev konvoluční sítě vede k artefaktům. Tento problém se obvykle řeší tzv. **progresivním růstem**, kdy se nejprve několik vrstev trénuje na obrázcích s nízkým rozlišením, a poté se vrstvy "odblokují" nebo přidají. Dalším řešením by bylo přidání dalších spojení mezi vrstvami a trénování několika rozlišení najednou - podrobnosti viz tento [Multi-Scale Gradient GANs paper](https://arxiv.org/abs/1903.06048).

## Přenos stylu

GANs jsou skvělým způsobem, jak generovat umělecké obrázky. Další zajímavou technikou je tzv. **přenos stylu**, který vezme jeden **obrázek obsahu** a překreslí ho v jiném stylu, aplikováním filtrů z **obrázku stylu**.

Jak to funguje:
* Začneme s náhodným šumovým obrázkem (nebo s obrázkem obsahu, ale pro lepší pochopení je jednodušší začít s náhodným šumem).
* Naším cílem bude vytvořit takový obrázek, který bude blízký jak obrázku obsahu, tak obrázku stylu. To bude určeno dvěma funkcemi ztráty:
   - **Ztráta obsahu** se vypočítává na základě vlastností extrahovaných CNN na některých vrstvách z aktuálního obrázku a obrázku obsahu.
   - **Ztráta stylu** se vypočítává mezi aktuálním obrázkem a obrázkem stylu chytrým způsobem pomocí Gramových matic (více podrobností v [příkladovém notebooku](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)).
* Aby byl obrázek hladší a odstranil šum, zavádíme také **ztrátu variace**, která vypočítává průměrnou vzdálenost mezi sousedními pixely.
* Hlavní optimalizační smyčka upravuje aktuální obrázek pomocí gradientního sestupu (nebo jiného optimalizačního algoritmu) tak, aby minimalizovala celkovou ztrátu, která je váženým součtem všech tří ztrát.

## ✍️ Příklad: [Přenos stylu](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/210)

## Závěr

V této lekci jste se naučili o GANs a jak je trénovat. Také jste se dozvěděli o speciálních výzvách, kterým tento typ neuronové sítě může čelit, a o některých strategiích, jak je překonat.

## 🚀 Výzva

Projděte si [notebook Přenos stylu](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) s použitím vlastních obrázků.

## Přehled & Samostudium

Pro referenci si přečtěte více o GANs v těchto zdrojích:

* Marco Pasini, [10 Lessons I Learned Training GANs for one Year](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), *de facto* architektura GAN, kterou stojí za to zvážit
* [Creating Generative Art using GANs on Azure ML](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Zadání

Znovu si projděte jeden ze dvou notebooků spojených s touto lekcí a znovu natrénujte GAN na vlastních obrázcích. Co dokážete vytvořit?

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.