<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2f7b97b375358cb51a1e098df306bf73",
  "translation_date": "2025-08-25T22:54:39+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/CNN_Architectures.md",
  "language_code": "hu"
}
-->
# Jól ismert CNN architektúrák

### VGG-16

A VGG-16 egy hálózat, amely 2014-ben 92,7%-os pontosságot ért el az ImageNet top-5 osztályozásban. Az alábbi rétegszerkezettel rendelkezik:

![ImageNet Layers](../../../../../translated_images/vgg-16-arch1.d901a5583b3a51baeaab3e768567d921e5d54befa46e1e642616c5458c934028.hu.jpg)

Amint látható, a VGG egy hagyományos piramis architektúrát követ, amely konvolúciós és pooling rétegek sorozatából áll.

![ImageNet Pyramid](../../../../../translated_images/vgg-16-arch.64ff2137f50dd49fdaa786e3f3a975b3f22615efd13efb19c5d22f12e01451a1.hu.jpg)

> Kép forrása: [Researchgate](https://www.researchgate.net/figure/Vgg16-model-structure-To-get-the-VGG-NIN-model-we-replace-the-2-nd-4-th-6-th-7-th_fig2_335194493)

### ResNet

A ResNet a Microsoft Research által 2015-ben javasolt modellek családja. A ResNet fő ötlete az **reziduális blokkok** használata:

<img src="images/resnet-block.png" width="300"/>

> Kép forrása: [ez a tanulmány](https://arxiv.org/pdf/1512.03385.pdf)

Az identitás-átvezetés használatának oka, hogy a réteg **a különbséget** jósolja meg az előző réteg eredménye és a reziduális blokk kimenete között - innen ered a *reziduális* elnevezés. Ezeket a blokkokat sokkal könnyebb tanítani, és akár több száz ilyen blokkból álló hálózatokat is lehet építeni (a leggyakoribb változatok: ResNet-52, ResNet-101 és ResNet-152).

Ezt a hálózatot úgy is elképzelhetjük, mint amely képes a komplexitását a datasethez igazítani. Kezdetben, amikor elkezdjük tanítani a hálózatot, a súlyok értékei kicsik, és a legtöbb jel az identitás-átvezetési rétegeken keresztül halad. Ahogy a tanítás előrehalad és a súlyok nagyobbak lesznek, a hálózati paraméterek jelentősége nő, és a hálózat alkalmazkodik a szükséges kifejezőerőhöz, hogy helyesen osztályozza a tanítási képeket.

### Google Inception

A Google Inception architektúra ezt az ötletet egy lépéssel tovább viszi, és minden hálózati réteget több különböző útvonal kombinációjaként épít fel:

<img src="images/inception.png" width="400"/>

> Kép forrása: [Researchgate](https://www.researchgate.net/figure/Inception-module-with-dimension-reductions-left-and-schema-for-Inception-ResNet-v1_fig2_355547454)

Itt ki kell emelnünk az 1x1 konvolúciók szerepét, mert elsőre nem tűnnek logikusnak. Miért lenne szükségünk arra, hogy 1x1 szűrővel végigmenjünk a képen? Azonban ne felejtsük el, hogy a konvolúciós szűrők több mélységi csatornával is dolgoznak (eredetileg - RGB színek, későbbi rétegekben - különböző szűrők csatornái), és az 1x1 konvolúciót arra használjuk, hogy ezeket a bemeneti csatornákat különböző tanítható súlyokkal összekeverjük. Ez úgy is tekinthető, mint csatorna dimenzióban történő mintavételezés (pooling).

Itt van [egy jó blogbejegyzés](https://medium.com/analytics-vidhya/talented-mr-1x1-comprehensive-look-at-1x1-convolution-in-deep-learning-f6b355825578) a témáról, és [az eredeti tanulmány](https://arxiv.org/pdf/1312.4400.pdf).

### MobileNet

A MobileNet egy olyan modellek családja, amelyek csökkentett méretűek, és mobil eszközökre alkalmasak. Használja őket, ha korlátozottak az erőforrásai, és hajlandó egy kis pontosságot feláldozni. A mögöttes fő ötlet az úgynevezett **mélységi szeparálható konvolúció**, amely lehetővé teszi, hogy a konvolúciós szűrőket térbeli konvolúciók és 1x1 konvolúciók kompozíciójaként ábrázoljuk a mélységi csatornák felett. Ez jelentősen csökkenti a paraméterek számát, így a hálózat kisebb méretű lesz, és kevesebb adattal is könnyebben tanítható.

Itt van [egy jó blogbejegyzés a MobileNetről](https://medium.com/analytics-vidhya/image-classification-with-mobilenet-cc6fbb2cd470).

## Összegzés

Ebben az egységben megismerte a számítógépes látás neurális hálózatainak fő koncepcióját - a konvolúciós hálózatokat. A valós életben használt architektúrák, amelyek képosztályozást, objektumfelismerést és akár képgenerálást is végeznek, mind CNN-ekre épülnek, csak több réteggel és néhány további tanítási trükkel.

## 🚀 Kihívás

A mellékelt jegyzetfüzetekben vannak megjegyzések az alján arról, hogyan lehet nagyobb pontosságot elérni. Végezzen kísérleteket, hogy megnézze, el tud-e érni magasabb pontosságot.

## [Előadás utáni kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/207)

## Áttekintés és önálló tanulás

Bár a CNN-eket leggyakrabban számítógépes látási feladatokhoz használják, általában jók fix méretű minták kinyerésére. Például, ha hangokkal dolgozunk, akkor is használhatunk CNN-eket, hogy bizonyos mintákat keressünk az audió jelben - ebben az esetben a szűrők 1-dimenziósak lennének (és ezt a CNN-t 1D-CNN-nek neveznénk). Néha 3D-CNN-t is használnak, hogy jellemzőket nyerjenek ki többdimenziós térben, például bizonyos események előfordulását videón - a CNN képes bizonyos mintákat megragadni a jellemzők időbeli változásában. Végezzen áttekintést és önálló tanulást arról, hogy milyen más feladatokat lehet elvégezni CNN-ekkel.

## [Feladat](lab/README.md)

Ebben a laborban különböző macska- és kutyafajták osztályozása a feladat. Ezek a képek bonyolultabbak, mint az MNIST adatállomány, nagyobb dimenziójúak, és több mint 10 osztály van.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.