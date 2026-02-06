# Emberi Test Szegmentáció

Laborfeladat az [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) keretében.

## Feladat

A videógyártásban, például időjárás-jelentések során, gyakran szükség van arra, hogy egy emberi alakot kivágjunk a kameraképből, és egy másik felvételre helyezzük. Ezt általában **chroma key** technikával végezzük, amikor az embert egy egyszínű háttér előtt filmezik, amelyet később eltávolítanak. Ebben a laborban egy neurális hálózat modellt fogunk tanítani, hogy kivágja az emberi sziluettet.

## Az Adatkészlet

A [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) adatkészletet fogjuk használni Kaggle-ről. Töltsd le az adatkészletet manuálisan Kaggle-ről.

## Indító Jegyzetfüzet

Nyisd meg a labort a [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb) fájl megnyitásával.

## Tanulság

Az emberi test szegmentációja csak egy a gyakori feladatok közül, amelyeket emberekről készült képekkel végezhetünk. Más fontos feladatok közé tartozik a **csontváz detektálása** és a **testtartás felismerése**. Nézd meg az [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) könyvtárat, hogy megtudd, hogyan valósíthatók meg ezek a feladatok.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.