# Segmentace lidského těla

Laboratorní úloha z [AI for Beginners Curriculum](https://github.com/microsoft/ai-for-beginners).

## Úkol

Při tvorbě videí, například v předpovědích počasí, často potřebujeme vystřihnout obraz člověka z kamery a umístit jej na jiné záběry. To se obvykle provádí pomocí technik **chroma key**, kdy je člověk natáčen před jednobarevným pozadím, které je následně odstraněno. V této laboratorní úloze vytrénujeme model neuronové sítě, který dokáže vystřihnout siluetu člověka.

## Datová sada

Budeme používat [Segmentation Full Body MADS Dataset](https://www.kaggle.com/datasets/tapakah68/segmentation-full-body-mads-dataset) z Kaggle. Stáhněte si datovou sadu ručně z Kaggle.

## Výchozí notebook

Začněte laboratorní úlohu otevřením [BodySegmentation.ipynb](../../../../../../lessons/4-ComputerVision/12-Segmentation/lab/BodySegmentation.ipynb)

## Závěr

Segmentace těla je jen jedním z běžných úkolů, které můžeme provádět s obrázky lidí. Mezi další důležité úkoly patří **detekce kostry** a **detekce póz**. Podívejte se na knihovnu [OpenPose](https://github.com/CMU-Perceptual-Computing-Lab/openpose), abyste zjistili, jak lze tyto úkoly implementovat.

**Prohlášení:**  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.