<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7f8a25ff13cfe9f4cd671cc23351fad",
  "translation_date": "2025-08-25T22:33:27+00:00",
  "source_file": "lessons/4-ComputerVision/12-Segmentation/README.md",
  "language_code": "hu"
}
-->
# Szegmentáció

Korábban már tanultunk az objektumfelismerésről, amely lehetővé teszi számunkra, hogy az objektumokat az *határoló dobozok* előrejelzésével lokalizáljuk a képen. Azonban bizonyos feladatokhoz nemcsak határoló dobozokra van szükségünk, hanem pontosabb objektum lokalizációra is. Ezt a feladatot **szegmentációnak** nevezzük.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/23)

A szegmentációt tekinthetjük **pixelek osztályozásának**, ahol a kép **minden egyes** pixeléről meg kell jósolnunk az osztályát (*háttér* is egy osztály). Két fő szegmentációs algoritmus létezik:

* **Szemantikus szegmentáció** csak a pixel osztályát határozza meg, és nem különbözteti meg az ugyanazon osztályba tartozó különböző objektumokat.
* **Instance szegmentáció** az osztályokat különböző példányokra osztja.

Például instance szegmentáció esetén ezek a juhok különböző objektumok, míg szemantikus szegmentáció esetén minden juh egy osztályba tartozik.

<img src="images/instance_vs_semantic.jpeg" width="50%">

> Kép ebből a [blogbejegyzésből](https://nirmalamurali.medium.com/image-classification-vs-semantic-segmentation-vs-instance-segmentation-625c33a08d50)

Különböző neurális architektúrák léteznek a szegmentációhoz, de mindegyiknek ugyanaz a szerkezete. Bizonyos értelemben hasonlít az autoencoderhez, amelyről korábban tanultál, de az eredeti kép dekonstruálása helyett a célunk egy **maszk** dekonstruálása. Így egy szegmentációs hálózatnak a következő részei vannak:

* **Encoder** kivonja a bemeneti képből a jellemzőket
* **Decoder** átalakítja ezeket a jellemzőket a **maszk képpé**, amelynek mérete és csatornaszáma megegyezik az osztályok számával.

<img src="images/segm.png" width="80%">

> Kép ebből a [publikációból](https://arxiv.org/pdf/2001.05566.pdf)

Különösen meg kell említenünk a szegmentációhoz használt veszteségfüggvényt. Klasszikus autoencoderek használatakor meg kell mérnünk a hasonlóságot két kép között, és ehhez használhatjuk az átlagos négyzetes hibát (MSE). Szegmentáció esetén a cél maszk kép minden egyes pixele az osztály számát képviseli (egy-hot kódolva a harmadik dimenzió mentén), így olyan veszteségfüggvényeket kell használnunk, amelyek kifejezetten osztályozásra alkalmasak - keresztentrópia veszteség, amelyet az összes pixelre átlagolunk. Ha a maszk bináris, akkor **bináris keresztentrópia veszteséget** (BCE) használunk.

> ✅ Az egy-hot kódolás egy olyan technika, amely egy osztály címkét egy olyan vektorrá alakít, amelynek hossza megegyezik az osztályok számával. Nézd meg [ezt a cikket](https://datagy.io/sklearn-one-hot-encode/) erről a technikáról.

## Szegmentáció az orvosi képalkotásban

Ebben a leckében a szegmentációt működés közben fogjuk látni, amikor a hálózatot arra tanítjuk, hogy felismerje az emberi anyajegyeket (más néven nevi) orvosi képeken. A képek forrásaként a <a href="https://www.fc.up.pt/addi/ph2%20database.html">PH<sup>2</sup> Adatbázist</a> fogjuk használni. Ez az adatbázis 200 képet tartalmaz három osztályból: tipikus nevus, atipikus nevus és melanoma. Minden képhez tartozik egy **maszk**, amely körvonalazza a nevust.

> ✅ Ez a technika különösen alkalmas az ilyen típusú orvosi képalkotásra, de milyen más valós alkalmazásokat tudnál elképzelni?

<img alt="navi" src="images/navi.png"/>

> Kép a PH<sup>2</sup> Adatbázisból

Egy modellt fogunk tanítani arra, hogy bármilyen nevust szegmentáljon a háttérből.

## ✍️ Gyakorlatok: Szemantikus szegmentáció

Nyisd meg az alábbi notebookokat, hogy többet megtudj a különböző szemantikus szegmentációs architektúrákról, gyakorold a velük való munkát, és lásd őket működés közben.

* [Semantic Segmentation Pytorch](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationPytorch.ipynb)
* [Semantic Segmentation TensorFlow](../../../../../lessons/4-ComputerVision/12-Segmentation/SemanticSegmentationTF.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/24)

## Összegzés

A szegmentáció egy nagyon erőteljes technika a képosztályozásban, amely túlmutat a határoló dobozokon, és pixel szintű osztályozást tesz lehetővé. Ez a technika az orvosi képalkotásban és számos más alkalmazásban is használható.

## 🚀 Kihívás

A test szegmentációja csak egy a gyakori feladatok közül, amelyeket emberek képeivel végezhetünk. Más fontos feladatok közé tartozik a **csontváz detektálása** és a **testtartás felismerése**. Próbáld ki az [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) könyvtárat, hogy lásd, hogyan használható a testtartás felismerése.

## Áttekintés és önálló tanulás

Ez a [wikipedia cikk](https://wikipedia.org/wiki/Image_segmentation) jó áttekintést nyújt a technika különböző alkalmazásairól. Ismerd meg önállóan az Instance szegmentáció és Panoptikus szegmentáció alágazatait ezen a területen.

## [Feladat](lab/README.md)

Ebben a laborban próbáld ki az **emberi test szegmentációját** a [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) adathalmazzal a Kaggle-ről.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.