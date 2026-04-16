# Klasifikace Oxfordských mazlíčků pomocí transferového učení

Laboratorní úkol z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úkol

Představte si, že potřebujete vyvinout aplikaci pro školku pro mazlíčky, která by katalogizovala všechna zvířata. Jednou z úžasných funkcí takové aplikace by bylo automatické rozpoznání plemene z fotografie. V tomto úkolu použijeme transferové učení k klasifikaci reálných obrázků mazlíčků z datasetu [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/).

## Dataset

Použijeme původní dataset [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/), který obsahuje 35 různých plemen psů a koček.

Pro stažení datasetu použijte tento kód:

```python
!wget https://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Spuštění notebooku

Začněte laboratorní úkol otevřením [OxfordPets.ipynb](../../../../../../lessons/4-ComputerVision/08-TransferLearning/lab/OxfordPets.ipynb)

## Shrnutí

Transferové učení a předtrénované sítě nám umožňují relativně snadno řešit reálné problémy klasifikace obrázků. Nicméně předtrénované sítě fungují dobře na obrázcích podobného typu, a pokud začneme klasifikovat velmi odlišné obrázky (např. lékařské snímky), pravděpodobně dosáhneme mnohem horších výsledků.

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.