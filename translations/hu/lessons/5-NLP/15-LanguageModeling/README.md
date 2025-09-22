<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "31b46ba1f3aa78578134d4829f88be53",
  "translation_date": "2025-08-25T21:55:17+00:00",
  "source_file": "lessons/5-NLP/15-LanguageModeling/README.md",
  "language_code": "hu"
}
-->
# Nyelvi Modellezés

A szemantikus beágyazások, mint például a Word2Vec és a GloVe, valójában az első lépést jelentik a **nyelvi modellezés** felé – olyan modellek létrehozása felé, amelyek valamilyen módon *megértik* (vagy *reprezentálják*) a nyelv természetét.

## [Előadás előtti kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/29)

A nyelvi modellezés fő gondolata az, hogy címkézetlen adathalmazokon tanítsuk őket felügyelet nélküli módon. Ez azért fontos, mert hatalmas mennyiségű címkézetlen szöveg áll rendelkezésünkre, míg a címkézett szövegek mennyiségét mindig korlátozza az a munka, amit a címkézésre fordíthatunk. Leggyakrabban olyan nyelvi modelleket építhetünk, amelyek képesek **hiányzó szavakat megjósolni** a szövegben, mivel egyszerűen ki lehet takarni egy véletlenszerű szót a szövegben, és azt használni tanítómintaként.

## Beágyazások tanítása

Korábbi példáinkban előre betanított szemantikus beágyazásokat használtunk, de érdekes látni, hogyan lehet ezeket a beágyazásokat betanítani. Számos lehetséges ötlet létezik, amelyeket felhasználhatunk:

* **N-Gram** nyelvi modellezés, amikor egy tokent az előző N token alapján jósolunk meg (N-gram).
* **Folytonos Szózsák** (CBoW), amikor a középső tokent $W_0$ jósoljuk meg egy token sorozatban $W_{-N}$, ..., $W_N$.
* **Skip-gram**, ahol a középső tokenből $W_0$ egy szomszédos tokenhalmazt {$W_{-N},\dots, W_{-1}, W_1,\dots, W_N$} jósolunk meg.

![kép egy tanulmányból, amely a szavak vektorokká alakítását mutatja](../../../../../translated_images/example-algorithms-for-converting-words-to-vectors.fbe9207a726922f6f0f5de66427e8a6eda63809356114e28fb1fa5f4a83ebda7.hu.png)

> Kép [ebből a tanulmányból](https://arxiv.org/pdf/1301.3781.pdf)

## ✍️ Példa Jegyzetfüzetek: CBoW modell tanítása

Folytasd a tanulást az alábbi jegyzetfüzetekben:

* [CBoW Word2Vec tanítása TensorFlow-val](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb)
* [CBoW Word2Vec tanítása PyTorch-csal](../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-PyTorch.ipynb)

## Összegzés

Az előző leckében láttuk, hogy a szóbeágyazások szinte varázslatosan működnek! Most már tudjuk, hogy a szóbeágyazások tanítása nem egy túl bonyolult feladat, és képesek lehetünk saját szóbeágyazásokat tanítani specifikus szakterületi szövegekhez, ha szükséges.

## [Előadás utáni kvíz](https://ff-quizzes.netlify.app/en/ai/quiz/30)

## Áttekintés és Önálló Tanulás

* [Hivatalos PyTorch oktatóanyag a nyelvi modellezésről](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html).
* [Hivatalos TensorFlow oktatóanyag a Word2Vec modell tanításáról](https://www.TensorFlow.org/tutorials/text/word2vec).
* A **gensim** keretrendszer használata a leggyakrabban használt beágyazások tanítására néhány kódsorral [ebben a dokumentációban](https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html) van leírva.

## 🚀 [Feladat: Skip-Gram Modell Tanítása](lab/README.md)

A laborban arra hívunk ki, hogy módosítsd az órai kódot, és taníts Skip-Gram modellt a CBoW helyett. [Olvasd el a részleteket](lab/README.md).

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.