# Többosztályos osztályozás perceptronnal

Laborfeladat az [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) anyagából.

## Feladat

A kódbázis felhasználásával, amelyet ebben a leckében az MNIST kézzel írt számjegyek bináris osztályozására fejlesztettünk, hozz létre egy többosztályos osztályozót, amely bármely számjegyet képes felismerni. Számítsd ki az osztályozási pontosságot a tanító és teszt adathalmazon, és jelenítsd meg a zavaró mátrixot.

## Tippek

1. Minden számjegyhez hozz létre egy adathalmazt, amely a "ez a számjegy vs. az összes többi számjegy" bináris osztályozásra szolgál.
1. Taníts meg 10 különböző perceptront bináris osztályozásra (egy-egy minden számjegyhez).
1. Definiálj egy függvényt, amely képes osztályozni egy bemeneti számjegyet.

> **Tipp**: Ha a 10 perceptron súlyait egy mátrixba kombináljuk, akkor egyetlen mátrixszorzással alkalmazhatjuk mind a 10 perceptront a bemeneti számjegyekre. A legvalószínűbb számjegy egyszerűen az `argmax` művelet alkalmazásával található meg a kimeneten.

## Kezdő Notebook

Kezdd a labort a [PerceptronMultiClass.ipynb](PerceptronMultiClass.ipynb) megnyitásával.

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.