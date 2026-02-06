# Az Oxford Pets osztályozása transzfer tanulással

Laborfeladat az [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners) anyagából.

## Feladat

Képzeld el, hogy egy alkalmazást kell fejlesztened egy kisállat-nevelő számára, amely az összes kisállatot katalogizálja. Egy ilyen alkalmazás nagyszerű funkciója lenne, ha egy fénykép alapján automatikusan felismerné a fajtát. Ebben a feladatban transzfer tanulást fogunk használni, hogy az [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) kisállat-adatkészlet valódi képeit osztályozzuk.

## Az adatkészlet

Az eredeti [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/) kisállat-adatkészletet fogjuk használni, amely 35 különböző kutya- és macskafajtát tartalmaz.

Az adatkészlet letöltéséhez használd az alábbi kódrészletet:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Induló notebook

Kezdd a labort az [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb) megnyitásával.

## Tanulság

A transzfer tanulás és az előre betanított hálózatok lehetővé teszik, hogy viszonylag könnyen megoldjunk valós képosztályozási problémákat. Azonban az előre betanított hálózatok jól működnek hasonló típusú képeken, és ha nagyon eltérő képeket kezdünk osztályozni (pl. orvosi képek), akkor valószínűleg sokkal rosszabb eredményeket kapunk.

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.