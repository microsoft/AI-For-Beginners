<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d9de7847385eeeda67cfdcce1640ab72",
  "translation_date": "2025-08-25T21:43:24+00:00",
  "source_file": "lessons/5-NLP/17-GenerativeNetworks/README.md",
  "language_code": "hu"
}
-->
# Generatív hálózatok

## [Előadás előtti kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/117)

A Rekurrens Neurális Hálózatok (RNN-ek) és azok kapuzott cellaváltozatai, mint például a Long Short Term Memory Cells (LSTM-ek) és a Gated Recurrent Units (GRU-k), lehetőséget biztosítanak a nyelvi modellezésre, mivel képesek megtanulni a szavak sorrendjét, és előre jelezni a következő szót egy sorozatban. Ez lehetővé teszi, hogy az RNN-eket **generatív feladatokra** használjuk, például egyszerű szöveggenerálásra, gépi fordításra, sőt akár képaláírások készítésére is.

> ✅ Gondolj arra, hányszor használtál generatív feladatokat, például szövegkiegészítést gépelés közben. Nézz utána kedvenc alkalmazásaidnak, hogy használtak-e RNN-eket.

Az előző egységben tárgyalt RNN architektúrában minden RNN egység a következő rejtett állapotot adta ki eredményként. Azonban hozzáadhatunk egy másik kimenetet is minden rekurrens egységhez, amely lehetővé teszi, hogy egy **sorozatot** adjunk ki (ami az eredeti sorozattal azonos hosszúságú). Továbbá használhatunk olyan RNN egységeket is, amelyek nem fogadnak bemenetet minden lépésben, hanem csak egy kezdeti állapotvektort vesznek, és ebből állítanak elő egy kimeneti sorozatot.

Ez különböző neurális architektúrákat tesz lehetővé, amelyeket az alábbi ábra mutat:

![Ábra, amely a rekurrens neurális hálózatok gyakori mintázatait mutatja.](../../../../../translated_images/unreasonable-effectiveness-of-rnn.541ead816778f42dce6c42d8a56c184729aa2378d059b851be4ce12b993033df.hu.jpg)

> Kép Andrej Karpaty [Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/) című blogbejegyzéséből

* **Egy-az-egyhez**: hagyományos neurális hálózat egy bemenettel és egy kimenettel
* **Egy-a-sokhoz**: generatív architektúra, amely egy bemeneti értéket fogad, és egy kimeneti értéksorozatot generál. Például, ha egy **képaláírás-generáló** hálózatot szeretnénk tanítani, amely egy kép szöveges leírását állítja elő, akkor a képet bemenetként használhatjuk, egy CNN-en keresztül rejtett állapotot nyerhetünk ki, majd egy rekurrens lánc szó szerint generálja az aláírást.
* **Sok-az-egyhez**: az előző egységben tárgyalt RNN architektúráknak felel meg, például szövegklasszifikáció esetén.
* **Sok-a-sokhoz**, vagy **sorozat-a-sorozathoz**: olyan feladatokhoz, mint például a **gépi fordítás**, ahol az első RNN összegyűjti az összes információt a bemeneti sorozatból a rejtett állapotba, majd egy másik RNN lánc ezt az állapotot bontja ki a kimeneti sorozattá.

Ebben az egységben egyszerű generatív modellekre fogunk összpontosítani, amelyek segítenek szöveget generálni. Az egyszerűség kedvéért karakteralapú tokenizálást fogunk használni.

Ezt az RNN-t lépésről lépésre tanítjuk szöveg generálására. Minden lépésben egy `nchars` hosszúságú karakterláncot veszünk, és megkérjük a hálózatot, hogy minden bemeneti karakterhez generálja a következő kimeneti karaktert:

![Ábra, amely egy RNN által a 'HELLO' szó generálását mutatja.](../../../../../translated_images/rnn-generate.56c54afb52f9781d63a7c16ea9c1b86cb70e6e1eae6a742b56b7b37468576b17.hu.png)

