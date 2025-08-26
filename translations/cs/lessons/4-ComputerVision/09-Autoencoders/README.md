<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-25T22:29:05+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "cs"
}
-->
# Autoenkodéry

Při trénování CNN je jedním z problémů potřeba velkého množství označených dat. V případě klasifikace obrázků je nutné rozdělit obrázky do různých tříd, což vyžaduje manuální úsilí.

## [Pre-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/109)

Můžeme však chtít použít surová (neoznačená) data pro trénování CNN extraktorů funkcí, což se nazývá **self-supervised learning**. Místo štítků použijeme trénovací obrázky jako vstup i výstup sítě. Hlavní myšlenkou **autoenkodéru** je, že budeme mít **enkodér síť**, která převede vstupní obrázek do nějakého **latentního prostoru** (obvykle je to jen vektor menší velikosti), a poté **dekodér síť**, jejímž cílem bude rekonstruovat původní obrázek.

> ✅ [Autoenkodér](https://wikipedia.org/wiki/Autoencoder) je "typ umělé neuronové sítě používané k učení efektivního kódování neoznačených dat."

Protože trénujeme autoenkodér, aby zachytil co nejvíce informací z původního obrázku pro přesnou rekonstrukci, síť se snaží najít nejlepší **embedding** vstupních obrázků, aby zachytila jejich význam.

![Schéma Autoenkodéru](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.cs.jpg)

> Obrázek z [blogu Keras](https://blog.keras.io/building-autoencoders-in-keras.html)

## Scénáře použití Autoenkodérů

Ačkoli samotná rekonstrukce původních obrázků nemusí být užitečná, existuje několik scénářů, kde jsou autoenkodéry obzvláště užitečné:

* **Snížení dimenze obrázků pro vizualizaci** nebo **trénování embeddingů obrázků**. Autoenkodéry obvykle poskytují lepší výsledky než PCA, protože berou v úvahu prostorovou povahu obrázků a hierarchické funkce.
* **Odstraňování šumu**, tj. odstranění šumu z obrázku. Protože šum obsahuje mnoho zbytečných informací, autoenkodér nemůže vše vměstnat do relativně malého latentního prostoru, a tak zachytí pouze důležité části obrázku. Při trénování odstraňovačů šumu začínáme s původními obrázky a používáme obrázky s uměle přidaným šumem jako vstup pro autoenkodér.
* **Super-rezoluce**, zvýšení rozlišení obrázku. Začínáme s obrázky ve vysokém rozlišení a používáme obrázky s nižším rozlišením jako vstup pro autoenkodér.
* **Generativní modely**. Jakmile autoenkodér vytrénujeme, dekodér může být použit k vytvoření nových objektů na základě náhodných latentních vektorů.

## Variabilní Autoenkodéry (VAE)

Tradiční autoenkodéry nějakým způsobem snižují dimenzi vstupních dat a zjišťují důležité vlastnosti vstupních obrázků. Latentní vektory však často nedávají příliš smysl. Jinými slovy, pokud vezmeme dataset MNIST jako příklad, zjistit, které číslice odpovídají různým latentním vektorům, není snadný úkol, protože blízké latentní vektory nemusí nutně odpovídat stejným číslicím.

Na druhou stranu, pro trénování *generativních* modelů je lepší mít nějaké porozumění latentnímu prostoru. Tato myšlenka nás vede k **variabilnímu autoenkodéru** (VAE).

VAE je autoenkodér, který se učí předpovídat *statistické rozdělení* latentních parametrů, tzv. **latentní rozdělení**. Například můžeme chtít, aby latentní vektory byly normálně rozdělené s nějakým průměrem z<sub>mean</sub> a standardní odchylkou z<sub>sigma</sub> (průměr i standardní odchylka jsou vektory nějaké dimenze d). Enkodér ve VAE se učí předpovídat tyto parametry a dekodér poté vezme náhodný vektor z tohoto rozdělení k rekonstrukci objektu.

Shrnutí:

 * Ze vstupního vektoru předpovídáme `z_mean` a `z_log_sigma` (místo předpovídání samotné standardní odchylky předpovídáme její logaritmus)
 * Vzorkujeme vektor `sample` z rozdělení N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>))
 * Dekodér se snaží dekódovat původní obrázek pomocí `sample` jako vstupního vektoru

 <img src="images/vae.png" width="50%">

