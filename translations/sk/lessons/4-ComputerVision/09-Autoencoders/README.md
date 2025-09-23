<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-25T22:29:32+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "sk"
}
-->
# Autoenkodéry

Pri trénovaní CNN je jedným z problémov, že potrebujeme veľa označených dát. V prípade klasifikácie obrázkov musíme obrázky rozdeliť do rôznych tried, čo je manuálna práca.

## [Kvíz pred prednáškou](https://ff-quizzes.netlify.app/en/ai/quiz/17)

Môžeme však chcieť použiť surové (neoznačené) dáta na trénovanie CNN extraktorov vlastností, čo sa nazýva **samoriadené učenie**. Namiesto označení použijeme trénovacie obrázky ako vstup aj výstup siete. Hlavnou myšlienkou **autoenkodéra** je, že budeme mať **enkodérovú sieť**, ktorá konvertuje vstupný obrázok do nejakého **latentného priestoru** (zvyčajne je to len vektor menšej veľkosti), a potom **dekodérovú sieť**, ktorej cieľom bude rekonštruovať pôvodný obrázok.

> ✅ [Autoenkodér](https://wikipedia.org/wiki/Autoencoder) je "typ umelej neurónovej siete, ktorá sa používa na učenie efektívneho kódovania neoznačených dát."

Keďže trénujeme autoenkodér, aby zachytil čo najviac informácií z pôvodného obrázku pre presnú rekonštrukciu, sieť sa snaží nájsť najlepšie **zobrazenie** vstupných obrázkov, aby zachytila ich význam.

![Schéma Autoenkodéra](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.sk.jpg)

> Obrázok z [Keras blogu](https://blog.keras.io/building-autoencoders-in-keras.html)

## Scenáre použitia autoenkodérov

Aj keď rekonštrukcia pôvodných obrázkov sama o sebe nemusí byť užitočná, existuje niekoľko scenárov, kde sú autoenkodéry obzvlášť užitočné:

* **Znižovanie dimenzie obrázkov pre vizualizáciu** alebo **trénovanie obrazových zobrazení**. Autoenkodéry zvyčajne poskytujú lepšie výsledky ako PCA, pretože berú do úvahy priestorovú povahu obrázkov a hierarchické vlastnosti.
* **Odstraňovanie šumu**, t.j. odstránenie šumu z obrázku. Keďže šum obsahuje veľa zbytočných informácií, autoenkodér ho nedokáže všetok zahrnúť do relatívne malého latentného priestoru, a tak zachytí iba dôležitú časť obrázku. Pri trénovaní odstraňovačov šumu začíname s pôvodnými obrázkami a používame obrázky s umelo pridaným šumom ako vstup pre autoenkodér.
* **Superrozlíšenie**, zvyšovanie rozlíšenia obrázkov. Začíname s obrázkami vo vysokom rozlíšení a používame obrázky s nižším rozlíšením ako vstup pre autoenkodér.
* **Generatívne modely**. Po natrénovaní autoenkodéra môžeme dekodérovú časť použiť na vytváranie nových objektov začínajúc od náhodných latentných vektorov.

## Variabilné autoenkodéry (VAE)

Tradičné autoenkodéry nejako znižujú dimenziu vstupných dát a zisťujú dôležité vlastnosti vstupných obrázkov. Latentné vektory však často nedávajú veľký zmysel. Inými slovami, ak vezmeme dataset MNIST ako príklad, zisťovanie, ktoré číslice zodpovedajú rôznym latentným vektorom, nie je jednoduchá úloha, pretože blízke latentné vektory nemusia nevyhnutne zodpovedať rovnakým čísliciam.

Na druhej strane, na trénovanie *generatívnych* modelov je lepšie mať nejaké pochopenie latentného priestoru. Táto myšlienka nás privádza k **variabilnému autoenkodéru** (VAE).

VAE je autoenkodér, ktorý sa učí predpovedať *štatistické rozdelenie* latentných parametrov, tzv. **latentné rozdelenie**. Napríklad môžeme chcieť, aby latentné vektory boli normálne rozdelené s nejakým priemerom z<sub>mean</sub> a štandardnou odchýlkou z<sub>sigma</sub> (obidva, priemer aj štandardná odchýlka, sú vektory nejakej dimenzie d). Enkodér vo VAE sa učí predpovedať tieto parametre a dekodér potom vezme náhodný vektor z tohto rozdelenia na rekonštrukciu objektu.

Zhrnutie:

 * Zo vstupného vektora predpovedáme `z_mean` a `z_log_sigma` (namiesto predpovedania samotnej štandardnej odchýlky predpovedáme jej logaritmus)
 * Vzorkujeme vektor `sample` z rozdelenia N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * Dekodér sa snaží dekódovať pôvodný obrázok pomocou `sample` ako vstupného vektora

 <img src="images/vae.png" width="50%">

> Obrázok z [tohto blogového príspevku](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) od Isaaka Dykemana

Variabilné autoenkodéry používajú komplexnú stratu, ktorá pozostáva z dvoch častí:

* **Rekonštrukčná strata** je funkcia straty, ktorá ukazuje, ako blízko je rekonštruovaný obrázok k cieľu (môže to byť Mean Squared Error, alebo MSE). Je to rovnaká funkcia straty ako pri bežných autoenkodéroch.
* **KL strata**, ktorá zabezpečuje, že rozdelenie latentných premenných zostáva blízke normálnemu rozdeleniu. Je založená na pojme [Kullback-Leiblerovej divergencie](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - metriky na odhad, ako podobné sú dve štatistické rozdelenia.

Jednou dôležitou výhodou VAE je, že nám umožňujú relatívne ľahko generovať nové obrázky, pretože vieme, z ktorého rozdelenia vzorkovať latentné vektory. Napríklad, ak trénujeme VAE s 2D latentným vektorom na MNIST, môžeme potom meniť komponenty latentného vektora, aby sme získali rôzne číslice:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Obrázok od [Dmitry Soshnikov](http://soshnikov.com)

Pozorujte, ako sa obrázky prelínajú, keď začíname získavať latentné vektory z rôznych častí latentného priestoru parametrov. Tento priestor môžeme tiež vizualizovať v 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Obrázok od [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Cvičenia: Autoenkodéry

Zistite viac o autoenkodéroch v týchto príslušných notebookoch:

* [Autoenkodéry v TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoenkodéry v PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Vlastnosti autoenkodérov

* **Špecifické pre dáta** - fungujú dobre iba s typom obrázkov, na ktorých boli trénované. Napríklad, ak trénujeme sieť na superrozlíšenie na kvetoch, nebude dobre fungovať na portrétoch. Je to preto, že sieť dokáže vytvoriť obrázok vo vyššom rozlíšení tým, že berie jemné detaily z vlastností naučených z trénovacej množiny.
* **Stratové** - rekonštruovaný obrázok nie je rovnaký ako pôvodný obrázok. Povaha straty je definovaná *funkciou straty* použitou počas trénovania.
* Funguje na **neoznačených dátach**

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Záver

V tejto lekcii ste sa naučili o rôznych typoch autoenkodérov dostupných pre vedca v oblasti AI. Naučili ste sa, ako ich vytvoriť a ako ich použiť na rekonštrukciu obrázkov. Tiež ste sa naučili o VAE a ako ich použiť na generovanie nových obrázkov.

## 🚀 Výzva

V tejto lekcii ste sa naučili používať autoenkodéry na obrázky. Ale môžu sa použiť aj na hudbu! Pozrite si projekt Magenta [MusicVAE](https://magenta.tensorflow.org/music-vae), ktorý používa autoenkodéry na učenie rekonštrukcie hudby. Urobte niekoľko [experimentov](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) s touto knižnicou a zistite, čo dokážete vytvoriť.

## [Kvíz po prednáške](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Prehľad a samoštúdium

Pre referenciu si prečítajte viac o autoenkodéroch v týchto zdrojoch:

* [Building Autoencoders in Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blogový príspevok na NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variational Autoencoders Explained](https://kvfrans.com/variational-autoencoders-explained/)
* [Conditional Variational Autoencoders](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Zadanie

Na konci [tohto notebooku s TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb) nájdete 'úlohu' - použite ju ako svoje zadanie.

**Zrieknutie sa zodpovednosti**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.