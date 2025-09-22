<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0b306c04f5337b6e7430e5c0b16bb5c0",
  "translation_date": "2025-08-25T22:28:38+00:00",
  "source_file": "lessons/4-ComputerVision/09-Autoencoders/README.md",
  "language_code": "hu"
}
-->
# Autoenkóderek

Amikor CNN-eket tanítunk, az egyik probléma az, hogy sok címkézett adatra van szükségünk. Képklasszifikáció esetén például manuálisan kell az egyes képeket különböző osztályokba sorolni.

## [Pre-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/17)

Azonban előfordulhat, hogy nyers (címkézetlen) adatokat szeretnénk használni a CNN jellemzők kinyerésére, amit **önfelügyelt tanulásnak** nevezünk. Címkék helyett a tanítóképeket használjuk hálózati bemenetként és kimenetként is. Az **autoenkóder** fő ötlete az, hogy lesz egy **enkóder hálózat**, amely a bemeneti képet valamilyen **rejtett térbe** alakítja (általában egy kisebb méretű vektor), majd egy **dekóder hálózat**, amelynek célja az eredeti kép rekonstruálása.

> ✅ Az [autoenkóder](https://wikipedia.org/wiki/Autoencoder) "egy mesterséges neurális hálózat típusa, amelyet címkézetlen adatok hatékony kódolásának megtanulására használnak."

Mivel az autoenkódert arra tanítjuk, hogy az eredeti képből minél több információt megragadjon a pontos rekonstrukció érdekében, a hálózat megpróbálja megtalálni a bemeneti képek legjobb **beágyazását**, hogy megragadja azok jelentését.

![AutoEncoder Diagram](../../../../../translated_images/autoencoder_schema.5e6fc9ad98a5eb6197f3513cf3baf4dfbe1389a6ae74daebda64de9f1c99f142.hu.jpg)

> Kép a [Keras blogból](https://blog.keras.io/building-autoencoders-in-keras.html)

## Autoenkóderek használati forgatókönyvei

Bár az eredeti képek rekonstruálása önmagában nem tűnik hasznosnak, van néhány forgatókönyv, ahol az autoenkóderek különösen hasznosak:

* **Képek dimenziójának csökkentése vizualizációhoz** vagy **képbeágyazások tanítása**. Az autoenkóderek általában jobb eredményeket adnak, mint a PCA, mivel figyelembe veszik a képek térbeli jellegét és hierarchikus jellemzőit.
* **Zajcsökkentés**, azaz zaj eltávolítása a képről. Mivel a zaj sok haszontalan információt hordoz, az autoenkóder nem tudja mindet beilleszteni a viszonylag kis rejtett térbe, így csak a kép fontos részét ragadja meg. Zajcsökkentők tanításakor az eredeti képekkel kezdünk, és mesterségesen zajt adunk hozzájuk, amelyeket az autoenkóder bemeneteként használunk.
* **Szuperfelbontás**, a kép felbontásának növelése. Magas felbontású képekkel kezdünk, és az alacsonyabb felbontású képet használjuk az autoenkóder bemeneteként.
* **Generatív modellek**. Miután az autoenkódert betanítottuk, a dekóder részt felhasználhatjuk új objektumok létrehozására véletlenszerű rejtett vektorokból kiindulva.

## Variációs Autoenkóderek (VAE)

A hagyományos autoenkóderek valamilyen módon csökkentik a bemeneti adatok dimenzióját, és megpróbálják azonosítani a bemeneti képek fontos jellemzőit. Azonban a rejtett vektorok gyakran nem értelmezhetők. Más szóval, ha például az MNIST adathalmazt vesszük, nem könnyű meghatározni, hogy mely számjegyek felelnek meg a különböző rejtett vektoroknak, mivel a közeli rejtett vektorok nem feltétlenül ugyanazokat a számjegyeket jelentik.

Ezzel szemben generatív modellek tanításához jobb, ha van némi megértésünk a rejtett térről. Ez az ötlet vezet el minket a **variációs autoenkóderhez** (VAE).

A VAE egy olyan autoenkóder, amely megtanulja előre jelezni a rejtett paraméterek *statisztikai eloszlását*, az úgynevezett **rejtett eloszlást**. Például azt szeretnénk, hogy a rejtett vektorok normálisan legyenek elosztva egy z<sub>mean</sub> átlaggal és z<sub>sigma</sub> szórással (mind az átlag, mind a szórás egy d dimenziós vektor). A VAE enkóder megtanulja ezeket a paramétereket előre jelezni, majd a dekóder véletlenszerű vektort vesz ebből az eloszlásból, hogy rekonstruálja az objektumot.

Összefoglalva:

 * A bemeneti vektorból előre jelezzük `z_mean` és `z_log_sigma` értékeket (a szórás helyett annak logaritmusát jelezzük előre)
 * Mintát veszünk egy `sample` vektorból az N(z<sub>mean</sub>,exp(z<sub>log\_sigma</sub>)) eloszlásból
 * A dekóder megpróbálja dekódolni az eredeti képet a `sample` vektort bemenetként használva

 <img src="images/vae.png" width="50%">

> Kép [Isaak Dykeman blogbejegyzéséből](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

A variációs autoenkóderek egy összetett veszteségfüggvényt használnak, amely két részből áll:

* **Rekonstrukciós veszteség**, amely azt mutatja, hogy a rekonstruált kép mennyire közel áll a célhoz (ez lehet például a Mean Squared Error, vagy MSE). Ez ugyanaz a veszteségfüggvény, mint a normál autoenkódereknél.
* **KL veszteség**, amely biztosítja, hogy a rejtett változó eloszlása közel maradjon a normál eloszláshoz. Ez a [Kullback-Leibler divergencia](https://www.countbayesie.com/blog/2017/5/9/kullback-leibler-divergence-explained) fogalmán alapul - egy metrika, amely két statisztikai eloszlás hasonlóságát méri.

A VAE-k egyik fontos előnye, hogy viszonylag könnyen lehet új képeket generálni, mivel tudjuk, mely eloszlásból kell mintát venni a rejtett vektorokhoz. Például, ha egy VAE-t tanítunk 2D rejtett vektorral az MNIST adathalmazon, akkor a rejtett vektor komponenseit változtatva különböző számjegyeket kapunk:

<img alt="vaemnist" src="images/vaemnist.png" width="50%"/>

> Kép [Dmitry Soshnikov](http://soshnikov.com) által

Figyeljük meg, hogyan olvadnak össze a képek, ahogy a rejtett paramétertér különböző részeiből kezdünk mintát venni. Ezt a teret 2D-ben is vizualizálhatjuk:

<img alt="vaemnist cluster" src="images/vaemnist-diag.png" width="50%"/> 

> Kép [Dmitry Soshnikov](http://soshnikov.com) által

## ✍️ Gyakorlatok: Autoenkóderek

További információ az autoenkóderekről az alábbi jegyzetekben található:

* [Autoenkóderek TensorFlow-ban](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb)
* [Autoenkóderek PyTorch-ban](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoEncodersPyTorch.ipynb)

## Az autoenkóderek tulajdonságai

* **Adatspecifikus** - csak azon képtípusokkal működnek jól, amelyeken tanították őket. Például, ha egy szuperfelbontású hálózatot virágokon tanítunk, az nem fog jól működni portrékon. Ennek oka, hogy a hálózat a magasabb felbontású képet úgy állítja elő, hogy finom részleteket vesz a tanító adathalmazból tanult jellemzőkből.
* **Veszteséges** - a rekonstruált kép nem ugyanaz, mint az eredeti kép. A veszteség jellege a tanítás során használt *veszteségfüggvénytől* függ.
* **Címkézetlen adatokkal működik**

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/18)

## Összegzés

Ebben a leckében megismerkedtél az autoenkóderek különböző típusaival, amelyeket az AI kutatók használhatnak. Megtanultad, hogyan építsd fel őket, és hogyan használd őket képek rekonstruálására. Emellett megismerkedtél a VAE-vel és azzal, hogyan lehet új képeket generálni vele.

## 🚀 Kihívás

Ebben a leckében megtanultad, hogyan használhatók az autoenkóderek képekhez. De zenéhez is használhatók! Nézd meg a Magenta projekt [MusicVAE](https://magenta.tensorflow.org/music-vae) projektjét, amely autoenkódereket használ a zene rekonstruálásának megtanulására. Végezzen néhány [kísérletet](https://colab.research.google.com/github/magenta/magenta-demos/blob/master/colab-notebooks/Multitrack_MusicVAE.ipynb) ezzel a könyvtárral, hogy lássa, mit tud létrehozni.

## [Post-lecture quiz](https://ff-quizzes.netlify.app/en/ai/quiz/16)

## Áttekintés és önálló tanulás

További információ az autoenkóderekről az alábbi forrásokban található:

* [Autoenkóderek építése Keras-ban](https://blog.keras.io/building-autoencoders-in-keras.html)
* [Blogbejegyzés a NeuroHive-on](https://neurohive.io/ru/osnovy-data-science/variacionnyj-avtojenkoder-vae/)
* [Variációs autoenkóderek magyarázata](https://kvfrans.com/variational-autoencoders-explained/)
* [Feltételes variációs autoenkóderek](https://ijdykeman.github.io/ml/2016/12/21/cvae.html)

## Feladat

A [TensorFlow jegyzet](../../../../../lessons/4-ComputerVision/09-Autoencoders/AutoencodersTF.ipynb) végén található egy "feladat" - ezt használd házi feladatként.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.