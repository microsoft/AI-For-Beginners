<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3d2cee9cb3c52160419e560c57a690e",
  "translation_date": "2025-08-25T22:58:01+00:00",
  "source_file": "lessons/4-ComputerVision/07-ConvNets/lab/README.md",
  "language_code": "cs"
}
-->
# Klasifikace obličejů domácích mazlíčků

Laboratorní úkol z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úkol

Představte si, že potřebujete vyvinout aplikaci pro školku domácích mazlíčků, která by katalogizovala všechna zvířata. Jednou z úžasných funkcí takové aplikace by bylo automatické rozpoznání plemene z fotografie. Toho lze úspěšně dosáhnout pomocí neuronových sítí.

Vaším úkolem je natrénovat konvoluční neuronovou síť, která bude klasifikovat různá plemena koček a psů pomocí datasetu **Pet Faces**.

## Dataset

Použijeme dataset **Pet Faces**, který je odvozen z datasetu domácích mazlíčků [Oxford-IIIT](https://www.robots.ox.ac.uk/~vgg/data/pets/). Obsahuje 35 různých plemen psů a koček.

![Dataset, se kterým budeme pracovat](../../../../../../translated_images/data.50b2a9d5484bdbf0f52f5765b381cec9efe2bd296a98f007f90bedb6ac67f2a8.cs.png)

Pro stažení datasetu použijte tento úryvek kódu:

```python
!wget https://thor.robots.ox.ac.uk/~vgg/data/pets/images.tar.gz
!tar xfz images.tar.gz
!rm images.tar.gz
```

## Výchozí notebook

Začněte laboratoř otevřením [PetFaces.ipynb](../../../../../../lessons/4-ComputerVision/07-ConvNets/lab/PetFaces.ipynb)

## Závěr

Vyřešili jste poměrně složitý problém klasifikace obrázků od základů! Bylo zde mnoho tříd, a přesto jste byli schopni dosáhnout rozumné přesnosti! Má také smysl měřit top-k přesnost, protože je snadné zaměnit některé třídy, které nejsou jasně odlišitelné ani pro lidské oko.

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.