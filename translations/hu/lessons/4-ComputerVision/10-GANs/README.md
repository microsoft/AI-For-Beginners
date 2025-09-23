<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f07c85bbf05a1f67505da98f4ecc124c",
  "translation_date": "2025-08-25T22:38:16+00:00",
  "source_file": "lessons/4-ComputerVision/10-GANs/README.md",
  "language_code": "hu"
}
-->
# Generatív Adverzális Hálózatok

Az előző részben megismerkedtünk a **generatív modellekkel**: olyan modellekkel, amelyek képesek új képeket generálni, amelyek hasonlóak a tanító adathalmazban lévőkhöz. A VAE egy jó példa volt a generatív modellre.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/19)

Azonban, ha valami igazán jelentős dolgot szeretnénk generálni, például egy festményt megfelelő felbontásban, a VAE-vel azt tapasztaljuk, hogy a tanítás nem konvergál jól. Ehhez az esethez meg kell ismerkednünk egy másik architektúrával, amelyet kifejezetten generatív modellekhez terveztek - **Generatív Adverzális Hálózatokkal**, vagy GAN-ekkel.

A GAN fő ötlete, hogy két neurális hálózatot tanítunk egymás ellen:

<img src="images/gan_architecture.png" width="70%"/>

> Kép: [Dmitry Soshnikov](http://soshnikov.com)

> ✅ Egy kis szószedet:
> * **Generátor**: egy hálózat, amely egy véletlenszerű vektort vesz, és eredményként képet állít elő.
> * **Diszkriminátor**: egy hálózat, amely egy képet vesz, és meg kell mondania, hogy az valódi kép-e (a tanító adathalmazból), vagy a generátor által generált. Lényegében egy képosztályozó.

### Diszkriminátor

A diszkriminátor architektúrája nem különbözik egy szokványos képosztályozó hálózattól. A legegyszerűbb esetben lehet egy teljesen összekapcsolt osztályozó, de valószínűleg egy [konvolúciós hálózat](../07-ConvNets/README.md) lesz.

> ✅ A konvolúciós hálózatokon alapuló GAN-t [DCGAN](https://arxiv.org/pdf/1511.06434.pdf)-nek hívják.

Egy CNN diszkriminátor a következő rétegekből áll: több konvolúció+pooling (csökkenő térbeli mérettel), és egy vagy több teljesen összekapcsolt réteg, hogy "jellemző vektort" kapjunk, végül egy bináris osztályozó.

> ✅ A 'pooling' ebben az összefüggésben egy olyan technika, amely csökkenti a kép méretét. "A pooling rétegek csökkentik az adatok dimenzióit azáltal, hogy az egyik réteg neuroncsoportjainak kimeneteit egyetlen neuronba kombinálják a következő rétegben." - [forrás](https://wikipedia.org/wiki/Convolutional_neural_network#Pooling_layers)

### Generátor

A generátor valamivel bonyolultabb. Úgy tekinthetjük, mint egy fordított diszkriminátort. Egy látens vektorból kiindulva (a jellemző vektor helyett) van egy teljesen összekapcsolt rétege, amely átalakítja a szükséges méretre/alakra, majd dekonvolúció+felbontásnövelés következik. Ez hasonló az [autoencoder](../09-Autoencoders/README.md) *dekóder* részéhez.

> ✅ Mivel a konvolúciós réteg lineáris szűrőként működik, amely végigmegy a képen, a dekonvolúció lényegében hasonló a konvolúcióhoz, és ugyanazzal a réteglogikával megvalósítható.

<img src="images/gan_arch_detail.png" width="70%"/>

> Kép: [Dmitry Soshnikov](http://soshnikov.com)

### A GAN tanítása

A GAN-eket **adverzálisnak** nevezik, mert folyamatos verseny zajlik a generátor és a diszkriminátor között. E verseny során mind a generátor, mind a diszkriminátor javul, így a hálózat egyre jobb képek előállítását tanulja meg.

A tanítás két szakaszban történik:

* **A diszkriminátor tanítása**. Ez a feladat viszonylag egyszerű: generálunk egy képcsomagot a generátorral, 0-val címkézve őket, ami hamis képet jelent, és veszünk egy képcsomagot a bemeneti adathalmazból (1-es címkével, valódi kép). Kapunk egy *diszkriminátor veszteséget*, és végrehajtjuk a backpropot.
* **A generátor tanítása**. Ez valamivel bonyolultabb, mert nem ismerjük közvetlenül a generátor várt kimenetét. Az egész GAN hálózatot, amely generátorból és diszkriminátorból áll, véletlenszerű vektorokkal tápláljuk, és azt várjuk, hogy az eredmény 1 legyen (ami valódi képeket jelent). Ekkor befagyasztjuk a diszkriminátor paramétereit (nem akarjuk, hogy ebben a lépésben tanuljon), és végrehajtjuk a backpropot.

E folyamat során a generátor és a diszkriminátor veszteségei nem csökkennek jelentősen. Ideális esetben oszcillálniuk kellene, ami azt jelzi, hogy mindkét hálózat javítja teljesítményét.

## ✍️ Feladatok: GAN-ek

* [GAN Notebook TensorFlow/Keras-ban](../../../../../lessons/4-ComputerVision/10-GANs/GANTF.ipynb)
* [GAN Notebook PyTorch-ban](../../../../../lessons/4-ComputerVision/10-GANs/GANPyTorch.ipynb)

### Problémák a GAN-ek tanításával

A GAN-ekről köztudott, hogy különösen nehéz őket tanítani. Íme néhány probléma:

* **Módusösszeomlás**. Ez azt jelenti, hogy a generátor megtanul egy sikeres képet előállítani, amely becsapja a diszkriminátort, de nem képes különféle képeket generálni.
* **Érzékenység a hiperparaméterekre**. Gyakran előfordulhat, hogy egy GAN egyáltalán nem konvergál, majd hirtelen a tanulási ráta csökkenése konvergenciát eredményez.
* **Egyensúly fenntartása** a generátor és a diszkriminátor között. Sok esetben a diszkriminátor vesztesége viszonylag gyorsan nullára csökkenhet, ami azt eredményezi, hogy a generátor nem képes tovább tanulni. Ennek leküzdésére megpróbálhatunk különböző tanulási rátákat beállítani a generátor és a diszkriminátor számára, vagy kihagyhatjuk a diszkriminátor tanítását, ha a veszteség már túl alacsony.
* **Magas felbontású tanítás**. Ugyanaz a probléma, mint az autoencodereknél, ez a probléma akkor jelentkezik, amikor túl sok konvolúciós hálózati réteget kell rekonstruálni, ami artefaktumokat eredményez. Ezt a problémát általában úgy oldják meg, hogy úgynevezett **progresszív növekedést** alkalmaznak, amikor először néhány réteget alacsony felbontású képeken tanítanak, majd a rétegeket "feloldják" vagy hozzáadják. Egy másik megoldás az lenne, hogy extra kapcsolatokat adunk a rétegek között, és egyszerre több felbontást tanítunk - részletekért lásd ezt a [Multi-Scale Gradient GANs tanulmányt](https://arxiv.org/abs/1903.06048).

## Stílusátvitel

A GAN-ek nagyszerű módot kínálnak művészi képek generálására. Egy másik érdekes technika az úgynevezett **stílusátvitel**, amely egy **tartalomképet** vesz, és egy másik stílusban újrarajzolja, szűrőket alkalmazva egy **stílusképből**.

A működése a következő:
* Véletlenszerű zajképpel kezdünk (vagy egy tartalomképpel, de a megértés kedvéért egyszerűbb zajképpel kezdeni)
* Célunk egy olyan kép létrehozása, amely közel áll mind a tartalomképhez, mind a stílusképhez. Ezt két veszteségfüggvény határozza meg:
   - **Tartalomveszteség**, amelyet a CNN által bizonyos rétegeken kinyert jellemzők alapján számítunk ki az aktuális kép és a tartalomkép között
   - **Stílusveszteség**, amelyet az aktuális kép és a stíluskép között számítunk ki egy okos módszerrel Gram-mátrixok segítségével (további részletek az [példa notebookban](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb))
* A kép simábbá tétele és a zaj eltávolítása érdekében bevezetjük a **Variációs veszteséget**, amely a szomszédos pixelek közötti átlagos távolságot számítja ki
* A fő optimalizációs ciklus az aktuális képet gradient descent (vagy más optimalizációs algoritmus) segítségével módosítja, hogy minimalizálja a teljes veszteséget, amely az összes veszteség súlyozott összege.

## ✍️ Példa: [Stílusátvitel](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb)

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/20)

## Összegzés

Ebben a leckében megismerkedtél a GAN-ekkel és azok tanításával. Megtanultad azokat a különleges kihívásokat is, amelyekkel ez a neurális hálózat típus szembesülhet, valamint néhány stratégiát, hogyan lehet ezeket leküzdeni.

## 🚀 Kihívás

Futtasd végig a [Stílusátvitel notebookot](../../../../../lessons/4-ComputerVision/10-GANs/StyleTransfer.ipynb) saját képeiddel.

## Áttekintés és önálló tanulás

További információért olvass többet a GAN-ekről az alábbi forrásokban:

* Marco Pasini, [10 tanulság, amit egy év alatt GAN-ek tanításából tanultam](https://towardsdatascience.com/10-lessons-i-learned-training-generative-adversarial-networks-gans-for-a-year-c9071159628)
* [StyleGAN](https://en.wikipedia.org/wiki/StyleGAN), egy *de facto* GAN architektúra, amit érdemes megfontolni
* [Generatív művészet létrehozása GAN-ekkel az Azure ML-en](https://soshnikov.com/scienceart/creating-generative-art-using-gan-on-azureml/)

## Feladat

Nézd át a leckéhez kapcsolódó két notebook egyikét, és tanítsd újra a GAN-t saját képeiden. Mit tudsz létrehozni?

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.