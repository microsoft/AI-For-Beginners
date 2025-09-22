<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "58bf4adb210aab53e8f78c8082040e7c",
  "translation_date": "2025-08-25T21:31:36+00:00",
  "source_file": "lessons/5-NLP/16-RNN/README.md",
  "language_code": "hu"
}
-->
# Rekurrens Neurális Hálózatok

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/31)

Az előző szakaszokban gazdag szemantikai reprezentációkat használtunk a szövegekhez, valamint egy egyszerű lineáris osztályozót az embeddingek tetején. Ez az architektúra a mondatokban szereplő szavak összesített jelentését ragadja meg, de nem veszi figyelembe a szavak **sorrendjét**, mivel az embeddingek tetején végzett aggregációs művelet eltávolította ezt az információt az eredeti szövegből. Mivel ezek a modellek nem képesek a szavak sorrendjét modellezni, nem tudnak megoldani összetettebb vagy kétértelmű feladatokat, mint például szöveg generálása vagy kérdés megválaszolása.

Ahhoz, hogy a szövegszekvencia jelentését megragadjuk, egy másik neurális hálózati architektúrát kell használnunk, amelyet **rekurrens neurális hálózatnak** (RNN) nevezünk. Az RNN-ben a mondatot egyesével, szimbólumonként adjuk át a hálózaton, amely egy **állapotot** hoz létre, amit aztán a következő szimbólummal együtt újra átadunk a hálózatnak.

![RNN](../../../../../translated_images/rnn.27f5c29c53d727b546ad3961637a267f0fe9ec5ab01f2a26a853c92fcefbb574.hu.png)

> Kép a szerzőtől

Az X<sub>0</sub>,...,X<sub>n</sub> tokenek bemeneti szekvenciáját figyelembe véve az RNN egy neurális hálózati blokkok sorozatát hozza létre, és ezt a sorozatot végponttól végpontig tanítja visszaterjesztéssel. Minden hálózati blokk egy (X<sub>i</sub>,S<sub>i</sub>) párt kap bemenetként, és S<sub>i+1</sub>-et állít elő eredményként. Az utolsó állapot S<sub>n</sub> vagy (kimenet Y<sub>n</sub>) egy lineáris osztályozóba kerül, hogy előállítsa az eredményt. Az összes hálózati blokk ugyanazokat a súlyokat osztja meg, és egyetlen visszaterjesztési lépésben végponttól végpontig tanul.

Mivel az állapotvektorok S<sub>0</sub>,...,S<sub>n</sub> átmennek a hálózaton, képes megtanulni a szavak közötti szekvenciális függőségeket. Például, amikor a *nem* szó megjelenik valahol a szekvenciában, megtanulhatja bizonyos elemek tagadását az állapotvektoron belül, ami tagadást eredményez.

> ✅ Mivel a fenti képen látható összes RNN blokk súlyai megosztottak, ugyanaz a kép egyetlen blokként is ábrázolható (a jobb oldalon) egy rekurrens visszacsatolási hurokkal, amely visszaviszi a hálózat kimeneti állapotát a bemenethez.

## Az RNN cella anatómiája

Nézzük meg, hogyan van felépítve egy egyszerű RNN cella. Elfogadja az előző állapotot S<sub>i-1</sub> és az aktuális szimbólumot X<sub>i</sub> bemenetként, és elő kell állítania a kimeneti állapotot S<sub>i</sub> (és néha érdekel minket egy másik kimenet Y<sub>i</sub> is, mint például generatív hálózatok esetében).

Egy egyszerű RNN cellának két súlymátrixa van: az egyik átalakítja a bemeneti szimbólumot (nevezzük W-nek), a másik pedig az állapotot (H). Ebben az esetben a hálózat kimenete σ(W×X<sub>i</sub>+H×S<sub>i-1</sub>+b) formában számítódik ki, ahol σ az aktivációs függvény, és b egy további bias.

<img alt="RNN Cell Anatomy" src="images/rnn-anatomy.png" width="50%"/>

> Kép a szerzőtől

Sok esetben a bemeneti tokenek az embedding rétegen keresztül jutnak az RNN-be, hogy csökkentsék a dimenziót. Ebben az esetben, ha a bemeneti vektorok dimenziója *emb_size*, és az állapotvektor *hid_size* - akkor W mérete *emb_size*×*hid_size*, és H mérete *hid_size*×*hid_size*.

## Hosszú-rövid távú memória (LSTM)

A klasszikus RNN-ek egyik fő problémája az úgynevezett **eltűnő gradiens** probléma. Mivel az RNN-eket egyetlen visszaterjesztési lépésben végponttól végpontig tanítják, nehézséget okoz a hiba propagálása a hálózat első rétegeihez, így a hálózat nem tudja megtanulni a távoli tokenek közötti kapcsolatokat. Ennek a problémának az elkerülésére az egyik megoldás az **explicit állapotkezelés** bevezetése úgynevezett **kapuk** segítségével. Két jól ismert architektúra létezik ebben a kategóriában: **Hosszú-rövid távú memória** (LSTM) és **Kapuzott relé egység** (GRU).