> Obrázek z [tohoto blogového příspěvku](https://ijdykeman.github.io/ml/2016/12/21/cvae.html) od Isaaka Dykemana

Variabilní autoenkodéry používají komplexní ztrátovou funkci, která se skládá ze dvou částí:

* **Ztráta rekonstrukce** je ztrátová funkce, která ukazuje, jak blízko je rekonstruovaný obrázek cíli (může to být Mean Squared Error, nebo MSE). Je to stejná ztrátová funkce jako u běžných autoenkodérů.
* **KL ztráta**, která zajišťuje, že rozdělení latentních proměnných zůstává blízko normálnímu rozdělení. Je založena na pojmu [Kullback-Leibler divergence](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) - metrice pro odhad podobnosti dvou statistických rozdělení.

Jednou z důležitých výhod VAE je, že umožňují relativně snadno generovat nové obrázky, protože víme, z jakého rozdělení vzorkovat latentní vektory. Například pokud trénujeme VAE s 2D latentním vektorem na MNIST, můžeme poté měnit komponenty latentního vektoru, abychom získali různé číslice:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Obrázek od [Dmitry Soshnikov](http://soshnikov.com)

Pozorujte, jak se obrázky prolínají, když začneme získávat latentní vektory z různých částí prostoru latentních parametrů. Tento prostor můžeme také vizualizovat ve 2D:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Obrázek od [Dmitry Soshnikov](http://soshnikov.com)

## ✍️ Cvičení: Autoenkodéry

Zjistěte více o autoenkodérech v těchto odpovídajících noteboocích:

* [Autoenkodéry v TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoenkodéry v PyTorch](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Vlastnosti Autoenkodérů

* **Specifické pro data** - fungují dobře pouze s typem obrázků, na kterých byly trénovány. Například pokud trénujeme síť pro super-rezoluce na květinách, nebude dobře fungovat na portrétech. Je to proto, že síť může vytvořit obrázek ve vyšším rozlišení tím, že vezme jemné detaily z funkcí naučených z trénovacího datasetu.
* **Ztrátové** - rekonstruovaný obrázek není stejný jako původní obrázek. Povaha ztráty je definována *ztrátovou funkcí* použitou během trénování.
* Fungují na **neoznačených datech**

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/209)

## Závěr

V této lekci jste se naučili o různých typech autoenkodérů dostupných pro vědce v oblasti AI. Naučili jste se, jak je vytvořit a jak je použít k rekonstrukci obrázků. Také jste se naučili o VAE a jak je použít k generování nových obrázků.

## 🚀 Výzva

V této lekci jste se naučili používat autoenkodéry pro obrázky. Ale mohou být také použity pro hudbu! Podívejte se na projekt Magenta [MusicVAE](https://magenta.tensorflow.org/music-vae), který používá autoenkodéry k učení rekonstrukce hudby. Udělejte několik [experimentů](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) s touto knihovnou a zjistěte, co můžete vytvořit.

## [Post-lecture quiz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/208)

## Přehled & Samostudium

Pro referenci si přečtěte více o autoenkodérech v těchto zdrojích:

* [Building Autoencoders in Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blogový příspěvek na NeuroHive](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variational Autoencoders Explained](https://kvfrans.com/variational-autoencoders-explained/)
* [Conditional Variational Autoencoders](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Úkol

Na konci [tohoto notebooku s TensorFlow](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb) najdete 'úkol' - použijte jej jako svůj domácí úkol.

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.