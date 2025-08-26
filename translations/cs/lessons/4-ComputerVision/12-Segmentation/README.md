<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-25T22:33:50+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "cs"
}
-->
# Segmentace

Dříve jsme se naučili o detekci objektů, která nám umožňuje lokalizovat objekty na obrázku předpovědí jejich *ohraničujících rámečků*. Pro některé úkoly však nepotřebujeme pouze ohraničující rámečky, ale také přesnější lokalizaci objektů. Tento úkol se nazývá **segmentace**.

## [Kvíz před lekcí](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/112)

Segmentaci lze chápat jako **klasifikaci pixelů**, kde pro **každý** pixel obrázku musíme předpovědět jeho třídu (*pozadí* je jednou z tříd). Existují dva hlavní algoritmy segmentace:

* **Sémantická segmentace** určuje pouze třídu pixelu a nerozlišuje mezi různými objekty stejné třídy.
* **Instance segmentace** rozděluje třídy na různé instance.

Například u instance segmentace jsou tyto ovce různé objekty, ale u sémantické segmentace jsou všechny ovce reprezentovány jednou třídou.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Obrázek z [tohoto blogového příspěvku](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Existují různé neuronové architektury pro segmentaci, ale všechny mají stejnou strukturu. Svým způsobem je to podobné autoenkodéru, o kterém jste se již učili, ale místo rekonstrukce původního obrázku je naším cílem vytvořit **masku**. Segmentační síť má tedy následující části:

* **Encoder** extrahuje rysy z vstupního obrázku.
* **Decoder** transformuje tyto rysy do **obrázku masky**, který má stejnou velikost a počet kanálů odpovídající počtu tříd.

<img src="images/segm.png" width="80%">

> Obrázek z [této publikace](https://arxiv.org/pdf/2001.05566.pdf)

Zvláštní zmínku si zaslouží ztrátová funkce používaná pro segmentaci. Při použití klasických autoenkodérů musíme měřit podobnost mezi dvěma obrázky, a k tomu můžeme použít střední kvadratickou chybu (MSE). U segmentace každý pixel v cílovém obrázku masky reprezentuje číslo třídy (one-hot-encoded ve třetím rozměru), takže musíme použít ztrátové funkce specifické pro klasifikaci - ztrátu křížové entropie, průměrovanou přes všechny pixely. Pokud je maska binární, používá se **binární ztráta křížové entropie** (BCE).

> ✅ One-hot encoding je způsob, jak zakódovat štítek třídy do vektoru o délce odpovídající počtu tříd. Podívejte se na [tento článek](https://datagy.io/sklearn-one-hot-encode/) o této technice.

## Segmentace v lékařském zobrazování

V této lekci uvidíme segmentaci v praxi tím, že budeme trénovat síť na rozpoznávání lidských névů (známých také jako mateřská znaménka) na lékařských snímcích. Budeme používat <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> databázi</a> dermoskopických snímků jako zdroj obrázků. Tato sada dat obsahuje 200 obrázků tří tříd: typický névus, atypický névus a melanom. Všechny obrázky také obsahují odpovídající **masku**, která vymezuje névus.

> ✅ Tato technika je obzvláště vhodná pro tento typ lékařského zobrazování, ale jaké další reálné aplikace si dokážete představit?

<img alt="navi" src="images/navi.png"/>

> Obrázek z PH<sup>2</sup> databáze

Natrénujeme model, který bude segmentovat jakýkoli névus od jeho pozadí.

## ✍️ Cvičení: Sémantická segmentace

Otevřete níže uvedené notebooky, abyste se dozvěděli více o různých architekturách sémantické segmentace, procvičili si práci s nimi a viděli je v akci.

* [Sémantická segmentace v Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Sémantická segmentace v TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Kvíz po lekci](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/212)

## Závěr

Segmentace je velmi silná technika pro klasifikaci obrázků, která jde nad rámec ohraničujících rámečků až na úroveň klasifikace pixelů. Tato technika se používá v lékařském zobrazování a dalších aplikacích.

## 🚀 Výzva

Segmentace těla je jen jedním z běžných úkolů, které můžeme provádět s obrázky lidí. Další důležité úkoly zahrnují **detekci kostry** a **detekci póz**. Vyzkoušejte knihovnu [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), abyste viděli, jak lze detekci póz využít.

## Přehled a samostudium

Tento [článek na Wikipedii](https://wikipedia.org/wiki/Image_segmentation) nabízí dobrý přehled různých aplikací této techniky. Zjistěte více o podoblastech Instance segmentace a Panoptické segmentace v této oblasti.

## [Úkol](lab/README.md)

V této laboratoři zkuste **segmentaci lidského těla** pomocí [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) z Kaggle.

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.