![Image showing an example long short term memory cell](../../../../../lessons/5-NLP/16-RNN/images/long-short-term-memory-cell.svg)

> Kép forrása TBD

Az LSTM hálózat felépítése hasonló az RNN-hez, de két állapotot továbbít rétegről rétegre: az aktuális állapotot C, és a rejtett vektort H. Minden egységnél a rejtett vektor H<sub>i</sub> össze van kapcsolva a bemenettel X<sub>i</sub>, és ezek irányítják, hogy mi történik az állapottal C **kapuk** segítségével. Minden kapu egy neurális hálózat szigmoid aktivációval (kimenet tartománya [0,1]), amely bitmaszkként működik, amikor megszorozzuk az állapotvektorral. A következő kapuk léteznek (balról jobbra a fenti képen):

* A **felejtő kapu** egy rejtett vektort vesz, és meghatározza, hogy az állapotvektor C mely komponenseit kell elfelejteni, és melyeket kell továbbítani.
* A **bemeneti kapu** információt vesz a bemeneti és rejtett vektorokból, és beilleszti az állapotba.
* A **kimeneti kapu** az állapotot egy lineáris rétegen keresztül átalakítja *tanh* aktivációval, majd kiválasztja annak bizonyos komponenseit a rejtett vektor H<sub>i</sub> segítségével, hogy új állapotot C<sub>i+1</sub> állítson elő.

Az állapot C komponensei gondolhatók úgy, mint bizonyos jelzők, amelyeket be- és kikapcsolhatunk. Például, amikor a *Alice* névvel találkozunk a szekvenciában, feltételezhetjük, hogy egy női karakterre utal, és bekapcsolhatjuk az állapotban azt a jelzőt, hogy női főnév van a mondatban. Amikor később találkozunk az *és Tom* kifejezéssel, bekapcsolhatjuk azt a jelzőt, hogy többes számú főnév van. Így az állapot manipulálásával nyomon követhetjük a mondatrészek nyelvtani tulajdonságait.

> ✅ Egy kiváló forrás az LSTM belső működésének megértéséhez Christopher Olah [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) című cikke.

## Bidirekcionális és többrétegű RNN-ek

Olyan rekurrens hálózatokat tárgyaltunk, amelyek egy irányban működnek, a szekvencia elejétől a végéig. Ez természetesnek tűnik, mivel hasonlít arra, ahogyan olvasunk és hallgatunk beszédet. Azonban mivel sok gyakorlati esetben véletlen hozzáférésünk van a bemeneti szekvenciához, érdemes lehet rekurrens számítást végezni mindkét irányban. Az ilyen hálózatokat **bidirekcionális** RNN-eknek nevezzük. Bidirekcionális hálózat esetén két rejtett állapotvektorra van szükségünk, egy-egy irányhoz.

Egy rekurrens hálózat, legyen az egyirányú vagy bidirekcionális, bizonyos mintákat ragad meg egy szekvencián belül, és ezeket az állapotvektorba menti vagy a kimenetbe továbbítja. Ahogy a konvolúciós hálózatoknál, itt is építhetünk egy másik rekurrens réteget az első fölé, hogy magasabb szintű mintákat ragadjunk meg, és az első réteg által kinyert alacsony szintű mintákból építkezzünk. Ez vezet minket a **többrétegű RNN** fogalmához, amely két vagy több rekurrens hálózatból áll, ahol az előző réteg kimenete bemenetként kerül a következő rétegbe.

![Image showing a Multilayer long-short-term-memory- RNN](../../../../../translated_images/multi-layer-lstm.dd975e29bb2a59fe58b429db833932d734c81f211cad2783797a9608984acb8c.hu.jpg)

*Kép Fernando López [ezen csodálatos bejegyzéséből](https://towardsdatascience.com/from-a-lstm-cell-to-a-multilayer-lstm-network-with-pytorch-2899eb5696f3)*

## ✍️ Gyakorlatok: Embeddingek

Folytasd a tanulást az alábbi jegyzetekben:

* [RNN-ek PyTorch segítségével](../../../../../lessons/5-NLP/16-RNN/RNNPyTorch.ipynb)
* [RNN-ek TensorFlow segítségével](../../../../../lessons/5-NLP/16-RNN/RNNTF.ipynb)

## Összegzés

Ebben az egységben láttuk, hogy az RNN-ek használhatók szekvencia osztályozásra, de valójában sok más feladatot is képesek kezelni, mint például szöveg generálása, gépi fordítás és még sok más. Ezeket a feladatokat a következő egységben fogjuk megvizsgálni.

## 🚀 Kihívás

Olvass el néhány irodalmat az LSTM-ekről, és gondold át az alkalmazásaikat:

- [Grid Long Short-Term Memory](https://arxiv.org/pdf/1507.01526v1.pdf)
- [Show, Attend and Tell: Neural Image Caption
Generation with Visual Attention](https://arxiv.org/pdf/1502.03044v2.pdf)

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/32)

## Áttekintés és önálló tanulás

- [Understanding LSTM Networks](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) Christopher Olah-tól.

## [Feladat: Jegyzetek](assignment.md)

**Felelősségkizárás**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.