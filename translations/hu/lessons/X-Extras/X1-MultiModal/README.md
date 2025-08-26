<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9c592c26aca16ca085d268c732284187",
  "translation_date": "2025-08-25T23:36:32+00:00",
  "source_file": "lessons/X-Extras/X1-MultiModal/README.md",
  "language_code": "hu"
}
-->
# Multi-Modális Hálózatok

A transzformer modellek sikerét követően az NLP feladatok megoldásában, hasonló architektúrákat kezdtek alkalmazni a számítógépes látás feladataira is. Egyre nagyobb az érdeklődés olyan modellek építése iránt, amelyek *kombinálják* a látás és a természetes nyelv feldolgozásának képességeit. Az egyik ilyen próbálkozás az OpenAI által készült CLIP és DALL.E.

## Kontrasztív Képelőtanulás (CLIP)

A CLIP fő ötlete, hogy képes legyen összehasonlítani szöveges utasításokat egy képpel, és meghatározni, mennyire felel meg a kép az utasításnak.

![CLIP Architektúra](../../../../../translated_images/clip-arch.b3dbf20b4e8ed8be1c38e2bc6100fd3cc257c33cda4692b301be91f791b13ea7.hu.png)

> *Kép [ebből a blogbejegyzésből](https://openai.com/blog/clip/)*

A modellt az internetről származó képeken és azok felirataival tanítják. Minden batch esetében N (kép, szöveg) párt veszünk, és ezeket valamilyen vektoriális reprezentációvá alakítjuk át I, ..., T formában. Ezeket a reprezentációkat ezután egymáshoz illesztjük. A veszteségfüggvény célja, hogy maximalizálja a koszinusz hasonlóságot az egy párhoz tartozó vektorok között (pl. I és T), és minimalizálja a koszinusz hasonlóságot az összes többi pár között. Ezért nevezik ezt a megközelítést **kontrasztívnak**.

A CLIP modell/könyvtár elérhető az [OpenAI GitHub](https://github.com/openai/CLIP) oldalán. A megközelítést [ebben a blogbejegyzésben](https://openai.com/blog/clip/) ismertetik, részletesebben pedig [ebben a tanulmányban](https://arxiv.org/pdf/2103.00020.pdf).

Miután a modellt betanították, megadhatunk neki egy batch képet és egy batch szöveges utasítást, és a kimenet egy valószínűségi tenzor lesz. A CLIP több feladatra is használható:

**Képosztályozás**

Tegyük fel, hogy képeket kell osztályoznunk például macskák, kutyák és emberek között. Ebben az esetben megadhatjuk a modellnek a képet, és egy sor szöveges utasítást: "*egy macska képe*", "*egy kutya képe*", "*egy ember képe*". A kapott 3 valószínűségi vektorban csak ki kell választanunk a legmagasabb értékű indexet.

![CLIP Képosztályozáshoz](../../../../../translated_images/clip-class.3af42ef0b2b19369a633df5f20ddf4f5a01d6c8ffa181e9d3a0572c19f919f72.hu.png)

> *Kép [ebből a blogbejegyzésből](https://openai.com/blog/clip/)*

**Szöveg-alapú Képkeresés**

Az ellenkezőjét is megtehetjük. Ha van egy képkollekciónk, átadhatjuk ezt a kollekciót a modellnek, valamint egy szöveges utasítást – ez megadja azt a képet, amely a legjobban hasonlít az adott utasításhoz.

## ✍️ Példa: [CLIP használata képosztályozáshoz és képkereséshez](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb)

Nyisd meg a [Clip.ipynb](../../../../../lessons/X-Extras/X1-MultiModal/Clip.ipynb) notebookot, hogy lásd a CLIP működését.

## Képalkotás VQGAN+CLIP segítségével

A CLIP **képalkotásra** is használható szöveges utasítás alapján. Ehhez szükség van egy **generátor modellre**, amely képes képeket generálni valamilyen vektoriális bemenet alapján. Az egyik ilyen modell a [VQGAN](https://compvis.github.io/taming-transformers/) (Vector-Quantized GAN).

A VQGAN főbb ötletei, amelyek megkülönböztetik a hagyományos [GAN](../../4-ComputerVision/10-GANs/README.md)-tól, a következők:
* Autoregresszív transzformer architektúra használata, amely kontextusban gazdag vizuális elemek sorozatát generálja, amelyek a képet alkotják. Ezeket a vizuális elemeket pedig [CNN](../../4-ComputerVision/07-ConvNets/README.md) tanulja meg.
* Alképrész-diszkriminátor használata, amely felismeri, hogy a kép részei "valósak" vagy "hamisak" (szemben a hagyományos GAN "mindent vagy semmit" megközelítésével).

További információ a VQGAN-ról a [Taming Transformers](https://compvis.github.io/taming-transformers/) weboldalon található.

A VQGAN és a hagyományos GAN egyik fontos különbsége, hogy az utóbbi bármilyen bemeneti vektorból képes elfogadható képet előállítani, míg a VQGAN valószínűleg nem koherens képet hoz létre. Ezért tovább kell irányítanunk a képalkotási folyamatot, amit a CLIP segítségével tehetünk meg.

![VQGAN+CLIP Architektúra](../../../../../translated_images/vqgan.5027fe05051dfa3101950cfa930303f66e6478b9bd273e83766731796e462d9b.hu.png)

Ahhoz, hogy egy szöveges utasításhoz illeszkedő képet generáljunk, egy véletlenszerű kódoló vektorral kezdünk, amelyet a VQGAN-on keresztül egy képpé alakítunk. Ezután a CLIP-et használjuk egy veszteségfüggvény előállítására, amely megmutatja, mennyire felel meg a kép a szöveges utasításnak. A cél ennek a veszteségnek a minimalizálása, a visszaterjesztés segítségével a bemeneti vektor paramétereinek módosításával.

Egy nagyszerű könyvtár, amely megvalósítja a VQGAN+CLIP-et, a [Pixray](http://github.com/pixray/pixray).

![Pixray által készített kép](../../../../../translated_images/a_closeup_watercolor_portrait_of_young_male_teacher_of_literature_with_a_book.2384968e9db8a0d09dc96de938b9f95bde8a7e1c721f48f286a7795bf16d56c7.hu.png) |  ![Pixray által készített kép](../../../../../translated_images/a_closeup_oil_portrait_of_young_female_teacher_of_computer_science_with_a_computer.e0b6495f210a439077e1c32cc8afdf714e634fe24dc78dc5aa45fd2f560b0ed5.hu.png) | ![Pixray által készített kép](../../../../../translated_images/a_closeup_oil_portrait_of_old_male_teacher_of_math.5362e67aa7fc2683b9d36a613b364deb7454760cd39205623fc1e3938fa133c0.hu.png)
----|----|----
Kép generálva az *egy fiatal irodalomtanár akvarell portréja könyvvel* utasítás alapján | Kép generálva az *egy fiatal női informatikatanár olajportréja számítógéppel* utasítás alapján | Kép generálva az *egy idős matematikatanár olajportréja táblával* utasítás alapján

> Képek az **Artificial Teachers** gyűjteményből, [Dmitry Soshnikov](http://soshnikov.com) által

## DALL-E
### [DALL-E 1](https://openai.com/research/dall-e)
A DALL-E a GPT-3 egy változata, amelyet képek generálására tanítottak szöveges utasítások alapján. 12 milliárd paraméterrel lett betanítva.

A CLIP-től eltérően a DALL-E egyszerre kapja meg a szöveget és a képet egyetlen tokenfolyamként. Ezért több utasításból képeket generálhatunk a szöveg alapján.

### [DALL-E 2](https://openai.com/dall-e-2)
A DALL.E 1 és 2 közötti fő különbség, hogy a második verzió valósághűbb képeket és művészeti alkotásokat generál.

Példák a DALL-E által generált képekre:
![DALL-E által készített kép](../../../../../translated_images/DALL·E%202023-06-20%2015.56.56%20-%20a%20closeup%20watercolor%20portrait%20of%20young%20male%20teacher%20of%20literature%20with%20a%20book.6c235e8271d9ed10ce985d86aeb241a58518958647973af136912116b9518fce.hu.png) |  ![DALL-E által készített kép](../../../../../translated_images/DALL·E%202023-06-20%2015.57.43%20-%20a%20closeup%20oil%20portrait%20of%20young%20female%20teacher%20of%20computer%20science%20with%20a%20computer.f21dc4166340b6c8b4d1cb57efd1e22127407f9b28c9ac7afe11344065369e64.hu.png) | ![DALL-E által készített kép](../../../../../translated_images/DALL·E%202023-06-20%2015.58.42%20-%20%20a%20closeup%20oil%20portrait%20of%20old%20male%20teacher%20of%20mathematics%20in%20front%20of%20blackboard.d331c2dfbdc3f7c46aa65c0809066f5e7ed4b49609cd259852e760df21051e4a.hu.png)
----|----|----
Kép generálva az *egy fiatal irodalomtanár akvarell portréja könyvvel* utasítás alapján | Kép generálva az *egy fiatal női informatikatanár olajportréja számítógéppel* utasítás alapján | Kép generálva az *egy idős matematikatanár olajportréja táblával* utasítás alapján

## Hivatkozások

* VQGAN tanulmány: [Taming Transformers for High-Resolution Image Synthesis](https://compvis.github.io/taming-transformers/paper/paper.pdf)
* CLIP tanulmány: [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/pdf/2103.00020.pdf)

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.