Szöveg generálásakor (inferencia során) egy **indító** szöveggel kezdünk, amelyet az RNN cellákon keresztülvezetünk, hogy előállítsuk a köztes állapotot, majd ebből az állapotból indul a generálás. Egy karaktert generálunk egyszerre, majd az állapotot és a generált karaktert továbbadjuk egy másik RNN cellának, hogy generálja a következőt, amíg elegendő karaktert nem generálunk.

<img src="images/rnn-generate-inf.png" width="60%"/>

> Kép a szerzőtől

## ✍️ Gyakorlatok: Generatív hálózatok

Folytasd a tanulást az alábbi jegyzetfüzetekben:

* [Generatív hálózatok PyTorch segítségével](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativePyTorch.ipynb)
* [Generatív hálózatok TensorFlow segítségével](../../../../../lessons/5-NLP/17-GenerativeNetworks/GenerativeTF.ipynb)

## Lágy szöveggenerálás és hőmérséklet

Minden RNN cella kimenete egy karakterekre vonatkozó valószínűségi eloszlás. Ha mindig a legnagyobb valószínűségű karaktert választjuk a generált szöveg következő karaktereként, a szöveg gyakran "ciklusba" kerülhet, és ugyanazokat a karakterláncokat ismételheti újra és újra, mint ebben a példában:

```
today of the second the company and a second the company ...
```

Azonban, ha megnézzük a következő karakter valószínűségi eloszlását, előfordulhat, hogy a néhány legmagasabb valószínűség közötti különbség nem nagy, például az egyik karakter valószínűsége 0,2, míg egy másiké 0,19 stb. Például, amikor a '*play*' sorozat következő karakterét keressük, a következő karakter lehet egyaránt szóköz vagy **e** (mint a *player* szóban).

Ez arra a következtetésre vezet, hogy nem mindig "igazságos" a legnagyobb valószínűségű karaktert választani, mert a második legnagyobb valószínűségű karakter választása is értelmes szöveghez vezethet. Bölcsebb, ha a karaktereket a hálózat kimenete által adott valószínűségi eloszlásból **mintavételezzük**. Használhatunk egy **hőmérséklet** nevű paramétert is, amely kisimítja a valószínűségi eloszlást, ha több véletlenszerűséget szeretnénk hozzáadni, vagy meredekebbé teszi, ha inkább a legnagyobb valószínűségű karakterekhez ragaszkodnánk.

Fedezd fel, hogyan valósul meg ez a lágy szöveggenerálás a fent hivatkozott jegyzetfüzetekben.

## Összegzés

Bár a szöveggenerálás önmagában is hasznos lehet, a fő előnyök abból származnak, hogy képesek vagyunk szöveget generálni RNN-ek segítségével egy kezdeti jellemzővektorból. Például a szöveggenerálást használják gépi fordítás során (sorozat-a-sorozathoz, ebben az esetben az *enkóder* állapotvektorát használják a fordított üzenet generálására vagy *dekódolására*), vagy egy kép szöveges leírásának generálására (ebben az esetben a jellemzővektor egy CNN kinyerőből származik).

## 🚀 Kihívás

Vegyél részt néhány Microsoft Learn leckén ebben a témában:

* Szöveggenerálás [PyTorch](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-pytorch/6-generative-networks/?WT.mc_id=academic-77998-cacaste)/[TensorFlow](https://docs.microsoft.com/learn/modules/intro-natural-language-processing-tensorflow/5-generative-networks/?WT.mc_id=academic-77998-cacaste) segítségével

## [Előadás utáni kvíz](https://red-field-0a6ddfd03.1.azurestaticapps.net/quiz/217)

## Áttekintés és önálló tanulás

Íme néhány cikk, amelyekkel bővítheted tudásodat:

* Különböző megközelítések szöveggenerálásra Markov-lánccal, LSTM-mel és GPT-2-vel: [blogbejegyzés](https://towardsdatascience.com/text-generation-gpt-2-lstm-markov-chain-9ea371820e1e)
* Szöveggenerálási példa a [Keras dokumentációjában](https://keras.io/examples/generative/lstm_character_level_text_generation/)

## [Feladat](lab/README.md)

Láttuk, hogyan lehet karakterenként szöveget generálni. A laborban a szóalapú szöveggenerálást fogod felfedezni.

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.