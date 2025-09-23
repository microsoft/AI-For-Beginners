<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f7b97b375358cb51a1e098df306bf73",
  "translation_date": "2025-08-25T22:54:59+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md",
  "language_code": "cs"
}
-->
# Dobře známé architektury CNN

### VGG-16

VGG-16 je síť, která v roce 2014 dosáhla 92,7% přesnosti v klasifikaci ImageNet top-5. Má následující strukturu vrstev:

![ImageNet Layers](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.cs.jpg)

Jak můžete vidět, VGG využívá tradiční pyramidovou architekturu, což je sekvence vrstev konvoluce a pooling.

![ImageNet Pyramid](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.cs.jpg)

> Obrázek z [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

ResNet je rodina modelů navržená Microsoft Research v roce 2015. Hlavní myšlenkou ResNet je použití **reziduálních bloků**:

<img src="images/resnet-block.png" width="300"/>

> Obrázek z [tohoto článku](https://arxiv.org/pdf/1512.03385.pdf)

Důvodem použití identity pass-through je, aby naše vrstva předpovídala **rozdíl** mezi výsledkem předchozí vrstvy a výstupem reziduálního bloku - odtud název *reziduální*. Tyto bloky se mnohem snáze trénují a je možné vytvořit sítě s několika stovkami těchto bloků (nejběžnější varianty jsou ResNet-52, ResNet-101 a ResNet-152).

Tuto síť si také můžete představit jako schopnou přizpůsobit svou složitost datové sadě. Na začátku, když začínáte síť trénovat, jsou hodnoty vah malé a většina signálu prochází vrstvami identity. Jak trénink pokračuje a váhy se zvětšují, význam parametrů sítě roste a síť se přizpůsobuje tak, aby poskytla potřebnou expresivní sílu pro správnou klasifikaci tréninkových obrázků.

### Google Inception

Architektura Google Inception posouvá tuto myšlenku o krok dál a buduje každou vrstvu sítě jako kombinaci několika různých cest:

<img src="images/inception.png" width="400"/>

> Obrázek z [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Zde je třeba zdůraznit roli konvolucí 1x1, protože na první pohled nedávají smysl. Proč bychom měli procházet obrázek filtrem 1x1? Musíte si však uvědomit, že konvoluční filtry pracují také s několika hloubkovými kanály (původně - RGB barvy, v následných vrstvách - kanály pro různé filtry) a konvoluce 1x1 se používá k míchání těchto vstupních kanálů pomocí různých trénovatelných vah. Může být také považována za downsampling (pooling) přes dimenzi kanálů.

Zde je [dobrý blogový příspěvek](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) na toto téma a [původní článek](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

MobileNet je rodina modelů s redukovanou velikostí, vhodná pro mobilní zařízení. Použijte je, pokud máte omezené zdroje a můžete obětovat trochu přesnosti. Hlavní myšlenkou je tzv. **hloubkově separovatelná konvoluce**, která umožňuje reprezentovat konvoluční filtry jako kompozici prostorových konvolucí a konvoluce 1x1 přes hloubkové kanály. To výrazně snižuje počet parametrů, což činí síť menší a také snadněji trénovatelnou s menším množstvím dat.

Zde je [dobrý blogový příspěvek o MobileNet](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Závěr

V této kapitole jste se naučili hlavní koncept za neuronovými sítěmi pro počítačové vidění - konvolučními sítěmi. Architektury používané v reálném světě pro klasifikaci obrázků, detekci objektů a dokonce i generování obrázků jsou všechny založeny na CNN, jen s více vrstvami a některými dalšími tréninkovými triky.

## 🚀 Výzva

V přiložených noteboocích jsou poznámky na konci o tom, jak dosáhnout vyšší přesnosti. Udělejte několik experimentů a zjistěte, zda můžete dosáhnout vyšší přesnosti.

## [Kvíz po přednášce](https://ff-quizzes.netlify.app/en/ai/quiz/14)

## Přehled & Samostudium

I když se CNN nejčastěji používají pro úlohy počítačového vidění, obecně jsou dobré pro extrakci vzorů s pevnou velikostí. Například pokud pracujeme se zvuky, můžeme také chtít použít CNN k hledání specifických vzorů v audio signálu - v takovém případě by filtry byly jednorozměrné (a tato CNN by se nazývala 1D-CNN). Také se někdy používá 3D-CNN k extrakci funkcí v vícerozměrném prostoru, například určitých událostí, které se odehrávají na videu - CNN může zachytit určité vzory změn funkcí v průběhu času. Udělejte si přehled a samostudium o dalších úlohách, které lze s CNN provádět.

## [Úkol](lab/README.md)

V tomto laboratorním cvičení máte za úkol klasifikovat různé plemena koček a psů. Tyto obrázky jsou složitější než dataset MNIST, mají vyšší rozměry a je zde více než 10 tříd.

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nenese odpovědnost za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.