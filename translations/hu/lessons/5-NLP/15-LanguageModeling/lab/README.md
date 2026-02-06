# Skip-Gram Modell Tréningje

Laborfeladat az [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) anyagából.

## Feladat

Ebben a laborban az a kihívás, hogy Word2Vec modellt taníts Skip-Gram technikával. Taníts egy hálózatot beágyazással, hogy megjósolja a szomszédos szavakat egy $N$ token széles Skip-Gram ablakban. Használhatod a [leckében található kódot](../../../../../../lessons/5-NLP/15-LanguageModeling/CBoW-TF.ipynb), és kicsit módosíthatod.

## Az Adatkészlet

Bármilyen könyvet használhatsz. Rengeteg ingyenes szöveget találhatsz a [Project Gutenberg](https://www.gutenberg.org/) oldalán, például itt van egy közvetlen link Lewis Carroll [Alice Csodaországban](https://www.gutenberg.org/files/11/11-0.txt) című művéhez. Vagy használhatod Shakespeare darabjait, amelyeket az alábbi kóddal szerezhetsz meg:

```python
path_to_file = tf.keras.utils.get_file(
   'shakespeare.txt', 
   'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
```

## Fedezd fel!

Ha van időd és szeretnél mélyebben elmerülni a témában, próbálj ki néhány dolgot:

* Hogyan befolyásolja a beágyazási méret az eredményeket?
* Hogyan hatnak a különböző szövegstílusok az eredményre?
* Vegyél néhány nagyon különböző típusú szót és azok szinonimáit, szerezd meg a vektoriális reprezentációikat, alkalmazz PCA-t a dimenziók 2-re csökkentéséhez, és ábrázold őket 2D térben. Látsz bármilyen mintázatot?

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.